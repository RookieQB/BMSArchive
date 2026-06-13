# BMS Archive — Shortcuts and Workflows

This guide tells you exactly which command to use, when to use it, and what to expect.

---

## Fastest Daily Usage — Master Workflows

Use these for complex multi-step tasks. Each runs the full pipeline automatically.

| Workflow | When to use |
|---|---|
| `/workflow:fix-safe-claims` | **Run this first** — fix 37 unqualified "safe" warnings in data.json |
| `/workflow:new-monograph [species]` | Adding a completely new monograph from scratch |
| `/workflow:update-monograph [species]` | Editing or expanding an existing monograph |
| `/workflow:pre-publish [species]` | Final PASS/FAIL gate before a monograph goes live |
| `/workflow:pre-deploy` | Full security + ops + validation check before every deploy |
| `/workflow:weekly-maintenance` | Read-only weekly health report (run every Monday) |
| `/workflow:research-inbox [PMID]` | Stage a new study without touching data.json |
| `/workflow:fix-and-verify [error]` | Diagnose and fix any broken state or validation error |

---

## Project Commands (single-task operations)

## Cheat Sheet

| What you want to do | Command |
|---|---|
| Add a new plant/fungus profile | `/project:add-monograph [name]` |
| Update an existing profile | `/project:update-monograph [name]` |
| Check plant name / synonyms | `/project:taxonomy-check [name]` |
| Extract data from a PubMed paper | `/project:extract-study [PMID or abstract]` |
| Scientific fact-check | `/project:review-science [name or file]` |
| Add a new website feature | `/project:plan-feature [description]` |
| Change archive data structure | `/project:plan-feature [description]` → then `archive-data-model-agent` |
| Run quality checks | `/project:qa` |
| Security-sensitive change | `/project:security-review` |
| Build/deploy readiness | `/project:prepare-deploy` |
| Fix a broken build/validation | `/project:fix-build [error]` |
| Start a work session | `/project:daily-check` |
| Validate database | `/project:validate-data` |

---

## Command Reference

### `/project:daily-check`

**Purpose:** See the current state of the project before starting work.

**When to use:** At the beginning of every work session. Takes < 60 seconds.

**When NOT to use:** When you already know exactly what you're working on and just want to start.

**Expected output:**
- Git status and recent commits
- data.json entry count (confirms JSON is valid)
- List of TODOs and known open issues
- Top priority items

**Follow-up:** Use the suggested command from the output to continue.

---

### `/project:add-monograph [species name]`

**Example:** `/project:add-monograph Hypericum perforatum`

**Purpose:** Create a complete new monograph entry following the full BMS Archive scientific workflow.

**When to use:** When adding a new plant or fungus to the database.

**When NOT to use:** To update an existing entry — use `/project:update-monograph` instead.

**Agents involved:**
1. `taxonomy-nomenclature-agent` — confirms accepted name, checks for duplicates
2. `extraction-synthesis-agent` — extracts PubMed evidence
3. `scientific-qa-evidence-agent` — validates all claims
4. `archive-data-model-agent` — confirms schema fit (or proposes schema changes)
5. `qa-test-agent` — validates JSON and required fields

**Expected output:** A complete, valid `data.json` entry added to the array. Validation summary.

**Required follow-up:** `/project:validate-data`, then `/project:qa`

---

### `/project:update-monograph [species name]`

**Example:** `/project:update-monograph Withania somnifera`

**Purpose:** Update or improve an existing monograph — add new studies, fix safety data, improve pharmacokinetics, correct taxonomy.

**When to use:** When new evidence becomes available, when a profile is incomplete, or when corrections are needed.

**When NOT to use:** When creating a new entry — use `/project:add-monograph` instead.

**Agents involved:**
1. `taxonomy-nomenclature-agent` — confirm name is still current
2. `scientific-qa-evidence-agent` — review existing claims and validate additions
3. `qa-test-agent` — validate after changes

**Expected output:** Updated entry with documented changes and rationale. Validation summary.

**Required follow-up:** `/project:validate-data`, `/project:qa`

---

### `/project:taxonomy-check [name]`

**Example:** `/project:taxonomy-check ginseng`
**Example:** `/project:taxonomy-check Panax ginseng`

**Purpose:** Check whether a species name is correct, unambiguous, and not already in the database.

**When to use:** Always before adding a new species. Also when a common name could be ambiguous.

**When NOT to use:** When you already have a confirmed accepted Latin name and just need to add it.

**Agents involved:** `taxonomy-nomenclature-agent`

**Expected output:** Accepted Latin name, botanical family, synonyms, type field value, duplicate check result, plant part clarification.

**Required follow-up:** If clear → proceed to `/project:add-monograph`. If ambiguous → clarify the species before proceeding.

---

### `/project:extract-study [PMID, DOI, or abstract text]`

**Example:** `/project:extract-study 38547821`
**Example:** `/project:extract-study [paste abstract text here]`

**Purpose:** Extract structured, standardized data from a scientific paper into BMS Archive format.

**When to use:** When processing a new study to add to a monograph. Before adding any new source to `data.json`.

**When NOT to use:** As a final step — extraction always goes to `scientific-qa-evidence-agent` before use.

**Agents involved:**
1. `extraction-synthesis-agent` — extracts all available fields
2. `scientific-qa-evidence-agent` — validates the extraction before use

**Expected output:** Completed `STUDY_EXTRACTION_TEMPLATE.json` fields with evidence level assessment and QA notes.

**Required follow-up:** Always run `/project:review-science` on extracted content before committing to `data.json`.

---

### `/project:review-science [name, file, or text]`

**Example:** `/project:review-science Ganoderma lucidum`
**Example:** `/project:review-science docs/draft-monograph.md`

**Purpose:** Scientific fact-check — validates all claims against cited sources, flags overclaiming, checks evidence levels.

**When to use:** After writing or editing any scientific content. Before committing monograph changes. When you want to verify a specific claim.

**When NOT to use:** As a replacement for writing good content in the first place — use the evidence scoring rubric.

**Agents involved:** `scientific-qa-evidence-agent`

**Expected output:** Per-claim review with severity ratings (Critical / Major / Minor), list of required fixes, and overall approval status.

**Required follow-up:** Fix all Critical issues before committing. Major issues should be fixed before deployment.

---

### `/project:validate-data`

**Purpose:** Run all data validation checks on `data.json`.

**When to use:** After any change to `data.json` — adding entries, editing entries, running seeding scripts. Always before commit and before deploy.

**When NOT to use:** Instead of fixing actual errors — validation reports problems, it doesn't fix them.

**Agents involved:** `qa-test-agent`

**Expected output:**
- JSON syntax check result
- Required field errors by entry
- Safety section warnings
- Placeholder text detection
- Overall pass/fail status

**Run command directly:**
```bash
python3 scripts/validate_archive_data.py
python3 scripts/validate_archive_data.py --strict
python3 scripts/validate_archive_data.py --entry "Ganoderma lucidum"
```

**Required follow-up:** Fix all errors before committing or deploying.

---

### `/project:plan-feature [description]`

**Example:** `/project:plan-feature Add category filter chips to database page`
**Example:** `/project:plan-feature Add dark mode toggle`
**Example:** `/project:plan-feature Create a Phase 2 user account system`

**Purpose:** Plan a new website feature before writing any code. Produces an implementation plan with acceptance criteria and risk assessment.

**When to use:** Before implementing any non-trivial change to the site. Before any structural change to routing, data model, or API.

**When NOT to use:** For tiny, isolated changes (e.g., fixing a typo). For scientific data changes — use `add-monograph` or `update-monograph` instead.

**Agents involved:**
- `project-architect-agent` — core planning
- Additional agents flagged as needed based on feature scope

**Expected output:** Structured plan with current state, proposed change, files to create/modify, acceptance criteria, and risks.

**Required follow-up:** Review and approve the plan before implementation. Then use the appropriate agents during implementation.

---

### `/project:security-review`

**Example:** `/project:security-review`
**Example:** `/project:security-review server.js`

**Purpose:** Security and privacy review for API changes, forms, secrets, Nginx config, and admin endpoints.

**When to use:** Before any change to `server.js`, `nginx.conf`, `docker-compose.yml`. Before any new form or API route. Before every production deployment.

**When NOT to use:** For scientific content changes — those go to `review-science`.

**Agents involved:** `security-privacy-agent`

**Expected output:** Security findings by severity (Critical / High / Medium / Low), specific recommendations, deployment approval status.

**Required follow-up:** Fix Critical and High findings before deployment.

---

### `/project:prepare-deploy`

**Purpose:** Full pre-deployment checklist — security, file list, data validation, SEO, and deployment command generation.

**When to use:** Before every production deployment to bmsarchive.com.

**When NOT to use:** As a substitute for the actual deployment — this prepares and shows the commands; the user runs them.

**Agents involved:**
1. `security-privacy-agent`
2. `ops-performance-agent`
3. `qa-test-agent`

**Expected output:** Complete readiness report, confirmed file list (with admin tools excluded), SEO gaps, and the exact deploy commands ready to review and run.

**Required follow-up:** Review the deploy commands carefully, then run them manually.

---

### `/project:qa`

**Example:** `/project:qa`
**Example:** `/project:qa updated database.html and data.json`

**Purpose:** General quality gate — runs all available checks after any change.

**When to use:** After any code, data, or config change. Before every commit. Before every deployment.

**When NOT to use:** As the only check after scientific content changes — also run `/project:review-science`.

**Agents involved:** `qa-test-agent`

**Expected output:** Table of checks run with pass/fail/not-run status, issues found, recommendation (ready to commit / needs fixes).

---

### `/project:fix-build [error]`

**Example:** `/project:fix-build JSON parse error line 1247`
**Example:** `/project:fix-build docker compose up fails with nginx exit code 1`

**Purpose:** Debug and fix build, validation, or deployment errors. Identifies root cause and makes the minimum safe fix.

**When to use:** When `validate_archive_data.py` fails, Docker build fails, or Nginx errors occur.

**When NOT to use:** For scientific content corrections — use `review-science` instead.

**Agents involved:** `qa-test-agent`

**Expected output:** Root cause identification, minimum fix applied, re-run of failed command showing pass, no-regression confirmation.

---

## Full Workflows

### Adding a new monograph

```
1. /project:taxonomy-check [species name]
   → Confirms accepted name, checks for duplicates, identifies plant part
   
2. /project:extract-study [PMID or abstract]
   → Extracts structured evidence from key studies
   (Repeat for multiple key sources)
   
3. /project:add-monograph [species name]
   → Runs full multi-agent workflow: taxonomy → extraction → QA → schema → write
   
4. /project:review-science [species name]
   → Final scientific review of the completed entry
   
5. /project:validate-data
   → Validates data.json structure and required fields
   
6. /project:qa
   → Confirms browser rendering, no JSON errors, no regressions
```

---

### Updating an existing monograph

```
1. /project:update-monograph [species name]
   → Locates entry, reviews taxonomy, validates existing claims,
     applies approved changes, preserves structure
     
2. /project:review-science [species name]
   → Checks updated content for accuracy
   
3. /project:validate-data
   → Confirms no structural issues introduced
   
4. /project:qa
   → Final quality check
```

---

### Adding a new website feature

```
1. /project:plan-feature [feature description]
   → Read relevant files, consult project-architect-agent,
     produce plan with acceptance criteria
   
2. [Implement the feature]

3. /project:security-review [new file or feature]
   → Required if: new API route, form, user input, auth, database write

4. /project:prepare-deploy
   → Required if: change affects deployment, SEO, or production behavior

5. /project:qa [what was changed]
   → Final quality gate
```

---

### Before every production deployment

```
1. /project:security-review
   → Confirms no secrets exposed, admin tools excluded, Nginx headers intact
   
2. /project:validate-data
   → Confirms data.json is valid (blocking — do not deploy if this fails)
   
3. /project:prepare-deploy
   → Generates deploy commands, confirms file list, checks SEO
   → Review the commands carefully
   → Run them manually (ssh / scp / pct push / docker compose up --build)
   
4. Post-deploy: manually verify https://bmsarchive.com loads correctly
```

---

### Starting a work session

```
1. /project:daily-check
   → Git status, data.json health, open issues, suggested next step
   
2. Continue with the appropriate command based on output
```

---

## Common Mistakes to Avoid

| Mistake | Correct approach |
|---|---|
| Adding a monograph without taxonomy check | Always run `/project:taxonomy-check` first |
| Committing without validating data.json | Always run `/project:validate-data` before commit |
| Deploying without security review | Always run `/project:security-review` before deploy |
| Writing "safe" without evidence | Write "Insufficient data" when safety data is missing |
| Presenting animal evidence as human efficacy | Label study type explicitly; use correct evidence level |
| Inventing PMIDs or citations | Only use real, verified PubMed URLs |
| Deploying admin.html to production | It is explicitly excluded from the deploy file list |
| Direct SSH to 192.168.0.240 | Always deploy via Proxmox host using pct push |

---

## Evidence Levels Quick Reference

| Level | Meaning | Example language |
|---|---|---|
| A | SR/Meta-analysis of RCTs | "Systematic reviews demonstrate..." |
| B | Human RCT(s) | "A randomized trial showed..." |
| C | Observational / pilot human | "Preliminary human data suggests..." |
| D | Animal studies | "In animal models, preclinical evidence indicates..." |
| E | In vitro / mechanistic | "Cell studies show... (not confirmed in humans)" |
| T | Traditional use | "Traditionally used for..." |
| U | Unknown / insufficient | "Evidence is insufficient to conclude..." |

See `docs/rubrics/EVIDENCE_SCORING.md` for the full rubric.

---

## File Locations

| Resource | Path |
|---|---|
| Project conventions | `CLAUDE.md` |
| Subagents | `.claude/agents/` |
| Slash commands | `.claude/commands/` |
| Monograph template | `docs/templates/MONOGRAPH_TEMPLATE.md` |
| Safety profile template | `docs/templates/SAFETY_PROFILE_TEMPLATE.md` |
| Study extraction template | `docs/templates/STUDY_EXTRACTION_TEMPLATE.json` |
| Evidence scoring rubric | `docs/rubrics/EVIDENCE_SCORING.md` |
| Example monograph | `examples/golden-monograph-outline.md` |
| Example study extraction | `examples/golden-study-extraction.json` |
| Example safety profile | `examples/golden-safety-profile.md` |
| Data validation script | `scripts/validate_archive_data.py` |
| Git workflow guide | `docs/GIT_WORKFLOW.md` |
| CI recommendations | `docs/CI_RECOMMENDATIONS.md` |
| Feature task template | `docs/tasks/FEATURE_TASK_TEMPLATE.md` |
| Monograph task template | `docs/tasks/MONOGRAPH_TASK_TEMPLATE.md` |
