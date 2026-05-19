# BMS Archive

**bmsarchive.com** — An evidence-based phytomedicine database linking clinical research to botanical medicines. Currently in pre-launch; Phase 1 is a static landing page with an email waitlist.

Instagram: [@thebmsarchive](https://instagram.com/thebmsarchive)

---

## What the site is

A single-page landing site that:

- Introduces the BMS Archive concept (structured, peer-reviewed botanical medicine data)
- Collects waitlist emails ahead of the full database launch
- Links to the Instagram account

The email form has a JS success state wired in but **no backend yet** — form submissions are not stored anywhere. The next integration step is Formspree, Mailchimp, or ConvertKit (see `wireForm()` in `index.html`).

---

## Stack

| Layer | Choice |
|---|---|
| HTML/CSS | Plain HTML5 + Tailwind CSS (CDN) |
| Font | Inter via Google Fonts |
| Server | Nginx 1.27-alpine |
| Container | Docker + Docker Compose (Compose v2+) |

No build step, no framework, no bundler. Tailwind runs from CDN so `index.html` is the entire frontend.

---

## File structure

```
BMS website/
├── index.html          # Entire frontend — hero, features, waitlist form, footer
├── nginx.conf          # Nginx config: gzip, cache headers, security headers
├── Dockerfile          # FROM nginx:1.27-alpine, copies index.html + nginx.conf
└── docker-compose.yml  # Single service, port 80:80, restart: unless-stopped
```

---

## Deployment

The site runs in a Docker container inside an LXC container on a self-hosted Proxmox server.

| | |
|---|---|
| Proxmox host | `192.168.0.100` (SSH as root) |
| LXC container | ID `102`, Debian 13 (Trixie), static IP `192.168.0.140` |
| Docker | v29.5.1 + Compose v5.1.3, enabled on boot |
| Files in container | `/opt/bms-archive/` |

### Deploy workflow

SSH to Proxmox cannot reach the container directly (unprivileged LXC), so files are pushed via `pct push`:

```bash
# 1. Stage files on the Proxmox host
ssh root@192.168.0.100 "mkdir -p /tmp/bms-deploy"
scp docker-compose.yml Dockerfile nginx.conf index.html root@192.168.0.100:/tmp/bms-deploy/

# 2. Push files into the container
ssh root@192.168.0.100 "
  for f in docker-compose.yml Dockerfile nginx.conf index.html; do
    pct push 102 /tmp/bms-deploy/\$f /opt/bms-archive/\$f
  done
"

# 3. Build and start
ssh root@192.168.0.100 "pct exec 102 -- bash -c 'cd /opt/bms-archive && docker compose up -d --build'"
```

### DNS fix (applied once, already in place)

Debian 13 LXC containers can have slow DNS resolution that breaks `docker build` pulls. The fix:

```bash
# /etc/resolv.conf inside container 102
nameserver 8.8.8.8
nameserver 8.8.4.4
options timeout:2 attempts:3

# /etc/docker/daemon.json inside container 102
{ "dns": ["8.8.8.8", "8.8.4.4"], "dns-opts": ["timeout:2", "attempts:3"] }
```

---

## Local development

No install needed — just open `index.html` in a browser. To test with the actual Nginx config:

```bash
docker compose up --build
# Site available at http://localhost:80
```

---

## Roadmap

- [ ] **Email backend** — wire `wireForm()` in `index.html` to Formspree / Mailchimp / ConvertKit
- [ ] **TLS** — Certbot + Let's Encrypt on the container, port 443 forwarded from router
- [ ] **Public DNS** — point `bmsarchive.com` A record to home public IP, set up DDNS if dynamic
- [ ] **Phase 2** — the actual phytomedicine database (stack TBD)
