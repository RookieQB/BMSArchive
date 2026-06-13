---
description: Run all available data validation checks on data.json and the BMS Archive monograph database. Reports errors, missing fields, safety gaps, and citation problems.
---

You are running data validation for the BMS Archive database.

Use `qa-test-agent` to run these checks. Do not skip any step. Report exactly what passed, what failed, and what was not available.

---

## Step 1 — JSON syntax validation

```bash
python3 -c "
import json
with open('data.json') as f:
    data = json.load(f)
fungi = [d for d in data if d.get('type') == 'Fungi']
plants = [d for d in data if d.get('type') == 'Plant']
print(f'PASS: Valid JSON — {len(data)} entries ({len(fungi)} Fungi, {len(plants)} Plant)')
"
```

If this fails, stop — the database file is broken and must be fixed before anything else.

---

## Step 2 — Required field validation

```bash
python3 -c "
import json
data = json.load(open('data.json'))
required_top = ['scientific_name','common_name','type','article_count','primary_categories']
errors = []
warnings = []
for i, d in enumerate(data):
    name = d.get('scientific_name', f'Entry #{i}')
    for f in required_top:
        if not d.get(f):
            errors.append(f'[{i}] {name}: MISSING {f}')
    if d.get('type') not in ('Fungi', 'Plant'):
        errors.append(f'[{i}] {name}: type must be Fungi or Plant, got: {d.get(\"type\")}')
    src = d.get('sources', {})
    if not src.get('top_studies_urls'):
        warnings.append(f'[{i}] {name}: no top_studies_urls')
    ns = d.get('narrative_summary', {})
    for field in ['historical_use','modern_application','side_effects','contraindications']:
        if not ns.get(field):
            errors.append(f'[{i}] {name}: narrative_summary.{field} is empty')
    cd = d.get('clinical_data', {})
    if not cd.get('used_part'):
        errors.append(f'[{i}] {name}: clinical_data.used_part is empty')
    if not cd.get('primary_active_compounds'):
        warnings.append(f'[{i}] {name}: primary_active_compounds is empty')
    if not cd.get('mechanism_of_action'):
        errors.append(f'[{i}] {name}: mechanism_of_action is empty')
    pk = cd.get('pharmacokinetics', {})
    for field in ['absorption','distribution','metabolism','excretion']:
        if not pk.get(field):
            errors.append(f'[{i}] {name}: pharmacokinetics.{field} is empty')
    safety = cd.get('safety_and_interactions', {})
    if not safety.get('drug_interactions'):
        errors.append(f'[{i}] {name}: drug_interactions is empty')
    prec = cd.get('special_precautions', {})
    for field in ['pregnancy','lactation','hepatic_impairment','renal_impairment']:
        if not prec.get(field):
            errors.append(f'[{i}] {name}: special_precautions.{field} is empty')
print(f'Errors: {len(errors)}')
for e in errors: print(f'  ERROR: {e}')
print(f'Warnings: {len(warnings)}')
for w in warnings: print(f'  WARN: {w}')
"
```

---

## Step 3 — Run extended validation script

```bash
python3 scripts/validate_archive_data.py
```

If this script does not exist yet, note it as missing and use Steps 1–2 only.

---

## Step 4 — Safety language check

```bash
python3 -c "
import json
data = json.load(open('data.json'))
issues = []
for i, d in enumerate(data):
    name = d.get('scientific_name', f'Entry #{i}')
    cd = d.get('clinical_data', {})
    prec = cd.get('special_precautions', {})
    safety = cd.get('safety_and_interactions', {})
    ns = d.get('narrative_summary', {})
    all_text = ' '.join([
        prec.get('pregnancy',''), prec.get('lactation',''),
        safety.get('drug_interactions',''), safety.get('toxicity',''),
        ns.get('side_effects',''), ns.get('contraindications','')
    ]).lower()
    if 'considered safe' in all_text or ('safe' in all_text and 'insufficient' not in all_text and 'limited' not in all_text):
        issues.append(f'[{i}] {name}: may contain unqualified \"safe\" claim — review manually')
    for placeholder in ['todo', 'lorem ipsum', 'insert source', 'citation needed', 'tbd', 'placeholder']:
        if placeholder in all_text:
            issues.append(f'[{i}] {name}: contains placeholder text: \"{placeholder}\"')
print(f'Safety/placeholder issues: {len(issues)}')
for issue in issues: print(f'  {issue}')
"
```

---

## Step 5 — Report summary

Produce a final validation report:

```
## Data Validation Report

Date: [today]
Total entries: [N] ([N] Fungi, [N] Plant)

### JSON syntax
[PASS / FAIL]

### Required fields
Errors: [N]
[list errors]

### Extended validation
[PASS / FAIL / SCRIPT NOT FOUND]

### Safety/placeholder check
Issues: [N]
[list issues]

### Overall status
[PASS — ready for commit/deploy]
[NEEDS FIXES — list critical issues]
```

---

## Rules

- **Do not claim validation passed unless every check was actually run**
- **If Step 1 (JSON syntax) fails, stop immediately** — do not run further checks
- **Report all errors and warnings** — do not filter or hide them
- **Do not make changes during validation** — report only; fix separately
