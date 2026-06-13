---
description: Master workflow — full production deployment readiness check for BMS Archive. Runs security, ops, QA, validation, and SEO checks in sequence. Produces the exact deploy commands for manual review. Does not deploy automatically.
---

You are running the **BMS Archive pre-deploy master workflow**.

This orchestrates `security-privacy-agent`, `ops-performance-agent`, and `qa-test-agent` in the correct sequence. Deploy commands are produced for manual review — they are never run automatically.

---

## PHASE 1 — Data validation (blocking)

Run before anything else. A broken database must not be deployed.

```bash
python3 -c "import json; data=json.load(open('data.json')); print(f'JSON valid — {len(data)} entries')"
python3 scripts/validate_archive_data.py
```

**If any ERROR: STOP. Fix with `/workflow:fix-and-verify` before proceeding.**

Safe-claim warnings are non-blocking for deployment but should be noted.

---

## PHASE 2 — Security review (security-privacy-agent)

Use `security-privacy-agent` to check:

**Secrets:**
- [ ] No `ANTHROPIC_API_KEY` or any API key in any staged/committed file
- [ ] No `.env` file with real values committed
- [ ] `.claude/settings.local.json` contains no secret values

**Deploy file list — CRITICAL:**
Read `Dockerfile` and confirm it copies only:
```
nginx.conf, index.html, database.html, data.json, tailwind.js, robots.txt, sitemap.xml, og-image.png, favicon.svg
```

Confirm these files are **NOT** in Dockerfile or docker-compose.yml commands:
- [ ] `admin.html` — excluded ✓
- [ ] `admin_server.py` — excluded ✓
- [ ] `build_plants.py` — excluded ✓
- [ ] `scripts/` — excluded ✓
- [ ] `CLAUDE.md` — excluded ✓
- [ ] `.claude/` — excluded ✓
- [ ] `docs/` — excluded ✓
- [ ] `examples/` — excluded ✓
- [ ] `docs/research-inbox/` — excluded ✓

**Nginx security headers (read `nginx.conf`):**
- [ ] `Strict-Transport-Security` with `preload` ✓
- [ ] `X-Frame-Options: SAMEORIGIN` ✓
- [ ] `X-Content-Type-Options: nosniff` ✓
- [ ] `Referrer-Policy: strict-origin-when-cross-origin` ✓
- [ ] HTTP → HTTPS redirect in place ✓
- [ ] TLS 1.2+ only ✓

**API (`server.js`):**
- [ ] Email regex validation present ✓
- [ ] JSON parse errors return 400, not stack trace ✓
- [ ] Only POST /api/waitlist handled ✓
- [ ] Rate limiting: flag as known gap if absent

**Known security gaps to note (non-blocking):**
- No rate limiting on `/api/waitlist`

Security result: APPROVED / BLOCKED — [reason]

---

## PHASE 3 — Ops readiness (ops-performance-agent)

Confirm deploy files exist locally:
```bash
for f in docker-compose.yml Dockerfile Dockerfile.api nginx.conf server.js index.html database.html data.json tailwind.js robots.txt sitemap.xml og-image.png favicon.svg; do
  [ -f "$f" ] && echo "✓ $f" || echo "✗ MISSING: $f"
done
```

Check SEO status:
```bash
grep -c "<title>" index.html database.html
grep -c "og:title\|og:description\|og:url" index.html
grep "og:image" index.html && echo "og:image present" || echo "⚠ og:image missing"
ls robots.txt sitemap.xml 2>/dev/null || echo "⚠ Missing: robots.txt, sitemap.xml"
```

Check for research-inbox draft content in deployed files:
```bash
grep -i "research-inbox\|draft\|pending review\|qa_status" index.html database.html 2>/dev/null && echo "⚠ DRAFT CONTENT FOUND" || echo "✓ No draft content in deployed files"
```

Check TLS certificates on server (informational only):
```bash
echo | openssl s_client -connect bmsarchive.com:443 -servername bmsarchive.com 2>/dev/null | openssl x509 -noout -dates 2>/dev/null || echo "TLS check requires network access — verify manually"
```

---

## PHASE 4 — QA verification (qa-test-agent)

```bash
git status
git diff --name-only HEAD~1 HEAD 2>/dev/null | head -20
```

Confirm browser checks are ready to run after deploy:
- `https://bmsarchive.com` — loads, returns 200
- `https://bmsarchive.com/database.html` — loads, grid renders
- `https://bmsarchive.com/data.json` — returns valid JSON
- Newsletter form submits successfully

---

## PHASE 5 — Generate deploy commands

Produce the exact deploy sequence for manual review:

```bash
# ── BMS Archive Deploy Sequence ────────────────────────────────────────────
# Review carefully before running. Each step shown separately.

# 1. Stage on Proxmox host
ssh root@192.168.0.100 "mkdir -p /tmp/bms-deploy"

scp docker-compose.yml Dockerfile Dockerfile.api nginx.conf server.js \
    index.html database.html data.json tailwind.js robots.txt sitemap.xml og-image.png favicon.svg \
    root@192.168.0.100:/tmp/bms-deploy/

# 2. Push into LXC container (ID 102)
ssh root@192.168.0.100 "
  for f in docker-compose.yml Dockerfile Dockerfile.api nginx.conf server.js \
            index.html database.html data.json tailwind.js robots.txt sitemap.xml og-image.png favicon.svg; do
    pct push 102 /tmp/bms-deploy/\$f /opt/bms-archive/\$f
  done
"

# 3. Rebuild and restart
ssh root@192.168.0.100 "pct exec 102 -- bash -c 'cd /opt/bms-archive && docker compose up -d --build'"

# 4. Verify containers running
ssh root@192.168.0.100 "pct exec 102 -- bash -c 'docker ps'"

# ── DO NOT RUN THESE AUTOMATICALLY ─────────────────────────────────────────
# Review the commands above, then run them manually.
```

**Never run these commands automatically. Always show for manual review first.**

---

## PHASE 6 — Post-deploy GitHub sync (github-sync-agent)

After the user confirms deployment succeeded, invoke `github-sync-agent` to commit and push all changes to `origin/main`.

The agent will:
1. Stage all appropriate files (excludes `.DS_Store`, `.env`, `plants_progress.json`, secrets)
2. Write a deployment-tagged commit message (`Deploy YYYY-MM-DD — <summary>`)
3. Push to `git@github.com:RookieQB/BMSArchive.git` on branch `main`
4. Confirm with `git log --oneline -3`

**Do not run this step before confirming the deployment succeeded.**
If the deploy was blocked or failed, skip Phase 6.

---

## PHASE 7 — Deployment readiness report

```
## Pre-Deploy Report
Date: [today]

### Data validation
JSON valid:          [PASS/FAIL]
Validation errors:   [N]
Validation warnings: [N] — [note safe-claim warnings]

### Security
Secrets check:       [PASS/FAIL]
Deploy file list:    [PASS/FAIL — admin tools excluded]
Nginx headers:       [PASS/FAIL]
API validation:      [PASS/FAIL]
Known gaps:          [list — e.g. no rate limiting, no CSP]

### Ops
All deploy files present: [PASS/FAIL]
SEO: og:image             [present/missing]
SEO: robots.txt           [present/missing]
SEO: sitemap.xml          [present/missing]
Draft content in deployed files: [None/FOUND — FAIL]

### QA
Browser checks:      [pending — run after deploy]

### Blocking issues
[list or "None"]

### Deploy commands
[shown above in Phase 5 — awaiting manual review and execution]

### GitHub sync
[pending — runs after user confirms deploy succeeded]

### OVERALL STATUS
[READY — deploy commands shown above for manual execution]
[BLOCKED — [reason] — fix before deploying]
```

---

## Rules

- **Never run deploy commands automatically** — always produce for manual review
- **Block if data validation has errors**
- **Block if admin tools are in deploy file list**
- **Block if secrets are found in committed files**
- **Block if draft/inbox content appears in deployed files**
- **Do not add Instagram or social media content**
