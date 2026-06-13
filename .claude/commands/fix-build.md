---
description: Debug and fix build, validation, or deployment errors in BMS Archive. Identifies root cause and makes the smallest safe fix. Use: /project:fix-build [error message or description]
---

You are debugging and fixing a BMS Archive error: **$ARGUMENTS**

---

## Step 1 — Read the exact error

Do not guess what the problem is. Read the full error message from "$ARGUMENTS" or reproduce it by running:

```bash
# For JSON errors:
python3 -c "import json; json.load(open('data.json'))"

# For validation errors:
python3 scripts/validate_archive_data.py

# For Docker build errors:
docker compose up --build 2>&1 | tail -50

# For Nginx config errors (run on server via pct exec):
# nginx -t
```

Read the error output completely before proposing a fix.

---

## Step 2 — Identify the root cause

State clearly:
- What failed
- What file is responsible
- What the exact error message says
- Why it failed (root cause, not symptom)

Do not propose a fix until the root cause is identified.

---

## Step 3 — Make the smallest safe fix

Apply only the minimum change needed to fix the error:
- Do not refactor surrounding code
- Do not change unrelated logic
- Do not introduce new patterns not already present in the codebase
- If fixing JSON: fix only the malformed entry; do not reformat the entire file

For JSON errors specifically:
```bash
# Find the line number of the JSON error:
python3 -c "
import json
try:
    json.load(open('data.json'))
except json.JSONDecodeError as e:
    print(f'Line {e.lineno}, Col {e.colno}: {e.msg}')
"
```

---

## Step 4 — Re-run the failed command

After the fix, run the exact command that failed:

```bash
# Whatever command produced the original error
```

Confirm the error is resolved. Do not assume the fix worked without running the check.

---

## Step 5 — Use qa-test-agent for final check

After confirming the specific error is fixed, run `qa-test-agent` to verify no regressions were introduced.

---

## Step 6 — Report

```
## Fix Report

Error: [exact error message]
Root cause: [why it failed]
Fix applied: [what was changed and in which file]
Fix verified: Yes / No — [command run and result]
Side effects: None / [list any]
Remaining issues: None / [list]
```

---

## Rules

- **Read the error first, fix second** — never make random changes to resolve an unknown error
- **Make the smallest possible fix** — do not refactor while fixing
- **Run the failed command again after fixing** — do not assume success
- **Do not skip the qa-test-agent check** after fixing
- **If the root cause is unclear, say so** and propose a diagnostic approach instead of guessing
