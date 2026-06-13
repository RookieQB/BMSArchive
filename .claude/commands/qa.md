---
description: General quality gate for BMS Archive. Runs all available checks after any code, data, or configuration change. Reports pass/fail for each check. Use: /project:qa [optional: what was changed]
---

You are running the BMS Archive quality gate after: **$ARGUMENTS**

Use `qa-test-agent`. Run every applicable check below. Never claim a check passed unless you actually ran it. Write `NOT RUN` if a check was skipped, and `NOT AVAILABLE` if a command or tool does not exist.

---

## Step 1 — Identify what changed

If "$ARGUMENTS" describes what was changed, focus on the relevant checks.
If no argument is given, run all checks.

Read `git status` to identify which files have been modified:
```bash
git status
```

---

## Step 2 — Data validation (if data.json was modified)

```bash
python3 -c "
import json
data = json.load(open('data.json'))
required = ['scientific_name','common_name','type','article_count','primary_categories']
errors = []
for i, d in enumerate(data):
    for f in required:
        if not d.get(f): errors.append(f'[{i}] {d.get(\"scientific_name\",\"?\")} missing {f}')
    if d.get('type') not in ('Fungi','Plant'): errors.append(f'[{i}]: invalid type')
fungi = len([d for d in data if d['type']=='Fungi'])
plants = len([d for d in data if d['type']=='Plant'])
print(f'JSON: valid — {len(data)} entries ({fungi} Fungi, {plants} Plant)')
print('Field errors:', errors if errors else 'None')
"
```

```bash
python3 scripts/validate_archive_data.py
```

---

## Step 3 — Browser check (if index.html or database.html was modified)

Open both pages in a browser and verify:

**index.html:**
- [ ] Page loads without console errors
- [ ] Newsletter form visible and accepts input
- [ ] Submit sends to `/api/waitlist` and shows success state
- [ ] Disclaimer banner visible
- [ ] "Browse Database" link works

**database.html:**
- [ ] All entries render in the grid
- [ ] Search filters correctly
- [ ] "Fungi" filter pill shows 25 entries; "Plant" shows 25
- [ ] Clicking a card opens the modal
- [ ] Modal shows all sections (narrative, clinical data, pharmacokinetics, safety, sources)
- [ ] Modal closes on ✕ and Escape
- [ ] Empty state shows when search finds nothing

---

## Step 4 — API smoke test (if server.js was modified)

Requires Docker running or Node.js directly:

```bash
# Valid email — expect: {"ok":true}
curl -s -X POST http://localhost:3000/api/waitlist \
  -H "Content-Type: application/json" \
  -d '{"email":"qa-check@example.com"}'

# Invalid email — expect: 400 + error message
curl -s -X POST http://localhost:3000/api/waitlist \
  -H "Content-Type: application/json" \
  -d '{"email":"notanemail"}'

# Unknown route — expect: 404
curl -s http://localhost:3000/api/unknown
```

---

## Step 5 — Admin panel check (if admin files were modified)

```bash
python3 admin_server.py &
sleep 1
curl -s http://localhost:5050/api/data | python3 -c "
import json, sys
data = json.load(sys.stdin)
print(f'Admin API: OK — {len(data)} entries')
"
kill %1 2>/dev/null
```

---

## Step 6 — Docker build check (if Dockerfile, nginx.conf, or server.js was modified)

```bash
docker compose up --build -d
# Wait for containers to start, then check:
curl -s -o /dev/null -w "%{http_code}" http://localhost:80
# Expect: 301 (redirect to HTTPS) or 200 if testing locally without TLS
docker compose down
```

---

## Step 7 — Unintended changes check

```bash
git diff --name-only
```

Confirm that no unrelated files were modified. Flag any unexpected changes.

---

## Step 8 — Produce QA report

```
## QA Report — $ARGUMENTS

Changed files: [list from git status]

| Check                    | Result    | Notes |
|--------------------------|-----------|-------|
| JSON syntax              | PASS/FAIL/NOT RUN | |
| Required field validation| PASS/FAIL/NOT RUN | |
| Extended validation      | PASS/FAIL/NOT AVAILABLE | |
| Browser: index.html      | PASS/FAIL/NOT RUN | |
| Browser: database.html   | PASS/FAIL/NOT RUN | |
| API smoke test           | PASS/FAIL/NOT RUN | |
| Admin panel              | PASS/FAIL/NOT RUN | |
| Docker build             | PASS/FAIL/NOT RUN | |
| Unintended changes       | None/[list] | |

Issues found: [list or None]
Missing test coverage: [list]

Recommendation: Ready to commit / Needs fixes
```

---

## Rules

- **Never claim PASS unless the check was run** — use NOT RUN
- **Never hide errors or warnings** — report all output
- **If JSON validation fails, everything else is secondary** — fix JSON first
- **Do not make fixes during QA** — report, then fix separately, then re-run
