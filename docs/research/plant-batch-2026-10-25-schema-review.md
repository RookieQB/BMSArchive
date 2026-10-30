# Data-model review — ten plant drafts, 2026-10-25

PROPOSED CHANGE: Append ten scientifically reviewed plant drafts using the existing data.json schema.

RECOMMENDATION: **PROCEED with local draft integration.** The one citation-format correction was completed and rechecked. No schema migration or renderer change is required. This is a schema gate, not manual scientific approval or deployment approval.

## Scope and evidence

Reviewed both corrected `plant-batch-2026-10-25-a/proposed-entries.json` and `plant-batch-2026-10-25-b/proposed-entries.json` after the all-ten scientific sign-off in `plant-batch-2026-10-25-scientific-review.md`. Current data.json contains 72 entries (25 Fungi, 47 Plant). No data.json, proposal, generated page, or UI files were changed by this review.

FIELDS AFFECTED: Existing scientific_name, common_name, type, article_count, primary_categories, sources, narrative_summary and clinical_data only. Every required nested field is present, non-empty and of its expected type. Arrays contain non-empty strings. article_count is a positive integer; type is exactly `Plant`. Optional consumer_view is absent, which is supported by the current fallback renderer. No draft-status, family, synonym, evidence-level, dosage or other undeclared field was introduced. All ten modern_application narratives visibly retain the draft/manual-review notice.

MIGRATION REQUIRED: No.

ENTRIES AFFECTED: Mentha × piperita, Cynara cardunculus, Senna alexandrina, Plantago ovata, Aloe vera, Sabdariffa gossypiifolia, Rosa canina, Pelargonium sidoides, Linum usitatissimum, Aesculus hippocastanum.

MIGRATION PLAN: None. Append after the existing Plant entries, preserving the original 72 objects and the first 25 Fungi. Expected result is 82 total, 57 Plant and 25 Fungi. Rebuild the existing generated monographs and sitemap so database.html card destinations exist.

## Citation-format correction — resolved

**Pelargonium sidoides, sources.cited_references[4]: the parent removed the literal `<i>` and `</i>` surrounding the Latin name; the corrected citation was re-read and contains no tags.** Source labels are escaped by database.html:1235–1250 and scripts/build_seo.py:93–106, so these tags display as text instead of italics. Plain text is the established citation representation. This is a formatting correction only; retain citation identity and content.

## Validation results

- JSON parsed for both five-entry proposals and current archive.
- All ten passed recursive required-field/type checks; no extra fields or nested shape changes.
- All ten passed direct calls to the existing validator's `validate_entry(..., strict=True)`: **zero errors, ten heuristic warnings**. The warning function matches the substring “safe” inside “safety” and misses qualifiers including “unestablished”, “does not establish”, “no maximum safe dose ... inferred”, “could not be established”, and “no ... adequate ... safety data”. Every flagged sentence was read: each reports an evidence gap or explicitly rejects an established-safety inference; none asserts unqualified safety. These are documented nonblocking validator warnings, not hidden or suppressed. These calls validate proposal objects without mutating data.json.
- All citation numbers form consecutive entry-local sequences beginning at [1]. Every defined reference is cited in narrative/clinical content, and every used number resolves. No orphan or out-of-range citation numbers were found.
- Every top_studies_urls value matches `https://pubmed.ncbi.nlm.nih.gov/<digits>/` and its PMID occurs in that entry's cited_references. Citation reality/source support was covered by scientific QA; this gate checks shape and internal linkage rather than repeating biomedical verification.
- All article_count values match the dated, quoted PubMed eSearch records in plant-batch-2026-10-25-counts.json. Values: peppermint 1569, artichoke 963, senna 182, psyllium 247, aloe 2957, roselle 862, dog rose 342, Pelargonium 190, flax 1142, horse chestnut 322. Counts are query-dependent literature totals, not counts of clinical trials or evidence scores. Roselle's query translation retains the older Hibiscus sabdariffa term; provenance explicitly records this.
- Scientific-name and generated-slug checks across the original 72 plus these ten found no collision. Peppermint's hybrid symbol normalizes consistently to mentha-piperita in the frontend and generator. Accepted roselle name generates sabdariffa-gossypiifolia.
- After the citation correction, no HTML remains outside mechanism_of_action. Mechanism strings use balanced `<strong>` tags without attributes or executable HTML.

## Renderer and editor implications

RENDERING IMPACT: database.html:1100–1128 uses textContent for narrative/safety/PK and escaped badges for compound strings; mechanism_of_action uses intentional innerHTML through setHTML at :1304–1306. All proposed mechanism markup is compatible. The generated static renderer preserves a limited scientific emphasis allowlist. Regulatory references without PMID/DOI remain visible plain source text; their URLs are not converted to clickable links by the existing source renderer. This is existing behavior and does not prevent the complete citation from being shown.

The database search haystack (database.html:750–752) searches scientific_name, common_name, type and categories, not all prose. Roselle includes Hibiscus sabdariffa in common_name, so its familiar alias is discoverable. Artichoke's older Cynara scolymus name is documented in evidence/taxonomy but is not currently present in common_name; searching that exact Latin synonym will not find it. Optional future common-name alias enrichment can use the existing string field without migration.

**Existing admin preservation risk:** admin.html:549 reconstructs `sources` with only top_studies_urls; its extra-field preservation loop at :553–560 preserves top-level fields only. Saving these entries through the current admin editor would drop cited_references. The new data does not create this defect. Integrate these drafts directly through validated JSON and avoid admin saves until a separately scoped fix preserves nested references. The editor otherwise maps the required existing fields correctly. No admin change was made here.

SEEDING SCRIPT IMPACT: No new schema fields, so no seeder schema migration. Automated count refreshes may use different species queries than the documented quoted/synonym queries; retain this batch's count provenance when reviewing future count changes.

VALIDATION RULE: After integration, parse full JSON, run the existing full validator and entry checks, confirm count/grouping, generate static pages with the established script, and perform browser QA of grid/filter/detail routes. This schema inspection does not claim those post-integration checks or browser checks have already run.

RISKS: Existing UI calls literature counts “studies”; all-ten raw counts remain search totals. Optional consumer fallback may shorten research prose; browser QA must confirm the draft notice remains visible in detail. Existing admin nested-reference loss must be respected operationally. No unsupported schema expansion or taxonomic duplicate found.

## Gate

The parent confirmed only the one citation tag pair was removed, without scientific wording changes. That citation was rechecked. Proceed with local integration. Retain manual scientific review before publication. No deployment is authorized by this report.
