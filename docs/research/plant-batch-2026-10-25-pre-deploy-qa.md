# Pre-deploy QA — ten additional plants, 2026-10-25

PRE-DEPLOY STAGE 1 RESULT: PASS — scoped technical QA for reviewed publication data. Scientific publication signoff separately passed for this exact data hash; security/operations release gates remain separate.

Publication request authorizes the scoped plant/static-content release and GitHub synchronization. This QA stage does not stage, commit, push or deploy files. Final scientific, security and operations gates are separate.

## Checks actually run (repeated on final reviewed data)

- `git status --short`: dirty pre-existing working tree confirmed; no staging performed.
- `git branch --show-current`: `codex/stripe-ebook-checkout`.
- `git diff --check`: PASS, exit zero, no output.
- `python3 scripts/validate_archive_data.py --strict`: PASS, 82 entries (25 Fungi/57 Plant), zero errors, 17 warnings.
- `python3 scripts/check_seo.py`: PASS, 82 complete monographs and 85 sitemap URLs; unique titles/canonicals, parseable JSON-LD, full content, internal links and deterministic regeneration.
- Current first72 data objects compared deeply with `/tmp/bms-plants-before-20261025.json`: PASS, exactly unchanged.
- Dockerfile explicit COPY and `.dockerignore` exclusions inspected: current static image excludes admin.html, admin_server.py, build_plants.py, plants_progress.json and research/docs. This is source inspection, not a container/runtime check.

## All 17 validator warnings

The heuristic matches the substring “safe”, including inside “safety”, and does not understand several negative qualifiers. The ten new warnings all describe unestablished/unknown safety or explicitly reject a safety inference. They are nonblocking false positives; they were not removed or suppressed. Seven warnings originate from unchanged baseline entries. Their presence does not authorize a fresh scientific safety endorsement of those entries.

| Entry | Field under clinical_data | Baseline/new | Inspection |
|---|---|---|---|
| Tanacetum parthenium | special_precautions.pregnancy | Baseline | No controlled human pregnancy safety data; avoidance stated. |
| Trigonella foenum-graecum | safety_and_interactions | Baseline | Safety-margin discussion is explicitly rodent/preclinical; does not establish broad human safety. |
| Trigonella foenum-graecum | special_precautions.pregnancy | Baseline | Pregnancy safety studies are explicitly absent. |
| Trigonella foenum-graecum | special_precautions.lactation | Baseline | Infant safety explicitly not established. |
| Uncaria tomentosa | special_precautions.pregnancy | Baseline | No controlled human pregnancy safety data; avoidance stated. |
| Taraxacum officinale | special_precautions.renal_impairment | Baseline | Reference to a safety statement excluding renal failure; medical supervision required. |
| Vitis vinifera | safety_and_interactions | Baseline | Rodent safety literature and qualified short human exposures; legacy claims remain subject to separate scientific review. |
| Mentha × piperita | special_precautions.renal_impairment | New | Reports renal safety/PK gaps. |
| Cynara cardunculus | special_precautions.pregnancy | New | Says safety unestablished; EMA does not recommend pregnancy use. |
| Cynara cardunculus | special_precautions.lactation | New | Says safety unestablished; EMA does not recommend lactation use. |
| Plantago ovata | safety_and_interactions | New | Explicitly says no maximum safe dose is inferred. |
| Sabdariffa gossypiifolia | safety_and_interactions | New | States short trials do not establish chronic safety. |
| Sabdariffa gossypiifolia | special_precautions.hepatic_impairment | New | States no hepatic dosing or safety studies identified. |
| Rosa canina | safety_and_interactions | New | States three trials do not establish broad safety. |
| Rosa canina | special_precautions.pregnancy | New | States medicinal pregnancy safety could not be established. |
| Pelargonium sidoides | special_precautions.renal_impairment | New | States no adequate renal-specific safety data identified. |
| Aesculus hippocastanum | special_precautions.hepatic_impairment | New | States no adequate hepatic-specific safety data identified. |

## Release scope and exclusions

Approved candidate transfer scope after the remaining audit gates: **data.json only**. Per parent verified deployment context, the existing server web-image build regenerates `monographs/` and `sitemap.xml`; Dockerfile/nginx/database hashes match local deployment configuration and production data hash matches the saved 72-entry baseline. These production observations were supplied by the parent, not independently re-run by this QA agent. No backend/config file is included in the transfer scope.

Do not deploy local admin tools, seeding scripts, progress files, `.env`, `.git`, `.claude`, research/task files, temporary/output directories or unrelated e-book drafts. Do not bundle unrelated current commerce/backend/frontend/config modifications into the ten-plant release.

Pre-existing dirty files include `.dockerignore`, `CLAUDE.md`, `Dockerfile`, `README.md`, `admin.html`, `admin_server.py`, `checkout-success.html`, `database.html`, `index.html`, `nginx.conf`, `server.js` and `sitemap.xml`; untracked e-book/SEO/output files were also already present. This QA does not claim they were created by the plant task or approve them for deployment.

## Checks not run / limits

Final-data validation and regenerated SEO checks: completed after parent final-data notification. Full strict validation and all ten strict entry invocations returned zero errors; 17 unchanged warnings. Publication data SHA-256: `d68912d878d6c4e87762915b4099a91c981982d9acb290f932e41ec12d3c3638`. The existing branch is eight commits ahead of local main (`git rev-list --count main..HEAD`); no Git state changed.

Additional final checks passed: exact ten additions/order; exact existing recursive schema; balanced strong markup; consecutive/used/resolved references; each PubMed URL matches a numbered PMID; all ten counts match dated eSearch queries; all 72 originals remain deeply unchanged. Final last-ten entries exactly equal the scientifically reviewed proposals after only known workflow-label/dose-disclaimer removal, opening capitalization and citation-prefix normalization. All remaining scientific text and source identifiers are unchanged, including rosehip full-text-appraisal uncertainty.

Local HTTP data equals the current 82-entry file exactly, and all ten new permalinks returned 200 with exact scientific names and no draft-workflow labels. SEO validator again passed all 82 pages/85 URLs and deterministic content. `git diff --check` again passed. These are local technical checks; parent owns production browser verification.

Live browser/production verification: parent owns this; not duplicated. Admin save: NOT RUN; existing editor drops nested cited_references, so no admin save should be used for release preparation. Backend/API, waitlist, checkout, nginx runtime and Docker image checks: NOT RUN because this release is data/static-content only. No production-safe assertion or deployment approval from this preliminary report.

## Final stage-1 recommendation

Proceed to the separate security and operations audit stages for the scoped data-only release. No technical blocker identified by these checks. The seven baseline warnings and ten new heuristic false positives are fully listed above. Do not stage unrelated branch/workspace work or infer GitHub/main release readiness from local validation alone. This agent changed only this report file and did not stage, push or deploy.

Scientific pre-publication gate confirmed: `plant-batch-2026-10-25-pre-publish.md` reports PASS for all ten on the same SHA-256 above. This completes stage-1 handoff to the security reviewer.
