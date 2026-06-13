# BMS Archive — CI Recommendations

BMS Archive does not currently have a CI/CD pipeline. This document describes what a practical CI setup would look like when the project is ready for it.

---

## Current State

- No GitHub Actions or other CI configuration exists
- No `package.json`, so no npm-based test/lint/build scripts
- The stack is plain HTML + Tailwind (local bundle) + vanilla JS + Python
- Deployment is manual: SSH → scp → pct push → docker compose up --build

---

## When to Add CI

CI becomes valuable when:
1. More than one person contributes to the repository
2. Monograph additions are frequent enough that manual validation becomes error-prone
3. A Phase 2 framework (React, Next.js, etc.) is introduced
4. The project moves to a managed hosting environment with a deployment API (Vercel, Fly.io, etc.)

At the current stage (solo project, manual deploy), CI is optional but recommended for `data.json` validation.

---

## Recommended CI Setup (GitHub Actions)

Create `.github/workflows/validate.yml` when ready:

```yaml
name: BMS Archive Validation

on:
  push:
    branches: [main, feature/**]
  pull_request:
    branches: [main]

jobs:
  validate-data:
    name: Validate data.json
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Validate archive data
        run: python3 scripts/validate_archive_data.py --strict

  validate-json-syntax:
    name: Validate JSON files
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check data.json syntax
        run: python3 -c "import json; json.load(open('data.json')); print('data.json: valid')"

      - name: Check study extraction template
        run: python3 -c "import json; json.load(open('docs/templates/STUDY_EXTRACTION_TEMPLATE.json')); print('template: valid')"

  validate-html:
    name: Validate HTML (optional)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install htmlhint
        run: npm install -g htmlhint

      - name: Lint HTML files
        run: htmlhint index.html database.html
        continue-on-error: true  # Warning only until rules are finalized
```

---

## CI Checks Priority Order

If adding CI incrementally, implement in this order:

### Priority 1 — Implement now

**`python3 scripts/validate_archive_data.py --strict`**

Why: This already works today. Run it on every push to catch missing fields, broken safety sections, and placeholder text before they reach production.

### Priority 2 — Implement before Phase 2

**JSON syntax validation for all JSON files**
- `data.json`
- `docs/templates/STUDY_EXTRACTION_TEMPLATE.json`

**HTML validation**
- Install `htmlhint` and run on `index.html` and `database.html`
- Catches unclosed tags, missing `alt` attributes, and structural issues in large HTML files

### Priority 3 — Implement with Phase 2

**JavaScript linting (ESLint)**
- Only relevant if a framework or build step is introduced
- Not useful for inline vanilla JS in HTML files

**TypeScript typecheck**
- Only relevant if TypeScript is adopted

**End-to-end browser test**
- Playwright or Cypress to verify database grid renders, search works, modal opens
- Most valuable after Phase 2 introduces a dynamic framework

**Docker build verification**
- `docker compose build` on every PR
- Currently expensive to run in CI without a persistent runner; feasible with self-hosted runner on the Proxmox server

---

## Deployment CI (Future)

**Automatic deploy on merge to `main`** — only implement when:
- A staging environment exists to test before production
- TLS and DNS are fully stable
- Admin tools are formally separated from the deployed codebase (e.g., in a separate repo or subfolder)

A self-hosted GitHub Actions runner on the Proxmox host would enable deploy automation without exposing the LXC container to the internet.

---

## No-CI Alternatives (Current Stage)

Until CI is set up, run these manually before every commit:

```bash
# 1. Validate archive data
python3 scripts/validate_archive_data.py --strict

# 2. Check JSON syntax
python3 -c "import json; json.load(open('data.json')); print('OK')"

# 3. Git status — confirm only intended files are staged
git status
git diff --staged

# 4. Before deploy: full pre-deploy check
# /project:prepare-deploy
```

Document these as team norms in `docs/GIT_WORKFLOW.md` until CI is in place.

---

## Security CI (Future)

Add dependency scanning when a `package.json` or Python `requirements.txt` is introduced:
- **Python:** `pip-audit` or GitHub Dependabot
- **Node:** `npm audit` or GitHub Dependabot
- **Docker:** Trivy image scanning

Currently not needed as the project has no npm dependencies and Python stdlib only.
