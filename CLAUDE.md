# CLAUDE.md — BMS Archive

## Project Overview

BMS Archive is a static, evidence-based phytomedicine website hosted at **bmsarchive.com**. It is a two-page public archive of botanical and fungal monographs sourced from peer-reviewed literature (PubMed), combined with a functional email waitlist/newsletter backend.

The site is currently in Phase 1: a landing page with a newsletter subscription form, and a searchable database of 50 bioactive monographs (25 medicinal fungi + 25 medicinal plants). There is no framework, no build step, and no npm dependencies — the site is plain HTML5 with a locally bundled Tailwind CSS file.

This project is **not** about Instagram, social media content creation, reels, captions, or any social media workflow. Do not introduce logic or features related to those topics.

---

## Product Profile

**Purpose:** Provide researchers, students, and health-conscious individuals with a structured, citation-backed reference database of botanical and fungal medicines at the level of academic pharmacognosy.

**Audience:** People who want evidence-based information on phytomedicines — not a general health blog audience. The tone is clinical, precise, and academic. Every claim should be traceable to a primary PubMed source.

**Core features:**
- Landing page (`index.html`) with hero section, newsletter/waitlist form, and a medical disclaimer
- Searchable database (`database.html`) — grid of cards, text search, type filter (Fungi/Plant), modal detail view
- Email waitlist backend — Node.js API endpoint (`POST /api/waitlist`) persists emails to `/data/waitlist.txt`
- Local admin panel (`admin.html` + `admin_server.py`) — browser-based editor for `data.json`, runs locally only, never deployed

**Key user flows:**
1. Visitor lands on `index.html` → reads about the project → enters email to subscribe → sees success confirmation
2. Visitor clicks "Browse Database" → `database.html` → searches/filters monographs → clicks a card → reads full modal with clinical data, pharmacokinetics, citations

**What this project is not:**
- Not a social media tool or content scheduler
- Not a medical advice platform (explicitly disclaimed)
- Not a dynamic web app (no React, Vue, Angular, or any JS framework)
- Not a blog or CMS

**Tone and brand:** Clean, scientific, archive-like. Dark forest-green (`#1c5235`) primary. Minimal visual noise. Typography-forward. Everything should feel like a well-organized research database, not a marketing site.

---

## Tech Stack

| Layer | Detail |
|---|---|
| HTML/CSS | Plain HTML5 + Tailwind CSS v3.4.17 (served locally as `tailwind.js`) |
| JavaScript | Vanilla JS inline in each HTML file — no bundler, no transpilation |
| Font | Inter (Google Fonts, loaded via non-blocking `preload` / `onload` pattern) |
| Data | `data.json` — 50 monograph entries, PubMed-verified |
| Web server | Nginx 1.27-alpine (Docker container) |
| API server | Node.js 20-alpine (Docker container), zero npm dependencies, plain `http` module |
| Container orchestration | Docker Compose v2+ |
| Deployment host | LXC container on self-hosted Proxmox server |
| Admin tool | Python 3 stdlib HTTP server (`admin_server.py`) — local only |
| Data-seeding scripts | Python 3, uses `anthropic` SDK and NCBI APIs — offline only |
| Package manager | None (no `package.json`) |
| Framework | None |
| Build step | None |
| Testing | None |
| Linting | None |
| TypeScript | Not used |

---

## Project Structure

```
BMS website/
├── index.html            # Landing page — hero, newsletter form, disclaimer, footer
├── database.html         # Searchable monograph database — grid, filters, modal
├── admin.html            # Local admin panel UI (not deployed, local editor for data.json)
├── data.json             # 50 monograph entries (25 Fungi + 25 Plants), PubMed-verified
├── tailwind.js           # Tailwind CSS v3.4.17 bundled locally — do NOT replace with CDN
├── nginx.conf            # Nginx config: HTTPS redirect, SSL, gzip, cache headers, security headers
├── Dockerfile            # nginx:1.27-alpine — serves static files (web container)
├── Dockerfile.api        # node:20-alpine — runs server.js (api container)
├── docker-compose.yml    # Two services: web (Nginx) + api (Node.js); volume: waitlist_data
├── server.js             # Node.js waitlist API — POST /api/waitlist, saves to /data/waitlist.txt
├── admin_server.py       # Local Python server on port 5050 — serves admin.html + GET/POST /api/data
├── build_plants.py       # Offline script — generates plant monographs via Claude + PubMed APIs
├── .claude/
│   └── settings.local.json   # Claude Code permissions
└── scripts/
    └── data-seeding/
        ├── add_plants_batch1.py … add_plants_batch11.py   # Batch plant data seeders
        └── update_sources.py   # Refreshes PubMed PMIDs and article counts in data.json
```

**Critical files — be careful:**
- `data.json` — the entire monograph database; edits here affect the live public site
- `nginx.conf` — server config; mistakes can break HTTPS or the API proxy
- `docker-compose.yml` — production container setup; changes affect deployment
- `tailwind.js` — 443 KB local Tailwind bundle; do not delete or replace with a CDN link

---

## How To Run The Project

### Local development (no server needed)

Open `index.html` or `database.html` directly in a browser. No install step required.

### Local with Nginx (Docker)

```bash
docker compose up --build
# Site at http://localhost:80
```

> Note: `nginx.conf` is configured for HTTPS with `bmsarchive.com`. For local testing, you may need a simplified config or just open the HTML files directly.

### Local admin panel

The admin panel edits `data.json` locally. It is **never deployed to the server**.

```bash
python3 admin_server.py
# Opens http://localhost:5050 in your browser automatically
```

### Refresh PubMed sources in data.json

```bash
python3 scripts/data-seeding/update_sources.py
```

Queries NCBI eSearch API (rate-limited to 0.5 s/request). Updates `article_count` and `sources.top_studies_urls` for all entries.

### Generate new plant monographs (requires Anthropic API key)

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python3 build_plants.py
```

Resumes automatically if interrupted (tracks progress in `plants_progress.json`).

### Missing / Recommended

- No `npm install`, `npm run dev`, `npm run build` — there is no Node build process
- No linting command — consider adding `htmlhint` or similar in future
- No test command — no test suite exists yet

---

## Environment Variables

| Variable | Used by | Purpose |
|---|---|---|
| `ANTHROPIC_API_KEY` | `build_plants.py` | Authenticates Claude API calls to generate monograph content |

No `.env` file exists in the project. The API key is set as a shell environment variable before running `build_plants.py`. Do not hardcode or commit API keys.

---

## Architecture Notes

### Routing

The site has two public routes served by Nginx:
- `/` → `index.html`
- `/database.html` → `database.html`
- `/api/waitlist` (POST) → proxied to Node.js container on port 3000

### Data flow

1. `database.html` fetches `/data.json` at page load via `fetch()`, renders cards client-side, filters in memory
2. Newsletter form in `index.html` posts `{ email }` JSON to `/api/waitlist`
3. Node.js (`server.js`) validates the email and appends `timestamp - email\n` to `/data/waitlist.txt` (Docker named volume `waitlist_data`)

### Admin panel (local only)

- `python3 admin_server.py` starts a Python HTTP server on `127.0.0.1:5050`
- `GET /api/data` returns the full `data.json`
- `POST /api/data` validates and overwrites `data.json` with edited payload
- `admin.html` is a browser UI that reads/writes via these endpoints

### Modal detail view

`database.html` builds the entire UI in vanilla JS. Cards are rendered by iterating over the fetched JSON array. Clicking a card populates the modal overlay with that entry's data fields and shows it with a CSS transition.

### SSL / HTTPS

Nginx terminates TLS using Let's Encrypt certificates mounted from the Proxmox host at `/etc/letsencrypt`. HTTP (port 80) redirects to HTTPS. HSTS is enforced with `max-age=63072000`.

### data.json schema

Each entry follows this structure:

```json
{
  "scientific_name": "Ganoderma lucidum",
  "common_name": "Reishi / Lingzhi",
  "type": "Fungi",
  "article_count": 3033,
  "primary_categories": ["Immunomodulation", "Oncology support"],
  "sources": {
    "top_studies_urls": ["https://pubmed.ncbi.nlm.nih.gov/PMID/"],
    "cited_references": ["[1] - Author, Title, Journal, Year, PMID"]
  },
  "narrative_summary": {
    "historical_use": "...",
    "modern_application": "...",
    "side_effects": "...",
    "contraindications": "..."
  },
  "clinical_data": {
    "used_part": "...",
    "primary_active_compounds": ["..."],
    "mechanism_of_action": "... <strong>TARGET</strong> ...",
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

Both `type` values are `"Fungi"` or `"Plant"` (capital first letter — the database filter depends on this exact casing).

---

## Development Rules For Claude Code

1. **Read relevant files before changing them.** This is especially important for `data.json`, `database.html`, and `index.html` — they are large files with structure that must be preserved.
2. **Do not refactor without a plan.** The codebase is intentionally simple. Resist the urge to introduce abstractions, components, or a build step unless explicitly requested.
3. **Preserve the existing structure and coding style.** JS is inline in HTML files. CSS is Tailwind utility classes. No external JS files. Keep it that way unless asked to change.
4. **Do not add a framework.** No React, Vue, Svelte, or any other framework unless the user explicitly requests a Phase 2 rewrite.
5. **Do not swap Tailwind to CDN.** `tailwind.js` is served locally for offline reliability and performance. Do not replace it with a CDN link.
6. **Never commit or log secrets.** The `ANTHROPIC_API_KEY` is a shell env var. Do not write it to any file.
7. **Do not touch `data.json` carelessly.** Any edit that breaks the JSON structure will break the entire database page. Validate JSON after manual edits.
8. **Do not add Instagram or social media logic.** The project scope is the website and its archive functionality only.
9. **Deploy via Proxmox, not direct SSH to the container.** See Deployment Notes below.
10. **The admin panel is local-only.** `admin.html` and `admin_server.py` are development tools. Do not add them to the Dockerfile or nginx config.
11. **Run a local browser check after UI changes.** There is no test suite — manually verify that the database grid renders, the modal opens, and the newsletter form submits.

---

## Coding Standards

### HTML

- Semantic HTML5 elements (`<section>`, `<header>`, `<footer>`, `<main>`, `<nav>`)
- ARIA attributes on interactive elements (`role`, `aria-label`, `aria-modal`, `aria-hidden`)
- Section dividers use the `<!-- ═══ SECTION NAME ═══ -->` comment style — preserve this for readability
- All inline JS goes at the bottom of `<body>` before `</body>`

### CSS / Styling

- Tailwind utility classes only — no separate stylesheet
- Custom colors use the `forest` palette defined in `tailwind.config` in each HTML file's `<script>` block:
  - `forest-950` (`#0c2519`) — darkest, used for wordmark and primary text on dark backgrounds
  - `forest-800` (`#1c5235`) — main green for buttons and links
  - `forest-700` (`#1f6640`) — hover states
  - `forest-600` (`#268050`) — accent labels
- Amber (`bg-amber-50`, `border-amber-200`) is reserved for disclaimer and contraindication highlights
- One-off custom CSS goes in a `<style>` block in the `<head>`, only when Tailwind cannot express it (e.g., transitions, scrollbar styling)

### JavaScript

- Vanilla JS only, no libraries
- `const` / `let` (no `var`)
- `async/await` for fetch calls with `try/catch`
- DOM element references captured at the top of the script block
- Event listeners use `addEventListener`, not inline `onclick` attributes (except in `admin.html`)

### Data / JSON

- `type` field must be exactly `"Fungi"` or `"Plant"` (capital first letter)
- `top_studies_urls` must contain real PubMed URLs — never fabricate PMIDs
- `mechanism_of_action` uses `<strong>` tags around key pharmacological targets (e.g., `<strong>NF-κB</strong>`) — this is intentional and rendered as innerHTML in the modal
- `article_count` must be an integer, not a string

---

## Design And UI Guidelines

- **Preserve the design system.** Do not change colors, typography, or spacing conventions without being asked.
- **Reuse existing Tailwind patterns.** Look at how cards, badges, and modal sections are styled before adding new elements. Copy-paste the pattern.
- **Mobile-first.** The site is responsive. Use `sm:` breakpoint prefixes for desktop variants. Test narrow viewport widths.
- **Accessibility.** Maintain `aria-label`, `role`, `aria-hidden`, and `sr-only` patterns that already exist. Do not remove them.
- **No animations beyond what exists.** The site has minimal transitions (`transition`, `animate-pulse`, `animate-spin`). Keep it clean.
- **Disclaimer banners are mandatory.** The sticky amber disclaimer bar and the medical disclaimer section in `index.html` must not be removed or hidden.
- **The wordmark is "BMS | Archive"** — a bold "BMS", a vertical divider, then "Archive" in light uppercase tracking. Preserve this across all pages.
- **Clean, archive-like experience.** When in doubt, add less rather than more. This is a reference tool, not a sales page.

---

## Data And Content Guidelines

- All monograph data must originate from peer-reviewed literature. Do not write speculative or unsourced content into `data.json`.
- `top_studies_urls` must be real, working PubMed URLs in the format `https://pubmed.ncbi.nlm.nih.gov/{PMID}/`. Use `update_sources.py` or `build_plants.py` to generate these — never guess PMIDs.
- `cited_references` (in plant entries) follow the format: `"[N] - Author(s), Title, Journal, Year, PMID: ..."`.
- `primary_categories` should be concise, clinically meaningful labels (e.g., `"Immunomodulation"`, `"Adaptogen"`, `"Hepatoprotection"`).
- When adding a new entry, validate the full JSON structure manually before saving. Required fields: `scientific_name`, `common_name`, `type`, `article_count`, `primary_categories`, `sources.top_studies_urls`, `narrative_summary` (all four subfields), `clinical_data` (all subfields including `pharmacokinetics` with all four ADME fields).
- Sorting in `data.json` is not enforced programmatically — the database UI renders entries in the order they appear in the array. Keep Fungi first (indices 0–24), Plants second (indices 25–49).

---

## Testing And Quality Checks

There is no automated test suite. Quality checks are manual:

1. **After any change to `data.json`:** Validate JSON syntax (e.g., `python3 -c "import json; json.load(open('data.json'))"`)
2. **After any change to `database.html` or `index.html`:** Open the file in a browser and verify:
   - Database grid renders all entries
   - Search input filters correctly
   - Type filter pills (All / Fungi / Plant) work
   - Clicking a card opens the modal with correct data
   - Modal closes on "×" button and Escape key
   - Newsletter form submits (requires the API container running)
3. **After any change to `server.js`:** Test the API endpoint manually:
   ```bash
   curl -X POST http://localhost:3000/api/waitlist \
     -H "Content-Type: application/json" \
     -d '{"email":"test@example.com"}'
   ```
4. **After any change to `nginx.conf`:** Run `docker compose up --build` and verify the site loads on port 80.
5. **After any change to `admin_server.py` or `admin.html`:** Run `python3 admin_server.py` and verify the panel loads, lists all entries, and can save changes.

---

## Deployment Notes

The site runs in a Docker Compose stack inside an LXC container (ID `102`) on a self-hosted Proxmox server.

| Resource | Value |
|---|---|
| Proxmox host | `192.168.0.100` (SSH as root) |
| LXC container | ID `102`, Debian 13 (Trixie), static IP `192.168.0.240` |
| Files in container | `/opt/bms-archive/` |
| Docker version | v29.5.1 + Compose v5.1.3 |
| Public domain | `bmsarchive.com` |

**Never SSH directly to `192.168.0.240`.** Always deploy via the Proxmox host using `pct push` and `pct exec`.

### Deploy workflow

```bash
# 1. Stage files on the Proxmox host
ssh root@192.168.0.100 "mkdir -p /tmp/bms-deploy"
scp docker-compose.yml Dockerfile Dockerfile.api nginx.conf server.js \
    index.html database.html data.json tailwind.js \
    root@192.168.0.100:/tmp/bms-deploy/

# 2. Push files into the LXC container
ssh root@192.168.0.100 "
  for f in docker-compose.yml Dockerfile Dockerfile.api nginx.conf server.js \
            index.html database.html data.json tailwind.js; do
    pct push 102 /tmp/bms-deploy/\$f /opt/bms-archive/\$f
  done
"

# 3. Rebuild and restart
ssh root@192.168.0.100 "pct exec 102 -- bash -c 'cd /opt/bms-archive && docker compose up -d --build'"
```

**Never deploy:** `admin.html`, `admin_server.py`, `build_plants.py`, or `scripts/`.

### SSL

TLS certificates are managed by Certbot/Let's Encrypt on the LXC container, mounted into the Nginx container via `/etc/letsencrypt`. Renewal is handled by Certbot on the host system. Do not modify the SSL volume mounts in `docker-compose.yml` without understanding the certificate renewal flow.

---

## Known Issues / Missing Documentation

- The README still references a v2 structure (25 fungi only); `data.json` now has 50 entries (25 fungi + 25 plants)
- No `.env.example` file — environment variables are undocumented outside this file
- No favicon or `og:image` — social link previews will show no image
- No `robots.txt` or `sitemap.xml` — relevant before public DNS goes live
- `admin.html` and `admin_server.py` are not in the `.gitignore` — they are committed to main but should not be deployed; this is currently handled by manual exclusion during deploy
- `docker-compose.yml` has TLS volume mounts (`/etc/letsencrypt`) that will cause `docker compose up` to fail locally if the certificates don't exist — for local dev, open the HTML files directly instead
- The `database.html` header still shows "Live — 25 profiles" — should be updated to 50
- `build_plants.py` uses `claude-opus-4-7` (now superseded by newer models); update the model ID when regenerating content

---

## Recommended Improvements

- **Update database.html entry count** — change "25 profiles" to "50 profiles" in the page header
- **Add `.env.example`** — document `ANTHROPIC_API_KEY` for future contributors
- **Add `robots.txt` and `sitemap.xml`** — needed before public DNS launch
- **Add a favicon** — at minimum a simple SVG favicon matching the brand
- **Add `og:image`** — improves social link previews significantly
- **Add `htmlhint` or a basic HTML linter** — catches tag mismatches in large HTML files
- **Add JSON schema validation** to `admin_server.py` — currently validates presence of required keys but not nested structure depth
- **Consider a `local-nginx.conf`** — a simplified config without SSL for local Docker testing, so `docker compose up` works without Let's Encrypt certs
- **Update README** — reflect the current 50-entry database and the admin panel tooling
- **Tag `admin.html` / `admin_server.py` clearly** in the repo as local-only dev tools (e.g., in a comment or README section) to prevent accidental deployment

---

## Claude Code Subagents

BMS Archive is an evidence-based phytomedicine and botanical science platform. **Scientific, medical, pharmacological, botanical, dosage, safety, and interaction claims must be reviewed by the `scientific-qa-evidence-agent` before being treated as final.**

**Do not add Instagram, social media, captions, reels, influencer workflows, or unrelated content creation logic to this project.**

Nine specialized subagents are configured in `.claude/agents/`. Claude Code will automatically select the appropriate agent based on the task. You can also explicitly invoke an agent by referring to it by name.

### Agent Directory

| Agent | File | Purpose |
|---|---|---|
| `project-architect-agent` | `.claude/agents/project-architect-agent.md` | High-level architecture, feature planning, routing, data flow, repository structure |
| `scientific-qa-evidence-agent` | `.claude/agents/scientific-qa-evidence-agent.md` | Scientific gatekeeper — validates all health, pharmacological, dosage, safety, and efficacy claims |
| `taxonomy-nomenclature-agent` | `.claude/agents/taxonomy-nomenclature-agent.md` | Botanical identity, Latin binomials, synonyms, plant parts, duplicate prevention |
| `archive-data-model-agent` | `.claude/agents/archive-data-model-agent.md` | `data.json` schema design, field definitions, migration planning, data integrity |
| `extraction-synthesis-agent` | `.claude/agents/extraction-synthesis-agent.md` | Extracts structured data from PubMed abstracts and papers for QA review |
| `security-privacy-agent` | `.claude/agents/security-privacy-agent.md` | API security, input validation, secrets, Nginx headers, admin endpoint protection |
| `ops-performance-agent` | `.claude/agents/ops-performance-agent.md` | Deployment, Docker/Nginx config, SEO, performance, Proxmox/LXC stack |
| `qa-test-agent` | `.claude/agents/qa-test-agent.md` | Post-change quality checks, JSON validation, browser testing, API smoke tests |
| `github-sync-agent` | `.claude/agents/github-sync-agent.md` | Commits and pushes changes to `origin/main` after successful deployment |

### When To Use Each Agent

**`project-architect-agent`** — Invoke before any significant structural change: new pages, routing changes, schema redesigns, Phase 2 planning (adding a framework or database), admin workflow design, or scientific data pipeline architecture.

**`scientific-qa-evidence-agent`** — Invoke for any text that makes a health, pharmacological, efficacy, dosage, safety, interaction, or contraindication claim. This agent must approve content before it is written to `data.json` or rendered on the site.

**`taxonomy-nomenclature-agent`** — Invoke before adding any new species, when common names are ambiguous, when a study uses an outdated Latin synonym, or when building name-based search or filter features.

**`archive-data-model-agent`** — Invoke when adding new fields to `data.json`, normalizing existing entries, designing evidence scoring, or planning migration to a real database.

**`extraction-synthesis-agent`** — Invoke when processing PubMed abstracts into structured data, summarizing clinical trials, comparing studies on a species, or reviewing `build_plants.py` output before committing.

**`security-privacy-agent`** — Invoke before any change to `server.js`, `nginx.conf`, `docker-compose.yml`, or any feature involving user input, forms, API routes, auth, or admin access.

**`ops-performance-agent`** — Invoke before and after any production deployment, when Docker or Nginx config changes, when adding SEO metadata, or when investigating performance issues.

**`qa-test-agent`** — Invoke after completing any task: data changes, UI changes, API changes, or before deployment. Runs all available quality checks and reports pass/fail.

**`github-sync-agent`** — Invoke after the user confirms a production deployment succeeded. Stages all appropriate files (never secrets or admin tools), writes a deployment-tagged commit, and pushes to `origin/main`.

### Recommended Workflows

#### Adding or editing a scientific monograph

1. `taxonomy-nomenclature-agent` — confirm accepted name, check for duplicates, verify plant part
2. `extraction-synthesis-agent` — extract structured data from PubMed sources
3. `scientific-qa-evidence-agent` — validate all claims, evidence levels, safety data
4. `archive-data-model-agent` — confirm data fits `data.json` schema; design new fields if needed
5. `qa-test-agent` — validate JSON, check required fields, verify browser rendering

#### Adding a new platform feature

1. `project-architect-agent` — plan the feature, assess trade-offs, define scope
2. Implement the feature
3. `security-privacy-agent` — review if feature involves forms, API routes, auth, uploads, or database writes
4. `ops-performance-agent` — review if feature affects deployment, SEO, performance, or production behavior
5. `qa-test-agent` — run all available checks, verify acceptance criteria

#### Production deployment

1. `security-privacy-agent` — confirm no secrets in files, admin tools excluded, headers intact
2. `ops-performance-agent` — verify deploy file list, Nginx config, Docker build, post-deploy site check
3. `qa-test-agent` — confirm site is accessible, database renders, API responds
4. `github-sync-agent` — after deployment confirmed, commit and push all changes to `origin/main`

#### Phase 2 planning (framework, real database, auth, CMS)

1. `project-architect-agent` — evaluate options, propose architecture, identify migration risks
2. `archive-data-model-agent` — design new schema and migration from flat JSON
3. `security-privacy-agent` — review auth design and new attack surface
4. `ops-performance-agent` — plan new deployment and infrastructure requirements

### Future Agents (Not Yet Implemented)

Two additional agents are recommended for Phase 2 of BMS Archive, once the infrastructure exists:

- **`ingestion-search-agent`** — Automated literature discovery via PubMed, Europe PMC, and Cochrane; structured ingestion pipeline for new monographs
- **`rag-search-agent`** — Semantic search and retrieval-augmented answers based exclusively on BMS Archive's verified database

Do not implement these until the project has the necessary infrastructure (vector store, search backend, or embedding pipeline).

---

## Slash Commands

Project-level slash commands are in `.claude/commands/`. Use them in Claude Code with `/project:[command]`.

| Command | Purpose |
|---|---|
| `/project:daily-check` | Start-of-session status check — git, data validity, open issues |
| `/project:add-monograph [name]` | Full multi-agent workflow to add a new species profile |
| `/project:update-monograph [name]` | Update an existing monograph with preserved structure |
| `/project:taxonomy-check [name]` | Verify accepted Latin name, synonyms, duplicate check |
| `/project:extract-study [PMID]` | Extract structured evidence from a paper into BMS Archive format |
| `/project:review-science [name]` | Scientific fact-check — flags overclaiming, validates sources |
| `/project:validate-data` | Run all data.json validation checks |
| `/project:plan-feature [idea]` | Architecture plan for new website features |
| `/project:security-review` | Security and privacy review |
| `/project:prepare-deploy` | Pre-deployment checklist and command generation |
| `/project:qa` | General quality gate after any change |
| `/project:fix-build [error]` | Debug and fix build/validation/deployment errors |

See `docs/SHORTCUTS_AND_WORKFLOWS.md` for full command reference with examples, workflows, and when-not-to-use guidance.

---

## Documentation Index

| Resource | Location |
|---|---|
| Workflow guide and cheat sheet | `docs/SHORTCUTS_AND_WORKFLOWS.md` |
| Monograph template | `docs/templates/MONOGRAPH_TEMPLATE.md` |
| Safety profile template | `docs/templates/SAFETY_PROFILE_TEMPLATE.md` |
| Study extraction template | `docs/templates/STUDY_EXTRACTION_TEMPLATE.json` |
| Evidence scoring rubric | `docs/rubrics/EVIDENCE_SCORING.md` |
| Example monograph outline | `examples/golden-monograph-outline.md` |
| Example study extraction | `examples/golden-study-extraction.json` |
| Example safety profile | `examples/golden-safety-profile.md` |
| Data validation script | `scripts/validate_archive_data.py` |
| Git workflow | `docs/GIT_WORKFLOW.md` |
| CI recommendations | `docs/CI_RECOMMENDATIONS.md` |
| Feature task template | `docs/tasks/FEATURE_TASK_TEMPLATE.md` |
| Monograph task template | `docs/tasks/MONOGRAPH_TASK_TEMPLATE.md` |

---

## Definition of Done

A task is not complete until all applicable items below are checked:

**Always:**
- [ ] Relevant files were read before making changes
- [ ] The correct subagent workflow was followed
- [ ] Changed files are summarized
- [ ] Remaining risks or unknowns are listed

**For scientific/monograph work:**
- [ ] Taxonomy was confirmed with `taxonomy-nomenclature-agent`
- [ ] Scientific claims were reviewed by `scientific-qa-evidence-agent`
- [ ] Safety sections (adverse effects, contraindications, interactions, pregnancy/lactation, hepatic/renal) are complete
- [ ] No claim implies the compound treats, cures, prevents, or diagnoses a disease
- [ ] All PubMed URLs are real and verifiable
- [ ] No unqualified "safe" claims where safety data is missing

**For data changes:**
- [ ] `python3 scripts/validate_archive_data.py` passed with no errors
- [ ] JSON syntax is valid
- [ ] data.json rendered correctly in the browser (database grid, modal, filters)

**For code/UI changes:**
- [ ] Browser check passed (index.html and/or database.html as applicable)
- [ ] No console errors in the browser
- [ ] API smoke test passed (if server.js was modified)

**For security-sensitive changes (API, forms, auth, database writes, env vars):**
- [ ] `security-privacy-agent` review completed
- [ ] No secrets in committed files
- [ ] Input validation is server-side
- [ ] Admin tools are not exposed

**For production deployments:**
- [ ] `/project:security-review` approved
- [ ] `/project:validate-data` passed
- [ ] `/project:prepare-deploy` ran — deploy file list reviewed (admin tools excluded)
- [ ] Deploy commands reviewed before running
- [ ] Post-deploy: site accessible at `https://bmsarchive.com`

**Always prohibited:**
- [ ] No Instagram, social media, or content creation logic added
- [ ] No secrets committed
- [ ] No fabricated PMIDs or citations
- [ ] No unverified scientific claims presented as fact

---

## Master Workflows

High-level pipeline commands that chain agents, commands, and scripts into repeatable workflows. All are in `.claude/commands/workflow-*.md`.

| Workflow | Trigger | What it does |
|---|---|---|
| `/workflow:new-monograph [species]` | Adding a new entry | Full pipeline: taxonomy → extraction → scientific QA → schema → write → validate → QA |
| `/workflow:update-monograph [species]` | Editing an existing entry | Gap analysis → targeted updates → QA → validation |
| `/workflow:fix-safe-claims` | Validation shows "safe" warnings | Batch fix all unqualified "safe" claims; scientific QA each replacement |
| `/workflow:weekly-maintenance` | Weekly (read-only) | Health check: git, validation, inbox, documentation drift, known issues |
| `/workflow:pre-publish [species]` | Before publishing a monograph | PASS/FAIL gate: taxonomy + scientific QA + safety completeness + validation |
| `/workflow:pre-deploy` | Before every production deploy | Security + ops + validation + deploy command generation (manual run) |
| `/workflow:research-inbox [PMID/DOI]` | New study to stage | Extract → inbox item → queue for QA → do not touch data.json |
| `/workflow:fix-and-verify [error]` | Any error or broken state | Diagnose root cause → smallest fix → re-run → regression check |

### Recommended first workflow

Run `/workflow:fix-safe-claims` first. The validation script found 37 warnings for unqualified "safe" claims across existing entries — these are scientific credibility issues that must be resolved before new content is added.

### Workflow rules

- Workflows produce reports; they do not deploy or commit automatically
- Scientific QA (`scientific-qa-evidence-agent`) is mandatory in every content workflow
- No workflow bypasses the validation script
- `/workflow:pre-deploy` always generates deploy commands for manual review — it never runs them
