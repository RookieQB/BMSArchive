# Feature Task — [Feature Name]

> Copy this template when planning a new website or infrastructure feature for BMS Archive.
> Fill in all sections before beginning implementation.
> Use `/project:plan-feature [description]` to generate this with agent assistance.

---

## Goal

[One clear sentence describing what this feature does and why it is needed.]

## Context

[What prompted this task? What problem does it solve? What user need or technical requirement is addressed? If this is part of a larger roadmap (Phase 2, etc.), note that here.]

## Affected Files

List all files that will be created or modified. Read each one before starting.

**New files:**
- `[path]` — [what it is]

**Modified files:**
- `[path]` — [what changes and why]

**Explicitly untouched:**
- `data.json` — [only if not touched]
- `admin.html` / `admin_server.py` — [not deployed, keep local-only]

## Required Agents

| Agent | Required | Reason |
|---|---|---|
| `project-architect-agent` | Yes / No | [why] |
| `scientific-qa-evidence-agent` | Yes / No | [why — required if scientific claims are involved] |
| `taxonomy-nomenclature-agent` | Yes / No | [why] |
| `archive-data-model-agent` | Yes / No | [why — required if data.json schema changes] |
| `extraction-synthesis-agent` | Yes / No | [why] |
| `security-privacy-agent` | Yes / No | [why — required if API, forms, auth, database writes involved] |
| `ops-performance-agent` | Yes / No | [why — required if deployment, SEO, performance affected] |
| `qa-test-agent` | Yes | Always required at the end |

## Acceptance Criteria

- [ ] [Specific, testable criterion 1]
- [ ] [Specific, testable criterion 2]
- [ ] [Specific, testable criterion 3]
- [ ] data.json remains valid (if touched)
- [ ] No regressions in existing database page behavior
- [ ] No regressions in newsletter form
- [ ] Admin tools are not deployed

## Scientific Review Needed?

- [ ] Yes — all health/pharmacological/botanical claims must pass `scientific-qa-evidence-agent`
- [ ] No — this is a purely technical/UI feature

## Security Review Needed?

- [ ] Yes — `security-privacy-agent` must review before deployment
  - Reason: [new API route / form / auth / user input / database write / env var / external API]
- [ ] No — no user input, auth, or backend changes

## Data Validation Needed?

- [ ] Yes — run `python3 scripts/validate_archive_data.py` after changes
- [ ] No — data.json is not modified by this task

## Deployment Impact

- [ ] Requires Docker rebuild — changes to `Dockerfile`, `nginx.conf`, `server.js`, or static files
- [ ] Requires `ops-performance-agent` review — performance, SEO, or infrastructure affected
- [ ] Deploy using standard workflow (see `CLAUDE.md` Deployment Notes)
- [ ] No deployment impact — local/dev-only change

## Tests and Checks

Run after implementation:

```bash
# Data validation (if data.json touched)
python3 scripts/validate_archive_data.py

# Browser check — open both pages and verify:
# - database.html grid renders all entries
# - search and filters work
# - modal opens and closes
# - newsletter form submits

# API smoke test (if server.js changed)
# curl -X POST http://localhost:3000/api/waitlist -H "Content-Type: application/json" -d '{"email":"test@example.com"}'

# Docker build (if Dockerfile or nginx.conf changed)
# docker compose up --build
```

**QA command:** `/project:qa [what was changed]`

## Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| [Risk 1, e.g. JSON structure change breaks database page] | High / Medium / Low | [Read database.html rendering code first; test in browser] |
| [Risk 2] | | |

## Out of Scope

The following are explicitly not part of this task:
- [Item 1]
- Instagram, social media, or content creation features
- Changes to `admin.html` or `admin_server.py` behavior (unless specifically requested)

## Final Summary

Complete this after the task is done:

**What was built:** [description]

**Files changed:** [list]

**Checks run:** [list with pass/fail]

**Remaining risks or issues:** [list or "None"]

**Deploy status:** Ready / Pending / Blocked — [reason]
