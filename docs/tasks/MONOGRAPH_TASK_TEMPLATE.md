# Monograph Task — [Species Name]

> Copy this template when adding or updating a BMS Archive monograph.
> Fill in all sections before beginning the extraction and writing workflow.
> Use `/project:add-monograph [name]` or `/project:update-monograph [name]` to run the full agent workflow.

---

## Species Identification

**Input name:** [what was given — common name, Latin name, etc.]
**Accepted Latin binomial:** [confirmed per POWO or Index Fungorum]
**Common names:** [list all relevant common names]
**Botanical family:** [confirmed family name]
**Type field value:** `"Fungi"` or `"Plant"` (exact casing required)
**Taxonomy check completed:** Yes / No / Pending
**Taxonomy source:** [POWO / Index Fungorum / MycoBank — with date checked]

## Duplicate Check

**Existing entry in data.json:** Yes — index [N] / No
**If yes:** Do not add a new entry. Update the existing one using `/project:update-monograph`.

## Task Type

- [ ] New monograph — species not yet in data.json
- [ ] Update — adding new studies to existing entry
- [ ] Correction — fixing errors in existing entry
- [ ] Completion — filling in missing sections of existing entry

## Target Clinical/Research Areas

[List the primary research areas this monograph will document.]

- [e.g. Immunomodulation]
- [e.g. Adaptogen / HPA axis modulation]
- [e.g. Anti-inflammatory]
- [e.g. Neuroprotection — if evidence exists]

## Key Sources

[List PubMed sources to be used. Run `/project:extract-study [PMID]` for each.]

| PMID | Citation (short) | Study type | Evidence level |
|---|---|---|---|
| [PMID 1] | [Author et al., Year — topic] | [RCT / SR-MA / etc.] | [A / B / C / D / E] |
| [PMID 2] | | | |
| [PMID 3] | | | |

**Regulatory monographs checked:**
- [ ] EMA/HMPC monograph — [exists / not available]
- [ ] ESCOP monograph — [exists / not available]
- [ ] WHO monograph — [exists / not available]
- [ ] NCCIH/NIH fact sheet — [exists / not available]

## Extraction Notes

[Notes from `/project:extract-study` runs — what was extracted, what was missing, any flags for QA.]

- Source 1 (PMID [N]): [summary of what was extracted and what was missing]
- Source 2 (PMID [N]): [summary]

## Required Safety Sections

Each of these must be documented before the monograph is finalized.
Write "Insufficient data" if no evidence exists — never leave empty.

- [ ] Adverse effects — documented or "Insufficient data"
- [ ] Contraindications — documented
- [ ] Drug interactions — documented (include CYP450 profile if known)
- [ ] Pregnancy — documented or "Insufficient data — not recommended"
- [ ] Lactation — documented or "Insufficient data — not recommended"
- [ ] Hepatic impairment — documented or precautionary guidance noted
- [ ] Renal impairment — documented or precautionary guidance noted
- [ ] Pre-surgery consideration — documented if relevant (antiplatelet, CYP effects)
- [ ] Pediatric use — documented or "Not recommended — insufficient data"

## Evidence Level Per Claimed Use

[Assign an evidence level to each primary use being documented.]

| Claimed use | Evidence level | Basis |
|---|---|---|
| [Primary use 1] | [A / B / C / D / E / T / U] | [study types and count] |
| [Primary use 2] | | |
| [Traditional use] | T | [ethnobotanical source] |

See `docs/rubrics/EVIDENCE_SCORING.md` for level definitions.

## Missing Data / Open Questions

[List anything that could not be confirmed during research.]

- [ ] [Missing field 1, e.g. Human pharmacokinetic data not available]
- [ ] [Missing field 2, e.g. No long-term safety data]
- [ ] [Missing field 3, e.g. Drug interaction data is in vitro only]

## Validation Checklist

Complete after writing the entry to `data.json`:

- [ ] scientific_name = accepted Latin binomial
- [ ] type = "Fungi" or "Plant" (exact casing)
- [ ] article_count = integer from PubMed eSearch
- [ ] All top_studies_urls are real PubMed URLs
- [ ] narrative_summary — all 4 fields complete
- [ ] clinical_data.used_part — specific and accurate
- [ ] mechanism_of_action — uses `<strong>` tags for key targets
- [ ] All 4 pharmacokinetics fields complete
- [ ] drug_interactions — complete (not empty)
- [ ] toxicity — complete (not empty)
- [ ] All 4 special_precautions fields complete
- [ ] No unqualified "safe" claims
- [ ] No placeholder text
- [ ] No fabricated PMIDs
- [ ] JSON is valid: `python3 -c "import json; json.load(open('data.json'))"`
- [ ] Full validation passed: `python3 scripts/validate_archive_data.py --entry "[name]"`

## Agent Workflow

```
/project:taxonomy-check [species name]      — Step 1
/project:extract-study [PMID 1]             — Step 2a
/project:extract-study [PMID 2]             — Step 2b
/project:add-monograph [species name]       — Step 3
/project:review-science [species name]      — Step 4
/project:validate-data                      — Step 5
/project:qa                                 — Step 6
```

## Final Summary

Complete after the monograph is written and validated:

**Species:** [scientific name]
**Added as:** New entry (index [N]) / Update to existing (index [N])
**Evidence level (primary use):** [level]
**Safety sections complete:** Yes / No — [missing sections if any]
**Validation status:** PASS / FAIL
**Scientific QA approval:** Approved / Pending / Issues to resolve
**Ready for commit:** Yes / No — [reason if no]
