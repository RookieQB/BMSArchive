---
description: Master workflow — create a complete new BMS Archive monograph from scratch. Orchestrates taxonomy, extraction, scientific QA, schema check, writing, validation, and QA in the correct order. Use: /workflow:new-monograph [species name]
---

You are running the **BMS Archive master new-monograph workflow** for: **$ARGUMENTS**

This is the complete, non-skippable creation pipeline. Every step must complete before the next begins. If a step fails or produces a blocker, stop and report — do not continue to the next step.

---

## PHASE 0 — Pre-flight

Read these files before doing anything:
- `CLAUDE.md` — project rules, schema, deployment rules
- `docs/templates/MONOGRAPH_TEMPLATE.md` — required structure
- `docs/rubrics/EVIDENCE_SCORING.md` — evidence level definitions
- `docs/tasks/MONOGRAPH_TASK_TEMPLATE.md` — task structure

Then check for an existing entry:
```bash
python3 -c "
import json
data = json.load(open('data.json'))
target = '$ARGUMENTS'.lower()
matches = [d for d in data if target in d.get('scientific_name','').lower() or target in d.get('common_name','').lower()]
if matches:
    for m in matches:
        print(f'DUPLICATE FOUND: Index {data.index(m)} — {m[\"scientific_name\"]} / {m[\"common_name\"]}')
else:
    print('No duplicate found — safe to proceed.')
"
```

**If a duplicate is found: STOP. Use `/workflow:update-monograph` instead.**

---

## PHASE 1 — Taxonomy (taxonomy-nomenclature-agent)

Use `taxonomy-nomenclature-agent` to produce a taxonomy confirmation block:

```
INPUT: $ARGUMENTS
ACCEPTED LATIN NAME: [confirmed]
SYNONYMS: [list]
BOTANICAL FAMILY: [family]
TYPE FIELD: "Fungi" or "Plant"
USED PART: [part used in clinical literature]
COMMON NAME AMBIGUITY: Yes/No — [explanation]
DUPLICATE CHECK: Clear
RECOMMENDATION: Proceed / Stop — [reason]
```

**If taxonomy is ambiguous or a duplicate is found: STOP and ask for clarification.**

---

## PHASE 2 — Task setup

Create a task file at `docs/tasks/active/[scientific-name-kebab].md` using `docs/tasks/MONOGRAPH_TASK_TEMPLATE.md`. Fill in all available fields from Phase 1 output.

If `docs/tasks/active/` does not exist:
```bash
mkdir -p docs/tasks/active
```

---

## PHASE 3 — Source collection

Search PubMed for the top studies on this species:
- Primary search: `[scientific name] AND (clinical trial OR systematic review OR randomized controlled trial) AND humans`
- Secondary: `[scientific name] AND pharmacokinetics`
- Safety: `[scientific name] AND (adverse effects OR toxicity OR drug interactions)`

Collect up to 5–8 key PubMed IDs. For each, note study type and available abstract.

Check whether regulatory monographs exist:
- EMA/HMPC — search `ema.europa.eu/en/herbal-products`
- ESCOP — note if monograph known
- WHO monographs on selected medicinal plants — note if included
- NCCIH fact sheet — check if available

**Document all sources found and all gaps at this stage.**

---

## PHASE 4 — Evidence extraction (extraction-synthesis-agent)

Use `extraction-synthesis-agent` for each key source. For each:

Apply `docs/templates/STUDY_EXTRACTION_TEMPLATE.json` fields.
Flag all missing values explicitly — never infer or invent.
Assign study type and evidence level.

After all extractions, produce a consolidated evidence table:

```
| PMID | Study type | Evidence level | Indication | n | Duration | Key finding |
|------|-----------|----------------|------------|---|----------|-------------|
| ... | ... | ... | ... | ... | ... | ... |
```

Identify the highest available evidence level for each claimed use.

---

## PHASE 5 — Scientific QA (scientific-qa-evidence-agent)

Use `scientific-qa-evidence-agent` to review all extracted content before writing.

For each claim that will appear in the monograph:
- Confirm the study type matches the language strength
- Confirm no animal/in vitro evidence is stated as human efficacy
- Confirm safety fields are complete and conservative
- Confirm `mechanism_of_action` uses `<strong>` tags for key targets
- Confirm no claim implies the compound treats, cures, prevents, or diagnoses any disease
- Confirm all PubMed URLs are real

**If scientific QA raises a Critical issue: fix it before Phase 6. Do not write to data.json with unresolved Critical issues.**

---

## PHASE 6 — Schema check (archive-data-model-agent)

Confirm the new entry fits the existing `data.json` schema exactly. Required field structure:

```
scientific_name, common_name, type, article_count, primary_categories,
sources.top_studies_urls, sources.cited_references (plants),
narrative_summary.{historical_use, modern_application, side_effects, contraindications},
clinical_data.used_part, primary_active_compounds, mechanism_of_action,
clinical_data.pharmacokinetics.{absorption, distribution, metabolism, excretion},
clinical_data.safety_and_interactions.{drug_interactions, toxicity},
clinical_data.special_precautions.{pregnancy, lactation, hepatic_impairment, renal_impairment}
```

If any field in the new entry requires a schema change, consult `archive-data-model-agent` and document the migration plan before proceeding.

---

## PHASE 7 — Write the monograph

Write the complete entry following `docs/templates/MONOGRAPH_TEMPLATE.md`.

Mandatory sections — all must be present and non-empty:

| Section | Empty allowed? | If no data |
|---|---|---|
| historical_use | No | Describe ethnobotanical use or write "No documented traditional use found" |
| modern_application | No | Summarize the state of evidence honestly |
| side_effects | No | "No adverse effects documented in available clinical trials" + evidence limitation note |
| contraindications | No | List known + precautionary; never leave blank |
| used_part | No | Must specify exact part |
| mechanism_of_action | No | With `<strong>` tags on targets |
| absorption/distribution/metabolism/excretion | No | Write "Human PK data not available. Preclinical data: [or insufficient data]" |
| drug_interactions | No | "No clinically significant interactions established. Theoretical interactions include: [or none identified]" |
| toxicity | No | "No toxicity data from human studies available." if absent |
| pregnancy | No | "Insufficient safety data. Not recommended during pregnancy." if absent |
| lactation | No | "Unknown if excreted in breast milk. Not recommended during breastfeeding." if absent |
| hepatic_impairment | No | Precautionary guidance |
| renal_impairment | No | Precautionary guidance |

Append to `data.json`. Maintain sort order: Fungi (indices 0–24), Plants (25+).

---

## PHASE 8 — Validation

```bash
python3 -c "import json; data=json.load(open('data.json')); print(f'JSON valid — {len(data)} entries')"
python3 scripts/validate_archive_data.py --entry "$ARGUMENTS"
python3 scripts/validate_archive_data.py
```

**If any ERROR is produced: fix it before continuing. Do not proceed to Phase 9 with errors.**

---

## PHASE 9 — QA (qa-test-agent)

Verify in the browser:
- `database.html` loads and renders all entries including the new one
- The new card appears in the grid
- Clicking the new card opens the modal with all sections populated
- Type filter (Fungi/Plant) still works correctly
- Entry count reflects the addition

---

## PHASE 10 — Summary report

Produce this report:

```
## New Monograph: $ARGUMENTS

### Taxonomy
Accepted name:    [name]
Type:             Fungi / Plant
Family:           [family]
Used part:        [part]

### Evidence summary
| Indication | Evidence level | Study types used |
|-----------|----------------|-----------------|
| [use 1]   | [A/B/C/D/E/T/U] | [list] |

### Sources used
[numbered list with PMIDs]

### Safety completeness
- Adverse effects:     ✓/✗
- Contraindications:   ✓/✗
- Drug interactions:   ✓/✗
- Pregnancy:           ✓/✗
- Lactation:           ✓/✗
- Hepatic impairment:  ✓/✗
- Renal impairment:    ✓/✗

### Missing data
[list — be specific about what could not be found]

### Validation
JSON valid:        ✓/✗
Validation errors: [N]
Validation warns:  [N]

### QA
Browser render:    ✓/✗ (manual check required)

### Scientific QA sign-off
[ ] Taxonomy confirmed
[ ] Evidence levels correctly assigned
[ ] No overclaiming
[ ] Safety sections complete and conservative
[ ] No fabricated citations
[ ] Approved by scientific-qa-evidence-agent

### Status
DRAFT — requires manual scientific review before publication
```

---

## Absolute rules

- **Never invent PMIDs or citations**
- **Never present animal or in vitro evidence as human efficacy**
- **Never write "safe" without qualifying evidence**
- **Never skip Phase 5 (scientific QA)**
- **Never mark a monograph as publication-ready from this command alone** — it produces a draft
- **Do not add Instagram or social media content**
