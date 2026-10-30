# Pre-publication gate — ten new plant reference profiles

Date: 25 October 2026 (Europe/Copenhagen)

## OVERALL RESULT: PASS — PUBLICATION READY AS SCOPED REFERENCE SUMMARIES

No Critical or Major issue remains in the last ten entries (indices 72–81) for publication as educational reference summaries with the existing medical disclaimer. This agent gate does not mean human scientific review, peer review, clinical validation, treatment guidance or approval of all possible products. Publication was explicitly requested by the user. Production deployment, security, operations, generated pages and GitHub synchronization are subsequent parent-owned gates.

Workflow applied: `.claude/commands/workflow-pre-publish.md`. Actual current data.json read in full for these entries and compared against exact prior reviewed proposals. All scientific, safety, mechanism and PK fields match the earlier claim-by-claim scientific review; only workflow status text and reference prefixes changed.

## Batch checklist

- JSON parsed: 82 entries, 25 fungi and 57 plants; ten new names distinct and absent from preceding 72 entries.
- Structural validation: each scientific name passed per-entry validator with zero errors. Numeric --entry filters were initially attempted, then discarded because script filters names rather than indexes; final checks use exact scientific names.
- Taxonomy: current names, Plant casing and used-part specificity match same-date live Kew report and source-specific scientific review. Roselle accepted-name/literature synonym and artichoke subspecies/cultivar scope remain explicit.
- Scientific QA: source-scoped RCT/SR outcomes, conservative evidence grades, no preclinical-to-human upgrades, no therapeutic/prescriptive claim. Mechanistic <strong> tags confirmed for all ten. No numeric medicinal dosing recommendations.
- Safety: every required adverse-effect, contraindication, interaction, pregnancy, lactation, hepatic, renal and toxicity field present, substantive and inspected. Missing evidence is disclosed rather than treated as reassuring safety evidence.
- Citations: every PubMed URL mapped to exact saved indexed PMID/title metadata; links correspond to narrative claims. References sequential and normalized to [N] - prefix. Regulatory/NIH source references intentionally have source titles/URLs rather than fabricated PMIDs.
- Disclaimer: database.html sticky research-only/non-medical banner and index.html disclaimer section confirmed in current source; database detail/footer statements also present. The profiles are reference summaries, not clinical advice.
- Placeholders and workflow drafts: none in final ten entries; uncertainty about evidence/full-text quality remains substantive and is preserved.
- Final full standard and strict validators both exit 0: zero errors, 17 warnings each; all 17 warning fields individually inspected below.

## Exact editorial edits

- Removed the “Draft research profile:” introduction and “Pending manual scientific review.” statement from modern_application only in all ten entries. This publishes the summaries without asserting that a human scientist reviewed them.
- Removed administrative remarks that no numeric dose is given; retained scientific dose/preparation limitations and full-text review caveats.
- Normalized all cited_references list prefixes to [N] - .
- No changes to clinical_data, safety text, historical_use, species names, URLs, counts, categories or prior 72 entries.

## Per-entry gates

### 72: Mentha × piperita — PASS — PUBLICATION READY

| Required gate | Result |
|---|---|
| JSON/required fields/substantive content | PASS — 0 errors |
| Accepted taxonomy/type/used part | PASS |
| Evidence language/no animal-to-human upgrade/no disease treatment claim | PASS |
| Real relevant citations/numbered references | PASS |
| Mechanism strong tags | PASS |
| Adverse effects/contraindications/interactions | PASS |
| Pregnancy/lactation/hepatic/renal precautions/toxicity | PASS |
| No unqualified safety claim | PASS |
| Site disclaimers | PASS |
| No placeholders/workflow draft content | PASS |
| Per-entry validator | PASS — 1 reviewed warning(s) |

Critical issues: None. Major issues: None. Minor issues: source-coverage and provisional appraisal limits remain disclosed; see exact scientific review and warning assessment.

Final modern_application: Enteric-coated peppermint oil has been studied for IBS symptoms, with inconsistent trial results [1][2]. A 2022 synthesis of 10 RCTs (1030 participants) reported pooled symptom benefit but rated certainty very low and found more adverse events [1]. A 6-week trial in people with Rome IV IBS found no superiority over placebo [2]. A 2026 trial in children aged 8–18 years likewise found neither peppermint oil nor peppermint sweets superior to placebo after eight weeks [6]. BMS Level U for a firm general efficacy conclusion; formulation-specific human research exists. Pediatric PK studies describe exposure, not established pediatric treatment regimens [3][4].

### 73: Cynara cardunculus — PASS — PUBLICATION READY

| Required gate | Result |
|---|---|
| JSON/required fields/substantive content | PASS — 0 errors |
| Accepted taxonomy/type/used part | PASS |
| Evidence language/no animal-to-human upgrade/no disease treatment claim | PASS |
| Real relevant citations/numbered references | PASS |
| Mechanism strong tags | PASS |
| Adverse effects/contraindications/interactions | PASS |
| Pregnancy/lactation/hepatic/renal precautions/toxicity | PASS |
| No unqualified safety claim | PASS |
| Site disclaimers | PASS |
| No placeholders/workflow draft content | PASS |
| Per-entry validator | PASS — 2 reviewed warning(s) |

Critical issues: None. Major issues: None. Minor issues: source-coverage and provisional appraisal limits remain disclosed; see exact scientific review and warning assessment.

Final modern_application: Artichoke leaf extracts have been investigated for functional dyspepsia and lipid biomarkers [1][2][3]. In a 6-week RCT (247 enrolled), a commercial leaf extract improved symptom scores versus placebo [1]. Meta-analyses reported lipid changes across varying products; cardiovascular event prevention is unproven [2][3]. BMS Level B provisional for the specific dyspepsia preparation and lipid markers, with full-text bias review pending; EMA traditional-use status remains distinct [4].

### 74: Senna alexandrina — PASS — PUBLICATION READY

| Required gate | Result |
|---|---|
| JSON/required fields/substantive content | PASS — 0 errors |
| Accepted taxonomy/type/used part | PASS |
| Evidence language/no animal-to-human upgrade/no disease treatment claim | PASS |
| Real relevant citations/numbered references | PASS |
| Mechanism strong tags | PASS |
| Adverse effects/contraindications/interactions | PASS |
| Pregnancy/lactation/hepatic/renal precautions/toxicity | PASS |
| No unqualified safety claim | PASS |
| Site disclaimers | PASS |
| No placeholders/workflow draft content | PASS |
| Per-entry validator | PASS — 0 reviewed warning(s) |

Critical issues: None. Major issues: None. Minor issues: source-coverage and provisional appraisal limits remain disclosed; see exact scientific review and warning assessment.

Final modern_application: Senna preparations have been studied for constipation, with short-term symptom benefits and important electrolyte and obstruction precautions [1][4]. A 28-day randomized trial in 90 adults compared senna, magnesium oxide and placebo; improvement favored active groups [1]. Exact senna part and anthranoid standardization were not specified in its abstract, so no product-specific dose is given here. BMS Level B provisional for constipation; a favorable OTC systematic review uses a different grading system [2]. EMA limits unsupervised leaf-medicine use to one week; the research duration is not general-use guidance [4].

### 75: Plantago ovata — PASS — PUBLICATION READY

| Required gate | Result |
|---|---|
| JSON/required fields/substantive content | PASS — 0 errors |
| Accepted taxonomy/type/used part | PASS |
| Evidence language/no animal-to-human upgrade/no disease treatment claim | PASS |
| Real relevant citations/numbered references | PASS |
| Mechanism strong tags | PASS |
| Adverse effects/contraindications/interactions | PASS |
| Pregnancy/lactation/hepatic/renal precautions/toxicity | PASS |
| No unqualified safety claim | PASS |
| Site disclaimers | PASS |
| No placeholders/workflow draft content | PASS |
| Per-entry validator | PASS — 1 reviewed warning(s) |

Critical issues: None. Major issues: None. Minor issues: source-coverage and provisional appraisal limits remain disclosed; see exact scientific review and warning assessment.

Final modern_application: Psyllium husk has been studied for constipation, IBS symptoms and lipid biomarkers [1][2][3]. A 12-week IBS RCT compared psyllium, bran and placebo in 275 adults; psyllium improved relief in early months [1]. Fiber meta-analysis supports a psyllium signal but pooled all-fiber effects cannot be assigned wholly to psyllium [2]. A 28-trial lipid meta-analysis found lower LDL, with moderate certainty limited by inconsistency [3]. BMS Level B provisional for these specific outcomes pending full-text appraisal; cardiovascular event prevention is not established.

### 76: Aloe vera — PASS — PUBLICATION READY

| Required gate | Result |
|---|---|
| JSON/required fields/substantive content | PASS — 0 errors |
| Accepted taxonomy/type/used part | PASS |
| Evidence language/no animal-to-human upgrade/no disease treatment claim | PASS |
| Real relevant citations/numbered references | PASS |
| Mechanism strong tags | PASS |
| Adverse effects/contraindications/interactions | PASS |
| Pregnancy/lactation/hepatic/renal precautions/toxicity | PASS |
| No unqualified safety claim | PASS |
| Site disclaimers | PASS |
| No placeholders/workflow draft content | PASS |
| Per-entry validator | PASS — 0 reviewed warning(s) |

Critical issues: None. Major issues: None. Minor issues: source-coverage and provisional appraisal limits remain disclosed; see exact scientific review and warning assessment.

Final modern_application: Aloe gel preparations have been investigated for wounds and oral inflammatory-bowel symptoms, with substantial uncertainty and product differences [1][2][5]. A small 4-week UC trial (44 evaluable participants) found more clinical responses with oral gel than placebo, but clinical remission and sigmoidoscopic findings were not convincingly different [1]. The 2012 wound review found insufficient high-quality evidence [2]. A later review of nine burn RCTs reported shorter healing with aloe preparations, while pain and infection differences were not significant; these burn findings cannot be generalized to all wounds or products [5]. BMS Level C for the exploratory UC signal, provisional B for the narrower burn-healing outcome pending full-text quality appraisal, and U for a firm broad wound-healing conclusion. Gel findings do not support oral latex or whole-leaf products.

### 77: Sabdariffa gossypiifolia — PASS — PUBLICATION READY

| Required gate | Result |
|---|---|
| JSON/required fields/substantive content | PASS — 0 errors |
| Accepted taxonomy/type/used part | PASS |
| Evidence language/no animal-to-human upgrade/no disease treatment claim | PASS |
| Real relevant citations/numbered references | PASS |
| Mechanism strong tags | PASS |
| Adverse effects/contraindications/interactions | PASS |
| Pregnancy/lactation/hepatic/renal precautions/toxicity | PASS |
| No unqualified safety claim | PASS |
| Site disclaimers | PASS |
| No placeholders/workflow draft content | PASS |
| Per-entry validator | PASS — 2 reviewed warning(s) |

Critical issues: None. Major issues: None. Minor issues: source-coverage and provisional appraisal limits remain disclosed; see exact scientific review and warning assessment.

Final modern_application: Roselle calyx infusions have been studied for blood-pressure outcomes, with substantial preparation and study-quality limitations [1][2]. In a double-blind trial of 65 adults aged 30–70 years with prehypertension or mild hypertension who were not taking blood-pressure medicines, a six-week calyx-tea regimen reduced systolic pressure more than placebo; the diastolic difference was not significant [1]. A review of 17 chronic trials found a systolic-pressure signal but very high heterogeneity (I²=95% in the placebo comparison); this supports a conservative Level B for the studied blood-pressure outcomes, not proven cardiovascular-event prevention or medication equivalence [2]. A 25-man acute crossover study improved flow-mediated dilation without a significant blood-pressure reduction [4].

### 78: Rosa canina — PASS — PUBLICATION READY

| Required gate | Result |
|---|---|
| JSON/required fields/substantive content | PASS — 0 errors |
| Accepted taxonomy/type/used part | PASS |
| Evidence language/no animal-to-human upgrade/no disease treatment claim | PASS |
| Real relevant citations/numbered references | PASS |
| Mechanism strong tags | PASS |
| Adverse effects/contraindications/interactions | PASS |
| Pregnancy/lactation/hepatic/renal precautions/toxicity | PASS |
| No unqualified safety claim | PASS |
| Site disclaimers | PASS |
| No placeholders/workflow draft content | PASS |
| Per-entry validator | PASS — 2 reviewed warning(s) |

Critical issues: None. Major issues: None. Minor issues: source-coverage and provisional appraisal limits remain disclosed; see exact scientific review and warning assessment.

Final modern_application: A particular rosehip seed-and-husk powder has been investigated for osteoarthritis pain, with small manufacturer-supported studies limiting confidence [1][2]. A meta-analysis of three trials (287 participants; median duration three months) found a small pain-score benefit, but all trials were supported by the same manufacturer and independent replication was requested [1]. A double-blind crossover study enrolled 94 patients with hip or knee osteoarthritis and compared seed-and-husk powder with placebo for three months per period [2]. Evidence is provisionally Level B for pain outcomes with that studied preparation, not all rosehip teas, oils, species mixtures or products. Other uses remain insufficiently established [3][4]. Full-text quality appraisal remains pending.

### 79: Pelargonium sidoides — PASS — PUBLICATION READY

| Required gate | Result |
|---|---|
| JSON/required fields/substantive content | PASS — 0 errors |
| Accepted taxonomy/type/used part | PASS |
| Evidence language/no animal-to-human upgrade/no disease treatment claim | PASS |
| Real relevant citations/numbered references | PASS |
| Mechanism strong tags | PASS |
| Adverse effects/contraindications/interactions | PASS |
| Pregnancy/lactation/hepatic/renal precautions/toxicity | PASS |
| No unqualified safety claim | PASS |
| Site disclaimers | PASS |
| No placeholders/workflow draft content | PASS |
| Per-entry validator | PASS — 1 reviewed warning(s) |

Critical issues: None. Major issues: None. Minor issues: source-coverage and provisional appraisal limits remain disclosed; see exact scientific review and warning assessment.

Final modern_application: Proprietary Pelargonium root extracts have been investigated for acute cough and respiratory symptoms, but certainty and formulation differences remain substantial [1][2][3]. The Cochrane review judged evidence low for acute bronchitis and very low for common cold or sinusitis, with suspected publication bias and differences between liquids and tablets [1]. A later meta-analysis of 11 EPs 7630 trials (2195 participants) reported cough improvement; the authors include manufacturer employees or paid consultants, and the analysis does not remove the limitations or establish interchangeability with other products [3]. A UK feasibility trial recruited 134 adults and demonstrated recruitment feasibility rather than definitive efficacy [2]. Archive classification is Level U for a firm clinical efficacy conclusion and Level T for EMA traditional common-cold use [1][6].

### 80: Linum usitatissimum — PASS — PUBLICATION READY

| Required gate | Result |
|---|---|
| JSON/required fields/substantive content | PASS — 0 errors |
| Accepted taxonomy/type/used part | PASS |
| Evidence language/no animal-to-human upgrade/no disease treatment claim | PASS |
| Real relevant citations/numbered references | PASS |
| Mechanism strong tags | PASS |
| Adverse effects/contraindications/interactions | PASS |
| Pregnancy/lactation/hepatic/renal precautions/toxicity | PASS |
| No unqualified safety claim | PASS |
| Site disclaimers | PASS |
| No placeholders/workflow draft content | PASS |
| Per-entry validator | PASS — 0 reviewed warning(s) |

Critical issues: None. Major issues: None. Minor issues: source-coverage and provisional appraisal limits remain disclosed; see exact scientific review and warning assessment.

Final modern_application: Flaxseed products have been studied for bowel function and blood-pressure outcomes, with seed, oil and lignan extracts representing different interventions [1][2][5]. A 2023 meta-analysis of 33 trials (2427 participants) reported modest pooled blood-pressure reductions but very high heterogeneity (I² above 92%); the archive uses conservative Level B for the studied pressure outcomes rather than generalizing to every product [1]. An earlier analysis also found formulation-dependent results [2]. EMA recognizes seed as a bulk laxative, while demulcent use is traditional (Level T); regulatory well-established use is not itself an archive Level A clinical-trial score [5]. A separate triple-blind trial studied flaxseed regimens for 12 weeks, but its abstract gives inconsistent participant totals, so it is not used for a precise sample-size or effect claim [4].

### 81: Aesculus hippocastanum — PASS — PUBLICATION READY

| Required gate | Result |
|---|---|
| JSON/required fields/substantive content | PASS — 0 errors |
| Accepted taxonomy/type/used part | PASS |
| Evidence language/no animal-to-human upgrade/no disease treatment claim | PASS |
| Real relevant citations/numbered references | PASS |
| Mechanism strong tags | PASS |
| Adverse effects/contraindications/interactions | PASS |
| Pregnancy/lactation/hepatic/renal precautions/toxicity | PASS |
| No unqualified safety claim | PASS |
| Site disclaimers | PASS |
| No placeholders/workflow draft content | PASS |
| Per-entry validator | PASS — 1 reviewed warning(s) |

Critical issues: None. Major issues: None. Minor issues: source-coverage and provisional appraisal limits remain disclosed; see exact scientific review and warning assessment.

Final modern_application: Standardized horse chestnut seed extracts have been studied for short-term venous-insufficiency symptoms, with larger and longer rigorous trials still needed [1]. A Cochrane review of 17 trials found signals for reduced leg pain and leg volume but emphasized caveats [1][3]. A randomized, partially blinded 12-week trial of 240 adults compared a dried seed extract with compression stockings and placebo; leg-volume findings do not establish prevention of thrombosis or equivalence for every clinical outcome [2]. Provisional archive Level B applies to studied short-term venous symptoms. Raw seeds and other raw parts are toxic and are not the tested preparations [4].

## Source limitations and literal workflow exceptions

The workflow text describes an eight-digit PMID URL. PMID8569363 (horse-chestnut comparison trial) is a real older seven-digit identifier; exact metadata verified. Its canonical https://pubmed.ncbi.nlm.nih.gov/8569363/ URL is intentionally retained. This is a minor documentation-pattern defect, not an unverifiable/fabricated citation or a scientific blocker. The validator accepts the canonical URL.

For artichoke, rosehip and several other primary trials, indexed abstracts were inspected rather than complete papers. No detailed dose or safety advice is inferred from these abstracts. Full regulatory/NIH safety documents were reviewed where available. Rosehip pregnancy/lactation/interactions remain explicitly unknown in selected sources. EDA roselle interaction alerts are attributed and their underlying clinical studies are explicitly not independently verified; no interaction magnitude/direction is asserted as established. Product-specific B classifications are provisional where full-text bias appraisal remains incomplete. These limits bound the public summary instead of being silently removed.

The updated negative pediatric peppermint RCT and narrower 2024 aloe burn review are included. Disputed Pelargonium case causality does not remove current EMA liver warnings; 2026 symptom-based seven-day surveillance cannot exclude rare/asymptomatic injury. Whole-plant, oil, latex, husk, standardized extract and isolated constituent evidence is not interchanged.

## Exact citation identity checks

| Entry | PMID | Verified indexed title |
|---|---|---|
| Mentha × piperita | 35942669 | Systematic review and meta-analysis: efficacy of peppermint oil in irritable bowel syndrome. |
| Mentha × piperita | 34319275 | Peppermint Oil Treatment for Irritable Bowel Syndrome: A Randomized Placebo-Controlled Trial. |
| Mentha × piperita | 34528282 | Randomised trial: Peppermint oil (menthol) pharmacokinetics in children and effects on gut motility in children with functional abdominal pain. |
| Mentha × piperita | 40390282 | Randomized trial: Peppermint oil (menthol) pharmacokinetics in children and effects on gut motility in children with functional abdominal pain: 540 mg vs. 900 mg dose comparison. |
| Mentha × piperita | 41610933 | Peppermint Oil and Sweets in Pediatric Irritable Bowel Syndrome and Functional Abdominal Pain: A Randomized Trial. |
| Cynara cardunculus | 14653829 | Efficacy of artichoke leaf extract in the treatment of patients with functional dyspepsia: a six-week placebo-controlled, double-blind, multicentre trial. |
| Cynara cardunculus | 28609140 | Lipid-lowering activity of artichoke extracts: A systematic review and meta-analysis. |
| Cynara cardunculus | 34569671 | Effects of artichoke leaf extract supplementation or artichoke juice consumption on lipid profile: A systematic review and dose-response meta-analysis of randomized controlled trials. |
| Senna alexandrina | 32969946 | Senna Versus Magnesium Oxide for the Treatment of Chronic Constipation: A Randomized, Placebo-Controlled Trial. |
| Senna alexandrina | 33767108 | Efficacy and Safety of Over-the-Counter Therapies for Chronic Constipation: An Updated Systematic Review. |
| Senna alexandrina | 16268429 | Subacute cholestatic hepatitis likely related to the use of senna for chronic constipation. |
| Plantago ovata | 19713235 | Soluble or insoluble fibre in irritable bowel syndrome in primary care? Randomised placebo controlled trial. |
| Plantago ovata | 35816465 | The Effect of Fiber Supplementation on Chronic Constipation in Adults: An Updated Systematic Review and Meta-Analysis of Randomized Controlled Trials. |
| Plantago ovata | 30239559 | Effect of psyllium (Plantago ovata) fiber on LDL cholesterol and alternative lipid targets, non-HDL cholesterol and apolipoprotein B: a systematic review and meta-analysis of randomized controlled trials. |
| Aloe vera | 15043514 | Randomized, double-blind, placebo-controlled trial of oral aloe vera gel for active ulcerative colitis. |
| Aloe vera | 22336851 | Aloe vera for treating acute and chronic wounds. |
| Aloe vera | 25073673 | Acute toxic hepatitis caused by an aloe vera preparation in a young patient: a case report with a literature review. |
| Aloe vera | 38605441 | Effects of Aloe vera on Burn Injuries: A Systematic Review and Meta-Analysis of Randomized Controlled Trials. |
| Sabdariffa gossypiifolia | 20018807 | Hibiscus sabdariffa L. tea (tisane) lowers blood pressure in prehypertensive and mildly hypertensive adults. |
| Sabdariffa gossypiifolia | 34927694 | A systematic review and meta-analysis of the effects of Hibiscus sabdariffa on blood pressure and cardiometabolic markers. |
| Sabdariffa gossypiifolia | 15647413 | Pharmacokinetics of anthocyanidin-3-glycosides following consumption of Hibiscus sabdariffa L. extract. |
| Sabdariffa gossypiifolia | 30764582 | Acute Effects of Hibiscus Sabdariffa Calyces on Postprandial Blood Pressure, Vascular Function, Blood Lipids, Biomarkers of Insulin Resistance and Inflammation in Humans. |
| Sabdariffa gossypiifolia | 15330492 | Effectiveness and tolerability of a standardized extract from Hibiscus sabdariffa in patients with mild to moderate hypertension: a controlled and randomized clinical trial. |
| Rosa canina | 18407528 | Does the hip powder of Rosa canina (rosehip) reduce pain in osteoarthritis patients?--a meta-analysis of randomized controlled trials. |
| Rosa canina | 16195164 | A powder made from seeds and shells of a rose-hip subspecies (Rosa canina) reduces symptoms of knee and hip osteoarthritis: a randomized, double-blind, placebo-controlled clinical trial. |
| Rosa canina | 18384191 | A systematic review on the Rosa canina effect and efficacy profiles. |
| Rosa canina | 16395741 | The evidence for clinical efficacy of rose hip and seed: a systematic review. |
| Pelargonium sidoides | 24146345 | Pelargonium sidoides extract for treating acute respiratory tract infections. |
| Pelargonium sidoides | 33514367 | Pelargonium sidoides root extract for the treatment of acute cough due to lower respiratory tract infection in adults: a feasibility double-blind, placebo-controlled randomised trial. |
| Pelargonium sidoides | 36051888 | Effects of Pelargonium sidoides extract EPs 7630 on acute cough and quality of life - a meta-analysis of randomized, placebo-controlled trials. |
| Pelargonium sidoides | 22381150 | Spontaneous reports of primarily suspected herbal hepatotoxicity by Pelargonium sidoides: was causality adequately ascertained? |
| Pelargonium sidoides | 41890334 | Short-term Liver Safety of &lt;i&gt;Pelargonium sidoides&lt;/i&gt; DC. Root (PELARGO) 20 mg Capsule: A Non-interventional Post-authorization Safety Study. |
| Linum usitatissimum | 36622248 | Effect of flaxseed supplementation on blood pressure: a systematic review, and dose-response meta-analysis of randomized clinical trials. |
| Linum usitatissimum | 26071633 | Effects of flaxseed supplements on blood pressure: A systematic review and meta-analysis of controlled clinical trial. |
| Linum usitatissimum | 24429845 | Metabolism of secoisolariciresinol-diglycoside the dietary precursor to the intestinally derived lignan enterolactone in humans. |
| Linum usitatissimum | 34119421 | Effects of flaxseed on blood pressure, body mass index, and total cholesterol in hypertensive patients: A randomized clinical trial. |
| Aesculus hippocastanum | 23152216 | Horse chestnut seed extract for chronic venous insufficiency. |
| Aesculus hippocastanum | 8569363 | Comparison of leg compression stocking and oral horse-chestnut seed extract therapy in patients with chronic venous insufficiency. |

## Every validator warning assessed

### Tanacetum parthenium — clinical_data.special_precautions.pregnancy
Current text: "Contraindicated. Feverfew has documented emmenagogue activity in traditional and pharmacological literature, and in vitro data suggest uterine-stimulating properties attributed to parthenolide [4]. No controlled human safety data in pregnancy exist. Avoid throughout pregnancy."
Assessment: Pre-existing field outside this batch. Text inspected; warning arises from “safety”/“safe” substring or qualified wording, not a new unqualified-safety assertion. This gate does not re-approve its underlying older claims.

### Trigonella foenum-graecum — clinical_data.safety_and_interactions
Current text: {"drug_interactions": "Antidiabetic agents (metformin, sulfonylureas, insulin): Fenugreek seed extracts demonstrate additive blood glucose-lowering effects via complementary mechanisms; co-administration requires blood glucose monitoring and may necessitate antidiabetic dose adjustment to avoid hypoglycaemia [1, 2]. Anticoagulants and antiplatelet agents: Fenugreek seeds contain coumarin compounds (including scopoletin) with theoretical anticoagulant potential. One case report documented increased INR in a patient taking a combined boldo-fenugreek preparation alongside warfarin [PMID: 11310527]; the individual contribution of fenugreek cannot be isolated from boldo in this report, and a controlled RCT did not demonstrate significant platelet aggregation effects from fenugreek alone. Evidence level is very low (single case report, mixed herbal product); clinical significance is unestablished. Caution is nonetheless warranted in patients on warfarin or other anticoagulants. Thyroid medications: Preclinical data (rat study) suggest fenugreek may suppress central thyroid signalling via leptin-mediated downregulation of TRH gene expression [PMID: 28407664]; the clinical relevance in humans on levothyroxine or antithyroid therapy is unknown but warrants caution. Iron absorption: Galactomannan fibre may reduce bioavailability of co-administered oral iron supplements when taken simultaneously.", "toxicity": "Fenugreek seeds have a long record of culinary use at low doses without significant toxicity signal. In clinical trials, adverse effects are predominantly mild and gastrointestinal. Preclinical toxicology in rodents indicates a wide safety margin at culinary-range doses; high-dose chronic exposure (exceeding medicinal ranges) is associated with reproductive effects in animal studies, including disruption of reproductive hormone levels. A preclinical study (rat model, PMID: 28407664) documents the potential for central hypothyroidism at high doses via leptin-mediated suppression of TRH mRNA expression; this finding has not been reproduced in human clinical trials. Allergic reactions, including anaphylaxis, have been reported in individuals with Fabaceae allergy. No established human LD50 data are available."}
Assessment: Pre-existing field outside this batch. Text inspected; warning arises from “safety”/“safe” substring or qualified wording, not a new unqualified-safety assertion. This gate does not re-approve its underlying older claims.

### Trigonella foenum-graecum — clinical_data.special_precautions.pregnancy
Current text: "Contraindicated in medicinal doses during pregnancy. Fenugreek has documented uterotonic activity in preclinical models and is classified as an emmenagogue in traditional medicine. Culinary quantities in food are not formally evaluated in human pregnancy safety studies; the distinction from medicinal doses is based on traditional practice and regulatory convention, not clinical evidence."
Assessment: Pre-existing field outside this batch. Text inspected; warning arises from “safety”/“safe” substring or qualified wording, not a new unqualified-safety assertion. This gate does not re-approve its underlying older claims.

### Trigonella foenum-graecum — clinical_data.special_precautions.lactation
Current text: "Fenugreek is among the most widely used botanical galactagogues. A 2018 network meta-analysis of 5 RCTs (n=122) found significant increases in breast milk volume compared to placebo (weighted mean difference 11.11 mL, 95% CI 6.77–15.46) [3], though fenugreek was inferior to other botanical comparators. The NLM LactMed database notes that this galactagogue effect may be primarily psychological in humans, and not all reviews support efficacy. Additionally, sotolon (the primary volatile compound) is excreted in breast milk and causes a maple syrup-like odour in the infant's urine and sweat. Safety for the breastfed infant has not been established in rigorous clinical studies; use at medicinal doses requires monitoring of both maternal and infant response."
Assessment: Pre-existing field outside this batch. Text inspected; warning arises from “safety”/“safe” substring or qualified wording, not a new unqualified-safety assertion. This gate does not re-approve its underlying older claims.

### Uncaria tomentosa — clinical_data.special_precautions.pregnancy
Current text: "Contraindicated during pregnancy. Uncaria tomentosa has been used historically as an abortifacient in some South American traditional contexts [4, 7]. No controlled human safety data exist. Avoid all use during pregnancy."
Assessment: Pre-existing field outside this batch. Text inspected; warning arises from “safety”/“safe” substring or qualified wording, not a new unqualified-safety assertion. This gate does not re-approve its underlying older claims.

### Taraxacum officinale — clinical_data.special_precautions.renal_impairment
Current text: "The EMA assessment of Taraxaci folium explicitly excludes patients with renal failure from its safety statement, citing the risk of clinically significant elevation of serum potassium (hyperkalaemia) due to the leaf's high potassium content. Patients with any degree of renal impairment should not use medicinal-dose Taraxacum leaf preparations without direct medical supervision. No human pharmacokinetic data exist for this population."
Assessment: Pre-existing field outside this batch. Text inspected; warning arises from “safety”/“safe” substring or qualified wording, not a new unqualified-safety assertion. This gate does not re-approve its underlying older claims.

### Vitis vinifera — clinical_data.safety_and_interactions
Current text: {"drug_interactions": "Anticoagulants (warfarin) and antiplatelet agents (aspirin, clopidogrel, NSAIDs): additive antiplatelet activity via PECAM-1 modulation is mechanistically plausible; pharmacodynamic interaction cannot be excluded, though no clinically documented pharmacokinetic INR-altering interaction specific to grape seed extract has been identified in the reviewed literature. CYP450 interactions: no significant CYP inhibition has been documented at clinical doses in human studies; pharmacokinetic interactions with CYP substrates appear low-risk at standard supplemental doses. Additive antihypertensive effects are possible when combined with blood pressure-lowering medications; monitor blood pressure accordingly [1, 2, 3].", "toxicity": "In 90-day rodent oral toxicity studies (regulatory preclinical safety literature; not directly cited in this monograph's five primary references), grape seed extract demonstrated a no-observed-adverse-effect level (NOAEL) of approximately 1,400–1,500 mg/kg/day. No evidence of mutagenicity was found in bacterial reverse mutation assays (regulatory preclinical data). No serious adverse events were reported in any of the clinical trials cited in this monograph. Grape seed extract preparations standardised to ≥95% OPCs are generally well tolerated in short-term trials up to 16 weeks; available clinical evidence does not support a significant hepatotoxic or nephrotoxic risk at supplemental doses up to 400 mg/day."}
Assessment: Pre-existing field outside this batch. Text inspected; warning arises from “safety”/“safe” substring or qualified wording, not a new unqualified-safety assertion. This gate does not re-approve its underlying older claims.

### Mentha × piperita — clinical_data.special_precautions.renal_impairment
Current text: "No validated renal dose adjustment identified; renal-impairment PK and safety remain gaps in this extraction [3][4][5]."
Assessment: False positive: explicit missing evidence/uncertainty, a negative safety assertion, or refusal to infer a safe maximum. The substring matcher includes “safety” and misses negation variants.

### Cynara cardunculus — clinical_data.special_precautions.pregnancy
Current text: "Safety unestablished; EMA does not recommend medicinal use during pregnancy [4]."
Assessment: False positive: explicit missing evidence/uncertainty, a negative safety assertion, or refusal to infer a safe maximum. The substring matcher includes “safety” and misses negation variants.

### Cynara cardunculus — clinical_data.special_precautions.lactation
Current text: "Safety unestablished; EMA does not recommend medicinal use during lactation [4]."
Assessment: False positive: explicit missing evidence/uncertainty, a negative safety assertion, or refusal to infer a safe maximum. The substring matcher includes “safety” and misses negation variants.

### Plantago ovata — clinical_data.safety_and_interactions
Current text: {"drug_interactions": "May delay absorption of other oral medicines. EMA specifies separation and notes supervision with thyroid hormones or motility-inhibiting drugs; diabetes therapy may require review. Interaction severity depends on the medicine [4].", "toxicity": "The major acute risks are mechanical obstruction and severe hypersensitivity; sufficient liquid is essential. No maximum safe dose for impaired populations is inferred from trials [4]."}
Assessment: False positive: explicit missing evidence/uncertainty, a negative safety assertion, or refusal to infer a safe maximum. The substring matcher includes “safety” and misses negation variants.

### Sabdariffa gossypiifolia — clinical_data.safety_and_interactions
Current text: {"drug_interactions": "Additive hypotension with antihypertensive drugs is a precautionary pharmacodynamic concern [2][6]. EDA also flags chloroquine, simvastatin and diabetes medicines, but this extraction has not independently verified the underlying clinical interaction studies; direction and magnitude must not be assumed [6]. A hydrochlorothiazide interaction described in the review was in rats and is not an established human interaction [2].", "toxicity": "No reliable long-term human toxicity threshold is established. Short trial tolerability and animal toxicity results do not establish safety during chronic concentrated-extract use [2]."}
Assessment: False positive: explicit missing evidence/uncertainty, a negative safety assertion, or refusal to infer a safe maximum. The substring matcher includes “safety” and misses negation variants.

### Sabdariffa gossypiifolia — clinical_data.special_precautions.hepatic_impairment
Current text: "No validated hepatic-impairment dosing or safety studies identified in the selected sources; concentrated-extract exposure requires individual clinical assessment [2][6]."
Assessment: False positive: explicit missing evidence/uncertainty, a negative safety assertion, or refusal to infer a safe maximum. The substring matcher includes “safety” and misses negation variants.

### Rosa canina — clinical_data.safety_and_interactions
Current text: {"drug_interactions": "No clinically quantified herb–drug interaction or validated CYP interaction profile was established in the selected sources. This is an evidence gap rather than proof of no interaction; concurrent medication and product composition require individual assessment [1][3].", "toxicity": "Long-term toxicity, rare hepatic or renal events and maximum tolerable exposure are unresolved. The three-trial pain meta-analysis does not establish broad safety of other rosehip preparations [1]."}
Assessment: False positive: explicit missing evidence/uncertainty, a negative safety assertion, or refusal to infer a safe maximum. The substring matcher includes “safety” and misses negation variants.

### Rosa canina — clinical_data.special_precautions.pregnancy
Current text: "Pregnancy safety for the studied medicinal powder could not be established from the selected sources; this is an evidence gap, not proof of fetal safety or harm [1][3]."
Assessment: False positive: explicit missing evidence/uncertainty, a negative safety assertion, or refusal to infer a safe maximum. The substring matcher includes “safety” and misses negation variants.

### Pelargonium sidoides — clinical_data.special_precautions.renal_impairment
Current text: "No validated renal-impairment adjustment or adequate disease-specific safety data identified in selected sources [6]."
Assessment: False positive: explicit missing evidence/uncertainty, a negative safety assertion, or refusal to infer a safe maximum. The substring matcher includes “safety” and misses negation variants.

### Aesculus hippocastanum — clinical_data.special_precautions.hepatic_impairment
Current text: "No validated hepatic-impairment dose adjustment or adequate disease-specific safety data identified; individualized assessment is required [3]."
Assessment: False positive: explicit missing evidence/uncertainty, a negative safety assertion, or refusal to infer a safe maximum. The substring matcher includes “safety” and misses negation variants.

## Final validator evidence

### Mentha × piperita
```text
BMS Archive — Data Validation
File: /Users/kubi/Desktop/BMS website/data.json
Mode: standard
Filter: Mentha × piperita
────────────────────────────────────────────────────────────

Entries: 82 total (25 Fungi, 57 Plant)

WARNINGS (1):
  [WARN]  Mentha × piperita | clinical_data.special_precautions.renal_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis

✓ No errors. 1 warning(s) — review recommended.
```

### Cynara cardunculus
```text
BMS Archive — Data Validation
File: /Users/kubi/Desktop/BMS website/data.json
Mode: standard
Filter: Cynara cardunculus
────────────────────────────────────────────────────────────

Entries: 82 total (25 Fungi, 57 Plant)

WARNINGS (2):
  [WARN]  Cynara cardunculus | clinical_data.special_precautions.pregnancy | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Cynara cardunculus | clinical_data.special_precautions.lactation | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis

✓ No errors. 2 warning(s) — review recommended.
```

### Senna alexandrina
```text
BMS Archive — Data Validation
File: /Users/kubi/Desktop/BMS website/data.json
Mode: standard
Filter: Senna alexandrina
────────────────────────────────────────────────────────────

Entries: 82 total (25 Fungi, 57 Plant)

✓ All checks passed — no errors or warnings.
```

### Plantago ovata
```text
BMS Archive — Data Validation
File: /Users/kubi/Desktop/BMS website/data.json
Mode: standard
Filter: Plantago ovata
────────────────────────────────────────────────────────────

Entries: 82 total (25 Fungi, 57 Plant)

WARNINGS (1):
  [WARN]  Plantago ovata | clinical_data.safety_and_interactions | Contains unqualified 'safe' claim — verify evidence basis

✓ No errors. 1 warning(s) — review recommended.
```

### Aloe vera
```text
BMS Archive — Data Validation
File: /Users/kubi/Desktop/BMS website/data.json
Mode: standard
Filter: Aloe vera
────────────────────────────────────────────────────────────

Entries: 82 total (25 Fungi, 57 Plant)

✓ All checks passed — no errors or warnings.
```

### Sabdariffa gossypiifolia
```text
BMS Archive — Data Validation
File: /Users/kubi/Desktop/BMS website/data.json
Mode: standard
Filter: Sabdariffa gossypiifolia
────────────────────────────────────────────────────────────

Entries: 82 total (25 Fungi, 57 Plant)

WARNINGS (2):
  [WARN]  Sabdariffa gossypiifolia | clinical_data.safety_and_interactions | Contains unqualified 'safe' claim — verify evidence basis
  [WARN]  Sabdariffa gossypiifolia | clinical_data.special_precautions.hepatic_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis

✓ No errors. 2 warning(s) — review recommended.
```

### Rosa canina
```text
BMS Archive — Data Validation
File: /Users/kubi/Desktop/BMS website/data.json
Mode: standard
Filter: Rosa canina
────────────────────────────────────────────────────────────

Entries: 82 total (25 Fungi, 57 Plant)

WARNINGS (2):
  [WARN]  Rosa canina | clinical_data.safety_and_interactions | Contains unqualified 'safe' claim — verify evidence basis
  [WARN]  Rosa canina | clinical_data.special_precautions.pregnancy | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis

✓ No errors. 2 warning(s) — review recommended.
```

### Pelargonium sidoides
```text
BMS Archive — Data Validation
File: /Users/kubi/Desktop/BMS website/data.json
Mode: standard
Filter: Pelargonium sidoides
────────────────────────────────────────────────────────────

Entries: 82 total (25 Fungi, 57 Plant)

WARNINGS (1):
  [WARN]  Pelargonium sidoides | clinical_data.special_precautions.renal_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis

✓ No errors. 1 warning(s) — review recommended.
```

### Linum usitatissimum
```text
BMS Archive — Data Validation
File: /Users/kubi/Desktop/BMS website/data.json
Mode: standard
Filter: Linum usitatissimum
────────────────────────────────────────────────────────────

Entries: 82 total (25 Fungi, 57 Plant)

✓ All checks passed — no errors or warnings.
```

### Aesculus hippocastanum
```text
BMS Archive — Data Validation
File: /Users/kubi/Desktop/BMS website/data.json
Mode: standard
Filter: Aesculus hippocastanum
────────────────────────────────────────────────────────────

Entries: 82 total (25 Fungi, 57 Plant)

WARNINGS (1):
  [WARN]  Aesculus hippocastanum | clinical_data.special_precautions.hepatic_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis

✓ No errors. 1 warning(s) — review recommended.
```

### Full database standard
```text
BMS Archive — Data Validation
File: /Users/kubi/Desktop/BMS website/data.json
Mode: standard
────────────────────────────────────────────────────────────

Entries: 82 total (25 Fungi, 57 Plant)

WARNINGS (17):
  [WARN]  Tanacetum parthenium | clinical_data.special_precautions.pregnancy | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Trigonella foenum-graecum | clinical_data.safety_and_interactions | Contains unqualified 'safe' claim — verify evidence basis
  [WARN]  Trigonella foenum-graecum | clinical_data.special_precautions.pregnancy | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Trigonella foenum-graecum | clinical_data.special_precautions.lactation | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Uncaria tomentosa | clinical_data.special_precautions.pregnancy | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Taraxacum officinale | clinical_data.special_precautions.renal_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Vitis vinifera | clinical_data.safety_and_interactions | Contains unqualified 'safe' claim — verify evidence basis
  [WARN]  Mentha × piperita | clinical_data.special_precautions.renal_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Cynara cardunculus | clinical_data.special_precautions.pregnancy | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Cynara cardunculus | clinical_data.special_precautions.lactation | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Plantago ovata | clinical_data.safety_and_interactions | Contains unqualified 'safe' claim — verify evidence basis
  [WARN]  Sabdariffa gossypiifolia | clinical_data.safety_and_interactions | Contains unqualified 'safe' claim — verify evidence basis
  [WARN]  Sabdariffa gossypiifolia | clinical_data.special_precautions.hepatic_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Rosa canina | clinical_data.safety_and_interactions | Contains unqualified 'safe' claim — verify evidence basis
  [WARN]  Rosa canina | clinical_data.special_precautions.pregnancy | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Pelargonium sidoides | clinical_data.special_precautions.renal_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Aesculus hippocastanum | clinical_data.special_precautions.hepatic_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis

✓ No errors. 17 warning(s) — review recommended.
```

### Full database strict
```text
BMS Archive — Data Validation
File: /Users/kubi/Desktop/BMS website/data.json
Mode: strict
────────────────────────────────────────────────────────────

Entries: 82 total (25 Fungi, 57 Plant)

WARNINGS (17):
  [WARN]  Tanacetum parthenium | clinical_data.special_precautions.pregnancy | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Trigonella foenum-graecum | clinical_data.safety_and_interactions | Contains unqualified 'safe' claim — verify evidence basis
  [WARN]  Trigonella foenum-graecum | clinical_data.special_precautions.pregnancy | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Trigonella foenum-graecum | clinical_data.special_precautions.lactation | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Uncaria tomentosa | clinical_data.special_precautions.pregnancy | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Taraxacum officinale | clinical_data.special_precautions.renal_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Vitis vinifera | clinical_data.safety_and_interactions | Contains unqualified 'safe' claim — verify evidence basis
  [WARN]  Mentha × piperita | clinical_data.special_precautions.renal_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Cynara cardunculus | clinical_data.special_precautions.pregnancy | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Cynara cardunculus | clinical_data.special_precautions.lactation | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Plantago ovata | clinical_data.safety_and_interactions | Contains unqualified 'safe' claim — verify evidence basis
  [WARN]  Sabdariffa gossypiifolia | clinical_data.safety_and_interactions | Contains unqualified 'safe' claim — verify evidence basis
  [WARN]  Sabdariffa gossypiifolia | clinical_data.special_precautions.hepatic_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Rosa canina | clinical_data.safety_and_interactions | Contains unqualified 'safe' claim — verify evidence basis
  [WARN]  Rosa canina | clinical_data.special_precautions.pregnancy | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Pelargonium sidoides | clinical_data.special_precautions.renal_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis
  [WARN]  Aesculus hippocastanum | clinical_data.special_precautions.hepatic_impairment | Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis

✓ No errors. 17 warning(s) — review recommended.
```

## Files changed by this gate

- data.json — last ten modern_application values and cited_references prefix formatting only.
- docs/research/plant-batch-2026-10-25-pre-publish.md — this report.

## Checks not claimed

No external human scientific review, complete full-text appraisal of every study, production deployment, browser regression test, security/ops audit, commit or push was performed by this agent. These are not implied by publication-readiness PASS.
