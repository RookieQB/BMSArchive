# Five plant profiles — extraction evidence, 2026-10-25

Status: DRAFT. Scientific QA and manual scientific review pending. No data.json edits.

Raw Europe PMC core responses preserve PMID/title/author/year/DOI/abstract. Regulatory PDFs and extracted text preserved locally. Indexed abstracts are not full article review.

Excluded lookup: PMID 14616149 is fluconazole hepatitis, NOT artichoke; excluded before drafting.

## Evidence table

| Species | PMID | Type | Provisional BMS level | Population | Duration | Key finding / limitation |

|---|---|---|---|---|---|---|

| Mentha × piperita | 35942669 | SR-MA | U | 10 RCTs; 1030 people with IBS | Variable across trials | Pooled benefit versus placebo for global symptoms and abdominal pain; authors rated evidence very low quality. Adverse events more frequent (RR 1.57, 95% CI 1.04–2.37). |

| Mentha × piperita | 34319275 | RCT | U | People with Rome IV IBS; moderate to severe symptoms; n not specified in abstract | 6 weeks | Both groups improved; no significant between-group IBS-SSS difference (P=0.97) or secondary endpoint difference. |

| Mentha × piperita | 34528282 | RCT | C | 30 children aged 7–12 years with functional abdominal pain | Blood sampling 24 hours; repeat motility after 1 week | Menthol exposure appeared dose proportional; evaluable AUC in 29; mean half-lives 2.1, 3.5 and 4.6 hours by dose. |

| Mentha × piperita | 40390282 | RCT | C | 40 children aged 7–12 years with functional abdominal pain; 25 at 540 mg and 15 at 900 mg | 24-hour blood sampling; repeat motility after 1 week | Menthol peak approximately 2.5 hours; dose-adjusted exposure similar. |

| Cynara cardunculus | 14653829 | RCT | B | 247 functional dyspepsia patients enrolled; 244 analyzed | 6 weeks | Overall symptom improvement score 8.3 versus 6.7 (P<0.01); disease-specific quality of life improved more than placebo. |

| Cynara cardunculus | 28609140 | SR-MA | B | 9 randomized trials; 702 participants | Variable / not specified in abstract | Pooled total and LDL cholesterol and triglycerides lower; HDL difference nonsignificant. |

| Cynara cardunculus | 34569671 | SR-MA | B | 14 studies; 15 effect sizes for extracts, plus juice analyses | Variable / not specified in abstract | Pooled reductions in several lipid markers; extract HDL difference nonsignificant. |

| Senna alexandrina | 32969946 | RCT | B | 90 adults with chronic constipation; mean age 42, 93% women | 28 days | Overall improvement 69.2% senna, 68.3% magnesium oxide, 11.7% placebo (P<0.0001); all completed. |

| Senna alexandrina | 33767108 | REVIEW | B | 41 trials of various OTC constipation products | Trials at least 4 weeks | Review judged senna evidence favorably; adverse effects across products included diarrhea, nausea, bloating and abdominal pain. |

| Senna alexandrina | 16268429 | CASE | U | 77-year-old man with chronic senna intake | Chronic; exact duration not reported | Cholestatic hepatitis with bridging necrosis; gradual improvement after withdrawal. |

| Plantago ovata | 19713235 | RCT | B | 275 adults with IBS in primary care | 12 weeks | Psyllium adequate-relief response exceeded placebo in first month (57% vs 35%) and second month (59% vs 41%); severity reduction larger at 3 months. |

| Plantago ovata | 35816465 | SR-MA | B | 16 fiber RCTs; 1251 adults with chronic constipation | Variable; subgroup at least 4 weeks | Psyllium subgroup showed benefit; overall fiber results heterogeneous and flatulence increased. |

| Plantago ovata | 30239559 | SR-MA | B | 28 RCTs; 1924 participants with or without hypercholesterolemia | Included trials at least 3 weeks | LDL reduction 0.33 mmol/L; non-HDL and apoB also decreased; moderate certainty LDL and non-HDL due to inconsistency. |

| Aloe vera | 15043514 | RCT | C | 44 evaluable outpatients with mildly to moderately active ulcerative colitis; gel 30, placebo 14 | 4 weeks | Clinical response 47% versus 14% (P<0.05); remission 30% versus 7% nonsignificant (P=0.09); sigmoidoscopy and laboratory variables did not differ. Minor adverse events similar. |

| Aloe vera | 22336851 | REVIEW | U | 7 RCTs; 347 participants with various acute/chronic wounds | Variable | No high-quality evidence supporting wound healing; clinical heterogeneity prevented meta-analysis; one surgical wound trial delayed healing. |

| Aloe vera | 25073673 | CASE | U | 21-year-old woman | 4 weeks exposure | Acute hepatitis associated with aloe preparation in case report. |

## Regulatory/source access checks

EMA full monograph text read: peppermint oil 2020 revision 1; artichoke leaf 2018 revision 1; senna leaf 2018 revision 1 published 2020; psyllium husk 2013. NCCIH Aloe Vera full safety sections retrieved. Draft uses these specified versions, not a claim that all current regulatory updates were exhausted.

ESCOP: full licensed monographs not accessed. WHO: full monograph verification not completed. NCCIH: peppermint page found; aloe full page reviewed. No dedicated NCCIH sheet established for other three in this extraction.

PubMed/Europe PMC clinical, review, PK and safety searches are preserved in search-*.json; source collection is targeted, not a comprehensive systematic search. Senna review search contains other species; those are excluded from proposed claims.

## Required further checks

Read full clinical articles for risk of bias, adverse-event counts, withdrawals, extract specifications, funding/conflicts, and preparation identity. Peppermint 2021 PK has a correction PMID 36377401; draft therefore uses the newer 2025 PK descriptively and no numerical half-life.

Senna: pregnancy/lactation statement explicitly follows EMA leaf monograph, whose precaution may differ from other clinical references. Distinguish pod PK from leaf RCT evidence.

Psyllium: pooled general-fiber results are not psyllium-only results. Artichoke: clinical extracts refer to cultivated artichoke literature (C. scolymus), not all cardoon products. Aloe: gel, latex, decolorized and non-decolorized whole leaf remain separate.

Evidence-level assignments are provisional and conservative; review existence alone does not qualify as BMS A. The topical aloe review had no meta-analysis and is REVIEW, not SR-MA.

## Article counts

Counts are query-dependent search totals, not trial counts or efficacy scores. Complete eSearch provenance follows:

```json

{
  "scientific_name": "Mentha × piperita",
  "query": "\"Mentha piperita\"[All Fields] OR \"Mentha x piperita\"[All Fields]",
  "article_count": 1569,
  "retrieved_date": "2026-10-25",
  "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=%22Mentha+piperita%22%5BAll+Fields%5D+OR+%22Mentha+x+piperita%22%5BAll+Fields%5D&retmode=json&retmax=0",
  "query_translation": "\"Mentha piperita\"[All Fields] OR \"Mentha x piperita\"[All Fields]",
  "note": "Query-dependent PubMed search count, not number of clinical trials or efficacy evidence."
}

```

```json

{
  "scientific_name": "Cynara cardunculus",
  "query": "\"Cynara cardunculus\"[All Fields] OR \"Cynara scolymus\"[All Fields]",
  "article_count": 963,
  "retrieved_date": "2026-10-25",
  "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=%22Cynara+cardunculus%22%5BAll+Fields%5D+OR+%22Cynara+scolymus%22%5BAll+Fields%5D&retmode=json&retmax=0",
  "query_translation": "\"Cynara cardunculus\"[All Fields] OR \"Cynara scolymus\"[All Fields]",
  "note": "Query-dependent PubMed search count, not number of clinical trials or efficacy evidence."
}

```

```json

{
  "scientific_name": "Senna alexandrina",
  "query": "\"Senna alexandrina\"[All Fields] OR \"Cassia senna\"[All Fields] OR \"Cassia angustifolia\"[All Fields] OR \"Cassia acutifolia\"[All Fields]",
  "article_count": 182,
  "retrieved_date": "2026-10-25",
  "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=%22Senna+alexandrina%22%5BAll+Fields%5D+OR+%22Cassia+senna%22%5BAll+Fields%5D+OR+%22Cassia+angustifolia%22%5BAll+Fields%5D+OR+%22Cassia+acutifolia%22%5BAll+Fields%5D&retmode=json&retmax=0",
  "query_translation": "\"Senna alexandrina\"[All Fields] OR \"Cassia senna\"[All Fields] OR \"Cassia angustifolia\"[All Fields] OR \"Cassia acutifolia\"[All Fields]",
  "note": "Query-dependent PubMed search count, not number of clinical trials or efficacy evidence."
}

```

```json

{
  "scientific_name": "Plantago ovata",
  "query": "\"Plantago ovata\"[All Fields]",
  "article_count": 247,
  "retrieved_date": "2026-10-25",
  "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=%22Plantago+ovata%22%5BAll+Fields%5D&retmode=json&retmax=0",
  "query_translation": "\"Plantago ovata\"[All Fields]",
  "note": "Query-dependent PubMed search count, not number of clinical trials or efficacy evidence."
}

```

```json

{
  "scientific_name": "Aloe vera",
  "query": "\"Aloe vera\"[All Fields] OR \"Aloe barbadensis\"[All Fields]",
  "article_count": 2957,
  "retrieved_date": "2026-10-25",
  "source_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=%22Aloe+vera%22%5BAll+Fields%5D+OR+%22Aloe+barbadensis%22%5BAll+Fields%5D&retmode=json&retmax=0",
  "query_translation": "\"Aloe vera\"[All Fields] OR \"Aloe barbadensis\"[All Fields]",
  "note": "Query-dependent PubMed search count, not number of clinical trials or efficacy evidence."
}

```
