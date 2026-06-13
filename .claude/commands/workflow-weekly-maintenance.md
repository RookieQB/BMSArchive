---
description: Master workflow — weekly BMS Archive health check. Validates data, reviews research inbox, checks documentation drift, and produces a prioritised action list for the coming week. Read-only unless explicit fixes are requested.
---

You are running the **BMS Archive weekly maintenance workflow**.

This is a read-only diagnostic run. No changes are made unless the output explicitly recommends a fix and you confirm it.

---

## PHASE 1 — Session status

```bash
git status
git log --oneline -10
git diff --stat HEAD~5 HEAD 2>/dev/null || echo "Less than 5 commits"
```

Report:
- Current branch
- Uncommitted changes (flag as urgent if data.json is dirty)
- What changed in the last week (from git log)

---

## PHASE 2 — Data validation

```bash
python3 -c "
import json
with open('data.json') as f:
    data = json.load(f)
fungi = [d for d in data if d.get('type') == 'Fungi']
plants = [d for d in data if d.get('type') == 'Plant']
print(f'data.json: {len(data)} entries ({len(fungi)} Fungi, {len(plants)} Plant) — valid JSON')
"
python3 scripts/validate_archive_data.py
python3 scripts/validate_archive_data.py --strict 2>&1 | tail -5
```

Record:
- Total entries
- Error count
- Warning count broken down by type
- Any new warnings compared to last known baseline (37 "safe" warnings before fix-safe-claims was run)

---

## PHASE 3 — Placeholder and draft content scan

```bash
grep -rn "TODO\|FIXME\|HACK\|citation needed\|lorem ipsum\|insert source\|placeholder\|tbd\|to be completed" \
  --include="*.html" --include="*.js" --include="*.py" --include="*.json" --include="*.md" \
  --exclude-dir=".git" --exclude-dir="node_modules" . 2>/dev/null
```

Flag any results that appear in deployed files (`index.html`, `database.html`, `data.json`).

---

## PHASE 4 — Research inbox review

```bash
ls docs/research-inbox/items/ 2>/dev/null | head -30 || echo "Inbox empty or not created"
```

If items exist, count by status:
```bash
grep -l "qa_status: \"pending\"" docs/research-inbox/items/*.md 2>/dev/null | wc -l
grep -l "extraction_status: \"pending\"" docs/research-inbox/items/*.md 2>/dev/null | wc -l
grep -l "monograph_status: \"not started\"" docs/research-inbox/items/*.md 2>/dev/null | wc -l
```

Report:
- Items awaiting extraction: [N]
- Items awaiting QA: [N]
- Items ready to promote to monograph: [N]
- Items with no next action assigned: [N]

---

## PHASE 5 — Documentation drift check

Check alignment between key documentation files:

```bash
# Count command files
ls .claude/commands/*.md | wc -l
# Count agent files
ls .claude/agents/*.md | wc -l
# Check CLAUDE.md references these
grep -c "workflow-" CLAUDE.md
grep -c "workflow:" docs/SHORTCUTS_AND_WORKFLOWS.md
```

Flag any drift:
- A command exists but is not referenced in `CLAUDE.md` or `SHORTCUTS_AND_WORKFLOWS.md`
- An agent exists but is not referenced in `CLAUDE.md`
- A template exists but is not referenced in `docs/SHORTCUTS_AND_WORKFLOWS.md`

---

## PHASE 6 — Monograph health summary

```bash
python3 -c "
import json
data = json.load(open('data.json'))
issues = []
for i, d in enumerate(data):
    name = d.get('scientific_name', f'Entry #{i}')
    cd = d.get('clinical_data', {})
    pk = cd.get('pharmacokinetics', {})
    prec = cd.get('special_precautions', {})
    safety = cd.get('safety_and_interactions', {})
    ns = d.get('narrative_summary', {})
    # Flag thin fields (under 50 chars)
    for field, val in [
        ('drug_interactions', safety.get('drug_interactions','')),
        ('pregnancy', prec.get('pregnancy','')),
        ('lactation', prec.get('lactation','')),
        ('side_effects', ns.get('side_effects','')),
        ('contraindications', ns.get('contraindications','')),
    ]:
        if isinstance(val, str) and 0 < len(val.strip()) < 50:
            issues.append(f'[{i}] {name}: {field} is very short ({len(val.strip())} chars) — may need expansion')
print(f'Thin field warnings: {len(issues)}')
for issue in issues[:15]: print(f'  {issue}')
if len(issues) > 15: print(f'  ... and {len(issues)-15} more')
"
```

---

## PHASE 7 — Known issues review

Read the "Known Issues" section from `CLAUDE.md` and check which are still open:
```bash
grep -A 20 "Known Issues" CLAUDE.md | head -25
```

Specifically check:
```bash
grep -n "25 profiles\|50 profiles" database.html 2>/dev/null
ls robots.txt sitemap.xml 2>/dev/null || echo "Missing: robots.txt, sitemap.xml"
grep "og:image" index.html 2>/dev/null || echo "og:image: missing"
```

---

## PHASE 8 — Weekly maintenance report

```
## BMS Archive — Weekly Maintenance Report
Date: [today]
Period: last 7 days

### Git activity
Commits this week: [N]
Files changed: [list]
Uncommitted changes: [Yes/No — list if yes]

### Data health
Total entries: [N] ([N] Fungi, [N] Plant)
Validation errors: [N]
Validation warnings: [N]
  - Safe-claim warnings: [N]
  - Other warnings: [N]

### Research inbox
Items pending extraction: [N]
Items pending QA: [N]
Items ready for monograph: [N]

### Documentation drift
Commands without CLAUDE.md entry: [N] — [list]
Templates without workflow doc entry: [N]

### Monograph health
Entries with thin safety fields: [N]
Entries with placeholder text: [N]

### Known issues still open
[list from CLAUDE.md Known Issues]

### Priority actions for next week
Priority 1: [most urgent — likely remaining safe-claim warnings]
Priority 2: [second priority]
Priority 3: [third priority]
Priority 4: [fourth priority]

### Recommended commands to run
[e.g. /workflow:fix-safe-claims — [N] warnings remaining]
[e.g. /workflow:research-inbox PMID:XXXXX — [N] items pending]
[e.g. /workflow:update-monograph [entry] — thin safety fields]

### No changes made in this run
All findings are reported only. Run the specific workflow commands to act on them.
```

---

## Rules

- **Make no changes in this workflow** — report only
- **Do not run Docker or deploy commands**
- **If data.json fails JSON parse, flag as Priority 1 immediately**
- **This workflow should complete in under 3 minutes**
- **Do not add Instagram or social media content**
