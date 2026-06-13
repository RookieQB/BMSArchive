---
description: Security and privacy review for BMS Archive. Checks API routes, forms, input validation, secrets, Nginx config, admin endpoints, and deployment safety. Use: /project:security-review [optional: specific file or feature to review]
---

You are performing a security and privacy review for BMS Archive.

Focus area (if specified): **$ARGUMENTS**

Use `security-privacy-agent` to conduct this review.

---

## Step 1 — Identify scope

If "$ARGUMENTS" specifies a file or feature, focus the review on that area.
If no argument is given, run a full project security review covering all areas below.

---

## Step 2 — Read relevant files

Read the files relevant to the scope:
- `server.js` — Node.js waitlist API
- `nginx.conf` — reverse proxy, TLS, headers, caching
- `docker-compose.yml` — container config, volume exposure, port mapping
- `Dockerfile`, `Dockerfile.api` — what gets deployed
- `index.html` — form submission code (`wireForm` function)
- `admin_server.py` — local admin server (check it is NOT in Dockerfile)
- `.claude/settings.local.json` — check no secrets present
- Any new files added in "$ARGUMENTS"

---

## Step 3 — Run the security checklist

**Secrets and credentials:**
- [ ] No API keys, passwords, or tokens in any committed file
- [ ] `ANTHROPIC_API_KEY` is only used as a shell environment variable, never written to a file
- [ ] No `.env` file with real values is committed
- [ ] `.claude/settings.local.json` contains no secret values

**API security (`server.js`):**
- [ ] Email input is validated by regex before any file write
- [ ] Email is normalized (trimmed, lowercased) before storage
- [ ] JSON parse errors return 400, not a stack trace
- [ ] Only `POST /api/waitlist` is handled; all other paths return 404
- [ ] No stack traces or internal paths leak in error responses
- [ ] Rate limiting: flag if absent (currently not implemented — known gap)

**Nginx configuration:**
- [ ] HTTP → HTTPS redirect is in place (port 80 returns 301)
- [ ] TLS 1.2 and 1.3 only; no TLS 1.0/1.1
- [ ] HSTS header present: `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`
- [ ] `X-Frame-Options: SAMEORIGIN`
- [ ] `X-Content-Type-Options: nosniff`
- [ ] `Referrer-Policy: strict-origin-when-cross-origin`
- [ ] `X-XSS-Protection: 1; mode=block`
- [ ] CSP header: flag if absent (currently missing — known gap)

**Admin panel:**
- [ ] `admin.html` is NOT in `Dockerfile` (COPY instructions)
- [ ] `admin_server.py` is NOT in `Dockerfile.api`
- [ ] `admin_server.py` binds to `127.0.0.1` only, not `0.0.0.0`
- [ ] Admin panel has no network exposure outside localhost

**Docker and deployment:**
- [ ] No unexpected ports exposed in `docker-compose.yml`
- [ ] Named volume `waitlist_data` is correctly configured
- [ ] TLS cert volume mounts use `:ro` (read-only)
- [ ] `admin.html`, `admin_server.py`, `build_plants.py`, `scripts/` are excluded from deploy

**Input validation (any new forms):**
- [ ] All user input is validated server-side before use
- [ ] File upload constraints if uploads exist (none currently)
- [ ] CORS is not opened beyond necessary scope

---

## Step 4 — Produce a security report

For each issue found:

```
RISK LEVEL: Critical / High / Medium / Low / Informational
COMPONENT: [file or feature]
ISSUE: [description]
ATTACK VECTOR: [how it could be exploited]
CURRENT MITIGATION: [what's in place, if any]
RECOMMENDED FIX: [specific change]
PRIORITY: Immediate / Before next deploy / Future improvement
```

Final summary:
```
SECURITY REVIEW SUMMARY
Critical issues: [N]
High issues:     [N]
Medium issues:   [N]
Known accepted gaps: [list — e.g. no rate limiting, no CSP]

Overall: APPROVED FOR DEPLOY / REQUIRES FIXES BEFORE DEPLOY
```

---

## Rules

- **Never print or log any secret value** — reference by name only
- **Never weaken authentication or authorization** for any reason
- **Never approve a deployment that includes admin tools** in the deployed file set
- **Flag every absent security header** even if it is a low-priority gap
- **Do not invent security vulnerabilities** — report only what can be confirmed from the code
