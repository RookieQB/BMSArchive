---
description: Master workflow — final publication readiness gate for a BMS Archive monograph. Checks all required sections, scientific accuracy, evidence grading, safety completeness, disclaimer, and validation. Produces a PASS/FAIL report. Use: /workflow:pre-publish [species name or data.json index]
---

You are running the **BMS Archive pre-publication gate** for: **$ARGUMENTS**

This is the final checkpoint before a monograph is treated as publication-ready. Every check is mandatory. If any Critical or Major issue is found, the result is FAIL.

---

## PHASE 0 — Locate entry

```bash
python3 -c "
import json
data = json.load(open('data.json'))
target = '$ARGUMENTS'.lower()
for i, d in enumerate(data):
    if target in d.get('scientific_name','').lower() or target in d.get('common_name','').lower() or str(i) == target.strip():
        print(f'Index {i}: {d[\"scientific_name\"]} ({d[\"common_name\"]})')
        print(f'Type: {d[\"type\"]} | Categories: {d[\"primary_categories\"]}')
"
```

Read the full entry. Do not proceed on memory — read the actual current data.

---

## PHASE 1 — Structural completeness check

Verify every required field is present and non-empty:

```bash
python3 scripts/validate_archive_data.py --entry "$ARGUMENTS"
```

**If any ERROR is reported: FAIL immediately. List the errors.**

For each required section, also check:
- Is the content substantive (not a one-word placeholder)?
- Does it use the correct evidence-level language?
- Does the safety section say "safe" without qualification? (→ FAIL)
- Does any field say "TODO", "placeholder", "insert source", "citation needed"? (→ FAIL)

---

## PHASE 2 — Taxonomy review (taxonomy-nomenclature-agent)

Use `taxonomy-nomenclature-agent` to confirm:
- `scientific_name` is the currently accepted binomial
- `type` field is "Fungi" or "Plant" (exact casing)
- `clinical_data.used_part` correctly identifies the part studied in the primary literature

Any taxonomy error → FAIL.

---

## PHASE 3 — Scientific QA (scientific-qa-evidence-agent)

Perform a full scientific review of the entry:

**Check every claim:**
- Is the language strength matched to the evidence level?
- Is any animal or in vitro evidence stated as human efficacy?
- Does any claim imply the compound treats, cures, prevents, or diagnoses a disease?
- Are all PubMed URLs in `top_studies_urls` real and do they correspond to the claims made?
- Does mechanism_of_action use `<strong>` tags on key targets?

**Check all safety fields:**
- `side_effects` — not empty, not "safe" without qualification
- `contraindications` — listed clearly, not empty
- `drug_interactions` — documented or states "No significant interactions established" with rationale
- `pregnancy` — conservative; "insufficient data" or "not recommended" if no human evidence
- `lactation` — conservative; "unknown if excreted in breast milk" if not studied
- `hepatic_impairment` — present and substantive
- `renal_impairment` — present and substantive
- `toxicity` — present; "no data available" is acceptable if stated, not blank

**For each issue found:**
```
LOCATION: [field]
SEVERITY: Critical / Major / Minor
ISSUE: [description]
REQUIRED ACTION: [fix needed]
```

Critical or Major issues → FAIL.

---

## PHASE 4 — Sources check

For each URL in `sources.top_studies_urls`:
- Does the URL follow the pattern `https://pubmed.ncbi.nlm.nih.gov/[8-digit-PMID]/`?
- Is there at least one URL? (zero sources → FAIL)

For plant entries with `cited_references`:
- Do references follow `[N] - Author(s), Title, Journal, Year, PMID: XXXXXXXX` format?

Any fabricated-looking URL or URL that does not match claimed content → FAIL.

---

## PHASE 5 — Disclaimer check

Verify the medical disclaimer is present in the relevant section of `index.html` and `database.html`:
- `database.html` sticky disclaimer banner: present?
- `index.html` disclaimer section: present?

If the monograph text itself needs a disclaimer note, confirm it is present.

---

## PHASE 6 — No placeholder / no draft content

Search the entry for placeholder text:
```bash
python3 -c "
import json
data = json.load(open('data.json'))
target = '$ARGUMENTS'.lower()
entry = next((d for d in data if target in d.get('scientific_name','').lower()), None)
if entry:
    text = str(entry).lower()
    placeholders = ['todo','lorem ipsum','insert source','citation needed','tbd','placeholder','[pmid]','[source]']
    found = [p for p in placeholders if p in text]
    print('Placeholders found:', found if found else 'None')
"
```

Any placeholder text → FAIL.

---

## PHASE 7 — Final validation run

```bash
python3 scripts/validate_archive_data.py
python3 scripts/validate_archive_data.py --strict
```

Errors → FAIL. Warnings must be reviewed (do not automatically FAIL on warnings, but each must be assessed).

---

## PHASE 8 — Publication readiness report

```
## Pre-Publication Gate: $ARGUMENTS
Date: [today]

### Structural check
JSON valid:                [PASS/FAIL]
Required fields complete:  [PASS/FAIL] — [N] errors
No placeholder text:       [PASS/FAIL]

### Taxonomy
Accepted name confirmed:   [PASS/FAIL]
Type field correct:        [PASS/FAIL]
Used part confirmed:       [PASS/FAIL]

### Scientific QA
Evidence language match:   [PASS/FAIL]
No animal→human upgrade:   [PASS/FAIL]
No disease treatment claim:[PASS/FAIL]
Sources real and relevant: [PASS/FAIL]
<strong> tags in MoA:      [PASS/FAIL]

### Safety completeness
Adverse effects:           [PASS/FAIL]
Contraindications:         [PASS/FAIL]
Drug interactions:         [PASS/FAIL]
Pregnancy:                 [PASS/FAIL]
Lactation:                 [PASS/FAIL]
Hepatic impairment:        [PASS/FAIL]
Renal impairment:          [PASS/FAIL]
No unqualified "safe":     [PASS/FAIL]

### Validation
Errors: [N]
Warnings: [N] — [brief assessment of each]

### Critical issues (must fix before publication)
[list or "None"]

### Major issues (should fix before publication)
[list or "None"]

### Minor issues (non-blocking)
[list or "None"]

### OVERALL RESULT
## [PASS — PUBLICATION READY] / [FAIL — DO NOT PUBLISH]

[If FAIL: list every blocking issue]
```

---

## Rules

- **FAIL on any Critical or Major scientific or safety issue**
- **FAIL on empty pregnancy/lactation sections**
- **FAIL on fabricated or unverifiable citations**
- **FAIL on unresolved validation errors**
- **Do not mark PASS unless every check was actually run**
- **A PASS here means the monograph is ready for the database — not that it is peer-reviewed medical advice**
- **Do not add Instagram or social media content**
