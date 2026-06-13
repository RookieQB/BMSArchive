---
description: Master workflow — add a new study, paper, or research source to the BMS Archive research inbox. Extracts structured data, assigns status, and queues for scientific QA review. Does not directly edit monographs. Use: /workflow:research-inbox [PMID, DOI, URL, or description]
---

You are running the **BMS Archive research inbox workflow** for: **$ARGUMENTS**

The research inbox is a controlled staging area. Raw research sources enter here, go through structured extraction and QA review, and are only promoted to final monographs after explicit approval. Nothing goes from inbox to published monograph automatically.

---

## PHASE 0 — Setup

Check if `docs/research-inbox/` exists:
```bash
ls docs/research-inbox/ 2>/dev/null || echo "Directory missing"
```

If it does not exist:
```bash
mkdir -p docs/research-inbox/items
```

Read `docs/research-inbox/README.md` for inbox conventions.

---

## PHASE 1 — Parse the input

Determine what "$ARGUMENTS" refers to:

- **PMID** (8-digit number or `PMID:XXXXXXXX`): fetch abstract from PubMed
- **DOI** (starts with `10.`): record as DOI, note if abstract is accessible
- **URL**: record URL, fetch available text
- **Description** (free text about a study): record as manual entry, mark as "no PMID confirmed"

If a PMID was provided, confirm it corresponds to a real article. If uncertain, mark `pmid_verified: false`.

---

## PHASE 2 — Extract structured data (extraction-synthesis-agent)

Use `extraction-synthesis-agent` and `docs/templates/STUDY_EXTRACTION_TEMPLATE.json` to extract all available fields.

Write all missing fields as `"Unknown / not reported"` — never infer.

Key fields to extract:
- `citation` — full citation string
- `pmid`, `doi`
- `study_type` — SR-MA / RCT / CCT / OBS / CASE / MONO / ANIMAL / IN-VITRO / REVIEW / TRAD
- `evidence_level` — A / B / C / D / E / T / U
- `plant_or_fungus.accepted_latin_name`
- `plant_or_fungus.part_used`
- `preparation.type`, `standardization`
- `intervention.dose`, `duration`
- `population_or_model.type`, `sample_size`, `condition`
- `results` — with statistical significance if reported
- `adverse_events`
- `limitations`
- `author_conclusion`
- `qa_notes` — anything needing scientific QA attention

---

## PHASE 3 — Create the inbox item

Generate a filename: `docs/research-inbox/items/[PMID or slug]-[species-kebab].md`

Example: `docs/research-inbox/items/38547821-ganoderma-lucidum.md`

If no PMID: `docs/research-inbox/items/[YYYY-MM-DD]-[species-kebab]-[condition-slug].md`

Write a source note using `docs/research-inbox/SOURCE_NOTE_TEMPLATE.md`:

```yaml
---
title: "[Study title]"
pmid: "[or Unknown]"
doi: "[or Unknown]"
pmid_verified: true/false
url: "[PubMed URL or source URL]"
plant_fungus: "[accepted Latin name]"
clinical_area: "[condition or use studied]"
study_type: "[SR-MA / RCT / CCT / OBS / ANIMAL / IN-VITRO / TRAD]"
evidence_level: "[A / B / C / D / E / T / U]"
evidence_type: "human / preclinical / in-vitro / traditional"
abstract_available: true/false
full_text_available: true/false
extraction_status: "complete / partial / pending"
qa_status: "pending"
monograph_status: "not started"
date_added: "[YYYY-MM-DD]"
added_by: "extraction-synthesis-agent via workflow-research-inbox"
---

## Key Findings
[2–4 sentences summarising what the study found — not interpretation]

## Limitations
[from the paper or obvious from study design]

## Safety Notes
[any adverse events, interactions, or contraindication data]

## Missing Fields
[explicitly list what could not be extracted]

## Notes for QA
[anything requiring scientific-qa-evidence-agent attention before this source can be used]

## Next Action
[ ] Scientific QA review required before use in monograph
[ ] Taxonomy check needed for: [reason]
[ ] Full text required for: [specific claim]
[ ] No existing monograph — may trigger new-monograph workflow
[ ] Can supplement existing monograph for: [species] — [field]
```

---

## PHASE 4 — Taxonomy quick check

If the species in this study is not already in `data.json`:
```bash
python3 -c "
import json
data = json.load(open('data.json'))
target = '[species from study]'.lower()
matches = [d for d in data if target in d.get('scientific_name','').lower()]
print(f'Existing entry: {\"Found — \" + str(len(matches)) if matches else \"None — may need new-monograph workflow\"}')
"
```

Note in the inbox item:
- `existing_monograph: true/false`
- `monograph_index: [N or null]`

---

## PHASE 5 — Queue for review

Update the inbox item status fields:
- `extraction_status: "complete"` (or "partial" if fields are missing)
- `qa_status: "pending"` — flags it for scientific-qa-evidence-agent review

Do **not** change `monograph_status` to anything other than `"not started"` from this workflow. Promoting to a monograph requires explicit `/workflow:new-monograph` or `/workflow:update-monograph` run.

---

## PHASE 6 — Summary

```
## Research Inbox: $ARGUMENTS

### Item created
File: docs/research-inbox/items/[filename].md
PMID: [or Unknown]
Species: [accepted Latin name]
Study type: [type]
Evidence level: [level]

### Extraction completeness
Complete fields: [N/total]
Missing fields: [list]
Full text required: Yes/No — [reason]

### Existing monograph
[Found at index N / Not found — would require new-monograph workflow]

### Next actions required
[ ] Scientific QA review (scientific-qa-evidence-agent)
[ ] Taxonomy check if species is new
[ ] Full text retrieval if needed
[ ] Promote to monograph via /workflow:new-monograph or /workflow:update-monograph
```

---

## Rules

- **Raw research is not final evidence** — inbox items are never treated as published
- **Abstract-only evidence must be marked as limited** — set `full_text_available: false` and note the limitation
- **Never edit `data.json` from this workflow** — inbox → QA → monograph workflow only
- **Never assume a PMID is real** without verification
- **Do not add Instagram or social media content**
