---
description: Master workflow — update an existing BMS Archive monograph. Preserves structure, identifies gaps, checks taxonomy, validates all claims, and runs QA. Use: /workflow:update-monograph [species name or index]
---

You are running the **BMS Archive master update-monograph workflow** for: **$ARGUMENTS**

This workflow preserves what is correct and fixes only what needs fixing. It does not rewrite entries that are structurally sound.

---

## PHASE 0 — Locate and read

Find the entry in `data.json`:
```bash
python3 -c "
import json
data = json.load(open('data.json'))
target = '$ARGUMENTS'.lower()
for i, d in enumerate(data):
    if target in d.get('scientific_name','').lower() or target in d.get('common_name','').lower():
        print(f'Found at index {i}: {d[\"scientific_name\"]} — {d[\"common_name\"]}')
        print(f'Type: {d[\"type\"]}')
        print(f'Article count: {d[\"article_count\"]}')
        print(f'Categories: {d[\"primary_categories\"]}')
"
```

**If no entry is found:** Stop. Use `/workflow:new-monograph $ARGUMENTS` instead.

Read the full existing entry from `data.json`. Report the current state:
- Which sections are populated vs. empty
- Which safety fields are missing or thin
- Approximate word count of each narrative field (flag if suspiciously short)

---

## PHASE 1 — Gap analysis

Produce a gap analysis checklist before touching anything:

```
## Gap Analysis: $ARGUMENTS

### Missing or empty required fields
- [ ] narrative_summary.historical_use: [present/empty/thin]
- [ ] narrative_summary.modern_application: [present/empty/thin]
- [ ] narrative_summary.side_effects: [present/empty/thin]
- [ ] narrative_summary.contraindications: [present/empty/thin]
- [ ] clinical_data.used_part: [present/empty]
- [ ] clinical_data.primary_active_compounds: [present/empty]
- [ ] clinical_data.mechanism_of_action: [present/uses <strong> tags/missing tags]
- [ ] pharmacokinetics.absorption: [present/empty]
- [ ] pharmacokinetics.distribution: [present/empty]
- [ ] pharmacokinetics.metabolism: [present/empty]
- [ ] pharmacokinetics.excretion: [present/empty]
- [ ] safety_and_interactions.drug_interactions: [present/empty]
- [ ] safety_and_interactions.toxicity: [present/empty]
- [ ] special_precautions.pregnancy: [present/empty]
- [ ] special_precautions.lactation: [present/empty]
- [ ] special_precautions.hepatic_impairment: [present/empty]
- [ ] special_precautions.renal_impairment: [present/empty]
- [ ] sources.top_studies_urls: [N URLs present]

### Unqualified "safe" claims
[list any fields containing "safe" without qualifying evidence language]

### Evidence language mismatches
[list any fields where language is stronger than the evidence level warrants]

### Update priority
High: [fields that are empty or contain unqualified claims]
Medium: [fields that are present but thin or missing detail]
Low: [fields that are present and adequate]
```

**Confirm the update scope with this analysis before making any changes.**

---

## PHASE 2 — Taxonomy check (if names are involved)

If the update touches `scientific_name`, `common_name`, or `clinical_data.used_part`, use `taxonomy-nomenclature-agent` to confirm:
- `scientific_name` is still the currently accepted binomial
- `used_part` correctly identifies the part studied in the literature being added

If taxonomy is correct and not being modified, this phase can be skipped.

---

## PHASE 3 — Evidence review for additions

If new studies are being added:

For each new source, use `extraction-synthesis-agent` with `docs/templates/STUDY_EXTRACTION_TEMPLATE.json`.
Extract: study type, evidence level, population, dose, extract type, outcomes, adverse events, PMID.
Flag all missing fields.

For each addition, confirm with `scientific-qa-evidence-agent`:
- Does the new source actually support the claim it will be cited for?
- Is the evidence level assignment correct?
- Does the language match the evidence level?

---

## PHASE 4 — Scientific QA on existing content (scientific-qa-evidence-agent)

Review the sections being modified (not the whole entry unless a full review was requested):

For each claim in the updated sections:
- Confirm study type matches language strength
- Confirm no unqualified "safe" claims remain
- Confirm all `<strong>` tags are present in mechanism_of_action
- Confirm safety fields are conservative and complete
- Confirm no claim implies treatment, cure, prevention, or diagnosis

---

## PHASE 5 — Make targeted changes

Apply only the changes identified and approved in Phases 1–4.

Rules:
- **Do not rewrite sections that are structurally sound** — edit what needs editing
- **Do not remove safety warnings** to make the profile look cleaner
- **Do not upgrade evidence level** without documented justification
- **Do not add new sources** that were not processed through extraction-synthesis-agent
- If adding to `cited_references`, continue the existing numbering sequence
- If editing mechanism_of_action, preserve `<strong>` tags on all key pharmacological targets

---

## PHASE 6 — Validation

```bash
python3 -c "import json; json.load(open('data.json')); print('JSON valid')"
python3 scripts/validate_archive_data.py --entry "$ARGUMENTS"
python3 scripts/validate_archive_data.py
```

**All errors must be resolved before continuing. Warnings should be reviewed.**

---

## PHASE 7 — QA check

Verify in the browser:
- `database.html` loads and renders the updated entry correctly
- Modal opens and all sections display properly
- No console errors

---

## PHASE 8 — Change summary

```
## Update Summary: $ARGUMENTS

### Fields modified
[list exact fields changed]

### Fields added
[list new content added]

### Sources added
[PMIDs if applicable]

### Warnings resolved
Before: [N] warnings
After:  [N] warnings

### Validation
JSON valid:  ✓/✗
Errors:      [N]
Warnings:    [N]

### What was NOT changed
[explain what was left as-is and why]

### Remaining gaps
[list anything still incomplete and why it was not fixed in this update]
```

---

## Rules

- **Do not rewrite entries unnecessarily** — targeted edits only
- **Do not downgrade safety warnings** under any circumstances
- **Do not mark an update as complete** if validation errors remain
- **Do not add Instagram or social media content**
