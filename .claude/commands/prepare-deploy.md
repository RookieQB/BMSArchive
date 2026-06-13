---
description: Full pre-deployment readiness check for BMS Archive. Runs security review, ops check, and QA before pushing to the Proxmox/LXC/Docker production server.
---

You are preparing BMS Archive for production deployment.

Use `security-privacy-agent`, `ops-performance-agent`, and `qa-test-agent` in that order.

BMS Archive deploys via Proxmox host `192.168.0.100` using `pct push` into LXC container `102`. Never SSH directly to `192.168.0.240`.

---

## Step 1 — Security pre-check (security-privacy-agent)

Verify:
- [ ] No secrets or API keys in any file being deployed
- [ ] `admin.html` is NOT in the deploy file list
- [ ] `admin_server.py` is NOT in the deploy file list
- [ ] `build_plants.py` is NOT in the deploy file list
- [ ] `scripts/` directory is NOT in the deploy file list
- [ ] Nginx security headers are all present in `nginx.conf`
- [ ] TLS redirect (HTTP → HTTPS) is intact
- [ ] HSTS is present

Read `Dockerfile` to confirm it only copies: `nginx.conf`, `index.html`, `database.html`, `data.json`, `tailwind.js`.

---

## Step 2 — Data validation

```bash
python3 -c "import json; data=json.load(open('data.json')); print(f'data.json: {len(data)} entries — valid')"
python3 scripts/validate_archive_data.py
```

Do not deploy if data.json fails validation.

---

## Step 3 — Ops readiness check (ops-performance-agent)

Verify the deploy file list is complete and correct:

```
Deploy files:
  docker-compose.yml    ✓/✗
  Dockerfile            ✓/✗
  Dockerfile.api        ✓/✗
  nginx.conf            ✓/✗
  server.js             ✓/✗
  index.html            ✓/✗
  database.html         ✓/✗
  data.json             ✓/✗
  tailwind.js           ✓/✗

Excluded (must NOT be deployed):
  admin.html            excluded ✓/✗
  admin_server.py       excluded ✓/✗
  build_plants.py       excluded ✓/✗
  scripts/              excluded ✓/✗
  CLAUDE.md             excluded ✓/✗
  .claude/              excluded ✓/✗
  docs/                 excluded ✓/✗
  examples/             excluded ✓/✗
```

Check SEO readiness:
- [ ] `<title>` tags present on all pages
- [ ] `<meta description>` present on all pages
- [ ] `og:title`, `og:description`, `og:url` present on `index.html`
- [ ] `robots.txt` — present or flagged as missing
- [ ] `sitemap.xml` — present or flagged as missing
- [ ] Favicon — present or flagged as missing

---

## Step 4 — Generate the deploy commands

Produce the exact deploy command sequence ready to run:

```bash
# 1. Stage on Proxmox host
ssh root@192.168.0.100 "mkdir -p /tmp/bms-deploy"
scp docker-compose.yml Dockerfile Dockerfile.api nginx.conf server.js \
    index.html database.html data.json tailwind.js \
    root@192.168.0.100:/tmp/bms-deploy/

# 2. Push into LXC container
ssh root@192.168.0.100 "
  for f in docker-compose.yml Dockerfile Dockerfile.api nginx.conf server.js \
            index.html database.html data.json tailwind.js; do
    pct push 102 /tmp/bms-deploy/\$f /opt/bms-archive/\$f
  done
"

# 3. Rebuild and restart
ssh root@192.168.0.100 "pct exec 102 -- bash -c 'cd /opt/bms-archive && docker compose up -d --build'"

# 4. Verify
ssh root@192.168.0.100 "pct exec 102 -- bash -c 'docker ps'"
```

**Do not run these commands automatically.** Show them to the user for manual review and approval first.

---

## Step 5 — GitHub sync (github-sync-agent)

After the user confirms the deployment succeeded, invoke `github-sync-agent`.

It will commit all changed and untracked files (excluding `.DS_Store`, `.env`, secrets) with a deployment-tagged message and push to `origin/main`.

**Only run this step after deployment is confirmed successful.**

---

## Step 6 — Post-deploy verification checklist

After deploy, verify:
- [ ] `https://bmsarchive.com` loads and returns 200
- [ ] `https://bmsarchive.com/database.html` loads and renders entries
- [ ] `https://bmsarchive.com/data.json` returns valid JSON
- [ ] Newsletter form submits successfully
- [ ] TLS certificate is valid (check expiry date)
- [ ] No Nginx error logs

---

## Step 7 — Produce deployment report

```
## Deployment Readiness Report

Security: APPROVED / BLOCKED — [reason]
Data validation: PASS / FAIL
Ops file list: COMPLETE / MISSING — [list]
SEO gaps: [list or None]

Deploy commands: SHOWN FOR REVIEW
Status: READY TO DEPLOY / DO NOT DEPLOY — [reason]
```

---

## Rules

- **Never run the deploy commands automatically** — always show them for user approval first
- **Block deployment if security review fails**
- **Block deployment if data.json validation fails**
- **Block deployment if admin tools are in the deploy file list**
- **Never modify production config** without explaining the impact
