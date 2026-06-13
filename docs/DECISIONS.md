# BMS Archive — Architectural and Scientific Decisions

> This document records decisions that are not obvious from the code. The purpose is to explain *why* something is the way it is, so future contributors do not "fix" it back to a worse state.
>
> Format: **Decision → Rationale → Alternatives considered → Status**

---

## Architecture

### A1 — No framework, no build step

**Decision:** The site uses plain HTML5, local Tailwind CSS (single file), and vanilla JS inline in HTML. No React, no Vue, no npm, no webpack, no build pipeline.

**Rationale:** The site is a static archive, not an app. Adding a framework would introduce dependency management, build steps, potential supply-chain risks, and maintenance overhead with no benefit. The site can be served by any HTTP server and edited without a development environment.

**Alternatives considered:** Next.js (rejected — overkill for static content), Astro (rejected — still a build step), pure HTML without Tailwind (rejected — Tailwind provides consistent design with no runtime cost).

**Status:** Permanent decision for Phase 1. Revisit only if Phase 3 (user accounts) is built.

---

### A2 — Local Tailwind file, not CDN

**Decision:** Tailwind CSS is served from a local `tailwind.js` file (v3.4.17, 443 KB), not from `cdn.tailwindcss.com`.

**Rationale:** The site should work offline for development, should not depend on Tailwind's CDN availability, and should not introduce an external CSP requirement. The file is version-pinned and known good.

**Alternatives considered:** CDN link (rejected — external dependency, CSP conflict), PostCSS build (rejected — requires npm build step).

**Status:** Permanent. Do not replace with a CDN link.

---

### A3 — data.json as the database

**Decision:** All 50 monograph entries are stored in a single `data.json` file, served directly by Nginx, with no database server.

**Rationale:** At 50 entries, a database server (PostgreSQL, SQLite, etc.) adds infrastructure complexity with no benefit. JSON is editable with the admin panel, version-controlled with git, and trivially backed up. The entire dataset fits in a single HTTP request.

**Alternatives considered:** SQLite (rejected — requires a backend API layer), PostgreSQL (rejected — overkill, requires container, no full-text search benefit at this scale), MDX files (rejected — requires build step).

**Status:** Revisit at ~500 entries or if full-text search is required.

---

### A4 — Docker Compose with two services

**Decision:** `web` (Nginx 1.27-alpine) serves static files and proxies `/api/*` to `api` (Node.js 20-alpine). Named volume `waitlist_data` persists the waitlist JSON file.

**Rationale:** Separation of concerns — static serving and API are separate processes. Alpine images are minimal. Named volume survives container rebuilds.

**Alternatives considered:** Single Node.js server serving both static files and API (rejected — Nginx is faster and simpler for static; Node overhead is unnecessary), serverless functions (rejected — requires external hosting).

**Status:** Current. If the waitlist grows, migrate to a proper database.

---

### A5 — Deployment via Proxmox/LXC pct push

**Decision:** Files are deployed from the local machine via SSH to the Proxmox host (`192.168.0.100`), which uses `pct push` to inject them into LXC container ID 102 (`192.168.0.240`). `pct exec` runs `docker compose up -d --build`.

**Rationale:** Direct SSH to the LXC container is not the operational pattern for this infrastructure. The Proxmox host is the management plane; containers are managed through it.

**Alternatives considered:** Direct SSH to .240 (rejected — not the correct operational pattern), CI/CD auto-deploy (rejected — Phase 1 is low-frequency deploy; risk of automated overwrite of live data).

**Status:** Current deployment method. Do not change to direct SSH without understanding the network topology.

---

### A6 — Admin panel is local-only, never deployed

**Decision:** `admin.html` and `admin_server.py` bind to `127.0.0.1:5050`. They are explicitly excluded from all Dockerfile COPY directives and deploy commands.

**Rationale:** The admin panel provides direct write access to `data.json` with no authentication layer. Running it on the public server would be a critical security vulnerability. It is a local editing tool only.

**Alternatives considered:** Auth-protected admin on server (deferred — adds complexity; local-only is sufficient for single-author site).

**Status:** Permanent constraint. Admin tools must never be deployed.

---

## Scientific and content decisions

### S1 — Evidence hierarchy A → U

**Decision:** All evidence claims are graded on a 7-level scale: A (SR-MA) → B (RCT) → C (CCT/OBS) → D (animal) → E (in vitro) → T (traditional use) → U (unknown).

**Rationale:** Evidence grading prevents overclaiming. Animal and in vitro evidence must not be presented as human efficacy. Traditional use is acknowledged but explicitly separated from clinical evidence. The scale is adapted from standard evidence-based medicine hierarchies (GRADE-adjacent).

**Alternatives considered:** Binary (clinical/not clinical) — rejected as too coarse; full GRADE scoring — rejected as requiring full text access and methodologist review.

**Status:** Current. See `docs/rubrics/EVIDENCE_SCORING.md` for detailed language guidelines.

---

### S2 — Taxonomy: POWO for plants, Index Fungorum for fungi

**Decision:** Plant accepted names are verified against Plants of the World Online (POWO / Kew). Fungal accepted names are verified against Index Fungorum.

**Rationale:** These are the globally recognised authorities for botanical and mycological nomenclature. Using them prevents synonym confusion (e.g., *Withania somnifera* vs *Physalis somnifera*) and ensures the scientific name field is stable.

**Alternatives considered:** NCBI Taxonomy (acceptable secondary check; covers both kingdoms but less authoritative than POWO/IF for botanical names).

**Status:** Mandatory. All `scientific_name` fields must be POWO/Index Fungorum-verified.

---

### S3 — "Fruiting body vs mycelium" must be documented

**Decision:** For all fungal monographs, the `clinical_data.used_part` field must specify whether studies used fruiting body, mycelium, or a standardised extract. The distinction must be carried through to efficacy and safety claims.

**Rationale:** The vast majority of commercially available fungal supplements use myceliated grain (mycelium on grain substrate), not fruiting bodies. Many studies use fruiting body extracts. The efficacy data for one does not automatically apply to the other. Blurring this distinction would be scientifically misleading.

**Status:** Mandatory. See `taxonomy-nomenclature-agent` for flagging rules.

---

### S4 — "Safe" is not a standalone claim

**Decision:** The word "safe" may not appear in any monograph field without being explicitly qualified by evidence type, duration, and population. "Generally safe" and "considered safe" are not acceptable without qualifiers.

**Rationale:** The validation script identified 37 instances of this language across the existing 50 entries (baseline: 0 errors, 37 warnings). Unqualified safety claims are scientifically inaccurate (absence of reported harm ≠ established safety), and are particularly dangerous in pregnancy/lactation contexts.

**Action required:** Run `/workflow:fix-safe-claims` to resolve all 37 instances.

**Status:** Active policy. See `scripts/validate_archive_data.py` for detection logic.

---

### S5 — No disease treatment claims

**Decision:** No monograph text may imply that a botanical or fungal preparation treats, cures, prevents, or diagnoses any disease. Language must describe observed outcomes in studies, not clinical recommendations.

**Rationale:** BMS Archive is an evidence archive, not a medical advice platform. Disease treatment claims would constitute medical advice and create legal exposure. The site's disclaimer reinforces this, but content must not contradict it.

**Status:** Permanent. Enforced by `scientific-qa-evidence-agent`.

---

### S6 — PubMed-verified sources only in top_studies_urls

**Decision:** All URLs in `sources.top_studies_urls` must be real, accessible PubMed URLs in the format `https://pubmed.ncbi.nlm.nih.gov/[8-digit-PMID]/`. No fabricated or unverifiable URLs.

**Rationale:** Citations are the evidence base. A fabricated citation makes the entire monograph scientifically fraudulent. The validation script checks URL format; manual verification confirms the PMID corresponds to the claimed study.

**Status:** Mandatory. The validation script enforces URL format. Manual PMID verification is required before adding a new source.

---

## Operations decisions

### O1 — ANTHROPIC_API_KEY is environment variable only

**Decision:** The `ANTHROPIC_API_KEY` used by `build_plants.py` is set as a shell environment variable. It is never written to any file — not `.env`, not any config file, not any script.

**Rationale:** Any file in the project directory is at risk of being committed, cached, or pushed to a public repository. Environment variables exist only in the shell session and are not captured by git.

**Status:** Permanent. The validation script checks that no API key appears in committed files.

---

### O2 — GitHub Actions CI is deliberately minimal

**Decision:** The CI pipeline runs only: (1) JSON syntax check on `data.json`, (2) `python3 scripts/validate_archive_data.py`. No npm, no lint, no browser tests, no deploy.

**Rationale:** The project has no npm dependency. Running non-existent commands in CI would always fail. CI should only check things that can actually be checked. Browser tests require a running server; the current CI does not spin one up.

**Status:** Current. Add linting/browser tests only if the tech stack changes to require them.
