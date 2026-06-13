---
description: Master workflow — diagnose and fix a bug, validation error, build failure, or broken workflow. Identifies root cause, makes the smallest safe fix, re-runs the failed check, and verifies no regressions. Use: /workflow:fix-and-verify [error message or description]
---

You are running the **BMS Archive fix-and-verify workflow** for: **$ARGUMENTS**

This workflow follows a strict diagnose → fix → verify → confirm sequence. No broad rewrites. No guessing.

---

## PHASE 1 — Read the exact error

Do not guess. Read the full error output first.

If "$ARGUMENTS" is a JSON error:
```bash
python3 -c "
import json
try:
    json.load(open('data.json'))
    print('JSON valid — error may be elsewhere')
except json.JSONDecodeError as e:
    print(f'Line {e.lineno}, Col {e.colno}: {e.msg}')
    # Show context
    with open('data.json') as f:
        lines = f.readlines()
    start = max(0, e.lineno-3)
    end = min(len(lines), e.lineno+2)
    for i, line in enumerate(lines[start:end], start+1):
        marker = '>>>' if i == e.lineno else '   '
        print(f'{marker} {i}: {line}', end='')
"
```

If "$ARGUMENTS" is a validation script error:
```bash
python3 scripts/validate_archive_data.py 2>&1
```

If "$ARGUMENTS" is a Docker error:
```bash
docker compose up --build 2>&1 | tail -30
```

If "$ARGUMENTS" is an Nginx config error (run on server via pct exec):
```
# nginx -t  [run manually on server]
```

**Read all output before proposing a fix.**

---

## PHASE 2 — State the root cause

Before making any change, write:

```
ROOT CAUSE ANALYSIS
Error: [exact error message]
File: [which file]
Line: [line number if applicable]
Cause: [why it failed — be specific, not vague]
```

If the root cause cannot be determined from available information, say so and propose a diagnostic step — not a random fix.

---

## PHASE 3 — Make the smallest safe fix

Apply only the minimum change needed:
- Fix the specific broken line/field — do not reformat surrounding content
- Do not refactor while fixing
- Do not change logic that was not part of the error

For JSON errors specifically — do not use a text editor approach that might introduce new errors. Fix the minimal amount:
```python
# Example: if a trailing comma was introduced
# Fix: remove the trailing comma on the specific line
```

For validation errors — fix the specific field that failed:
```bash
# Example: an empty pregnancy field
# Fix: add "Insufficient safety data during pregnancy. Use is not recommended." to that entry only
```

---

## PHASE 4 — Re-run the failed command

After the fix, run the exact command that originally failed:

```bash
# Whatever produced the original error — run it again here
```

**Do not assume the fix worked without running the check.**

If the same error persists → re-examine root cause analysis. Do not apply a second random fix.

---

## PHASE 5 — Regression check

Run the full validation to confirm nothing else broke:

```bash
python3 -c "import json; data=json.load(open('data.json')); print(f'JSON valid — {len(data)} entries')"
python3 scripts/validate_archive_data.py
```

Check git diff to confirm only the intended file/field was changed:
```bash
git diff
```

If unexpected files appear in the diff → investigate before committing.

---

## PHASE 6 — QA check

If the fix touched `index.html` or `database.html`, verify in browser:
- No console errors
- Database grid renders
- Modal opens correctly

If the fix touched `server.js`:
```bash
curl -s -X POST http://localhost:3000/api/waitlist \
  -H "Content-Type: application/json" \
  -d '{"email":"fix-verify-test@example.com"}'
```

---

## PHASE 7 — Fix report

```
## Fix Report: $ARGUMENTS

### Root cause
[exact cause]

### Fix applied
File: [path]
Change: [what was changed — specific, not vague]

### Verification
Failed command re-run: [PASS/FAIL]
Full validation: [PASS/FAIL — N errors, N warnings]
Regression check: [PASS/FAIL]
Unexpected diff: [None/list]

### QA
[if applicable: browser check, API test]

### Remaining issues
[None / list]

### Status
FIXED — ready to commit / PARTIALLY FIXED — [remaining issues] / NOT FIXED — [next diagnostic step]
```

---

## Rules

- **Diagnose before fixing** — never apply a random change hoping it works
- **Make the smallest possible fix** — avoid scope creep during bug fixes
- **Re-run the failed command** — never claim fixed without verification
- **Check git diff** — confirm only the intended change was made
- **If root cause is unclear, say so** and propose a diagnostic step
- **Do not add Instagram or social media content**
