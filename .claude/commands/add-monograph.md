---
description: Create a new BMS Archive phytomedicine monograph following the official multi-agent scientific workflow. Use: /project:add-monograph [species name]
---

You are creating a new BMS Archive monograph for: **$ARGUMENTS**

BMS Archive publishes structured, peer-reviewed monographs for medicinal plants and fungi. Every claim must be traceable to a real PubMed-indexed source. The database is `data.json` (50 entries: 25 Fungi, 25 Plants). The `type` field must be exactly `"Fungi"` or `"Plant"`.

This is a multi-agent workflow. Execute each step in order.

---

## Step 1 — Taxonomy check (taxonomy-nomenclature-agent)

Use `taxonomy-nomenclature-agent` to:
- Confirm the currently accepted Latin binomial (not a synonym)
- Identify the botanical family
- Check for synonyms used in clinical literature
- Flag if the common name "$ARGUMENTS" is ambiguous (could refer to multiple species)
- Confirm the `type` field value: `"Fungi"` or `"Plant"`
- Identify the plant/fungus part(s) used in studies
- Check whether an entry for this species already exists in `data.json`

If a duplicate is found, stop and report it. Do not create a duplicate entry.

---

## Step 2 — Literature extraction (extraction-synthesis-agent)

Use `extraction-synthesis-agent` to:
- Search for relevant PubMed studies on this species
- Extract from top studies: study type, population, dose, extract type, plant part, outcomes, adverse events, PMID
- Identify the highest evidence level available (SR-MA → RCT → CCT → OBS → ANIMAL → IN-VITRO → TRAD)
- Build a numbered reference list with real PMIDs in the format: `[N] - Author(s), Title, Journal, Year, PMID: XXXXXXXX`
- Flag all missing information explicitly — do not infer or invent

---

## Step 3 — Scientific QA (scientific-qa-evidence-agent)

Use `scientific-qa-evidence-agent` to validate every field before writing to `data.json`:
- Confirm that narrative_summary fields do not overclaim
- Confirm mechanism_of_action uses `<strong>` tags for key pharmacological targets
- Confirm pharmacokinetics data matches the evidence level (human vs. preclinical)
- Confirm safety_and_interactions and special_precautions are complete
- Confirm all contraindications are documented
- Confirm no field implies the compound treats, cures, or prevents a disease
- Confirm all PubMed URLs are real and support the claims made

---

## Step 4 — Write the data.json entry

Write a new entry conforming exactly to the BMS Archive schema:

```json
{
  "scientific_name": "[accepted Latin binomial]",
  "common_name": "[primary common name(s)]",
  "type": "Fungi or Plant",
  "article_count": [integer from PubMed eSearch],
  "primary_categories": ["Category1", "Category2"],
  "sources": {
    "top_studies_urls": ["https://pubmed.ncbi.nlm.nih.gov/PMID/"],
    "cited_references": ["[N] - Author(s), Title, Journal, Year, PMID: XXXXXXXX"]
  },
  "narrative_summary": {
    "historical_use": "...",
    "modern_application": "...",
    "side_effects": "...",
    "contraindications": "..."
  },
  "clinical_data": {
    "used_part": "...",
    "primary_active_compounds": ["Compound1"],
    "mechanism_of_action": "... <strong>TARGET</strong> ...",
    "pharmacokinetics": {
      "absorption": "...",
      "distribution": "...",
      "metabolism": "...",
      "excretion": "..."
    },
    "safety_and_interactions": {
      "drug_interactions": "...",
      "toxicity": "..."
    },
    "special_precautions": {
      "pregnancy": "...",
      "lactation": "...",
      "hepatic_impairment": "...",
      "renal_impairment": "..."
    }
  }
}
```

Append the new entry to `data.json`. Keep Fungi entries first (indices 0–24), Plants second (indices 25+).

---

## Step 5 — Validation (qa-test-agent)

Use `qa-test-agent` to:
```bash
python3 -c "
import json
data = json.load(open('data.json'))
required = ['scientific_name','common_name','type','article_count','primary_categories']
errors = []
for d in data:
    for f in required:
        if not d.get(f):
            errors.append(f'{d.get(\"scientific_name\",\"?\")} missing {f}')
    if d.get('type') not in ('Fungi','Plant'):
        errors.append(f'{d[\"scientific_name\"]}: invalid type')
fungi = len([d for d in data if d['type']=='Fungi'])
plants = len([d for d in data if d['type']=='Plant'])
print(f'Total: {len(data)} ({fungi} Fungi, {plants} Plant)')
print('Errors:', errors if errors else 'None')
"
```

Then run `python3 scripts/validate_archive_data.py` if available.

---

## Absolute rules

- **Never invent PMIDs or citations** — every URL and reference must be real and verifiable
- **Never present animal or in vitro evidence as human efficacy**
- **Never write "safe" when safety data is missing** — write "Insufficient data"
- **Never omit safety sections** — all precaution fields are required
- **Never create a duplicate entry** for a species already in `data.json`
- **Do not add Instagram or social media content**
- If PubMed data is insufficient to complete a section, write exactly what is known and flag gaps
