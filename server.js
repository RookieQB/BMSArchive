const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = Number(process.env.PORT || 3000);
const SITE_URL = (process.env.SITE_URL || 'https://bmsarchive.com').replace(/\/$/, '');
const DATA_DIR = process.env.DATA_DIR || '/data';
const EBOOK_DIR = process.env.EBOOK_DIR || path.join(__dirname, 'E-books');
const WAITLIST_FILE = path.join(DATA_DIR, 'waitlist.txt');
const FULFILLED_FILE = path.join(DATA_DIR, 'fulfilled-orders.jsonl');
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const PHONE_RE = /^[+()\d\s.-]{6,30}$/;
const MAX_BODY_BYTES = 256 * 1024;

let stripe = null;
if (process.env.STRIPE_SECRET_KEY) {
  const Stripe = require('stripe');
  stripe = new Stripe(process.env.STRIPE_SECRET_KEY);
}

// Prices and file paths are server-owned. Never accept price or file data from the browser.
const PRODUCTS = Object.freeze({
  'complete-field-guide': {
    name: 'The Complete Field Guide to Botanical Medicine',
    priceCents: 3900,
    currency: 'usd',
    filename: 'BMS_Archive_Complete_Field_Guide.pdf',
  },
  'medicinal-fungi': {
    name: 'Medicinal Fungi',
    priceCents: 2400,
    currency: 'usd',
    filename: 'BMS_Archive_Medicinal_Fungi.pdf',
  },
  'medicinal-plants': {
    name: 'Medicinal Plants',
    priceCents: 2400,
    currency: 'usd',
    filename: 'BMS_Archive_Medicinal_Plants.pdf',
  },
  'little-guide': {
    name: 'The Little Guide',
    priceCents: 100,
    currency: 'usd',
    filename: 'BMS_Archive_The_Little_Guide.pdf',
  },
});

function ebookPath(product) {
  return path.join(EBOOK_DIR, product.filename);
}

function isAvailable(product) {
  return fs.existsSync(ebookPath(product));
}

function sendJson(res, status, body) {
  const payload = JSON.stringify(body);
  res.writeHead(status, {
    'Content-Type': 'application/json; charset=utf-8',
    'Content-Length': Buffer.byteLength(payload),
    'Cache-Control': 'no-store',
  });
  res.end(payload);
}

function readBody(req, callback) {
  let raw = '';
  let tooLarge = false;

  req.on('data', chunk => {
    if (tooLarge) return;
    raw += chunk;
    if (Buffer.byteLength(raw) > MAX_BODY_BYTES) {
      tooLarge = true;
    }
  });
  req.on('end', () => callback(tooLarge ? null : raw));
}

function parseJson(raw) {
  try {
    return JSON.parse(raw);
  } catch {
    return null;
  }
}

function getFulfilledSessionIds() {
  try {
    return new Set(
      fs.readFileSync(FULFILLED_FILE, 'utf8')
        .split('\n')
        .filter(Boolean)
        .map(line => JSON.parse(line).sessionId),
    );
  } catch (error) {
    if (error.code !== 'ENOENT') console.error('Fulfilment log read error:', error.message);
    return new Set();
  }
}

const fulfilledSessions = getFulfilledSessionIds();
const fulfillmentInProgress = new Set();

function selectedProducts(productIds) {
  if (!Array.isArray(productIds) || productIds.length === 0) return null;
  const uniqueIds = [...new Set(productIds.map(String))];
  if (uniqueIds.length > Object.keys(PRODUCTS).length) return null;

  const products = uniqueIds.map(id => ({ id, ...PRODUCTS[id] }));
  if (products.some(product => !product.name || !isAvailable(product))) return null;
  return products;
}

async function createCheckout(req, res) {
  if (!stripe) return sendJson(res, 503, { error: 'Checkout is not configured yet.' });

  readBody(req, async raw => {
    if (raw === null) return sendJson(res, 413, { error: 'Request is too large.' });
    const body = parseJson(raw);
    const products = selectedProducts(body?.productIds);
    const name = String(body?.name || '').trim();
    const email = String(body?.email || '').trim().toLowerCase();
    const phone = String(body?.phone || '').trim();
    const digitalConsent = body?.digitalConsent === true;

    if (!products) return sendJson(res, 400, { error: 'One or more selected e-books are unavailable.' });
    if (name.length < 2 || name.length > 120) return sendJson(res, 400, { error: 'Please enter your name.' });
    if (!EMAIL_RE.test(email)) return sendJson(res, 400, { error: 'Please enter a valid email.' });
    if (!PHONE_RE.test(phone)) return sendJson(res, 400, { error: 'Please enter a valid phone number.' });
    if (!digitalConsent) return sendJson(res, 400, { error: 'Please accept immediate digital delivery.' });

    try {
      const session = await stripe.checkout.sessions.create({
        mode: 'payment',
        line_items: products.map(product => ({
          quantity: 1,
          price_data: {
            currency: product.currency,
            unit_amount: product.priceCents,
            product_data: { name: product.name },
          },
        })),
        customer_email: email,
        metadata: {
          product_ids: products.map(product => product.id).join(','),
          customer_name: name,
          customer_phone: phone,
          digital_delivery_consent: 'yes',
        },
        success_url: `${SITE_URL}/checkout-success.html?session_id={CHECKOUT_SESSION_ID}`,
        cancel_url: `${SITE_URL}/?checkout=cancelled#ebooks`,
        locale: 'auto',
      });
      sendJson(res, 200, { url: session.url });
    } catch (error) {
      console.error('Stripe Checkout error:', error.message);
      sendJson(res, 502, { error: 'Checkout could not be opened. Please try again.' });
    }
  });
}

async function sendOrderEmail(session, products) {
  if (!process.env.RESEND_API_KEY || !process.env.ORDER_FROM_EMAIL) {
    throw new Error('Resend is not configured');
  }

  const email = session.customer_details?.email || session.customer_email;
  if (!email || !EMAIL_RE.test(email)) throw new Error('Paid session has no valid email');

  const attachments = products.map(product => ({
    filename: product.filename,
    content: fs.readFileSync(ebookPath(product)).toString('base64'),
  }));
  const bookList = products.map(product => `<li>${product.name}</li>`).join('');

  const response = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
      'Content-Type': 'application/json',
      'Idempotency-Key': `bms-order-${session.id}`,
    },
    body: JSON.stringify({
      from: process.env.ORDER_FROM_EMAIL,
      to: [email],
      subject: 'Your BMS Archive e-book order',
      html: `<p>Thank you for your order.</p><p>Your e-book${products.length > 1 ? 's are' : ' is'} attached:</p><ul>${bookList}</ul><p>Keep this email so you can find your purchase again.</p><p>BMS Archive<br><a href="https://bmsarchive.com">bmsarchive.com</a></p>`,
      attachments,
    }),
  });

  const detail = await response.text();
  if (!response.ok) {
    throw new Error(`Resend rejected delivery (${response.status}): ${detail.slice(0, 300)}`);
  }

  try {
    return JSON.parse(detail).id || null;
  } catch {
    return null;
  }
}

async function fulfillPaidSession(session, eventId) {
  if (session.payment_status !== 'paid') return;
  if (fulfilledSessions.has(session.id) || fulfillmentInProgress.has(session.id)) return;

  const productIds = String(session.metadata?.product_ids || '').split(',').filter(Boolean);
  const products = selectedProducts(productIds);
  if (!products) throw new Error(`Invalid products in paid session ${session.id}`);

  fulfillmentInProgress.add(session.id);
  try {
    const emailId = await sendOrderEmail(session, products);
    const record = {
      sessionId: session.id,
      eventId,
      emailId,
      emailAcceptedAt: new Date().toISOString(),
      productIds,
    };
    await fs.promises.appendFile(FULFILLED_FILE, `${JSON.stringify(record)}\n`, { mode: 0o600 });
    fulfilledSessions.add(session.id);
    console.log('E-book email accepted by Resend:', session.id, emailId || 'no-email-id');
  } finally {
    fulfillmentInProgress.delete(session.id);
  }
}

async function handleStripeWebhook(req, res) {
  if (!stripe || !process.env.STRIPE_WEBHOOK_SECRET) {
    return sendJson(res, 503, { error: 'Stripe webhook is not configured.' });
  }

  readBody(req, async raw => {
    if (raw === null) return sendJson(res, 413, { error: 'Request is too large.' });

    let event;
    try {
      event = stripe.webhooks.constructEvent(
        raw,
        req.headers['stripe-signature'],
        process.env.STRIPE_WEBHOOK_SECRET,
      );
    } catch (error) {
      console.warn('Rejected Stripe webhook:', error.message);
      return sendJson(res, 400, { error: 'Invalid webhook signature.' });
    }

    try {
      if (event.type === 'checkout.session.completed' || event.type === 'checkout.session.async_payment_succeeded') {
        await fulfillPaidSession(event.data.object, event.id);
      }
      sendJson(res, 200, { received: true });
    } catch (error) {
      console.error('Stripe fulfillment error:', error.message);
      sendJson(res, 500, { error: 'Order delivery failed and will be retried.' });
    }
  });
}

async function getSessionStatus(req, res, url) {
  if (!stripe) return sendJson(res, 503, { error: 'Checkout is not configured yet.' });
  const sessionId = url.searchParams.get('session_id');
  if (!sessionId || !/^cs_(test_|live_)[A-Za-z0-9]+$/.test(sessionId)) {
    return sendJson(res, 400, { error: 'Invalid checkout session.' });
  }

  try {
    const session = await stripe.checkout.sessions.retrieve(sessionId);
    const productIds = String(session.metadata?.product_ids || '').split(',').filter(Boolean);
    const products = selectedProducts(productIds) || [];
    sendJson(res, 200, {
      status: session.status,
      paymentStatus: session.payment_status,
      email: session.customer_details?.email || session.customer_email || '',
      delivered: fulfilledSessions.has(session.id),
      products: products.map(product => ({ id: product.id, name: product.name })),
    });
  } catch (error) {
    console.warn('Session lookup error:', error.message);
    sendJson(res, 404, { error: 'Checkout session not found.' });
  }
}

async function downloadPurchasedProduct(req, res, url) {
  if (!stripe) return sendJson(res, 503, { error: 'Checkout is not configured yet.' });

  const sessionId = url.searchParams.get('session_id');
  const productId = url.searchParams.get('product_id');
  if (!sessionId || !/^cs_(test_|live_)[A-Za-z0-9]+$/.test(sessionId)) {
    return sendJson(res, 400, { error: 'Invalid checkout session.' });
  }

  try {
    const session = await stripe.checkout.sessions.retrieve(sessionId);
    if (session.status !== 'complete' || session.payment_status !== 'paid') {
      return sendJson(res, 403, { error: 'Payment has not been completed.' });
    }

    const purchasedIds = String(session.metadata?.product_ids || '').split(',').filter(Boolean);
    if (!purchasedIds.includes(productId)) {
      return sendJson(res, 403, { error: 'This product is not part of the order.' });
    }

    const products = selectedProducts([productId]);
    if (!products) return sendJson(res, 404, { error: 'The purchased file is unavailable.' });

    const product = products[0];
    const filePath = ebookPath(product);
    const stat = await fs.promises.stat(filePath);
    res.writeHead(200, {
      'Content-Type': 'application/pdf',
      'Content-Length': stat.size,
      'Content-Disposition': `attachment; filename="${product.filename}"`,
      'Cache-Control': 'private, no-store',
      'X-Content-Type-Options': 'nosniff',
    });
    fs.createReadStream(filePath).pipe(res);
  } catch (error) {
    console.warn('Paid download error:', error.message);
    if (!res.headersSent) sendJson(res, 404, { error: 'Purchased file could not be retrieved.' });
    else res.destroy();
  }
}

function addToWaitlist(req, res) {
  readBody(req, raw => {
    if (raw === null) return sendJson(res, 413, { error: 'Request is too large.' });
    const body = parseJson(raw);
    const email = String(body?.email || '').trim().toLowerCase();
    if (!EMAIL_RE.test(email)) return sendJson(res, 400, { error: 'Please enter a valid email address.' });

    const now = new Date().toISOString().replace('T', ' ').slice(0, 19);
    fs.appendFile(WAITLIST_FILE, `${now} - ${email}\n`, { mode: 0o600 }, error => {
      if (error) {
        console.error('Waitlist write error:', error.message);
        return sendJson(res, 500, { error: 'Could not save your email. Please try again.' });
      }
      sendJson(res, 200, { ok: true });
    });
  });
}

fs.mkdirSync(DATA_DIR, { recursive: true });

http.createServer((req, res) => {
  const url = new URL(req.url, 'http://api.local');

  if (req.method === 'POST' && url.pathname === '/api/waitlist') return addToWaitlist(req, res);
  if (req.method === 'POST' && url.pathname === '/api/checkout') return createCheckout(req, res);
  if (req.method === 'POST' && url.pathname === '/api/stripe/webhook') return handleStripeWebhook(req, res);
  if (req.method === 'GET' && url.pathname === '/api/session-status') return getSessionStatus(req, res, url);
  if (req.method === 'GET' && url.pathname === '/api/download') return downloadPurchasedProduct(req, res, url);

  sendJson(res, 404, { error: 'Not found.' });
}).listen(PORT, () => {
  const available = Object.values(PRODUCTS).filter(isAvailable).length;
  console.log(`API listening on :${PORT}; ${available} e-book(s) available`);
  if (!stripe) console.warn('STRIPE_SECRET_KEY is missing; checkout is disabled');
});
