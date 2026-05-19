const http = require('http');
const fs   = require('fs');
const path = require('path');

const PORT      = 3000;
const DATA_FILE = path.join('/data', 'waitlist.txt');
const EMAIL_RE  = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function send(res, status, body) {
  const payload = JSON.stringify(body);
  res.writeHead(status, {
    'Content-Type':  'application/json',
    'Content-Length': Buffer.byteLength(payload),
  });
  res.end(payload);
}

http.createServer((req, res) => {
  if (req.method === 'POST' && req.url === '/api/waitlist') {
    let raw = '';
    req.on('data', chunk => { raw += chunk; });
    req.on('end', () => {
      let email;
      try {
        ({ email } = JSON.parse(raw));
      } catch {
        return send(res, 400, { error: 'Invalid request body.' });
      }

      if (!email || !EMAIL_RE.test(String(email).trim())) {
        return send(res, 400, { error: 'Please enter a valid email address.' });
      }

      const clean = String(email).trim().toLowerCase();
      const now   = new Date().toISOString().replace('T', ' ').slice(0, 19);
      const line  = `${now} - ${clean}\n`;

      fs.appendFile(DATA_FILE, line, err => {
        if (err) {
          console.error('Write error:', err);
          return send(res, 500, { error: 'Could not save your email. Please try again.' });
        }
        console.log('Waitlist:', clean);
        send(res, 200, { ok: true });
      });
    });
    return;
  }

  send(res, 404, { error: 'Not found.' });
}).listen(PORT, () => console.log(`API listening on :${PORT}`));
