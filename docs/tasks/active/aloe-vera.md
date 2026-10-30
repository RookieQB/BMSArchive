# Monograph Task — Aloe vera

Date completed locally: 2026-10-25. Status: **DRAFT — pending manual scientific review and pre-publication gate.**

## Species Identification

**Input name:** Aloe vera
**Accepted Latin binomial:** Aloe vera
**Common names:** Aloe vera
**Botanical family:** Asphodelaceae
**Type field value:** `Plant`
**Taxonomy check completed:** Yes
**Taxonomy source:** [Kew POWO](https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:530017-1), checked 2026-10-25.

See the [batch taxonomy report](../../research/plant-batch-2026-10-25-taxonomy.md) for aliases and common-name ambiguity.

## Duplicate Check

Absent from the original 72-entry archive, including relevant literature aliases. Added once at index 76 (zero based). It is now an existing draft; future work should update it rather than append another entry.

## Task Type

- [x] New monograph — added locally after taxonomy, extraction, scientific QA and schema checks.
- [ ] Manual scientific approval for publication.

## Target Clinical/Research Areas

- Skin health
- Digestive health

## Key Sources

- [1] Langmead L, Feakins RM, Goldthorpe S, Holt H, Tsironi E, De Silva A, Jewell DP, Rampton DS. Randomized, double-blind, placebo-controlled trial of oral aloe vera gel for active ulcerative colitis. Alimentary pharmacology & therapeutics 2004. PMID: 15043514. DOI: 10.1111/j.1365-2036.2004.01902.x.
- [2] Dat AD, Poon F, Pham KB, Doust J. Aloe vera for treating acute and chronic wounds. The Cochrane database of systematic reviews 2012. PMID: 22336851. DOI: 10.1002/14651858.cd008762.pub2.
- [3] Lee J, Lee MS, Nam KW. Acute toxic hepatitis caused by an aloe vera preparation in a young patient: a case report with a literature review. The Korean journal of gastroenterology = Taehan Sohwagi Hakhoe chi 2014. PMID: 25073673. DOI: 10.4166/kjg.2014.64.1.54.
- [4] NCCIH. Aloe Vera: Usefulness and Safety. https://www.nccih.nih.gov/health/aloe-vera Accessed 2026-10-25.
- [5] Huang YN, Chen KC, Wang JH, Lin YK. Effects of Aloe vera on Burn Injuries: A Systematic Review and Meta-Analysis of Randomized Controlled Trials. Journal of Burn Care & Research 2024;45:1536–1545. PMID: 38605441. DOI: 10.1093/jbcr/irae061. Abstract reviewed; full-text appraisal pending.

**Regulatory monographs checked:** Full official regulatory/NIH texts used are explicitly identified above and in the evidence ledger. Licensed ESCOP and complete WHO monographs were not reviewed. A missing source is not a claim that no monograph exists.

## Extraction Notes

See [batch A evidence](../../research/plant-batch-2026-10-25-a/EVIDENCE.md), [batch B ledger](../../research/plant-batch-2026-10-25-b/evidence-ledger.md), structured study-extractions JSON in those folders, and A supplemental-study-extractions.json for the newer peppermint/aloe studies. Source reading was targeted; full clinical risk-of-bias appraisal remains pending. Abstract-only numeric medicinal regimens were omitted from final profiles.

**Preparation specificity:** Inner-leaf gel in the UC trial and varied topical products in wound research. Latex is the outer-leaf exudate; whole-leaf extracts contain different fractions and require separate safety assessment [1][2][4].

## Required Safety Sections

- [x] Adverse effects documented or evidence gap stated.
- [x] Contraindications and preparation-specific cautions documented.
- [x] Interactions documented, with theoretical/unknown status retained.
- [x] Pregnancy and lactation evidence/gaps explicit.
- [x] Hepatic and renal evidence/gaps explicit.
- [x] Pediatric restrictions documented where supported; no pediatric regimen inferred from PK.
- [x] No perioperative interval invented; any retained interval is regulatory-attributed.

Complete fields do not imply complete safety evidence. See the actual profile and scientific review for population-specific gaps.

## Evidence Level Per Claimed Use

C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy.

These are conservative archive draft classifications, not blanket ratings for the species. The [scientific review](../../research/plant-batch-2026-10-25-scientific-review.md) documents indication and preparation limits.

## Missing Data / Open Questions

- Full trial methods, risk of bias, funding and adverse-event tables remain incompletely reviewed.
- Long-term/rare-event safety and impairment-specific dosing are generally unresolved.
- PK gaps refer to the selected sources, not an exhaustive proof that no research exists.
- Independent manual scientific review and the separate pre-publication gate remain required.

## Validation Checklist

- [x] Accepted taxon and unique entry/URL slug.
- [x] Exact type casing, integer article_count from dated NCBI query.
- [x] Real matching PubMed metadata, numbered citations and source URLs.
- [x] All narrative and clinical-data fields populated or explicit uncertainty.
- [x] Mechanism emphasis uses allowed `<strong>` tags.
- [x] Entry validator and full JSON validator: zero errors.
- [x] Existing original 72 entries preserved unchanged.
- [x] Generated permalink responds with complete local profile.
- [x] Browser: card/modal, safety/PK/source sections and visible draft statement verified.

Validator heuristic warnings are reviewed in the [QA report](../../research/plant-batch-2026-10-25-qa.md); a warning is not hidden or treated as an automatic failure.

## Agent Workflow

Taxonomy → source collection/extraction → scientific QA → schema review → local integration → entry/full validation → generated pages → browser QA. Completed for this local draft.

## Final Summary

**Species:** Aloe vera
**Added as:** New local entry, index 76
**Evidence:** C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy.
**Safety sections complete:** Yes, including explicit uncertainty.
**Validation status:** PASS, zero errors; heuristic warnings reviewed.
**Scientific QA approval:** Approved as a draft after revisions.
**Manual scientific approval:** Pending.
**Publication/deployment status:** Not approved for publication; not deployed.
**Admin limitation:** Existing admin saves drop cited_references; no admin save was performed.
