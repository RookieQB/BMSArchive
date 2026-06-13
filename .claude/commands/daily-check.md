---
description: Quick daily project status check for BMS Archive. Inspects git status, identifies changed files, checks for issues, and summarizes what needs attention. Makes no changes.
---

You are running a daily status check for BMS Archive. Read-only — make no changes.

---

## Step 1 — Git status

```bash
git status
git log --oneline -10
```

Report:
- Current branch
- Modified or untracked files
- Last 10 commits (to understand recent work context)

---

## Step 2 — Data integrity check

```bash
python3 -c "
import json
with open('data.json') as f:
    data = json.load(f)
fungi = len([d for d in data if d.get('type') == 'Fungi'])
plants = len([d for d in data if d.get('type') == 'Plant'])
print(f'data.json: {len(data)} entries ({fungi} Fungi, {plants} Plant) — valid JSON')
"
```

If this fails, flag it as the top priority issue.

---

## Step 3 — Check for obvious TODOs and placeholders

```bash
grep -rn "TODO\|FIXME\|HACK\|XXX\|placeholder\|citation needed\|lorem ipsum\|insert source" \
  --include="*.html" --include="*.js" --include="*.py" --include="*.json" \
  --exclude-dir=".git" . 2>/dev/null | head -20
```

---

## Step 4 — Check project structure

```bash
ls -la
ls -la .claude/agents/ 2>/dev/null
ls -la .claude/commands/ 2>/dev/null
ls -la docs/ 2>/dev/null
ls -la scripts/ 2>/dev/null
```

Confirm:
- `data.json` exists and is recent
- `CLAUDE.md` exists
- `.claude/agents/` has 8 agent files
- `.claude/commands/` has 12 command files
- `scripts/validate_archive_data.py` exists

---

## Step 5 — Check for known issues

Review the "Known Issues" section of `CLAUDE.md` and flag which items are still unresolved.

Also check these specific known gaps:
- [ ] `database.html` entry count — still shows "25 profiles" instead of 50?
- [ ] `robots.txt` — exists?
- [ ] `sitemap.xml` — exists?
- [ ] Favicon — exists?
- [ ] `og:image` — present in `index.html`?

```bash
grep -n "25 profiles\|50 profiles" database.html 2>/dev/null
ls -la robots.txt sitemap.xml favicon.* 2>/dev/null || echo "Missing: robots.txt, sitemap.xml, favicon"
grep -n "og:image" index.html 2>/dev/null || echo "og:image: missing from index.html"
```

---

## Step 6 — Produce status report

```
## BMS Archive — Daily Status Check
Date: [today]

### Git status
Branch: [branch name]
Modified files: [list or "Clean"]
Recent commits: [last 3]

### Data integrity
data.json: [N entries — VALID / INVALID]

### TODOs/Placeholders found
[list or "None"]

### Known issues still open
[list from CLAUDE.md Known Issues section + specific checks above]

### What needs attention today
Priority 1: [most urgent item]
Priority 2: [second item]
Priority 3: [third item]

### Suggested next command
[e.g., /project:validate-data, /project:qa, /project:add-monograph]
```

---

## Rules

- **Make no changes** — this is a read-only status check
- **Do not run Docker or deploy commands**
- **If data.json fails JSON parse, flag as Priority 1 immediately**
- **This command should complete in under 60 seconds**
