# Scientific QA signoff — ten plant drafts, 25 October 2026

MONOGRAPH AUDIT RESULT: APPROVE AS DRAFTS AFTER REVISIONS

All ten proposed profiles may proceed to archive-data-model review and local draft integration. This is an agent scientific gate, not manual scientific approval, publication approval, deployment authorization or a claim that every intervention is effective. Every profile visibly retains “Pending manual scientific review.” No data.json or UI edits were made by this reviewer.

## Scope and methods

Reviewed exact proposed JSON claims against saved Europe PMC core abstracts and full local EMA/NCCIH/EDA safety texts; inspected roselle and Pelargonium full-text XML where supplied. Applied docs/rubrics/EVIDENCE_SCORING.md. Abstract-only numeric medicinal amounts were removed even when bibliographic abstracts mentioned them. No dosing recommendation remains. Mechanistic and PK claims are preparation/compound specific; evidence gaps are gaps in selected sources, not proof that no study exists. No trial label automatically implies Level A. Provisional B is a draft classification pending manual full-text risk-of-bias appraisal.

Live recency check identified [2026 pediatric peppermint trial](https://pubmed.ncbi.nlm.nih.gov/41610933/) and [2024 Aloe burn review](https://pubmed.ncbi.nlm.nih.gov/38605441/); both now have exact indexed records and parent extraction supplements in batch A. Supplemental records reviewed: narrow conclusions and full-text restrictions are appropriate. Peppermint reported total and age strata conflict, so age-stratum counts are not published. A 2026 broad fiber network review PMID42317046 was screened online but is not used to assert psyllium-only effects or to upgrade evidence. Search was targeted, not an exhaustive updated systematic review.

## Cross-cutting restrictions

- Human RCT/SR abstracts support only the quoted study design and scoped outcome summaries, not detailed safety or product dosing.
- Regulatory texts supply preparation-specific safety; “none reported” never becomes “no interactions.”
- Rosehip safety lacks adequate full-text confirmation; the profile states gaps and does not make positive safety assertions.
- Impairment dosing, tissue distribution and extract-level clearance generally remain unknown in these sources. Precautionary inferences are marked.
- Existing scientific disclaimer remains necessary. No replacement of standard medical care is implied.

## Species decisions

### Mentha × piperita — APPROVE AS DRAFT
EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate.

ISSUES / REVISIONS: Replaced unsupported calcium-dependent target wording with EMA smooth-muscle spasmolysis. Removed abstract-only exact dose and unsourced essential-oil distillation/part detail. Added current negative pediatric RCT PMID41610933 as [6]. EMA oil monograph sections 4.3–4.9 and 5.1–5.3 directly support safety, CYP observation and menthol-glucuronide statements. Pediatric Tmax is a compound-specific abstract finding, not an adult regimen.

SOURCE SUPPORT: Exact indexed abstracts reviewed for clinical narratives; source-local numbered citations below. Safety additionally checked against complete regulatory or NIH text as described above.

RECOMMENDATION: Approve corrected draft for schema review; retain manual scientific review gate. No unresolved blocker to honest draft presentation.

Sources:
- [1] Ingrosso MR, Ianiro G, Nee J, Lembo AJ, Moayyedi P, Black CJ, Ford AC. Systematic review and meta-analysis: efficacy of peppermint oil in irritable bowel syndrome. Alimentary pharmacology & therapeutics 2022. PMID: 35942669. DOI: 10.1111/apt.17179.
- [2] Nee J, Ballou S, Kelley JM, Kaptchuk TJ, Hirsch W, Katon J, Cheng V, Rangan V, Lembo A, Iturrino J. Peppermint Oil Treatment for Irritable Bowel Syndrome: A Randomized Placebo-Controlled Trial. The American journal of gastroenterology 2021. PMID: 34319275. DOI: 10.14309/ajg.0000000000001395.
- [3] Shulman RJ, Chumpitazi BP, Abdel-Rahman SM, Garg U, Musaad S, Kearns GL. Randomised trial: Peppermint oil (menthol) pharmacokinetics in children and effects on gut motility in children with functional abdominal pain. British journal of clinical pharmacology 2022. PMID: 34528282. DOI: 10.1111/bcp.15076.
- [4] Shulman RJ, Chumpitazi BP, Gonzalez D, Garg U, Musaad S, Wen J, Kearns GL. Randomized trial: Peppermint oil (menthol) pharmacokinetics in children and effects on gut motility in children with functional abdominal pain: 540 mg vs. 900 mg dose comparison. British journal of clinical pharmacology 2025. PMID: 40390282. DOI: 10.1002/bcp.70097.
- [5] EMA/HMPC. Official herbal monograph, full regulatory text, sections 4.3–5.3. https://www.ema.europa.eu/en/documents/herbal-monograph/european-union-herbal-monograph-mentha-x-piperita-l-aetheroleum-revision-1_en.pdf Accessed 2026-10-25.
- [6] Vermeijden NK et al. Peppermint Oil and Sweets in Pediatric Irritable Bowel Syndrome and Functional Abdominal Pain: A Randomized Trial. Clinical Gastroenterology and Hepatology 2026;24:2286–2296. PMID: 41610933. DOI: 10.1016/j.cgh.2026.01.014. Abstract reviewed; full-text appraisal pending.

Field-level claim audit (exact reviewed text):

**narrative_summary.historical_use**
- CLAIM: Peppermint oil has a documented European history of digestive use; traditional cough, muscle-pain and itching applications have a separate evidence basis from oral IBS research [5].
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.modern_application**
- CLAIM: Draft research profile: enteric-coated peppermint oil has been studied for IBS symptoms, with inconsistent trial results [1][2]. A 2022 synthesis of 10 RCTs (1030 participants) reported pooled symptom benefit but rated certainty very low and found more adverse events [1]. A 6-week trial in people with Rome IV IBS found no superiority over placebo [2]. A 2026 trial in children aged 8–18 years likewise found neither peppermint oil nor peppermint sweets superior to placebo after eight weeks [6]. BMS Level U for a firm general efficacy conclusion; formulation-specific human research exists. Pediatric PK studies describe exposure, not established pediatric treatment regimens [3][4]. Pending manual scientific review.
- SOURCE: [1], [2], [6], [3], [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.side_effects**
- CLAIM: Heartburn, nausea and perianal burning are reported; reflux can worsen, including in people with hiatal hernia. Allergy can occur. Trial adverse events were more frequent than placebo in the synthesis [1][5].
- SOURCE: [1], [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.contraindications**
- CLAIM: EMA lists oil/menthol hypersensitivity, liver disease, cholangitis, gallstones, other biliary disorders and achlorhydria for oral gastro-resistant preparations. Oral IBS preparations are not recommended below age 8; other routes have distinct age restrictions, including contraindication below age 2 [5]. Worsening symptoms warrant medical advice [5]. EMA also contraindicates its traditional-use preparations in children with a seizure history; age limits vary by route [5].
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.used_part**
- CLAIM: Peppermint essential oil; clinical evidence here concerns enteric-coated oil, not leaf tea [2][5].
- SOURCE: [2], [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[0]**
- CLAIM: Menthol (monoterpene; studied PK marker) [3][4]
- SOURCE: [3], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[1]**
- CLAIM: Essential-oil terpenes; product composition varies [5]
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.mechanism_of_action**
- CLAIM: EMA describes <strong>gastrointestinal smooth-muscle spasmolysis</strong> in human pharmacological studies. This does not establish symptom benefit in every IBS population or identify a single clinically validated molecular target [5].
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.absorption**
- CLAIM: Human studies measured systemic menthol after enteric-coated oil; exposure depends on dose/formulation. In a small pediatric study peak concentration occurred about 2.5 hours after dosing [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.distribution**
- CLAIM: Human whole-oil tissue distribution is insufficiently characterized in the retrieved sources; pediatric PK findings do not establish adult distribution [3][4].
- SOURCE: [3], [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.metabolism**
- CLAIM: EMA describes glucuronide formation and limited clinical observations of CYP3A4 inhibition; interaction magnitude remains incompletely defined [5].
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.excretion**
- CLAIM: Menthol glucuronide elimination is described in EMA; modified release delays urinary excretion relative to immediate release. No universal whole-oil half-life is established here [5].
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.drug_interactions**
- CLAIM: Antacids, H2 blockers and proton-pump inhibitors may cause premature dissolution of gastro-resistant coatings. Limited CYP3A4 observations do not establish a quantified interaction with every substrate [5].
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.toxicity**
- CLAIM: Concentrated oil overdose can cause serious neurologic and cardiac effects. Animal high-dose pulegone/menthofuran findings are not direct estimates of clinical cancer risk [5].
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.pregnancy**
- CLAIM: Medicinal-oil pregnancy safety is unestablished; EMA does not recommend use with insufficient data [5].
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.lactation**
- CLAIM: EMA does not recommend medicinal use; milk transfer is unknown [5].
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.hepatic_impairment**
- CLAIM: Oral gastro-resistant oil is contraindicated in liver disease in the EMA monograph [5].
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.renal_impairment**
- CLAIM: No validated renal dose adjustment identified; renal-impairment PK and safety remain gaps in this extraction [3][4][5].
- SOURCE: [3], [4], [5]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm general symptom efficacy; human RCT/SR evidence exists; pediatric PK separate; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

### Cynara cardunculus — APPROVE AS DRAFT
EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication.

ISSUES / REVISIONS: Removed unsupported constituent list formerly cited to the RCT abstract. Removed exact abstract-only capsule amount. Preserved leaf-specific intervention, mixed products, traditional EMA status, biliary contraindications and pregnancy/lactation limits. Molecular and whole-extract PK gaps are explicitly bounded to selected sources.

SOURCE SUPPORT: Exact indexed abstracts reviewed for clinical narratives; source-local numbered citations below. Safety additionally checked against complete regulatory or NIH text as described above.

RECOMMENDATION: Approve corrected draft for schema review; retain manual scientific review gate. No unresolved blocker to honest draft presentation.

Sources:
- [1] Holtmann G, Adam B, Haag S, Collet W, Grünewald E, Windeck T. Efficacy of artichoke leaf extract in the treatment of patients with functional dyspepsia: a six-week placebo-controlled, double-blind, multicentre trial. Alimentary pharmacology & therapeutics 2003. PMID: 14653829. DOI: 10.1046/j.1365-2036.2003.01767.x.
- [2] Sahebkar A, Pirro M, Banach M, Mikhailidis DP, Atkin SL, Cicero AFG. Lipid-lowering activity of artichoke extracts: A systematic review and meta-analysis. Critical reviews in food science and nutrition 2018. PMID: 28609140. DOI: 10.1080/10408398.2017.1332572.
- [3] Shahinfar H, Bazshahi E, Amini MR, Payandeh N, Pourreza S, Noruzi Z, Shab-Bidar S. Effects of artichoke leaf extract supplementation or artichoke juice consumption on lipid profile: A systematic review and dose-response meta-analysis of randomized controlled trials. Phytotherapy research : PTR 2021. PMID: 34569671. DOI: 10.1002/ptr.7247.
- [4] EMA/HMPC. Official herbal monograph, full regulatory text, sections 4.3–5.3. https://www.ema.europa.eu/en/documents/herbal-monograph/final-european-union-herbal-monograph-cynara-cardunculus-l-syn-cynara-scolymus-l-folium_en.pdf Accessed 2026-10-25.

Field-level claim audit (exact reviewed text):

**narrative_summary.historical_use**
- CLAIM: Artichoke leaf has documented traditional use for fullness, bloating and flatulence; EMA categorizes this digestive indication as traditional use [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.modern_application**
- CLAIM: Draft research profile: artichoke leaf extracts have been investigated for functional dyspepsia and lipid biomarkers [1][2][3]. In a 6-week RCT (247 enrolled), a commercial leaf extract improved symptom scores versus placebo [1]. Meta-analyses reported lipid changes across varying products; cardiovascular event prevention is unproven [2][3]. BMS Level B provisional for the specific dyspepsia preparation and lipid markers, with full-text bias review pending; EMA traditional-use status remains distinct [4]. Pending manual scientific review.
- SOURCE: [1], [2], [3], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.side_effects**
- CLAIM: Mild diarrhea, abdominal spasm, nausea, heartburn and allergic reactions are reported; frequencies are unknown [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.contraindications**
- CLAIM: EMA lists Asteraceae hypersensitivity, bile-duct obstruction, cholangitis, liver disease, gallstones and other biliary disorders requiring medical advice. Use below age 12 is not established [4]. Persistent digestive symptoms beyond two weeks warrant medical advice [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.used_part**
- CLAIM: Leaf extract of cultivated artichoke, reported in literature as Cynara scolymus; evidence must not be transferred to all C. cardunculus varieties or edible hearts. EMA covers specified leaf preparations [1][4].
- SOURCE: [1], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[0]**
- CLAIM: Commercial leaf-extract mixture; the retrieved trial abstract does not identify constituent concentrations or clinical standardization, so no individual active compound is assigned [1].
- SOURCE: [1]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.mechanism_of_action**
- CLAIM: <strong>Digestive symptom modulation</strong> and <strong>lipid metabolism</strong> are studied outcomes; molecular causation is not established by the retrieved human trials. No specific molecular target is assigned here [1][2][3].
- SOURCE: [1], [2], [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.absorption**
- CLAIM: Human absorption of the trial extract is not characterized in the retrieved studies; no bioavailability estimate assigned [1][4].
- SOURCE: [1], [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.distribution**
- CLAIM: Human tissue distribution is not characterized in the retrieved sources [1][4].
- SOURCE: [1], [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.metabolism**
- CLAIM: Human metabolism of the whole leaf extract is not characterized in this extraction; no CYP claim assigned [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.excretion**
- CLAIM: No human elimination route or half-life established for the whole extract in the retrieved sources [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.drug_interactions**
- CLAIM: EMA reports no interactions; formal interaction data remain limited. This does not establish compatibility with all medicines [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.toxicity**
- CLAIM: Long-term human toxicity is not established by short trials. EMA notes inadequate reproductive, genotoxicity and carcinogenicity testing; no quantified human safe maximum is assigned [1][4].
- SOURCE: [1], [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.pregnancy**
- CLAIM: Safety unestablished; EMA does not recommend medicinal use during pregnancy [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.lactation**
- CLAIM: Safety unestablished; EMA does not recommend medicinal use during lactation [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.hepatic_impairment**
- CLAIM: Liver disease and biliary disease are listed contraindications in EMA; experimental liver research does not override this [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.renal_impairment**
- CLAIM: No renal dose-adjustment evidence identified; renal-impairment safety remains insufficiently characterized [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for trial-specific dyspepsia/lipid markers; T for EMA indication; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

### Senna alexandrina — APPROVE AS DRAFT
EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only.

ISSUES / REVISIONS: Removed abstract-only exact amount; part/anthranoid uncertainty remains explicit. Added hypersensitivity and QT-prolonging medication consultation. EMA full monograph confirms one-week limit, obstruction/IBD/dehydration contraindications, pregnancy/lactation contraindications, electrolyte interactions, bacterial activation, and pod-versus-leaf PK distinction. Hepatitis case cannot estimate incidence.

SOURCE SUPPORT: Exact indexed abstracts reviewed for clinical narratives; source-local numbered citations below. Safety additionally checked against complete regulatory or NIH text as described above.

RECOMMENDATION: Approve corrected draft for schema review; retain manual scientific review gate. No unresolved blocker to honest draft presentation.

Sources:
- [1] Morishita D, Tomita T, Mori S, Kimura T, Oshima T, Fukui H, Miwa H. Senna Versus Magnesium Oxide for the Treatment of Chronic Constipation: A Randomized, Placebo-Controlled Trial. The American journal of gastroenterology 2021. PMID: 32969946. DOI: 10.14309/ajg.0000000000000942.
- [2] Rao SSC, Brenner DM. Efficacy and Safety of Over-the-Counter Therapies for Chronic Constipation: An Updated Systematic Review. The American journal of gastroenterology 2021. PMID: 33767108. DOI: 10.14309/ajg.0000000000001222.
- [3] Sonmez A, Yilmaz MI, Mas R, Ozcan A, Celasun B, Dogru T, Taslipinar A, Kocar IH. Subacute cholestatic hepatitis likely related to the use of senna for chronic constipation. Acta gastro-enterologica Belgica 2005. PMID: 16268429. DOI: Not reported.
- [4] EMA/HMPC. Official herbal monograph, full regulatory text, sections 4.3–5.3. https://www.ema.europa.eu/en/documents/herbal-monograph/final-european-union-herbal-monograph-senna-alexandrina-mill-cassia-senna-l-cassia-angustifolia-vahl-folium-revision-1_en.pdf Accessed 2026-10-25.

Field-level claim audit (exact reviewed text):

**narrative_summary.historical_use**
- CLAIM: Senna leaf has longstanding laxative use; EMA recognizes well-established short-term use for occasional constipation [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.modern_application**
- CLAIM: Draft research profile: senna preparations have been studied for constipation, with short-term symptom benefits and important electrolyte and obstruction precautions [1][4]. A 28-day randomized trial in 90 adults compared senna, magnesium oxide and placebo; improvement favored active groups [1]. Exact senna part and anthranoid standardization were not specified in its abstract, so no product-specific dose is given here. BMS Level B provisional for constipation; a favorable OTC systematic review uses a different grading system [2]. EMA limits unsupervised leaf-medicine use to one week; the research duration is not general-use guidance [4]. Pending manual scientific review.
- SOURCE: [1], [4], [2]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.side_effects**
- CLAIM: Abdominal cramps, diarrhea and allergic reactions can occur. Prolonged use may disturb fluid/electrolyte balance and cause reversible intestinal pigmentation; incidence is not established here [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.contraindications**
- CLAIM: EMA contraindications include hypersensitivity, bowel obstruction/stenosis, atony, appendicitis, inflammatory bowel disease, unexplained abdominal pain, severe dehydration, pregnancy, lactation and age under 12. Persistent constipation or symptoms suggesting obstruction require medical assessment [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.used_part**
- CLAIM: EMA profile concerns senna leaf. Pods have related but separately specified preparations. Constipation RCT abstract does not identify plant part or sennoside content [1][4].
- SOURCE: [1], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[0]**
- CLAIM: Sennosides (hydroxyanthracene glycosides); preparations are standardized, but the RCT abstract omits content [1][4]
- SOURCE: [1], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.mechanism_of_action**
- CLAIM: Colonic bacteria convert sennosides to <strong>rhein anthrone</strong>; anthranoid laxative action alters <strong>colonic motility and water/electrolyte transport</strong>. Mechanism does not justify chronic unrestricted use [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.absorption**
- CLAIM: Sennosides are not absorbed or split by human enzymes in the upper gut; some metabolites are absorbed after colonic activation [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.distribution**
- CLAIM: Whole-preparation distribution is incompletely defined. EMA describes a small human pod-powder PK study; pod findings are not identical to a leaf-product PK profile [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.metabolism**
- CLAIM: Bacterial conversion to rhein anthrone occurs in the colon; circulating metabolites include conjugates [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.excretion**
- CLAIM: EMA describes mainly fecal elimination with some urinary/biliary metabolite elimination; no universal leaf-extract half-life is established here [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.drug_interactions**
- CLAIM: Potassium depletion during prolonged misuse can potentiate cardiac glycosides and interact with antiarrhythmics; diuretics, corticosteroids and liquorice may increase potassium loss [4]. EMA advises medical consultation with QT-prolonging medicines and these interacting drug classes [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.toxicity**
- CLAIM: Fluid/electrolyte depletion is a principal misuse risk. A case report linked chronic senna exposure with cholestatic hepatitis, with confounders and no incidence estimate [3][4].
- SOURCE: [3], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.pregnancy**
- CLAIM: Contraindicated in the EMA senna-leaf monograph; experimental anthranoid findings underpin precaution [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.lactation**
- CLAIM: Contraindicated by EMA; small quantities of active metabolites can enter milk [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.hepatic_impairment**
- CLAIM: Suspected liver injury has been reported; no validated hepatic dose adjustment identified [3][4].
- SOURCE: [3], [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.renal_impairment**
- CLAIM: Kidney disorders increase concern about electrolyte disturbances; no validated renal dose adjustment identified [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for constipation; case report is safety signal only; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

### Plantago ovata — APPROVE AS DRAFT
EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings.

ISSUES / REVISIONS: Removed exact abstract-only study amount. Preserved psyllium-versus-all-fiber distinction, moderate LDL certainty, and cardiovascular-outcome uncertainty. EMA full husk monograph supports local mucilage action, limited fermentation, fluid/obstruction/allergy risks, drug absorption precautions and conditional pregnancy/lactation consideration.

SOURCE SUPPORT: Exact indexed abstracts reviewed for clinical narratives; source-local numbered citations below. Safety additionally checked against complete regulatory or NIH text as described above.

RECOMMENDATION: Approve corrected draft for schema review; retain manual scientific review gate. No unresolved blocker to honest draft presentation.

Sources:
- [1] Bijkerk CJ, de Wit NJ, Muris JW, Whorwell PJ, Knottnerus JA, Hoes AW. Soluble or insoluble fibre in irritable bowel syndrome in primary care? Randomised placebo controlled trial. BMJ (Clinical research ed.) 2009. PMID: 19713235. DOI: 10.1136/bmj.b3154.
- [2] van der Schoot A, Drysdale C, Whelan K, Dimidi E. The Effect of Fiber Supplementation on Chronic Constipation in Adults: An Updated Systematic Review and Meta-Analysis of Randomized Controlled Trials. The American journal of clinical nutrition 2022. PMID: 35816465. DOI: 10.1093/ajcn/nqac184.
- [3] Jovanovski E, Yashpal S, Komishon A, Zurbau A, Blanco Mejia S, Ho HVT, Li D, Sievenpiper J, Duvnjak L, Vuksan V. Effect of psyllium (Plantago ovata) fiber on LDL cholesterol and alternative lipid targets, non-HDL cholesterol and apolipoprotein B: a systematic review and meta-analysis of randomized controlled trials. The American journal of clinical nutrition 2018. PMID: 30239559. DOI: 10.1093/ajcn/nqy115.
- [4] EMA/HMPC. Official herbal monograph, full regulatory text, sections 4.3–5.3. https://www.ema.europa.eu/en/documents/herbal-monograph/final-community-herbal-monograph-plantago-ovata-forssk-seminis-tegumentum_en.pdf Accessed 2026-10-25.

Field-level claim audit (exact reviewed text):

**narrative_summary.historical_use**
- CLAIM: Ispaghula seed husk has established medicinal use as a bulk-forming laxative; this profile concerns husk, not unrelated Plantago species [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.modern_application**
- CLAIM: Draft research profile: psyllium husk has been studied for constipation, IBS symptoms and lipid biomarkers [1][2][3]. A 12-week IBS RCT compared psyllium, bran and placebo in 275 adults; psyllium improved relief in early months [1]. Fiber meta-analysis supports a psyllium signal but pooled all-fiber effects cannot be assigned wholly to psyllium [2]. A 28-trial lipid meta-analysis found lower LDL, with moderate certainty limited by inconsistency [3]. BMS Level B provisional for these specific outcomes pending full-text appraisal; cardiovascular event prevention is not established. Pending manual scientific review.
- SOURCE: [1], [2], [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.side_effects**
- CLAIM: Flatulence, distension and allergy, including anaphylaxis, can occur. Inadequate fluid can cause choking or esophageal/intestinal obstruction; powder inhalation may sensitize [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.contraindications**
- CLAIM: EMA contraindications include swallowing/throat disorders, GI narrowing, potential/existing obstruction, megacolon, undiagnosed rectal bleeding, persistent sudden bowel-habit change and failure to defecate after a laxative. Allergy is a contraindication [4]. Constipation persisting beyond three days or abdominal pain warrants medical advice; pediatric age restrictions depend on the indication [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.used_part**
- CLAIM: Seed coats (ispaghula/psyllium husk), whole or powdered. Seed, husk and other Plantago species are not interchangeable [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[0]**
- CLAIM: Gel-forming mucilage polysaccharides, including arabinoxylan-type fiber; whole husk is not a purified systemic drug [4]
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.mechanism_of_action**
- CLAIM: <strong>Water-retaining mucilage</strong> increases stool hydration/bulk; predominantly local gut action differs from systemic receptor pharmacology. Lipid-marker effects do not demonstrate prevention of cardiovascular events [3][4].
- SOURCE: [3], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.absorption**
- CLAIM: Husk mucilage is minimally absorbed intact; EMA distinguishes local fiber action from uptake of degradation products [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.distribution**
- CLAIM: No conventional whole-husk systemic tissue-distribution profile is established; local luminal action predominates [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.metabolism**
- CLAIM: Limited colonic fermentation produces short-chain fatty acids; do not treat fiber as a CYP-metabolized small-molecule drug [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.excretion**
- CLAIM: Unabsorbed fiber and metabolites pass in feces; a conventional whole-husk elimination half-life is not applicable [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.drug_interactions**
- CLAIM: May delay absorption of other oral medicines. EMA specifies separation and notes supervision with thyroid hormones or motility-inhibiting drugs; diabetes therapy may require review. Interaction severity depends on the medicine [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.toxicity**
- CLAIM: The major acute risks are mechanical obstruction and severe hypersensitivity; sufficient liquid is essential. No maximum safe dose for impaired populations is inferred from trials [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.pregnancy**
- CLAIM: EMA permits consideration when diet change fails, with limited pregnancy data; no claim of established fetal safety [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.lactation**
- CLAIM: EMA allows consideration when needed; specific infant-safety evidence remains limited [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.hepatic_impairment**
- CLAIM: No hepatic dose-adjustment evidence identified for husk; impairment-specific safety is not established by these trials [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.renal_impairment**
- CLAIM: Fluid restrictions and swallowing/obstruction risk require individual clinical assessment; no renal dose-adjustment evidence identified [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for outcome-specific constipation/IBS/lipid findings; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

### Aloe vera — APPROVE AS DRAFT
EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy.

ISSUES / REVISIONS: Removed oral-gel exact amount and unsupported gel-polysaccharide active assignment. Added 2024 burn meta-analysis PMID38605441 as [5], avoiding obsolete implication that 2012 review is the newest burn evidence. New abstract supports narrow healing signal, not preparation-wide safety, pain improvement, infection prevention or all wounds. NCCIH full page supports topical reactions, oral latex cramps/diarrhea, hepatitis association, pregnancy/lactation and digoxin risk. Rodent non-decolorized whole-leaf toxicity is clearly separated from human gel.

SOURCE SUPPORT: Exact indexed abstracts reviewed for clinical narratives; source-local numbered citations below. Safety additionally checked against complete regulatory or NIH text as described above.

RECOMMENDATION: Approve corrected draft for schema review; retain manual scientific review gate. No unresolved blocker to honest draft presentation.

Sources:
- [1] Langmead L, Feakins RM, Goldthorpe S, Holt H, Tsironi E, De Silva A, Jewell DP, Rampton DS. Randomized, double-blind, placebo-controlled trial of oral aloe vera gel for active ulcerative colitis. Alimentary pharmacology & therapeutics 2004. PMID: 15043514. DOI: 10.1111/j.1365-2036.2004.01902.x.
- [2] Dat AD, Poon F, Pham KB, Doust J. Aloe vera for treating acute and chronic wounds. The Cochrane database of systematic reviews 2012. PMID: 22336851. DOI: 10.1002/14651858.cd008762.pub2.
- [3] Lee J, Lee MS, Nam KW. Acute toxic hepatitis caused by an aloe vera preparation in a young patient: a case report with a literature review. The Korean journal of gastroenterology = Taehan Sohwagi Hakhoe chi 2014. PMID: 25073673. DOI: 10.4166/kjg.2014.64.1.54.
- [4] NCCIH. Aloe Vera: Usefulness and Safety. https://www.nccih.nih.gov/health/aloe-vera Accessed 2026-10-25.
- [5] Huang YN, Chen KC, Wang JH, Lin YK. Effects of Aloe vera on Burn Injuries: A Systematic Review and Meta-Analysis of Randomized Controlled Trials. Journal of Burn Care & Research 2024;45:1536–1545. PMID: 38605441. DOI: 10.1093/jbcr/irae061. Abstract reviewed; full-text appraisal pending.

Field-level claim audit (exact reviewed text):

**narrative_summary.historical_use**
- CLAIM: Aloe has documented historical skin and wound use in several ancient medical traditions. Historical use is not evidence that contemporary gel, latex and whole-leaf products have equivalent effects [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.modern_application**
- CLAIM: Draft research profile: aloe gel preparations have been investigated for wounds and oral inflammatory-bowel symptoms, with substantial uncertainty and product differences [1][2][5]. A small 4-week UC trial (44 evaluable participants) found more clinical responses with oral gel than placebo, but clinical remission and sigmoidoscopic findings were not convincingly different [1]. The 2012 wound review found insufficient high-quality evidence [2]. A later review of nine burn RCTs reported shorter healing with aloe preparations, while pain and infection differences were not significant; these burn findings cannot be generalized to all wounds or products [5]. BMS Level C for the exploratory UC signal, provisional B for the narrower burn-healing outcome pending full-text quality appraisal, and U for a firm broad wound-healing conclusion. Gel findings do not support oral latex or whole-leaf products. Pending manual scientific review.
- SOURCE: [1], [2], [5]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.side_effects**
- CLAIM: Topical gel may cause burning, itching or rash. Oral latex causes cramps and diarrhea. Acute hepatitis has been associated with oral aloe preparations, whose exact plant fraction may be unclear [3][4].
- SOURCE: [3], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.contraindications**
- CLAIM: Known aloe hypersensitivity precludes the relevant product. Oral aloe is discouraged in pregnancy and lactation. Gel research must not be generalized to anthranoid-containing latex/whole-leaf laxatives; obstruction or unexplained abdominal symptoms require clinical assessment, not self-treatment [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.used_part**
- CLAIM: Inner-leaf gel in the UC trial and varied topical products in wound research. Latex is the outer-leaf exudate; whole-leaf extracts contain different fractions and require separate safety assessment [1][2][4].
- SOURCE: [1], [2], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[0]**
- CLAIM: Inner-leaf gel is a complex preparation; its clinical constituent standardization is not established in the retrieved trial abstract [1].
- SOURCE: [1]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[1]**
- CLAIM: Aloin is an anthraquinone constituent relevant to oral aloe-product safety; gel, latex and whole-leaf extracts require separate assessment [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.mechanism_of_action**
- CLAIM: <strong>Inflammatory activity</strong> was assessed clinically/histologically in the small gel trial; it does not establish a molecular mechanism. No specific receptor or signaling target is attributed from these clinical sources [1].
- SOURCE: [1]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.absorption**
- CLAIM: Human absorption/bioavailability of the studied whole gel is not characterized in retrieved sources; no intact-polysaccharide systemic exposure assumed [1][4].
- SOURCE: [1], [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.distribution**
- CLAIM: Human tissue distribution of the gel preparation is unknown in this extraction [1][4].
- SOURCE: [1], [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.metabolism**
- CLAIM: Human gel-product metabolic pathways are insufficiently characterized; anthranoid pharmacology cannot be assigned to anthranoid-depleted gel [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.excretion**
- CLAIM: No validated gel-product elimination route or half-life identified in the retrieved literature [1][4].
- SOURCE: [1], [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.drug_interactions**
- CLAIM: NCCIH flags increased cardiac-glycoside adverse-effect risk with latex overuse. This is preparation specific and must not be automatically assigned to topical inner-leaf gel [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.toxicity**
- CLAIM: Oral aloe preparations have been associated with hepatitis [3]. Non-decolorized whole-leaf extracts produced GI tumors in rodents; this is animal evidence and not interchangeable with inner gel or a quantified human cancer risk [4].
- SOURCE: [3], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.pregnancy**
- CLAIM: Oral gel, latex and whole-leaf products may be unsafe during pregnancy per NCCIH; topical pregnancy evidence is insufficiently characterized here [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.lactation**
- CLAIM: Oral aloe may be unsafe while breastfeeding; infant exposure for specific products is inadequately characterized [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.hepatic_impairment**
- CLAIM: Hepatitis reports warrant particular caution with oral products; no validated hepatic adjustment exists in these sources [3][4].
- SOURCE: [3], [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.renal_impairment**
- CLAIM: Renal-impairment safety is inadequately characterized in the selected sources. Diarrhea-producing oral products warrant particular caution because of fluid losses; this is a precautionary inference, not a tested renal dosing rule [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: C for exploratory UC; provisional B for narrow burn-healing endpoint; U for broad wound efficacy; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

### Sabdariffa gossypiifolia — APPROVE AS DRAFT
EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence.

ISSUES / REVISIONS: Clinical publications use Hibiscus sabdariffa; accepted-name reconciliation is the completed taxonomy gate. Removed numeric tea amount while retaining study population/duration. EDA full calyx monograph confirms family hypersensitivity, pregnancy/lactation uncertainty and its perioperative precaution. Interaction alerts are attributed to EDA with underlying studies explicitly unverified; no quantified interaction is asserted. Roselle review/acute full texts support GI events, preclinical ACE/calcium/NO hypotheses and compound-specific phenolic exposure. Removed exact abstract-only PK administration quantity.

SOURCE SUPPORT: Exact indexed abstracts reviewed for clinical narratives; source-local numbered citations below. Safety additionally checked against complete regulatory or NIH text as described above.

RECOMMENDATION: Approve corrected draft for schema review; retain manual scientific review gate. No unresolved blocker to honest draft presentation.

Sources:
- [1] - McKay DL, Chen CY, Saltzman E, Blumberg JB. Hibiscus sabdariffa L. tea (tisane) lowers blood pressure in prehypertensive and mildly hypertensive adults. The Journal of nutrition, 2010. PMID: 20018807. DOI: 10.3945/jn.109.115097
- [2] - Ellis LR, Zulfiqar S, Holmes M, Marshall L, Dye L, Boesch C. A systematic review and meta-analysis of the effects of Hibiscus sabdariffa on blood pressure and cardiometabolic markers. Nutrition reviews, 2022. PMID: 34927694. DOI: 10.1093/nutrit/nuab104
- [3] - Frank T, Janssen M, Netzel M, Netzel M, Netzel M, Strass G, Kler A, Kriesl E, Bitsch I. Pharmacokinetics of anthocyanidin-3-glycosides following consumption of Hibiscus sabdariffa L. extract. Journal of clinical pharmacology, 2005. PMID: 15647413. DOI: 10.1177/0091270004270561
- [4] - Abubakar SM, Ukeyima MT, Spencer JPE, Lovegrove JA. Acute Effects of Hibiscus Sabdariffa Calyces on Postprandial Blood Pressure, Vascular Function, Blood Lipids, Biomarkers of Insulin Resistance and Inflammation in Humans. Nutrients, 2019. PMID: 30764582. DOI: 10.3390/nu11020341
- [5] - Herrera-Arellano A, Flores-Romero S, Chávez-Soto MA, Tortoriello J. Effectiveness and tolerability of a standardized extract from Hibiscus sabdariffa in patients with mild to moderate hypertension: a controlled and randomized clinical trial. Phytomedicine : international journal of phytotherapy and phytopharmacology, 2004. PMID: 15330492. DOI: 10.1016/j.phymed.2004.04.001
- [6] - Egyptian Drug Authority. Egyptian Herbal Monograph, Hibiscus sabdariffa L. 2025 edition; last revision 26 November 2023. https://www.edaegypt.gov.eg/media/vw3ngdwl/hibiscus-sabdariffa-l-%D9%83%D8%B1%D9%83%D8%AF%D9%8A%D9%87.pdf

Field-level claim audit (exact reviewed text):

**narrative_summary.historical_use**
- CLAIM: Roselle calyces, reported in the literature as Hibiscus sabdariffa, are used as sour beverages and in traditional medicine in Africa and Asia; this history is distinct from clinical evidence [2][6].
- SOURCE: [2], [6]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.modern_application**
- CLAIM: Draft research profile: roselle calyx infusions have been studied for blood-pressure outcomes, with substantial preparation and study-quality limitations [1][2]. In a double-blind trial of 65 adults aged 30–70 years with prehypertension or mild hypertension who were not taking blood-pressure medicines, a six-week calyx-tea regimen reduced systolic pressure more than placebo; the diastolic difference was not significant [1]. A review of 17 chronic trials found a systolic-pressure signal but very high heterogeneity (I²=95% in the placebo comparison); this supports a conservative Level B for the studied blood-pressure outcomes, not proven cardiovascular-event prevention or medication equivalence [2]. A 25-man acute crossover study improved flow-mediated dilation without a significant blood-pressure reduction [4]. Pending manual scientific review. Numeric medicinal doses are omitted because product and population details must be assessed together.
- SOURCE: [1], [2], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.side_effects**
- CLAIM: Mild, transient gastrointestinal symptoms were reported in one trial summarized by the review; short trials and incomplete reporting cannot establish long-term safety or rare-event rates [2]. Hypersensitivity is a regulatory contraindication [6].
- SOURCE: [2], [6]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.contraindications**
- CLAIM: Hypersensitivity to roselle or related Malvaceae is listed by EDA [6]. Low blood pressure and concurrent blood-pressure treatment warrant precautionary clinical assessment because additive effects are plausible [2][6]. Medicinal use in children is insufficiently characterized in these sources. EDA includes a precaution to stop two weeks before planned surgery because of possible glucose effects; a clinical perioperative benefit of that interval has not been established [6].
- SOURCE: [6], [2]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.used_part**
- CLAIM: Fleshy red calyces, usually dried and infused in water; tea and concentrated extracts have different constituent exposures. Clinical sources use the synonym Hibiscus sabdariffa [1][5][6].
- SOURCE: [1], [5], [6]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[0]**
- CLAIM: Delphinidin-3-sambubioside (anthocyanin) [2][3]
- SOURCE: [2], [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[1]**
- CLAIM: Cyanidin-3-sambubioside (anthocyanin) [2][3]
- SOURCE: [2], [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[2]**
- CLAIM: Phenolic acids including gallic acid [4]
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[3]**
- CLAIM: Hibiscus acid and related organic acids [6]
- SOURCE: [6]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.mechanism_of_action**
- CLAIM: Animal and in-vitro work summarized in the review investigates <strong>angiotensin-converting enzyme (ACE)</strong>, vascular calcium influx and endothelial nitric-oxide signaling; these hypotheses do not establish clinical ACE inhibition or explain all human effects [2]. Human flow-mediated dilation improved in one small acute trial, but nitric-oxide and blood-pressure changes were not significant [4].
- SOURCE: [2], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.absorption**
- CLAIM: In six healthy volunteers given a single Hibiscus extract, measured intact anthocyanins peaked in plasma at a median 1.5 hours. These abstract-level, compound-specific findings cannot describe absorption of the complete botanical or establish calyx-product dosing [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.distribution**
- CLAIM: Human tissue distribution and protein binding of complete calyx extracts were not established in the selected sources [2][3].
- SOURCE: [2], [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.metabolism**
- CLAIM: A small human crossover trial detected circulating gallic acid and methylated phenolic acids after an aqueous calyx drink; complete metabolic pathways and clinically relevant CYP effects remain unresolved [4].
- SOURCE: [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.excretion**
- CLAIM: In six volunteers, 0.018% of the administered total anthocyanins was recovered as measured intact anthocyanins in urine within seven hours. This is not total recovery of all metabolites; extract-level clearance and impairment adjustments are unknown [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.drug_interactions**
- CLAIM: Additive hypotension with antihypertensive drugs is a precautionary pharmacodynamic concern [2][6]. EDA also flags chloroquine, simvastatin and diabetes medicines, but this extraction has not independently verified the underlying clinical interaction studies; direction and magnitude must not be assumed [6]. A hydrochlorothiazide interaction described in the review was in rats and is not an established human interaction [2].
- SOURCE: [2], [6]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.toxicity**
- CLAIM: No reliable long-term human toxicity threshold is established. Short trial tolerability and animal toxicity results do not establish safety during chronic concentrated-extract use [2].
- SOURCE: [2]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.pregnancy**
- CLAIM: Insufficient human pregnancy safety data; EDA does not recommend medicinal use during pregnancy [6].
- SOURCE: [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.lactation**
- CLAIM: Milk transfer and infant safety are unknown; EDA does not recommend medicinal use during breastfeeding [6].
- SOURCE: [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.hepatic_impairment**
- CLAIM: No validated hepatic-impairment dosing or safety studies identified in the selected sources; concentrated-extract exposure requires individual clinical assessment [2][6].
- SOURCE: [2], [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.renal_impairment**
- CLAIM: No validated renal-impairment dosing data identified in these sources; potential blood-pressure and diuretic effects warrant individualized assessment with concurrent medicines. This is a precautionary inference, not an impairment-specific clinical finding [2][6].
- SOURCE: [2], [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; no event prevention or drug equivalence; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

### Rosa canina — APPROVE AS DRAFT
EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis.

ISSUES / REVISIONS: Removed exact abstract-only powder amount. Manufacturer support and need for independent replication remain prominent. No adverse-event rates, pregnancy reassurance, interaction severity or washout period invented. Pregnancy/lactation text now states source-limited gaps rather than a claimed regulatory prohibition. Lipophilic constituent wording comes directly from review abstract; no specific molecule invented.

SOURCE SUPPORT: Exact indexed abstracts reviewed for clinical narratives; source-local numbered citations below. Safety additionally checked against complete regulatory or NIH text as described above.

RECOMMENDATION: Approve corrected draft for schema review; retain manual scientific review gate. No unresolved blocker to honest draft presentation.

Sources:
- [1] - Christensen R, Bartels EM, Altman RD, Astrup A, Bliddal H. Does the hip powder of Rosa canina (rosehip) reduce pain in osteoarthritis patients?--a meta-analysis of randomized controlled trials. Osteoarthritis and cartilage, 2008. PMID: 18407528. DOI: 10.1016/j.joca.2008.03.001
- [2] - Winther K, Apel K, Thamsborg G. A powder made from seeds and shells of a rose-hip subspecies (Rosa canina) reduces symptoms of knee and hip osteoarthritis: a randomized, double-blind, placebo-controlled clinical trial. Scandinavian journal of rheumatology, 2005. PMID: 16195164. DOI: 10.1080/03009740510018624
- [3] - Chrubasik C, Roufogalis BD, Müller-Ladner U, Chrubasik S. A systematic review on the Rosa canina effect and efficacy profiles. Phytotherapy research : PTR, 2008. PMID: 18384191. DOI: 10.1002/ptr.2400
- [4] - Chrubasik C, Duke RK, Chrubasik S. The evidence for clinical efficacy of rose hip and seed: a systematic review. Phytotherapy research : PTR, 2006. PMID: 16395741. DOI: 10.1002/ptr.1729

Field-level claim audit (exact reviewed text):

**narrative_summary.historical_use**
- CLAIM: Rose hip, seed and combined hip-and-seed preparations are described as traditional medicinal materials in the pharmacological review. Their different composition and preparation should be distinguished; traditional use is not proof of clinical benefit [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.modern_application**
- CLAIM: Draft research profile: a particular rosehip seed-and-husk powder has been investigated for osteoarthritis pain, with small manufacturer-supported studies limiting confidence [1][2]. A meta-analysis of three trials (287 participants; median duration three months) found a small pain-score benefit, but all trials were supported by the same manufacturer and independent replication was requested [1]. A double-blind crossover study enrolled 94 patients with hip or knee osteoarthritis and compared seed-and-husk powder with placebo for three months per period [2]. Evidence is provisionally Level B for pain outcomes with that studied preparation, not all rosehip teas, oils, species mixtures or products. Other uses remain insufficiently established [3][4]. Pending manual scientific review. Full-text quality appraisal remains pending; no numeric dose is given.
- SOURCE: [1], [2], [3], [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.side_effects**
- CLAIM: Adverse-event frequencies, rare events and long-term safety are not established by the accessible abstracts. The meta-analysis specifically calls for further efficacy and safety evaluation [1]. Absence of a detailed adverse-event table in an abstract is not absence of adverse effects [1][2].
- SOURCE: [1], [2]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.contraindications**
- CLAIM: Known hypersensitivity to the product is a precautionary reason to avoid exposure. Other specific contraindications, pediatric safety and perioperative washout intervals could not be established from the selected sources; no validated interval is proposed [1][3].
- SOURCE: [1], [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.used_part**
- CLAIM: The clinical evidence concerns powder made from the seeds and shells/husks of a Rosa canina subspecies. Seed oil, seed-free hip material, teas and multi-species rosehip blends are not interchangeable with this powder [2][3].
- SOURCE: [2], [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[0]**
- CLAIM: Lipophilic constituents investigated in rosehip/seed pharmacology; specific clinical standardization not established in the accessible abstracts [3]
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.mechanism_of_action**
- CLAIM: The pharmacological review describes antioxidant and anti-inflammatory effects involving <strong>lipophilic constituents</strong> in experimental preparations. A clinically established receptor or enzyme target and proof that these mechanisms cause pain changes are lacking; mechanistic evidence must not be equated with disease modification [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.absorption**
- CLAIM: Human absorption parameters for the studied complete powder were not established in the selected sources [1][3].
- SOURCE: [1], [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.distribution**
- CLAIM: Human tissue distribution and protein binding for the studied powder were not established [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.metabolism**
- CLAIM: Human metabolite and clinically meaningful CYP interaction profiles for the studied powder were not established [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.excretion**
- CLAIM: Human clearance, half-life and renal/biliary recovery of the complete powder were not established [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.drug_interactions**
- CLAIM: No clinically quantified herb–drug interaction or validated CYP interaction profile was established in the selected sources. This is an evidence gap rather than proof of no interaction; concurrent medication and product composition require individual assessment [1][3].
- SOURCE: [1], [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.toxicity**
- CLAIM: Long-term toxicity, rare hepatic or renal events and maximum tolerable exposure are unresolved. The three-trial pain meta-analysis does not establish broad safety of other rosehip preparations [1].
- SOURCE: [1]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.pregnancy**
- CLAIM: Pregnancy safety for the studied medicinal powder could not be established from the selected sources; this is an evidence gap, not proof of fetal safety or harm [1][3].
- SOURCE: [1], [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.lactation**
- CLAIM: Milk transfer and infant safety for the studied medicinal powder could not be established from the selected sources; an evidence-based safety recommendation cannot be made here [1][3].
- SOURCE: [1], [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.hepatic_impairment**
- CLAIM: No hepatic-impairment study or validated dose adjustment was identified in the selected sources [1][3].
- SOURCE: [1], [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.renal_impairment**
- CLAIM: No renal-impairment study or validated dose adjustment was identified in the selected sources [1][3].
- SOURCE: [1], [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for product-specific pain outcome; no A upgrade despite meta-analysis; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

### Pelargonium sidoides — APPROVE AS DRAFT
EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use.

ISSUES / REVISIONS: Full EMA revision 2 (2024) checked: under three oral use not recommended; dry-extract preparations b/c under six require liquid finished dosage forms. Clarified this distinction and one-week medical-review trigger. Added manufacturer links to the later meta-analysis. Current EMA hepatitis/hepatotoxicity and bleeding warnings retained despite disputed case causality. Full-text 2026 surveillance is manufacturer sponsored and symptom based; exact regimen removed, seven-day horizon retained without rare/delayed/asymptomatic reassurance. Mechanisms remain preclinical.

SOURCE SUPPORT: Exact indexed abstracts reviewed for clinical narratives; source-local numbered citations below. Safety additionally checked against complete regulatory or NIH text as described above.

RECOMMENDATION: Approve corrected draft for schema review; retain manual scientific review gate. No unresolved blocker to honest draft presentation.

Sources:
- [1] - Timmer A, Günther J, Motschall E, Rücker G, Antes G, Kern WV. Pelargonium sidoides extract for treating acute respiratory tract infections. The Cochrane database of systematic reviews, 2013. PMID: 24146345. DOI: 10.1002/14651858.cd006323.pub3
- [2] - Willcox M, Simpson C, Wilding S, Stuart B, Soilemezi D, Whitehead A, Morgan A, Wrixon E, Zhu S, Yao G, Webley F, Yan R, Bostock J, Bell M, Griffiths G, Leydon G, Little P, Butler C, Hay AD, Moore M. Pelargonium sidoides root extract for the treatment of acute cough due to lower respiratory tract infection in adults: a feasibility double-blind, placebo-controlled randomised trial. BMC complementary medicine and therapies, 2021. PMID: 33514367. DOI: 10.1186/s12906-021-03206-4
- [3] - Kardos P, Lehmacher W, Zimmermann A, Brandes-Schramm J, Funk P, Matthys H, Kamin W. Effects of Pelargonium sidoides extract EPs 7630 on acute cough and quality of life - a meta-analysis of randomized, placebo-controlled trials. Multidisciplinary respiratory medicine, 2022. PMID: 36051888. DOI: 10.4081/mrm.2022.868
- [4] - Teschke R, Frenzel C, Schulze J, Eickhoff A. Spontaneous reports of primarily suspected herbal hepatotoxicity by Pelargonium sidoides: was causality adequately ascertained? Regulatory toxicology and pharmacology : RTP, 2012. PMID: 22381150. DOI: 10.1016/j.yrtph.2012.02.009
- [5] - Alvero RGY, Balmadrid AS, Aquino RCC, Balaccua GP. Short-term Liver Safety of <i>Pelargonium sidoides</i> DC. Root (PELARGO) 20 mg Capsule: A Non-interventional Post-authorization Safety Study. Acta medica Philippina, 2026. PMID: 41890334. DOI: 10.47895/amp.vi0.12322
- [6] - EMA/HMPC. European Union herbal monograph on Pelargonium sidoides DC; Pelargonium reniforme Curt., radix. Final revision 2, 29 May 2024. https://www.ema.europa.eu/en/documents/herbal-monograph/final-european-union-herbal-monograph-pelargonium-sidoides-dc-pelargonium-reniforme-curt-radix-revision-2_en.pdf

Field-level claim audit (exact reviewed text):

**narrative_summary.historical_use**
- CLAIM: Pelargonium root preparations have a documented tradition of use for respiratory complaints; the EMA common-cold indication is based on long-standing traditional use, rather than a finding of well-established clinical efficacy. The EMA monograph covers P. sidoides and/or P. reniforme [1][6].
- SOURCE: [1], [6]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.modern_application**
- CLAIM: Draft research profile: proprietary Pelargonium root extracts have been investigated for acute cough and respiratory symptoms, but certainty and formulation differences remain substantial [1][2][3]. The Cochrane review judged evidence low for acute bronchitis and very low for common cold or sinusitis, with suspected publication bias and differences between liquids and tablets [1]. A later meta-analysis of 11 EPs 7630 trials (2195 participants) reported cough improvement; the authors include manufacturer employees or paid consultants, and the analysis does not remove the limitations or establish interchangeability with other products [3]. A UK feasibility trial recruited 134 adults and demonstrated recruitment feasibility rather than definitive efficacy [2]. Archive classification is Level U for a firm clinical efficacy conclusion and Level T for EMA traditional common-cold use [1][6]. Pending manual scientific review. Study regimens describe research exposure and are not dosing advice.
- SOURCE: [1], [2], [3], [6]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.side_effects**
- CLAIM: EMA 2024 lists gastrointestinal complaints, nasal or gum bleeding, hypersensitivity including anaphylaxis, rash, pruritus, urticaria, angioedema, hepatitis and hepatotoxicity, with frequency unknown [6]. The Cochrane trials reported more adverse events with extract than placebo, without serious events in those trials [1]. Liver causality remains disputed: a case reassessment found none of 15 reports probable or highly probable, but this does not negate current regulatory warnings [4][6].
- SOURCE: [6], [1], [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.contraindications**
- CLAIM: Hypersensitivity is an EMA contraindication. Signs of liver injury require stopping the product and medical assessment [6]. The 2024 monograph does not recommend oral use below age three. For its dry-extract preparations b) and c), children under six should receive only liquid dosage forms; a dry extract and a solid finished dosage form are different concepts. Symptoms persisting longer than one week or worsening require medical advice [6]. No evidence-based perioperative washout interval was established in this extraction.
- SOURCE: [6]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.used_part**
- CLAIM: Root; clinical findings mainly concern proprietary EPs 7630 liquid/dry extracts. EMA describes defined ethanol-extracted preparations and also covers P. reniforme, so genus-level and mixed-species preparations cannot be assumed equivalent to P. sidoides trial material [2][3][6].
- SOURCE: [2], [3], [6]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[0]**
- CLAIM: Root extract is a mixture; no single clinically proven active constituent accounts for the symptom findings [1][3]
- SOURCE: [1], [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.mechanism_of_action**
- CLAIM: Experimental work summarized by the EPs 7630 review investigates host-defense signaling, including <strong>interferon</strong> and <strong>tumor necrosis factor</strong>, alongside antiviral and mucociliary effects. These are primarily preclinical hypotheses; they do not establish antiviral treatment efficacy, prevention of complications or a clinically validated molecular target [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.absorption**
- CLAIM: Human constituent-specific absorption and absolute bioavailability were not established in the selected clinical sources; EMA traditional-use monograph does not provide pharmacokinetic parameters [1][6].
- SOURCE: [1], [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.distribution**
- CLAIM: Human tissue distribution and protein binding of whole root extracts remain insufficiently characterized in the selected sources [6].
- SOURCE: [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.metabolism**
- CLAIM: Complete human metabolic pathways and clinically relevant CYP effects were not established in the selected sources [6].
- SOURCE: [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.excretion**
- CLAIM: Validated whole-extract half-life, renal clearance and impairment adjustments are unavailable in the selected sources [6].
- SOURCE: [6]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.drug_interactions**
- CLAIM: EMA reports no interactions, which is not proof that all combinations are safe [6]. Nasal and gingival bleeding are reported adverse reactions; a clinically quantified interaction with anticoagulants or antiplatelets was not established in this extraction. Medication review remains prudent [6].
- SOURCE: [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.toxicity**
- CLAIM: Hepatitis and hepatotoxicity reports remain in current EMA warnings even though causality was not substantiated in one reassessment [4][6]. A manufacturer-sponsored, non-interventional 2026 study enrolled 300 adults (298 completing) and reported no clinical signs of liver injury after a seven-day PELARGO capsule course. Short follow-up and symptom-based surveillance cannot rule out rare, delayed or asymptomatic injury [5]. Product-specific findings cannot establish long-term safety of all root extracts.
- SOURCE: [4], [6], [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.pregnancy**
- CLAIM: Safety in pregnancy is not established and EMA does not recommend medicinal use [6].
- SOURCE: [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.lactation**
- CLAIM: Milk transfer and infant safety are unknown; EMA does not recommend medicinal use during breastfeeding [6].
- SOURCE: [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.hepatic_impairment**
- CLAIM: No validated impairment adjustment identified. Reported hepatitis/hepatotoxicity warrants particular caution in existing liver disease and immediate medical assessment of possible liver-injury symptoms [6].
- SOURCE: [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.renal_impairment**
- CLAIM: No validated renal-impairment adjustment or adequate disease-specific safety data identified in selected sources [6].
- SOURCE: [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: U for firm efficacy conclusion; T for current EMA common-cold use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

### Linum usitatissimum — APPROVE AS DRAFT
EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use.

ISSUES / REVISIONS: Removed exact abstract-only flaxseed amounts and avoided inconsistent trial sample size PMID34119421. High meta-analysis heterogeneity retained. Full EMA supports mucilage mechanism, bowel contraindications, obstruction/fluid risk, hormone-dependent tumour caution, medicine separation and pregnancy/lactation uncertainty. SDG PK abstract supports the stated compound-specific timing/half-lives, not whole seed or oil exposure. NCCIH anticoagulant concern explicitly theoretical.

SOURCE SUPPORT: Exact indexed abstracts reviewed for clinical narratives; source-local numbered citations below. Safety additionally checked against complete regulatory or NIH text as described above.

RECOMMENDATION: Approve corrected draft for schema review; retain manual scientific review gate. No unresolved blocker to honest draft presentation.

Sources:
- [1] - Li L, Li H, Gao Y, Vafaei S, Zhang X, Yang M. Effect of flaxseed supplementation on blood pressure: a systematic review, and dose-response meta-analysis of randomized clinical trials. Food & function, 2023. PMID: 36622248. DOI: 10.1039/d2fo02566c
- [2] - Ursoniu S, Sahebkar A, Andrica F, Serban C, Banach M, Lipid and Blood Pressure Meta-analysis Collaboration (LBPMC) Group. Effects of flaxseed supplements on blood pressure: A systematic review and meta-analysis of controlled clinical trial. Clinical nutrition (Edinburgh, Scotland), 2016. PMID: 26071633. DOI: 10.1016/j.clnu.2015.05.012
- [3] - Setchell KD, Brown NM, Zimmer-Nechemias L, Wolfe B, Jha P, Heubi JE. Metabolism of secoisolariciresinol-diglycoside the dietary precursor to the intestinally derived lignan enterolactone in humans. Food & function, 2014. PMID: 24429845. DOI: 10.1039/c3fo60402k
- [4] - Toulabi T, Yarahmadi M, Goudarzi F, Ebrahimzadeh F, Momenizadeh A, Yarahmadi S. Effects of flaxseed on blood pressure, body mass index, and total cholesterol in hypertensive patients: A randomized clinical trial. Explore (New York, N.Y.), 2022. PMID: 34119421. DOI: 10.1016/j.explore.2021.05.003
- [5] - EMA/HMPC. European Union herbal monograph on Linum usitatissimum L., semen. 10 March 2015. https://www.ema.europa.eu/en/documents/herbal-monograph/final-community-herbal-monograph-linum-usitatissimum-l-semen_en.pdf
- [6] - NCCIH. Flaxseed and Flaxseed Oil. Accessed 25 October 2026. https://www.nccih.nih.gov/health/flaxseed-and-flaxseed-oil

Field-level claim audit (exact reviewed text):

**narrative_summary.historical_use**
- CLAIM: Linseed has long been used as a bulk-forming laxative; EMA distinguishes well-established use of seed for habitual constipation from traditional demulcent use for mild gastrointestinal discomfort [5].
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.modern_application**
- CLAIM: Draft research profile: flaxseed products have been studied for bowel function and blood-pressure outcomes, with seed, oil and lignan extracts representing different interventions [1][2][5]. A 2023 meta-analysis of 33 trials (2427 participants) reported modest pooled blood-pressure reductions but very high heterogeneity (I² above 92%); the archive uses conservative Level B for the studied pressure outcomes rather than generalizing to every product [1]. An earlier analysis also found formulation-dependent results [2]. EMA recognizes seed as a bulk laxative, while demulcent use is traditional (Level T); regulatory well-established use is not itself an archive Level A clinical-trial score [5]. A separate triple-blind trial studied flaxseed regimens for 12 weeks, but its abstract gives inconsistent participant totals, so it is not used for a precise sample-size or effect claim [4]. Pending manual scientific review. No numeric medicinal dose is given here.
- SOURCE: [1], [2], [5], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.side_effects**
- CLAIM: EMA lists flatulence as common and hypersensitivity including anaphylaxis-like reactions as very rare. Insufficient fluid can cause choking, oesophageal blockage or intestinal obstruction; excessive seed exposure can cause abdominal discomfort and flatulence [5]. NCCIH also notes bloating, fullness and diarrhea with higher exposures [6].
- SOURCE: [5], [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.contraindications**
- CLAIM: EMA contraindicates hypersensitivity, swallowing/throat disorders, intestinal narrowing or obstruction/ileus, megacolon and certain unexplained bowel symptoms, including rectal bleeding or persistent sudden bowel-habit changes. Medicinal use under age 12 is not recommended; EMA also cautions against use in women with hormone-dependent tumours [5]. A validated perioperative washout interval was not identified.
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.used_part**
- CLAIM: Dried ripe seeds, whole/broken or milled, and seed mucilage. Seed oil lacks the same bulk-forming fibre exposure; purified lignan extracts have a separate pharmacokinetic and safety evidence base [3][5][6].
- SOURCE: [3], [5], [6]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[0]**
- CLAIM: Mucilage polysaccharides and dietary fibre [5]
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[1]**
- CLAIM: Secoisolariciresinol diglycoside (SDG; lignan) [3]
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[2]**
- CLAIM: Alpha-linolenic acid in seed oil [6]
- SOURCE: [6]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.mechanism_of_action**
- CLAIM: For bowel effects, <strong>water-binding mucilage</strong> increases intestinal content volume and softens stool, with stretch-related effects on transit; this is a local bulk mechanism described by EMA, not a receptor-specific systemic action [5]. Blood-pressure mechanisms are not conclusively assigned to a single constituent in the human meta-analyses [1][2].
- SOURCE: [5], [1], [2]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.absorption**
- CLAIM: In healthy postmenopausal women given purified flax lignan extracts, secoisolariciresinol peaked at approximately 5–7 hours; enterodiol and enterolactone appeared later. These results describe SDG-derived compounds, not whole-seed mucilage or seed oil [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.distribution**
- CLAIM: Human tissue distribution of complete seed products was not established in the selected sources; purified-lignan serum exposure does not establish all tissue concentrations [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.metabolism**
- CLAIM: SDG is hydrolyzed to secoisolariciresinol and converted by intestinal bacteria to enterodiol and enterolactone [3]. Some seed bulk material is fermented to short-chain fatty acids while some is passed in stool [5].
- SOURCE: [3], [5]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.excretion**
- CLAIM: Human SDG studies measured urinary lignans and reported approximate serum half-lives of 4.8 hours for secoisolariciresinol, 9.4 hours for enterodiol and 13.2 hours for enterolactone; these cannot define whole-seed clearance or impairment dosing [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.drug_interactions**
- CLAIM: EMA warns that linseed can delay intestinal absorption of medicines and specifies separation of at least half to one hour. Co-use with motility-suppressing medicines such as opioids or loperamide requires medical supervision because of obstruction risk [5]. NCCIH describes anticoagulant/antiplatelet interactions as theoretical, not established clinical bleeding interactions [6].
- SOURCE: [5], [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.toxicity**
- CLAIM: NCCIH advises against eating raw or unripe seeds because of potentially toxic constituents; seed preparation matters [6]. EMA identifies obstruction risk when fluid intake is inadequate and incomplete reproductive/genotoxicity/carcinogenicity testing. No universal long-term toxicity threshold can be inferred from short supplementation trials [5][6].
- SOURCE: [6], [5]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.pregnancy**
- CLAIM: Medicinal pregnancy safety is not established and EMA does not recommend use; NCCIH notes inconclusive possible pregnancy risk. This does not equate medicinal preparations with ordinary food exposure [5][6].
- SOURCE: [5], [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.lactation**
- CLAIM: Milk transfer and infant safety are insufficiently characterized; EMA does not recommend medicinal use while breastfeeding [5][6].
- SOURCE: [5], [6]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.hepatic_impairment**
- CLAIM: No validated hepatic-impairment adjustment for medicinal seed or lignan extract was established in the selected sources [3][5].
- SOURCE: [3], [5]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.renal_impairment**
- CLAIM: No validated renal-impairment adjustment is established. Fluid-dependent bulk use requires individual assessment when fluid intake is restricted; this is a precaution rather than a tested dosing rule [5].
- SOURCE: [5]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for blood-pressure surrogate; EMA well-established seed laxative use distinct from T demulcent use; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

### Aesculus hippocastanum — APPROVE AS DRAFT
EVIDENCE LEVEL: Provisional B for short-term venous symptoms.

ISSUES / REVISIONS: Removed abstract-only exact aescin amount. Full EMA supports venous tone/capillary filtration, raw-versus-standardized product distinction, warnings, absent relevant PK, unknown AE frequencies and pregnancy/lactation caution. No thrombosis-prevention claim or universal compression equivalence. NCCIH full safety page confirms raw-part toxicity and distinction from standardized extracts.

SOURCE SUPPORT: Exact indexed abstracts reviewed for clinical narratives; source-local numbered citations below. Safety additionally checked against complete regulatory or NIH text as described above.

RECOMMENDATION: Approve corrected draft for schema review; retain manual scientific review gate. No unresolved blocker to honest draft presentation.

Sources:
- [1] - Pittler MH, Ernst E. Horse chestnut seed extract for chronic venous insufficiency. The Cochrane database of systematic reviews, 2012. PMID: 23152216. DOI: 10.1002/14651858.cd003230.pub4
- [2] - Diehm C, Trampisch HJ, Lange S, Schmidt C. Comparison of leg compression stocking and oral horse-chestnut seed extract therapy in patients with chronic venous insufficiency. Lancet (London, England), 1996. PMID: 8569363. DOI: 10.1016/s0140-6736(96)90467-5
- [3] - EMA/HMPC. European Union herbal monograph on Aesculus hippocastanum L., semen. Final revision 1, 15 January 2020. https://www.ema.europa.eu/en/documents/herbal-monograph/european-union-herbal-monograph-aesculus-hippocastanum-l-semen-final-revision-1_en.pdf
- [4] - NCCIH. Horse Chestnut. Accessed 25 October 2026. https://www.nccih.nih.gov/health/horse-chestnut

Field-level claim audit (exact reviewed text):

**narrative_summary.historical_use**
- CLAIM: Horse chestnut seed extracts have been traditionally used for pain, swelling and other complaints. EMA distinguishes specific standardized oral extracts with well-established use in venous insufficiency from traditional oral/topical preparations for minor venous complaints or bruises [3][4].
- SOURCE: [3], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.modern_application**
- CLAIM: Draft research profile: standardized horse chestnut seed extracts have been studied for short-term venous-insufficiency symptoms, with larger and longer rigorous trials still needed [1]. A Cochrane review of 17 trials found signals for reduced leg pain and leg volume but emphasized caveats [1][3]. A randomized, partially blinded 12-week trial of 240 adults compared a dried seed extract with compression stockings and placebo; leg-volume findings do not establish prevention of thrombosis or equivalence for every clinical outcome [2]. Provisional archive Level B applies to studied short-term venous symptoms. Raw seeds and other raw parts are toxic and are not the tested preparations [4]. Pending manual scientific review. No numeric medicinal dose is given here.
- SOURCE: [1], [3], [2], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.side_effects**
- CLAIM: Standardized oral seed extracts may cause gastrointestinal complaints, headache, vertigo/dizziness, itching or allergic reactions; EMA gives frequency as unknown. Topical preparations may cause skin hypersensitivity [3][4]. Short-term trial tolerability cannot exclude rare or delayed adverse events [1].
- SOURCE: [3], [4], [1]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**narrative_summary.contraindications**
- CLAIM: Hypersensitivity is an EMA contraindication. Sudden leg swelling, severe pain, thrombophlebitis, ulcers, skin inflammation or possible cardiac/renal insufficiency require medical evaluation rather than self-treatment [3]. Oral venous-use preparations are not recommended below age 18 in the EMA monograph. Raw seed, leaf, bark and flower ingestion must be avoided [3][4]. No validated perioperative washout interval was established.
- SOURCE: [3], [4]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.used_part**
- CLAIM: Seed-derived standardized extracts used in clinical trials; not raw seeds, bark, leaves or flowers. EMA standardized extracts specify constituent assay and extraction solvent, so older aescin values and newer protoaescigenin-based values should not be casually interchanged [1][3][4].
- SOURCE: [1], [3], [4]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.primary_active_compounds[0]**
- CLAIM: Aescin/escin (mixture of triterpene saponins in standardized seed extracts) [1][2][3]
- SOURCE: [1], [2], [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.mechanism_of_action**
- CLAIM: The exact mechanism is unknown. EMA describes preclinical and clinical pharmacological evidence involving <strong>venous tone</strong> and <strong>capillary filtration</strong>; these are pharmacological processes rather than established single molecular targets, and symptom evidence does not imply antithrombotic efficacy [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.absorption**
- CLAIM: Relevant human absorption parameters for the specified whole extract are not supplied by the EMA monograph; formulation-specific bioavailability cannot be inferred from symptom trials [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.distribution**
- CLAIM: Human tissue distribution and protein binding for complete standardized extracts were not established in the selected sources [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.metabolism**
- CLAIM: Complete human metabolic pathways and clinically relevant CYP effects were not established in selected sources [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.pharmacokinetics.excretion**
- CLAIM: Reliable extract-level renal/biliary recovery, half-life and impairment adjustment were not established in the selected sources [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.drug_interactions**
- CLAIM: EMA reports no interactions for the defined preparations; this is not proof that all products or drug combinations lack interactions. A clinically quantified anticoagulant or CYP interaction was not established in the selected sources, so no severity grade or washout interval is invented [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.safety_and_interactions.toxicity**
- CLAIM: Raw seeds, bark, flowers and leaves contain a toxic component and are unsafe for oral use. NCCIH distinguishes these from standardized seed extracts in which that component has been removed [4]. The evidence concerns short exposures, often no longer than 12 weeks; reproductive, genotoxicity and carcinogenicity testing is incomplete and long-term human toxicity remains uncertain [3][4].
- SOURCE: [4], [3]
- SOURCE SUPPORTS CLAIM: Yes, as scoped; study findings, regulatory attribution and precautionary interpretation remain distinct.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.pregnancy**
- CLAIM: Pregnancy safety is not established; EMA does not recommend use [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.lactation**
- CLAIM: Milk transfer and infant safety are unknown; EMA does not recommend use during breastfeeding [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.hepatic_impairment**
- CLAIM: No validated hepatic-impairment dose adjustment or adequate disease-specific safety data identified; individualized assessment is required [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

**clinical_data.special_precautions.renal_impairment**
- CLAIM: EMA specifically calls for medical evaluation in renal insufficiency or unexplained leg oedema; no validated renal dosing adjustment is established [3].
- SOURCE: [3]
- SOURCE SUPPORTS CLAIM: Partially / selected-source limitation: retained only as an explicit uncertainty, not an affirmative proof of absence.
- EVIDENCE LEVEL: Provisional B for short-term venous symptoms; regulatory safety / PK / preclinical evidence assessed separately from efficacy.
- RECOMMENDATION: Approve corrected draft wording.

## Checks run

- Parsed both proposed-entry JSON files; confirmed ten distinct accepted names and ten visible draft/manual-review statements.
- Checked numbered scientific citations against each entry reference count and verified additional PMID/DOI metadata.
- Reviewed A study extraction, B ledger and parent supplemental records; full-text gaps retained.
- Examined every narrative and clinical-data field in the exact corrected proposals.

## Checks not run

- No clinical examination, exhaustive systematic update, independent manual scientific approval or complete full-text appraisal of every cited trial.
- No production/deployment checks, schema integration or browser QA (assigned to later gates).

## Changed files

- docs/research/plant-batch-2026-10-25-a/proposed-entries.json
- docs/research/plant-batch-2026-10-25-b/proposed-entries.json
- docs/research/plant-batch-2026-10-25-scientific-review.md
