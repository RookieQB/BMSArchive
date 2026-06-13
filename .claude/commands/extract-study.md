---
description: Extract structured evidence from a scientific paper, PubMed abstract, or study summary into BMS Archive format. Use: /project:extract-study [PMID, DOI, or study description]
---

You are extracting structured evidence from a scientific source for BMS Archive: **$ARGUMENTS**

Use `extraction-synthesis-agent` to perform this extraction. The output will be reviewed by `scientific-qa-evidence-agent` before use.

---

## Step 1 — Retrieve the source

If "$ARGUMENTS" is a PMID, retrieve the abstract from:
`https://pubmed.ncbi.nlm.nih.gov/{PMID}/`

If "$ARGUMENTS" is a DOI or URL, fetch the abstract or available text.

If "$ARGUMENTS" is pasted text, use it directly.

Read the full available text before extracting.

---

## Step 2 — Classify the study

Assign one of these study type labels:

| Label | Description |
|---|---|
| `SR-MA` | Systematic review + meta-analysis of RCTs |
| `RCT` | Randomized controlled trial in humans |
| `CCT` | Controlled clinical trial (non-randomized) in humans |
| `OBS` | Observational study (cohort, case-control, cross-sectional) |
| `CASE` | Case report or case series |
| `MONO` | Official regulatory monograph (EMA, WHO, ESCOP, USP) |
| `ANIMAL` | Animal (in vivo preclinical) study |
| `IN-VITRO` | In vitro / cell culture study |
| `REVIEW` | Narrative review |
| `TRAD` | Traditional / ethnobotanical report |

---

## Step 3 — Extract all available fields

Complete this structured extraction. Write `Unknown / not reported` for any field not found in the source — never infer or estimate missing values.

```json
{
  "citation": "[Author(s). Title. Journal. Year;Volume(Issue):Pages.]",
  "pmid": "[8-digit number or Unknown]",
  "doi": "[DOI string or Unknown]",
  "study_type": "[label from table above]",
  "evidence_level": "[SR-MA / RCT / CCT / OBS / CASE / MONO / ANIMAL / IN-VITRO / REVIEW / TRAD]",
  "plant_or_fungus": {
    "accepted_latin_name": "[confirmed binomial or flag for taxonomy-nomenclature-agent]",
    "synonyms_used_in_study": [],
    "common_names": [],
    "family": "[or Unknown]",
    "part_used": "[root / fruiting body / leaf / seed / etc. or Unknown]"
  },
  "preparation": {
    "type": "[aqueous extract / ethanol extract / standardized extract / powder / etc. or Unknown]",
    "extract_ratio": "[e.g. 4:1 or Unknown]",
    "solvent": "[water / ethanol / etc. or Unknown]",
    "standardization": "[compound and % or Unknown]",
    "active_compounds": []
  },
  "intervention": {
    "dose": "[amount + unit or Unknown]",
    "frequency": "[e.g. twice daily or Unknown]",
    "duration": "[e.g. 8 weeks or Unknown]",
    "route": "[oral / topical / IV / etc. or Unknown]"
  },
  "population_or_model": {
    "type": "[human / rat / mouse / cell line + specific condition]",
    "sample_size": "[n= or Unknown]",
    "age_range": "[or Unknown]",
    "sex": "[or Unknown]",
    "condition": "[disease, symptom, or healthy volunteers]"
  },
  "comparator": "[placebo / active control / no control or Unknown]",
  "outcomes": ["[primary outcome]", "[secondary outcome]"],
  "results": "[key findings with numbers and statistical significance where reported]",
  "adverse_events": "[reported AEs or 'None reported' or 'Not assessed']",
  "limitations": ["[as stated by authors or obvious methodological issues]"],
  "author_conclusion": "[verbatim or close paraphrase of authors' stated conclusion]",
  "bms_archive_interpretation": "[brief factual summary — does not upgrade evidence level]",
  "qa_notes": "[anything requiring scientific-qa-evidence-agent review]",
  "last_reviewed": "[today's date ISO format]"
}
```

---

## Step 4 — Map to data.json fields

Show which `data.json` fields this extraction can populate:

```
narrative_summary.historical_use     → [Yes / No / Partial]
narrative_summary.modern_application → [Yes / No / Partial]
narrative_summary.side_effects       → [Yes / No / Partial]
narrative_summary.contraindications  → [Yes / No / Partial]
clinical_data.used_part              → [Yes / No / Partial]
clinical_data.primary_active_compounds → [Yes / No / Partial]
clinical_data.mechanism_of_action    → [Yes / No / Partial]
clinical_data.pharmacokinetics.*     → [Yes / No / Partial]
clinical_data.safety_and_interactions.* → [Yes / No / Partial]
clinical_data.special_precautions.*  → [Yes / No / Partial]
sources.top_studies_urls             → [Yes / No]
sources.cited_references             → [Yes / No]
```

---

## Step 5 — Send to scientific QA

Flag the extraction for `scientific-qa-evidence-agent` review before any content from this study is written to `data.json`.

Note any fields where the extraction is uncertain or where the evidence level might be misclassified.

---

## Absolute rules

- **Never infer or invent missing fields** — write `Unknown / not reported`
- **Never treat an abstract as full-text evidence for dosage or safety claims** — flag when full text is required
- **Never make clinical recommendations** — extract, do not advise
- **Never fabricate a PMID** — if unsure, mark as unverified
- **Never upgrade evidence level** — an animal study stays an animal study
- **Always separate the authors' conclusions from your interpretation**
