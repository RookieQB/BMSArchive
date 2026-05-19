# BMS Archive — v3

**bmsarchive.com** — An evidence-based phytomedicine database linking clinical research to botanical medicines. Currently in pre-launch; Phase 1 is a static landing page + searchable database with a functional email waitlist.

Instagram: [@thebmsarchive](https://instagram.com/thebmsarchive)

---

## What's new in v3

- **Functional waitlist** — email form now submits via `fetch()` to a real Node.js backend; emails saved to a persistent `waitlist.txt` on the server
- **Node.js API** (`server.js`) — lightweight HTTP server on port 3000, no npm dependencies, validates email format, appends timestamped entries to `/data/waitlist.txt`
- **Nginx reverse proxy** — `/api/` traffic proxied to the Node.js container; everything on port 80, no CORS
- **Two-container Docker setup** — `web` (Nginx) + `api` (Node.js) services via Docker Compose, named volume `waitlist_data` for persistence across rebuilds
- **Polished form UX** — solid-green "You're on the list! 🎉" confirmation, inline error messages for invalid email or network failure, button disabled during submit

## What's new in v2

- **Searchable database** (`database.html`) — 25 medicinal fungi profiles with live filtering by type and category
- **PubMed-verified sources** — all `sources.top_studies_urls` replaced with real PMIDs fetched from the NCBI eSearch API; zero hallucinated citations
- **Real article counts** — `article_count` per species pulled live from PubMed
- **Pharmacokinetics: Distribution** — added to all 25 profiles (tissue distribution, protein binding)
- **Mechanism of action** — key pharmacological targets (`<strong>` tags) highlighted across all 25 entries
- **Local Tailwind bundle** — Tailwind CSS v3.4.17 served locally (`tailwind.js`); no CDN render-blocking
- **Non-blocking fonts** — Google Fonts loaded via `preload` / `onload` pattern
- **Network fix** — container moved to `192.168.0.240` (resolved IP conflict with DHCP pool)

---

## What the site is

A two-page static site:

| Page | Purpose |
|---|---|
| `index.html` | Landing page — brand intro, email waitlist |
| `database.html` | Searchable phytomedicine database (25 entries, modal detail view) |

The email form has a JS success state but **no backend yet**. Next integration step is Formspree, Mailchimp, or ConvertKit (see `wireForm()` in `index.html`).

---

## Stack

| Layer | Choice |
|---|---|
| HTML/CSS | Plain HTML5 + Tailwind CSS v3.4.17 (local bundle) |
| Font | Inter via Google Fonts (non-blocking preload) |
| Data | `data.json` — 25 fungi profiles, PubMed-verified |
| Server | Nginx 1.27-alpine |
| Container | Docker + Docker Compose (Compose v2+) |

No build step, no framework, no bundler.

---

## File structure

```
BMS website/
├── index.html          # Landing page — hero, features, waitlist form, footer
├── database.html       # Phytomedicine database — grid, filters, modal detail view
├── data.json           # 25 medicinal fungi profiles (PubMed-verified sources)
├── tailwind.js         # Tailwind CSS v3.4.17 — served locally, no CDN dependency
├── nginx.conf          # Nginx config: gzip, cache headers, security headers
├── Dockerfile          # FROM nginx:1.27-alpine; copies all site assets
├── docker-compose.yml  # Single service, port 80:80, restart: unless-stopped
└── update_sources.py   # NCBI eSearch script — refreshes PMIDs and article counts
```

---

## Database schema (`data.json`)

Each of the 25 entries follows this structure:

```json
{
  "scientific_name": "Ganoderma lucidum",
  "common_name": "Reishi / Lingzhi",
  "type": "Fungi",
  "article_count": 3033,
  "primary_categories": ["Immunomodulation", "Oncology support", "Adaptogen"],
  "sources": {
    "top_studies_urls": [
      "https://pubmed.ncbi.nlm.nih.gov/42148569/",
      "https://pubmed.ncbi.nlm.nih.gov/42147328/",
      "https://pubmed.ncbi.nlm.nih.gov/42142826/"
    ]
  },
  "narrative_summary": {
    "historical_use": "...",
    "modern_application": "...",
    "side_effects": "...",
    "contraindications": "..."
  },
  "clinical_data": {
    "used_part": "Fruiting body and mycelium",
    "primary_active_compounds": ["..."],
    "mechanism_of_action": "... <strong>TLR-4</strong> / <strong>NF-κB</strong> ...",
    "pharmacokinetics": {
      "absorption": "...",
      "distribution": "...",
      "metabolism": "...",
      "excretion": "..."
    },
    "safety_and_interactions": {
      "drug_interactions": "...",
      "toxicity": "..."
    },
    "special_precautions": {
      "pregnancy": "...",
      "lactation": "...",
      "hepatic_impairment": "...",
      "renal_impairment": "..."
    }
  }
}
```

### Refreshing sources

`update_sources.py` queries the NCBI PubMed eSearch API (anonymous, rate-limited to 0.5 s per request) and overwrites `article_count` and `sources.top_studies_urls` for all 25 entries:

```bash
cd "BMS website"
python3 update_sources.py
```

---

## Deployment

The site runs in a Docker container inside an LXC container on a self-hosted Proxmox server.

| | |
|---|---|
| Proxmox host | `192.168.0.100` (SSH as root) |
| LXC container | ID `102`, Debian 13 (Trixie), static IP `192.168.0.240` |
| Docker | v29.5.1 + Compose v5.1.3, enabled on boot |
| Files in container | `/opt/bms-archive/` |

### Deploy workflow

```bash
# 1. Stage files on the Proxmox host
ssh root@192.168.0.100 "mkdir -p /tmp/bms-deploy"
scp docker-compose.yml Dockerfile nginx.conf index.html database.html data.json tailwind.js \
    root@192.168.0.100:/tmp/bms-deploy/

# 2. Push files into the container
ssh root@192.168.0.100 "
  for f in docker-compose.yml Dockerfile nginx.conf index.html database.html data.json tailwind.js; do
    pct push 102 /tmp/bms-deploy/\$f /opt/bms-archive/\$f
  done
"

# 3. Build and start
ssh root@192.168.0.100 "pct exec 102 -- bash -c 'cd /opt/bms-archive && docker compose up -d --build'"
```

### Known server fixes (already applied)

| Issue | Fix |
|---|---|
| Slow DNS in Debian 13 LXC | `/etc/resolv.conf` + `/etc/docker/daemon.json` set to `8.8.8.8` / `8.8.4.4` |
| IP conflict at `192.168.0.140` | Container moved to static IP `192.168.0.240` |
| Proxmox firewall bridge loop | `firewall=0` set on LXC net0 (`pct set 102 -net0 ...`) |

---

## Local development

No install needed — open `index.html` or `database.html` directly in a browser. To test with the actual Nginx config:

```bash
docker compose up --build
# Site at http://localhost:80
```

---

## Roadmap

- [ ] **Email backend** — wire `wireForm()` in `index.html` to Formspree / Mailchimp / ConvertKit
- [ ] **TLS** — Certbot + Let's Encrypt on the container, port 443 forwarded from router
- [ ] **Public DNS** — point `bmsarchive.com` A record to home public IP; DDNS if dynamic
- [ ] **Expand database** — add herbs/plants beyond fungi; increase to 50+ entries
- [ ] **Phase 2** — full interactive phytomedicine database (stack TBD)
