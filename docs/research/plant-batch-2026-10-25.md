# Ten new plant drafts — 2026-10-25

## Publication addendum — 2026-10-30

The ten educational reference profiles listed below were published to [BMS Archive](https://bmsarchive.com/database.html) on 2026-10-30. The live archive contains 82 entries (57 plants, 25 fungi). Publication does not imply a clinical recommendation or independent full-text risk-of-bias review; the limitations recorded in the original review remain in force. Deployment and live URL verification are recorded in [the deployment report](plant-batch-2026-10-25-deployment.md).

MONOGRAPH AUDIT RESULT: APPROVE

**Scope of approval:** Local drafts only. Manual scientific review and pre-publication approval remain pending. No production deployment, commit or push was performed.

**Entries reviewed and added:**

| Common name | Accepted scientific name | PubMed query count | Cited PubMed sources |
|---|---|---:|---:|
| Peppermint | Mentha × piperita | 1569 | 5 |
| Artichoke | Cynara cardunculus | 963 | 3 |
| Senna | Senna alexandrina | 182 | 3 |
| Psyllium / Ispaghula | Plantago ovata | 247 | 3 |
| Aloe vera | Aloe vera | 2957 | 4 |
| Roselle / Hibiscus sabdariffa | Sabdariffa gossypiifolia | 862 | 5 |
| Dog Rose / Rosehip | Rosa canina | 342 | 4 |
| African Geranium / Umckaloabo | Pelargonium sidoides | 190 | 5 |
| Flax / Linseed | Linum usitatissimum | 1142 | 4 |
| Horse Chestnut | Aesculus hippocastanum | 322 | 2 |

The archive now contains **82 entries: 57 plants and 25 fungi**, up from 72 (47 plants, 25 fungi). The original 72 entries remain deep-equal to the pre-task snapshot. This batch cites 38 distinct PubMed records, with source metadata and structured extraction retained. Counts are dated, query-dependent literature totals, not clinical-trial counts or efficacy scores.

## Taxonomy findings

All ten accepted taxa were checked live against Kew POWO and screened for existing entries/aliases. Roselle uses accepted Sabdariffa gossypiifolia with Hibiscus sabdariffa retained for discovery. Artichoke literature Cynara scolymus is mapped to cultivated artichoke within Cynara cardunculus. Plant parts and preparations are kept distinct.

## Citation/source findings

38 cited PMID/title/year records match preserved primary metadata. Clinical findings based on abstracts remain scoped; abstract-only numeric medicinal regimens were removed. Official EMA/EDA/NCCIH sources support preparation-specific precautions. Full trial appraisal, licensed ESCOP and complete WHO monograph review were not performed. See [citation registry](plant-batch-2026-10-25-citation-registry.json), [dated counts](plant-batch-2026-10-25-counts.json) and the two evidence folders.

## Scientific claim findings

All ten passed [scientific QA as drafts](plant-batch-2026-10-25-scientific-review.md) after revisions, including newer peppermint/aloe evidence. Uncertainty, negative results and formulation limits remain explicit. No molecular target or impairment dosing was invented to fill a gap. Every final narrative/clinical string was matched to the exact field-level review.

## Schema/rendering findings

[Schema review](plant-batch-2026-10-25-schema-review.md): no migration required. All original fields/types, PubMed-only top-study links, citation indices, dates/counts and unique slugs pass. Static pages were regenerated: 82 monographs, directory and 85 sitemap URLs. Existing admin save logic can drop citations; this pre-existing issue was documented and no admin save was performed.

## Required revisions before publication

Independent manual scientific review and the separate pre-publication gate remain required. These profiles are visibly labeled drafts. Address any findings from that review before deploying.

## Optional improvements

Improve the existing validator's word-boundary/negation handling and fix citation preservation in the local admin editor in separate changes. Do not rerun preliminary draft generators over reviewed proposals.

## Checks run

JSON parse; full and ten per-entry strict validators; citation metadata/linkage; exact added-species/count checks; original-entry preservation; SEO generation/checker; local HTTP for JSON and all ten permalinks; git diff --check; browser cards/modals, filters, synonym search, Simple/Advanced mode, Close/Escape and empty search. Zero validation errors. Seventeen validator warnings were inspected: seven pre-existing and ten conservative safety-wording heuristic false positives. See [full QA report](plant-batch-2026-10-25-qa.md).

## Checks not run

Complete independent clinical full-text risk-of-bias review, manual scientific publication approval, mobile viewport matrix, admin saves, unrelated commerce/API integration checks, Docker deployment and production verification.

## Files changed by this batch

- data.json: ten appended draft entries.
- monographs/: regenerated profiles/directory using the existing generator; original-entry page content changes only where generated neighbor links require it.
- sitemap.xml: generated sitemap for the expanded archive.
- docs/tasks/active/: ten final draft task records.
- docs/research/: taxonomy, source records/extractions, dated counts, reviewed proposals, scientific/schema/QA reports and preview screenshot.

Other workspace changes predated this task and were preserved.
