# QA Summary — ten new plant draft monographs

Date: 2026-10-25. Scope: local data addition and regenerated archive pages. No production deployment or commit/push performed.

## Changes reviewed

`data.json`, ten new species task records, batch research records, regenerated `monographs/` and `sitemap.xml`. Original 72-entry state was compared with `/tmp/bms-plants-before-20261025.json`; all original objects remain exactly equal in their original order. Ten Plant records are appended after them. Final counts: **82 total, 25 Fungi and 57 Plant**.

## Checks run

| Check | Result | Notes |
|---|---|---|
| JSON syntax / full strict validator | PASS with warnings | `python3 scripts/validate_archive_data.py --strict`: zero errors, 17 warnings; each warning inspected below. |
| Ten strict per-entry validators | PASS with warnings | `python3 scripts/validate_archive_data.py --strict --entry NAME`, separately for each of the ten names below: zero errors; ten warnings across new entries. |
| Baseline preservation | PASS | Original first 72 objects deeply equal the saved before snapshot; no originals edited. |
| Exact append set/order | PASS | Exactly Mentha × piperita, Cynara cardunculus, Senna alexandrina, Plantago ovata, Aloe vera, Sabdariffa gossypiifolia, Rosa canina, Pelargonium sidoides, Linum usitatissimum and Aesculus hippocastanum. |
| Schema and types | PASS | Each new object has the exact recursive key/type shape of the existing last Plant object; exact Plant casing and integer article counts; fungi remain the first 25. |
| Duplicate names and generated routes | PASS | 82 distinct case-normalized scientific names; SEO checks verify unique canonical/title/path links. |
| Scientific markup | PASS | Every new mechanism includes balanced `<strong>` tags. Scientific/schema reviews separately assessed supported markup and content. |
| Citation internal consistency | PASS | Consecutive local reference numbers; all defined references used; every inline number resolves; every PubMed URL matches a numbered PMID citation. This check verifies linkage, while citation identity and claim support were reviewed in scientific QA. |
| Article-count provenance | PASS | All ten counts exactly equal the dated NCBI eSearch provenance records in `plant-batch-2026-10-25-counts.json`. Counts are query-dependent article totals, not clinical trials. |
| Generated SEO check | PASS | `python3 scripts/check_seo.py`: 82 complete pages, 85 sitemap URLs, unique titles/canonicals, parseable JSON-LD, working internal targets and deterministic output. Checker builds comparison output only in a temporary directory. |
| Whitespace/conflict check | PASS | `git diff --check`: exit zero, no output. |
| Local HTTP archive | PASS | `http://127.0.0.1:8080/data.json`: parsed JSON exactly equals current disk data, all 82 entries. |
| Local HTTP ten new permalinks | PASS | Every URL below returned HTTP 200 and contained the exact scientific name plus visible draft-research wording in HTML. Initial sandbox loopback restriction was resolved by approved elevated read-only request. |
| Admin deployment exclusions | PASS, static inspection | Current Dockerfile uses explicit COPY statements without admin.html, admin_server.py, build_plants.py or research/docs. `.dockerignore` excludes admin files and docs, and permits only the SEO builder in scripts. No task change introduced an admin COPY. No Docker build/runtime assertion is implied. |
| Live browser grid/search/filter/detail | PARENT RUNNING — append later | Parent owns browser QA; no duplicate browser interaction from this agent. |
| Admin save round-trip | NOT RUN | Existing `collectForm` reconstructs sources without cited_references; do not save new entries through admin until separately fixed. No admin save was tested or used. |
| API/newsletter/checkout mutations | NOT RUN | Outside this data-addition scope; existing unrelated API changes were not approved or validated by this QA. |
| Docker build / nginx runtime | NOT RUN | No deployment requested; unrelated deployment-file changes are outside this batch QA. |
| Unit/lint/typecheck | NOT AVAILABLE | No relevant configured repository suite for this static-content addition; scripts and browser checks used instead. |

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

## HTTP routes checked

Each route was fetched under `http://127.0.0.1:8080`:

- `/monographs/mentha-piperita.html`
- `/monographs/cynara-cardunculus.html`
- `/monographs/senna-alexandrina.html`
- `/monographs/plantago-ovata.html`
- `/monographs/aloe-vera.html`
- `/monographs/sabdariffa-gossypiifolia.html`
- `/monographs/rosa-canina.html`
- `/monographs/pelargonium-sidoides.html`
- `/monographs/linum-usitatissimum.html`
- `/monographs/aesculus-hippocastanum.html`

## Issues and missing coverage

No data-integrity, schema, citation-linkage, local HTTP or generated-page blocker found in this batch. Remaining gates are parent browser QA and manual scientific review before publication. Full extraction access limitations remain documented in the research and scientific-review reports; this technical QA cannot resolve those scientific gaps.

The existing admin nested-reference-loss defect is material to future edits, but the drafts were integrated directly into validated JSON and no admin save occurred. General backend, checkout and deployment readiness are outside this report. No claim of production safety or deployment approval is made.

## Unrelated pre-existing working-tree changes

The root task recorded a dirty baseline including `.dockerignore`, `CLAUDE.md`, `Dockerfile`, `README.md`, `admin.html`, `admin_server.py`, `checkout-success.html`, `database.html`, `index.html`, `nginx.conf`, `server.js`, `sitemap.xml`, and untracked e-book/output/SEO work. These were not attributed to the plant task. The regenerated sitemap/monographs incorporate this batch using the existing SEO work; full-file git diffs also contain earlier changes. Current untracked `E-books/` customer-clean artifacts, `exports/`, `output/`, `tmp/`, `docs/SEO.md`, and SEO scripts are not claimed as this agent's work.

## Recommendation

**Technical local-draft checks pass with documented warnings.** Parent must finish browser checks and retain the manual scientific-review gate. This report is not a pre-deploy audit and does not authorize publication/deployment. This QA agent changed only this report file.

## Parent browser verification completed — 2026-10-25

The local in-app browser loaded 82 profiles (57 plants, 25 fungi). All ten new cards were present; every new Advanced modal was opened and verified for correct name, draft/manual-review statement, pharmacokinetics, precautions and PubMed sources. Plant filter showed 57, Fungi showed 25 and hid the new plants, All restored 82. Searching `Hibiscus sabdariffa` returned the single accepted roselle entry. Simple mode retained draft/safety/source content. Close button, Escape and no-result state passed. These are actual browser checks, replacing the earlier PARENT RUNNING status.

Preview screenshot: `plant-batch-2026-10-25-browser.png`. No mobile viewport resizing, API commerce, production deployment or admin-save test was performed. Existing Simple-mode automatic terminology substitutions were not modified by this content task.
