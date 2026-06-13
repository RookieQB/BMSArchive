# BMS Archive — Pull Request Checklist

Complete this checklist before requesting a merge. Every item marked [BLOCKING] must pass. Items marked [RECOMMENDED] should pass unless there is a documented reason to defer.

---

## Data integrity [BLOCKING]

- [ ] `data.json` parses without error: `python3 -c "import json; json.load(open('data.json'))"`
- [ ] Validation script passes with 0 errors: `python3 scripts/validate_archive_data.py`
- [ ] No new entries added without a full pass through `scientific-qa-evidence-agent`
- [ ] No existing entries silently modified (check `git diff data.json`)

## Scientific accuracy [BLOCKING]

- [ ] All new or modified claims have a verifiable PubMed source
- [ ] Evidence language matches evidence level (see `docs/rubrics/EVIDENCE_SCORING.md`)
- [ ] No animal or in vitro evidence presented as human efficacy
- [ ] No disease treatment, cure, prevention, or diagnosis claims
- [ ] No unqualified "safe" claims (validation script checks this)

## Taxonomy [BLOCKING]

- [ ] All `scientific_name` values are currently accepted binomials (POWO or Index Fungorum)
- [ ] `type` field is exactly "Fungi" or "Plant" (case-sensitive)
- [ ] `clinical_data.used_part` specifies the correct botanical part

## Safety [BLOCKING]

- [ ] Pregnancy field is non-empty and conservative for all new/modified entries
- [ ] Lactation field is non-empty and conservative for all new/modified entries
- [ ] Drug interactions field is non-empty for all new/modified entries
- [ ] No safety warnings were removed or weakened

## Secrets and security [BLOCKING]

- [ ] No API keys, passwords, or secrets in any committed file
- [ ] No `.env` file with real values
- [ ] `admin.html` and `admin_server.py` are not in the changed file list
- [ ] `build_plants.py` is not in the changed file list (if present, explain)
- [ ] ANTHROPIC_API_KEY appears only as a shell environment variable reference, not as a value

## Deploy safety [BLOCKING for deploy PRs]

- [ ] Admin tools excluded from Dockerfile COPY directives
- [ ] `docs/research-inbox/` items not referenced in index.html or database.html
- [ ] No draft content in deployed HTML files

## Validation [BLOCKING]

- [ ] `python3 scripts/validate_archive_data.py` exits with code 0
- [ ] No new ERRORs introduced (new warnings must be assessed and documented)

---

## Code quality [RECOMMENDED]

- [ ] HTML is valid (no unclosed tags, no duplicate IDs)
- [ ] JavaScript has no console.error calls in the browser for the main user flow
- [ ] No placeholder text ("TODO", "lorem ipsum", "citation needed", "tbd") in deployed files
- [ ] Inline JS follows existing patterns (no new framework dependencies introduced)

## Documentation [RECOMMENDED]

- [ ] If a new slash command was added: referenced in `CLAUDE.md` and `docs/SHORTCUTS_AND_WORKFLOWS.md`
- [ ] If a new agent was added: referenced in `CLAUDE.md`
- [ ] If a significant architectural decision was made: recorded in `docs/DECISIONS.md`
- [ ] If roadmap items were completed or added: `docs/ROADMAP.md` updated

## Browser QA [RECOMMENDED]

- [ ] `index.html` loads without console errors
- [ ] `database.html` renders all entries in grid
- [ ] Monograph modal opens and closes correctly
- [ ] Type filter (Fungi/Plant) works
- [ ] Disclaimer banner is visible on `database.html`

---

## For monograph additions specifically

Run the full pre-publication gate before merging a new monograph:
```
/workflow:pre-publish [species name]
```

This must produce `PASS — PUBLICATION READY` before the PR is merged.

---

## CI status

The GitHub Actions CI automatically runs on every PR:
- JSON syntax check: must pass
- Validation script: must pass with 0 errors

CI results appear on the PR. Do not merge a PR with failing CI.
