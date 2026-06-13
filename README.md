# BMS Archive

**bmsarchive.com** — An evidence-based phytomedicine database. A searchable archive of 50 botanical and fungal monographs sourced from peer-reviewed literature (PubMed). For educational and research purposes only — not medical advice.

Instagram: [@thebmsarchive](https://instagram.com/thebmsarchive)

---

## What it is

Two public pages:

| Page | Purpose |
|---|---|
| `index.html` | Landing page — hero, email waitlist form, medical disclaimer |
| `database.html` | Searchable monograph database — grid, type filter, modal detail view |

The database contains 50 entries: 25 medicinal fungi + 25 medicinal plants. Every profile has PubMed-verified citations, ADME pharmacokinetics, mechanism of action, safety data, and special precautions (pregnancy, lactation, hepatic/renal impairment).

---

## Stack

| Layer | Detail |
|---|---|
| HTML/CSS | Plain HTML5 + Tailwind CSS v3.4.17 (served locally as `tailwind.js`) |
| JavaScript | Vanilla JS, inline in each HTML file — no bundler, no framework |
| Font | Inter (Google Fonts, non-blocking preload) |
| Data | `data.json` — 50 monograph entries, PubMed-verified |
| Web server | Nginx 1.27-alpine (Docker) |
| API server | Node.js 20-alpine (Docker), zero npm dependencies |
| Container orchestration | Docker Compose v2+ |
| Deployment host | LXC container on self-hosted Proxmox server |
| Admin tool | Python 3 stdlib HTTP server — local only, never deployed |
| Data-seeding | Python 3 + `anthropic` SDK + NCBI APIs — offline only |

No build step. No `package.json`. No framework.

---

## File structure

```
BMS website/
├── index.html            # Landing page
├── database.html         # Searchable database
├── data.json             # 50 monograph entries (25 Fungi + 25 Plants)
├── tailwind.js           # Tailwind CSS v3.4.17 — local bundle, do not replace with CDN
├── nginx.conf            # Nginx: HTTPS, gzip, cache, security headers, rate limiting
├── Dockerfile            # nginx:1.27-alpine — serves static files
├── Dockerfile.api        # node:20-alpine — runs server.js
├── docker-compose.yml    # Two services: web (Nginx) + api (Node.js)
├── server.js             # Node.js waitlist API — POST /api/waitlist
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

**No install needed** — open `index.html` or `database.html` directly in a browser.

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
    index.html database.html data.json tailwind.js \
    robots.txt sitemap.xml og-image.png favicon.svg \
    root@192.168.0.100:/tmp/bms-deploy/

# 2. Push into LXC container
ssh root@192.168.0.100 "
  for f in docker-compose.yml Dockerfile Dockerfile.api nginx.conf server.js \
            index.html database.html data.json tailwind.js \
            robots.txt sitemap.xml og-image.png favicon.svg; do
    pct push 102 /tmp/bms-deploy/\$f /opt/bms-archive/\$f
  done
"

# 3. Rebuild and restart
ssh root@192.168.0.100 "pct exec 102 -- bash -c 'cd /opt/bms-archive && docker compose up -d --build'"
```

**Never deploy:** `admin.html`, `admin_server.py`, `build_plants.py`, `scripts/`, `docs/`, `.claude/`

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
