# BMS Archive

**bmsarchive.com** — An evidence-based phytomedicine database and e-book storefront. The searchable archive currently contains 66 botanical and fungal monographs sourced from peer-reviewed literature. For educational and research purposes only — not medical advice.

Instagram: [@thebmsarchive](https://instagram.com/thebmsarchive)

---

## What it is

Public pages and services:

| Page | Purpose |
|---|---|
| `index.html` | Landing page — hero, email waitlist form, medical disclaimer |
| `database.html` | Searchable monograph database — grid, type filter, modal detail view |
| `checkout-success.html` | Stripe return page — polls delivery status after payment |
| `server.js` | Waitlist, Stripe Checkout, signed webhook, and Resend e-book delivery API |

The database contains 66 entries: 25 medicinal fungi + 41 medicinal plants. Every profile has citations, ADME pharmacokinetics, mechanism of action, safety data, and special precautions (pregnancy, lactation, hepatic/renal impairment).

---

## Stack

| Layer | Detail |
|---|---|
| HTML/CSS | Plain HTML5 + Tailwind CSS v3.4.17 (served locally as `tailwind.js`) |
| JavaScript | Vanilla JS, inline in each HTML file — no bundler, no framework |
| Font | Inter (Google Fonts, non-blocking preload) |
| Data | `data.json` — 66 monograph entries (25 fungi + 41 plants) |
| Web server | Nginx 1.27-alpine (Docker) |
| API server | Node.js 20-alpine (Docker) + Stripe Node SDK |
| Container orchestration | Docker Compose v2+ |
| Deployment host | LXC container on self-hosted Proxmox server |
| Admin tool | Python 3 stdlib HTTP server — local only, never deployed |
| Data-seeding | Python 3 + `anthropic` SDK + NCBI APIs — offline only |

No frontend build step and no framework. The Node API dependencies are declared in `package.json`.

---

## File structure

```
BMS website/
├── index.html            # Landing page
├── database.html         # Searchable database
├── checkout-success.html # Stripe return and e-book delivery status page
├── data.json             # 66 monograph entries (25 Fungi + 41 Plants)
├── tailwind.js           # Tailwind CSS v3.4.17 — local bundle, do not replace with CDN
├── nginx.conf            # Nginx: HTTPS, gzip, cache, security headers, rate limiting
├── Dockerfile            # nginx:1.27-alpine — serves static files
├── Dockerfile.api        # node:20-alpine — runs server.js
├── docker-compose.yml    # Two services: web (Nginx) + api (Node.js)
├── server.js             # Waitlist, Stripe Checkout/webhook, and order delivery API
├── package.json          # API dependency and start command
├── E-books/              # Customer PDFs copied into the API image
├── favicon.svg           # SVG favicon — forest green, "B"
├── og-image.png          # Open Graph image (1200×630) for Instagram link previews
├── robots.txt            # Allow all; references sitemap
├── sitemap.xml           # Two URLs: / and /database.html
├── .env.example          # Documents required environment variables
├── admin.html            # Local admin panel UI — NOT deployed
├── admin_server.py       # Local Python server (port 5050) for admin.html — NOT deployed
├── build_plants.py       # Offline script — generates plant monographs via Claude API
├── CLAUDE.md             # Project conventions and rules for Claude Code
├── docs/                 # Workflow guides, templates, rubrics, roadmap
└── scripts/
    └── data-seeding/     # Batch data scripts and update_sources.py
```

---

## Running locally

The static pages can be opened directly. Checkout needs the Node API and environment variables.

```bash
npm install
node --env-file=.env server.js
# API listens on http://localhost:3000 by default
```

### With Docker (Nginx + Node.js)

```bash
docker compose up --build
# Site at http://localhost:80
# Note: nginx.conf expects TLS certs — for local testing, open HTML files directly instead
```

### Local admin panel

Edits `data.json` locally. Never deploy this.

```bash
python3 admin_server.py
# Opens http://localhost:5050
```

### Validate data.json

```bash
python3 scripts/validate_archive_data.py
```

### Refresh PubMed sources

```bash
python3 scripts/data-seeding/update_sources.py
# Queries NCBI eSearch API — rate-limited to 0.5 s/request
```

### Generate new monographs (requires Anthropic API key)

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python3 build_plants.py
# Resumes automatically if interrupted (tracks progress in plants_progress.json)
```

---

## API

### `POST /api/waitlist`

Saves an email address to the waitlist. Rate-limited to 5 requests/minute per IP (Nginx `limit_req`).

```bash
curl -X POST https://bmsarchive.com/api/waitlist \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com"}'
# → {"ok":true}
```

Emails are appended to `/data/waitlist.txt` inside the Docker named volume `waitlist_data`.

### Stripe e-book checkout

The storefront posts a server-validated list of product IDs plus the customer's name, email, and
phone number to `POST /api/checkout`. Prices are defined only in `server.js`; browser-supplied
prices are never accepted. Stripe hosts the payment form, so BMS Archive never receives card data.

After payment, Stripe calls `POST /api/stripe/webhook`. A valid signed
`checkout.session.completed` event triggers delivery of the purchased PDF files through Resend.
Completed deliveries are recorded in the Docker data volume to prevent duplicate emails.

#### Current $1 test product (19 June 2026)

| Field | Value |
|---|---|
| Product ID | `little-guide` |
| Storefront name | The Little Guide |
| Server-owned price | `100` cents USD (`$1`) |
| Customer PDF | `E-books/BMS_Archive_The_Little_Guide.pdf` |
| Editable reviewed source | `output/documents/BMS_Archive_The_Little_Guide_REVIEWED_FINAL.html` |

The final PDF has 15 A4 pages. It was visually rendered and checked page by page; the cover
byline overlap was fixed and the final PDF geometry check reported no overlapping or out-of-page
text. Scientific wording was tightened for evidence strength, interactions, contraindications,
red flags, and Danish ashwagandha status. The reference page now contains 23 linked primary or
official sources.

The browser displays `$1`, but that value is presentation only. `server.js` remains the authority
and creates the Stripe line item at `100` cents, preventing price manipulation in the browser.

Required production secrets belong in an untracked `.env` file:

```env
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
SITE_URL=https://bmsarchive.com
RESEND_API_KEY=re_...
ORDER_FROM_EMAIL=BMS Archive <contact@bmsarchive.com>
```

In Stripe, register `https://bmsarchive.com/api/stripe/webhook` for these events:

- `checkout.session.completed`
- `checkout.session.async_payment_succeeded`

Only e-books whose PDF filename matches the server-side product catalogue can be sold. Add each
final PDF under `E-books/`, then rebuild the API container. Use Stripe test mode until the full
payment, webhook, Resend delivery, and duplicate-event flow has passed.

The owner reports that the Resend DNS records are verified and the local untracked `.env` contains
the Stripe/Resend settings. Do not copy those values into source files or commits. Confirm that the
same variables exist on the deployment host before rebuilding. A real Stripe test-mode `$1` payment
completed successfully on 19 June 2026 and confirmed all of the following:

1. Checkout collects name, email, and phone number.
2. Stripe redirects to `checkout-success.html`.
3. The signed webhook returns HTTP 200.
4. Resend accepts the customer PDF as an attachment and returns an e-mail ID.
5. Replaying the same event does not send a duplicate delivery email.
6. The success page provides a Stripe-validated direct PDF download fallback.

Resend acceptance is not proof that the recipient mailbox has displayed the message. Outlook and
other clients may synchronize at different speeds. The API therefore records `emailAcceptedAt` and
`emailId`, while the paid download remains available independently of e-mail delivery timing.

---

## Deployment

The stack runs in an LXC container on a self-hosted Proxmox server.

| Resource | Value |
|---|---|
| Proxmox host | `192.168.0.100` (SSH as root) |
| LXC container | ID `102`, Debian 13, static IP `192.168.0.240` |
| Files in container | `/opt/bms-archive/` |
| Public domain | `bmsarchive.com` |

**Never SSH directly to `192.168.0.240`.** Always deploy via the Proxmox host using `pct push`.

```bash
# 1. Stage on Proxmox host
ssh root@192.168.0.100 "mkdir -p /tmp/bms-deploy"
scp docker-compose.yml Dockerfile Dockerfile.api nginx.conf server.js \
    package.json index.html checkout-success.html database.html grow.html \
    data.json tailwind.js robots.txt sitemap.xml og-image.png favicon.svg \
    root@192.168.0.100:/tmp/bms-deploy/
ssh root@192.168.0.100 "mkdir -p /tmp/bms-deploy/E-books"
scp E-books/BMS_Archive_The_Little_Guide.pdf \
    root@192.168.0.100:/tmp/bms-deploy/E-books/

# 2. Push into LXC container
ssh root@192.168.0.100 "
  for f in docker-compose.yml Dockerfile Dockerfile.api nginx.conf server.js \
            package.json index.html checkout-success.html database.html grow.html data.json tailwind.js \
            robots.txt sitemap.xml og-image.png favicon.svg; do
    pct push 102 /tmp/bms-deploy/\$f /opt/bms-archive/\$f
  done
  pct exec 102 -- mkdir -p /opt/bms-archive/E-books
  pct push 102 /tmp/bms-deploy/E-books/BMS_Archive_The_Little_Guide.pdf \
    /opt/bms-archive/E-books/BMS_Archive_The_Little_Guide.pdf
"

# 3. Rebuild and restart
ssh root@192.168.0.100 "pct exec 102 -- bash -c 'cd /opt/bms-archive && docker compose up -d --build'"
```

**Never deploy:** `.env` from the workstation, `admin.html`, `admin_server.py`, `build_plants.py`,
`scripts/`, `docs/`, `.claude/`, `tmp/`, `output/`, or editable e-book source files.

---

## Developer reference

| Resource | Path |
|---|---|
| Project conventions and rules | [`CLAUDE.md`](CLAUDE.md) |
| Workflow guide and slash commands | [`docs/SHORTCUTS_AND_WORKFLOWS.md`](docs/SHORTCUTS_AND_WORKFLOWS.md) |
| Roadmap | [`docs/ROADMAP.md`](docs/ROADMAP.md) |
| Monograph template | [`docs/templates/MONOGRAPH_TEMPLATE.md`](docs/templates/MONOGRAPH_TEMPLATE.md) |
| Evidence scoring rubric | [`docs/rubrics/EVIDENCE_SCORING.md`](docs/rubrics/EVIDENCE_SCORING.md) |
| Architectural decisions | [`docs/DECISIONS.md`](docs/DECISIONS.md) |

**Claude Code slash commands:**

| Command | Purpose |
|---|---|
| `/project:daily-check` | Start-of-session status check |
| `/project:add-monograph [name]` | Full pipeline to add a new species profile |
| `/project:validate-data` | Run all data.json validation checks |
| `/project:prepare-deploy` | Pre-deployment checklist |
| `/project:security-review` | Security and privacy review |

Full command list in [`docs/SHORTCUTS_AND_WORKFLOWS.md`](docs/SHORTCUTS_AND_WORKFLOWS.md).
