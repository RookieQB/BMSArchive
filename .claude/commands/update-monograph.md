---
description: Update or improve an existing BMS Archive monograph. Preserves structure, checks taxonomy, verifies claims, updates safety data and sources. Use: /project:update-monograph [species name or index]
---

You are updating an existing BMS Archive monograph for: **$ARGUMENTS**

---

## Step 1 — Locate the existing entry

Search `data.json` for the entry matching "$ARGUMENTS" by `scientific_name` or `common_name`. Read the full current entry before making any changes.

Report:
- Index in the array
- Current `scientific_name` and `common_name`
- Current `type`
- Which fields exist and which are empty or thin
- Any obvious problems (missing sections, weak language, unsupported claims)

Do not modify anything yet.

---

## Step 2 — Taxonomy check (taxonomy-nomenclature-agent)

Use `taxonomy-nomenclature-agent` to confirm:
- `scientific_name` is the currently accepted binomial (not a synonym)
- `common_name` is unambiguous for this species
- `clinical_data.used_part` correctly identifies the plant/fungus part used in studies
- No taxonomy issues have arisen since the entry was created

If the name needs updating, document the change and reason before making it.

---

## Step 3 — Evidence review (scientific-qa-evidence-agent)

Use `scientific-qa-evidence-agent` to:
- Check whether all existing claims are still supported by the cited sources
- Identify fields that contain overclaiming, weak language mismatch, or unsourced statements
- Check whether new studies have changed the evidence picture
- Verify that `pharmacokinetics` data is labeled correctly (human vs. preclinical)
- Verify that all safety fields are complete and up to date
- Confirm `mechanism_of_action` uses `<strong>` tags on key pharmacological targets

Produce a list of required changes before any edits are made.

---

## Step 4 — Make approved changes

Apply only the changes approved in Steps 2–3:
- Preserve existing structure — do not rewrite for style
- Update only the specific fields that have identified problems
- Add new sources using real PubMed URLs only
- If adding to `cited_references`, continue the existing numbering sequence
- If a section was previously thin and new human evidence exists, expand it proportionally
- If a section was previously speculative and better evidence exists, correct the evidence level language

---

## Step 5 — Validate

Run JSON validation:
```bash
python3 -c "import json; data=json.load(open('data.json')); print(f'{len(data)} entries — valid JSON')"
```

Run full validation if available:
```bash
python3 scripts/validate_archive_data.py
```

Then use `qa-test-agent` to verify the database page still renders correctly in the browser.

---

## Rules

- **Preserve existing structure** — do not reformat fields that are correct
- **Do not rewrite narrative unnecessarily** — only fix what is wrong
- **Do not add sources without verifying they are real and support the claim**
- **Do not downgrade safety warnings** — only strengthen them if evidence warrants
- **Never write "safe" when data is missing** — write "Insufficient data"
- **Do not add Instagram or social media content**
- Summarize what changed and why after the update is complete
