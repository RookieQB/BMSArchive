# Pre-deploy security review — ten plant additions

Date: 25 October 2026, Europe/Copenhagen.

PRE-DEPLOY AUDIT RESULT: PASS — scoped static data release; runtime operations checks remain separate.

Reviewed data SHA-256: `d68912d878d6c4e87762915b4099a91c981982d9acb290f932e41ec12d3c3638`.

## Release scope and conditions

Production transfer is **data.json only** into the existing Proxmox/LXC 102 deployment. The existing server-side image build regenerates monographs and sitemap. No API, checkout, environment, certificate, admin, Docker configuration or routing update is authorized by this release scope. Parent reports production byte hashes of `.dockerignore`, `Dockerfile`, `nginx.conf`, `database.html`, `index.html`, and `scripts/build_seo.py` already match the local SEO sources; this review does not independently recheck remote hashes.

GitHub scope is the ten-entry data update, generated `monographs/` and `sitemap.xml`, associated research and ten task documents, plus the already deployed SEO sources needed for reproducibility: `.dockerignore`, `Dockerfile`, `index.html`, `database.html`, `nginx.conf`, `scripts/build_seo.py`, `scripts/check_seo.py`, `docs/SEO.md`. Stage exact named files, not the entire dirty tree. Old local `server.js` and `checkout-success.html` changes differ from production and must be excluded from both deployment and this commit. Also exclude admin, unrelated CLAUDE/README edits, E-books, exports, output, tmp, environment and local runtime data.

## Critical blockers

None found for the exact reviewed data and scoped release. This is not approval to deploy unrelated dirty files or rebuild the API from local sources.

## High-priority issues

None introduced by the data-only release. Existing observations below are follow-up work, not a reason to broaden this deployment.

## Component review

### Public JSON and generated monographs

- COMPONENT REVIEWED: `data.json`, `database.html`, `scripts/build_seo.py`, generated-page path and link handling.
- RISK LEVEL: Low for this reviewed batch; Medium latent risk in trusted-data HTML sink.
- VULNERABILITY: Database `setHTML` writes trusted strings via innerHTML; arbitrary future malicious JSON could execute in that context. This batch contains no such strings.
- ATTACK VECTOR: Unauthorized or insufficiently reviewed future archive edits.
- CURRENT MITIGATION: All ten new entries recursively checked: only literal attribute-free `<strong>`/`</strong>` markup; no script/iframe/event-handler/javascript markers. All top-study links are exact HTTPS PubMed numeric-ID URLs. Other cited HTTPS domains are PubMed, EMA, NCCIH and Egyptian Drug Authority; no URL credentials. Prior 72 JSON objects exactly equal the saved baseline. All archive markup is strong emphasis except one existing subscript pair. SEO generator escapes scalar HTML and only restores six attribute-free formatting tags; links escape attributes and accept HTTP(S); JSON-LD escapes `<`; slug generation restricts paths to lowercase ASCII letters, digits and hyphens.
- RECOMMENDED FIX: Consider a shared allowlist sanitizer for future archive writes. Maintain the per-release trusted-data check.
- PRIORITY: Future.

### Secrets and public research files

- COMPONENT REVIEWED: Candidate GitHub text sources and research artifacts, including extracted regulatory PDF text.
- RISK LEVEL: Low.
- VULNERABILITY: None identified in the scoped files.
- ATTACK VECTOR: Accidental credential inclusion during broad staging.
- CURRENT MITIGATION: Scanned 211 candidate files, including eight extracted PDFs, for credential assignments and Anthropic, Stripe, webhook, GitHub, Resend, AWS and private-key formats across two passes. No actual credential values found. Six loose OpenAI-pattern matches in three downloaded NCCIH HTML files were inspected without printing matched values and proved to be ordinary public page/build asset slugs containing the word “ask”; they are not keys. Placeholders and environment variable names are not treated as leaked values. Downloaded official HTML contains third-party site code as source evidence; it is not copied into the production web image.
- RECOMMENDED FIX: Explicitly stage the reviewed paths. Never add `.env`, runtime user data or unrelated E-book artifacts.
- PRIORITY: Before next deploy/commit: preserve scope.

### Container image and local admin exposure

- COMPONENT REVIEWED: `.dockerignore`, `Dockerfile`, `Dockerfile.api`, `docker-compose.yml`, `admin_server.py` binding.
- RISK LEVEL: Low for data release; Informational hardening opportunity.
- VULNERABILITY: `.dockerignore` does not exclude every local `tmp/`, `output/` or `exports/` directory, so they could enter a build context; explicit Docker COPY statements do not place them in the web image.
- ATTACK VECTOR: Future broad COPY or indiscriminate source transfer.
- CURRENT MITIGATION: Web image copies only named public assets and SEO-generated pages; no admin/server/build_plants/research/env files copied. `.env`, admin files and research are excluded from context. API image has separate explicit server/package/PDF COPY statements and is outside this release. Compose exposes only web 80/443; API has no host port mapping. Admin binds `127.0.0.1` and is excluded from the image. Certificate mounts are read-only. Persistent waitlist volume remains defined and untouched.
- RECOMMENDED FIX: In future hardening, exclude local export/temp/output directories from build context; do not alter configuration as part of this data release.
- PRIORITY: Future.

### Existing TLS, headers and traffic controls

- COMPONENT REVIEWED: Current local `nginx.conf`, reported by parent to match production.
- RISK LEVEL: Low; existing Medium hardening limitations.
- VULNERABILITY: Asset location overrides inherited add_header directives and repeats only nosniff plus cache headers; CSP permits unsafe-inline. Generic `/api/` status/download endpoints do not share form rate limits. Nginx version disclosure is not explicitly disabled.
- ATTACK VECTOR: Existing response-header gaps or abuse of unthrottled session lookups; not introduced by data.
- CURRENT MITIGATION: HTTP redirects to HTTPS except ACME; TLS 1.2/1.3; HSTS, SAMEORIGIN, nosniff, strict-origin-when-cross-origin, and CSP at server scope. CSP restricts origin families, objects and form targets. Waitlist is limited to 5 requests/minute with burst 3; checkout 10/minute with burst 5; 429 configured. HTML/JSON/monograph locations do not override the server security headers.
- RECOMMENDED FIX: Future review of consistent asset headers, nonce/hash-based script policy, non-webhook API throttling and server_tokens off. Preserve existing controls during this release.
- PRIORITY: Future.

### Existing API and privacy handling — inspection only

- COMPONENT REVIEWED: Current local `server.js`, which differs from production and is excluded.
- RISK LEVEL: Informational for this deployment; Medium existing robustness/privacy follow-up.
- VULNERABILITY: Session status returns customer email to the holder of a checkout session ID; session URLs therefore carry bearer sensitivity. Global URL construction lacks an explicit exception handler. Request body handling caps accumulated content but does not abort a continuing oversized stream. These are existing code observations, not newly deployed changes.
- ATTACK VECTOR: Leaked session IDs, malformed request targets, repeated API requests.
- CURRENT MITIGATION: Server-owned prices and product filenames; email normalization and regex validation; explicit consent checks; 256 KiB body limit with 413; generic public API errors without stack paths; no permissive CORS response; Stripe webhook signature verification against raw bytes; completed/paid order validation; cryptographic short-lived one-use download grants in the local version; JSON responses no-store; download private/no-store; waitlist/fulfillment file creation mode 0600. Named volume persists user data. Production behavior of the excluded local checkout changes is not asserted.
- RECOMMENDED FIX: Review production API separately before its next change; preserve session URL confidentiality, consider status-response data minimization, guard request-target parsing and abort oversized uploads. Do not deploy local API changes now.
- PRIORITY: Future API maintenance.

## Checks run

- Git dirty-file inventory; deployment/GitHub allowlist compared with parent scope.
- SHA-256 of current data; parsed all 82 entries; exact prior-72 object equality to `/tmp/bms-plants-before-20261025.json`.
- Recursive new-entry HTML/event/URL scan; zero unsafe markup or link results.
- Candidate secret scanning with paths/counts only and manual classification of loose-pattern false positives; 211 scanned files including eight PDF text extracts; zero real credentials found.
- Static inspection of Docker COPY/context exclusions, admin binding, Compose port/volume configuration, Nginx TLS/header/rate-limit directives, API validation/error/privacy/authentication controls, and SEO escaping/URL/path handling.
- Final scientific gate report read; no scientific reapproval claimed by this security review.

## Checks not run

No live TLS/certificate probe, remote Nginx syntax/runtime inspection, deployed API comparison, container image filesystem inspection, live rate-limit test, pentest, vulnerability/dependency scan or volume ownership/backup verification. Parent owns runtime TLS, backups and `nginx -t` checks before/after deployment. Secret-pattern scanning is bounded to reviewed candidate content; it is not a guarantee of absence of every secret format or a full Git history audit.

## Files safe to deploy

`data.json` at the exact reviewed SHA-256. Generated monographs and sitemap may be regenerated by the existing production build. No other local dirty source should be transferred for this release.

## Files that must not be deployed

`.env`/keys, admin tools, source research and task files, local API/checkout edits, CLAUDE/README changes, E-books, exports, output, tmp, data-seeding scripts, downloaded source HTML/PDF files and runtime user-data volumes. Research/task sources may be included in the explicitly scoped GitHub commit, but not the production web root.

## Recommended next actions

Proceed to operations review for this exact hash and data-only transfer; verify backups, live TLS and existing Nginx validity. Recheck hash immediately before upload. Confirm generated pages and production count after rebuild, then commit/push only the explicit reviewed allowlist. No unrelated code changes are required by this review.
