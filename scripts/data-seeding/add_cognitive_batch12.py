#!/usr/bin/env python3
"""Batch 12 - add cognitive-enhancement plant monographs.

Adds six evidence-screened cognitive research entries:
Salvia officinalis, Crocus sativus, Paullinia cupana, Theobroma cacao,
Polygala tenuifolia, and Huperzia serrata.
"""
import json

DATA_FILE = "data.json"

NEW_ENTRIES = [
    {
        "scientific_name": "Salvia officinalis",
        "common_name": "Common Sage / Garden Sage",
        "type": "Plant",
        "article_count": 1161,
        "primary_categories": [
            "Cognitive Function Research",
            "Cholinergic Research",
            "Neurological & Cognitive Research",
            "Oxidative Stress Research",
        ],
        "sources": {
            "top_studies_urls": [
                "https://pubmed.ncbi.nlm.nih.gov/12605619/",
                "https://pubmed.ncbi.nlm.nih.gov/24836739/",
                "https://pubmed.ncbi.nlm.nih.gov/18350281/",
                "https://pubmed.ncbi.nlm.nih.gov/27888449/",
                "https://pubmed.ncbi.nlm.nih.gov/33466627/",
            ],
            "cited_references": [
                "[1] - Akhondzadeh S et al. Salvia officinalis extract in the treatment of patients with mild to moderate Alzheimer's disease: a double blind, randomized and placebo-controlled trial. J Clin Pharm Ther, 2003. PMID: 12605619",
                "[2] - Miroddi M et al. Systematic review of clinical trials assessing pharmacological properties of Salvia species on memory, cognitive impairment and Alzheimer's disease. CNS Neurosci Ther, 2014. PMID: 24836739",
                "[3] - Scholey AB et al. An extract of Salvia (sage) with anticholinesterase properties improves memory and attention in healthy older volunteers. Psychopharmacology (Berl), 2008. PMID: 18350281",
                "[4] - Lopresti AL. Salvia (Sage): A Review of its Potential Cognitive-Enhancing and Protective Effects. Drugs R D, 2017. PMID: 27888449",
                "[5] - Wightman EL et al. The Acute and Chronic Cognitive Effects of a Sage Extract: A Randomized, Placebo Controlled Study in Healthy Humans. Nutrients, 2021. PMID: 33466627",
            ],
        },
        "narrative_summary": {
            "historical_use": "Common sage is a Mediterranean Lamiaceae herb used in European, Middle Eastern, and monastic herbal traditions as a culinary aromatic and as a traditional preparation for digestion, sweating, mouth and throat complaints, and memory-related folk uses. Historical uses are ethnobotanical and do not establish clinical efficacy for cognition.",
            "modern_application": "Human research on common sage is centered on cholinergic and cognitive outcomes. A small double-blind randomized placebo-controlled trial in mild-to-moderate Alzheimer's disease reported improvements on ADAS-cog and CDR-SB over 4 months using Salvia officinalis extract [1]. A systematic review of Salvia clinical trials found preliminary support for memory and cognitive outcomes, but emphasized small sample sizes, heterogeneous preparations, and limited replication [2]. Acute studies in healthy older adults reported memory and attention effects with anticholinesterase Salvia extracts [3]. A later healthy-adult trial used a proprietary combination of S. officinalis and S. lavandulaefolia, so those findings should not be attributed to S. officinalis alone [5].",
            "side_effects": "In the Alzheimer's disease RCT, adverse-event frequency was not greater than placebo and agitation was reported more often in the placebo group [1]. Broader Salvia tolerability concerns include gastrointestinal discomfort, dizziness, headache, and allergic reactions in susceptible individuals. Essential-oil or high-thujone preparations are not equivalent to the leaf extracts studied for cognition and may carry higher neurologic risk at excessive doses.",
            "contraindications": "Avoid medicinal-dose preparations in known hypersensitivity to Salvia or other Lamiaceae plants. Use caution with cholinesterase inhibitors or anticholinergic medications because Salvia extracts can inhibit acetylcholinesterase in vitro and in clinical pharmacology contexts [2][3]. Essential-oil products and concentrated high-thujone preparations should be avoided in seizure disorders and during pregnancy unless specifically supervised; cognition trials do not establish use in these populations.",
        },
        "clinical_data": {
            "used_part": "Leaf and aerial leaf extract; some cognition studies use standardized hydroalcoholic or anticholinesterase Salvia extracts. Combination products with Salvia lavandulaefolia must be treated separately.",
            "primary_active_compounds": [
                "Rosmarinic acid",
                "Carnosic acid",
                "Carnosol",
                "1,8-cineole",
                "Alpha-thujone and beta-thujone",
                "Ursolic acid",
                "Flavonoids including luteolin and apigenin derivatives",
            ],
            "mechanism_of_action": "Cognitive research focuses on cholinergic modulation, especially inhibition of <strong>acetylcholinesterase</strong>, which is pharmacologically relevant to attention and memory but remains preparation-dependent [2][3]. Polyphenols such as rosmarinic acid and carnosic acid are investigated for antioxidant effects through <strong>Nrf2</strong> signaling and for suppression of inflammatory pathways such as <strong>NF-kB</strong> in preclinical models [4]. Monoterpenes in sage essential oil may contribute to central nervous system activity, but essential-oil chemistry differs from the leaf extracts used in most cognition trials [2][4].",
            "pharmacokinetics": {
                "absorption": "No comprehensive human pharmacokinetic profile is available for Salvia officinalis leaf extract as a whole. Rosmarinic acid and lipophilic diterpenes such as carnosic acid are orally absorbed to varying degrees, while volatile monoterpenes have faster absorption when used as essential-oil preparations; cognition trials do not provide a complete ADME dataset [2][4].",
                "distribution": "Human tissue-distribution data for standardized Salvia officinalis extracts are not established. Lipophilic monoterpenes and diterpenes are expected to distribute into lipid-rich tissues, whereas phenolic acids circulate largely as conjugated metabolites; direct blood-brain distribution data for the complete extract are insufficient [4].",
                "metabolism": "Phenolic constituents undergo phase II conjugation, including glucuronidation, sulfation, and methylation. Monoterpenes and diterpenes are expected to undergo hepatic oxidative metabolism; clinically meaningful CYP450 interaction data for Salvia officinalis cognition extracts are not established [4].",
                "excretion": "Conjugated phenolic metabolites are eliminated primarily in urine and bile. Elimination half-lives for the complete extract and for cognition-relevant active fractions are not established in humans [4].",
            },
            "safety_and_interactions": {
                "drug_interactions": "Potential pharmacodynamic interaction with cholinesterase inhibitors, anticholinergic drugs, sedatives, and seizure-threshold-lowering drugs should be considered because anticholinesterase activity and thujone-containing essential-oil chemistry are documented for Salvia preparations [2][3][4]. No clinically graded interaction trials for Salvia officinalis cognition extracts were identified.",
                "toxicity": "Leaf extracts used in short clinical studies were generally tolerated, but long-term controlled tolerability data are limited [1][2]. Concentrated essential oil is not interchangeable with leaf extract; thujone-rich oils can produce neurotoxicity at excessive exposure, including seizure risk, based on broader toxicology literature summarized in reviews [4].",
            },
            "special_precautions": {
                "pregnancy": "Insufficient human data for medicinal-dose Salvia officinalis extracts during pregnancy. Avoid concentrated extracts and essential-oil preparations as a precaution.",
                "lactation": "Insufficient data on excretion of Salvia constituents into human milk. Avoid medicinal-dose preparations during lactation unless supervised.",
                "hepatic_impairment": "No formal studies in hepatic impairment. Because volatile and phenolic constituents undergo hepatic metabolism, use caution in severe liver disease.",
                "renal_impairment": "No formal studies in renal impairment. Phenolic metabolites are partly renally eliminated; no dose-adjustment guidance has been established.",
            },
        },
    },
    {
        "scientific_name": "Crocus sativus",
        "common_name": "Saffron / Saffron Crocus",
        "type": "Plant",
        "article_count": 1460,
        "primary_categories": [
            "Cognitive Function Research",
            "Neurological & Cognitive Research",
            "Mood & Neuropsychiatric Research",
            "Oxidative Stress Research",
        ],
        "sources": {
            "top_studies_urls": [
                "https://pubmed.ncbi.nlm.nih.gov/33167948/",
                "https://pubmed.ncbi.nlm.nih.gov/32445136/",
                "https://pubmed.ncbi.nlm.nih.gov/19838862/",
                "https://pubmed.ncbi.nlm.nih.gov/20831681/",
                "https://pubmed.ncbi.nlm.nih.gov/25163440/",
            ],
            "cited_references": [
                "[1] - Ayati Z et al. The efficacy of Crocus sativus (saffron) versus placebo and common drugs in the treatment of cognitive disorders: a systematic review and meta-analysis. BMC Complement Med Ther, 2020. PMID: 33167948",
                "[2] - Avgerinos KI et al. Effects of saffron (Crocus sativus L.) on cognitive function: a systematic review and meta-analysis of randomized controlled trials. Neurol Sci, 2020. PMID: 32445136",
                "[3] - Akhondzadeh S et al. A 22-week, multicenter, randomized, double-blind controlled trial of Crocus sativus in the treatment of mild-to-moderate Alzheimer's disease. Psychopharmacology (Berl), 2010. PMID: 19838862",
                "[4] - Akhondzadeh S et al. Saffron in the treatment of patients with mild to moderate Alzheimer's disease: a 16-week, randomized and placebo-controlled trial. J Clin Pharm Ther, 2010. PMID: 20831681",
                "[5] - Farokhnia M et al. Comparing the efficacy and safety of Crocus sativus L. with memantine in patients with moderate to severe Alzheimer's disease: a double-blind randomized clinical trial. Hum Psychopharmacol, 2014. PMID: 25163440",
            ],
        },
        "narrative_summary": {
            "historical_use": "Saffron is the dried stigma of Crocus sativus, a cultivated Iridaceae geophyte historically used across Persian, Mediterranean, Indian, and Middle Eastern medical and culinary traditions. Traditional uses included mood, menstrual, digestive, and general tonic indications; these are historical records and do not establish clinical efficacy.",
            "modern_application": "Saffron is one of the better-studied botanical candidates in dementia-related cognitive research. Systematic reviews and meta-analyses of randomized trials report benefits versus placebo in mild cognitive impairment or Alzheimer's disease outcomes, but also note small samples, overlapping research groups, and risk-of-bias concerns [1][2]. A 22-week randomized trial found Crocus sativus 30 mg/day comparable to donepezil 10 mg/day in mild-to-moderate Alzheimer's disease, with different adverse-event patterns [3]. A placebo-controlled 16-week trial in mild-to-moderate Alzheimer's disease and a 12-month comparator trial against memantine in moderate-to-severe Alzheimer's disease further support research interest, but confirmatory independent trials are still needed [4][5].",
            "side_effects": "Clinical trials in cognitive disorders generally reported similar tolerability to comparator or placebo, with no consistent serious adverse-event signal in the reviewed RCTs [1][2][5]. Reported or plausible adverse effects include nausea, appetite change, dizziness, headache, dry mouth, and allergic reactions. High-dose saffron outside trial ranges is not equivalent to the 30 mg/day extract used in most dementia trials.",
            "contraindications": "Avoid in known allergy to saffron or Crocus species. Use caution with anticoagulant or antiplatelet medications because saffron constituents have platelet and vascular effects in preclinical literature, although cognition trials do not establish a clinically graded interaction. Use during pregnancy is not recommended at medicinal doses because traditional and pharmacological sources raise uterotonic concerns and cognition trials did not study pregnant populations.",
        },
        "clinical_data": {
            "used_part": "Dried stigma; clinical trials typically used saffron extract capsules around 30 mg/day.",
            "primary_active_compounds": [
                "Crocin",
                "Crocetin",
                "Safranal",
                "Picrocrocin",
                "Kaempferol glycosides",
                "Crocus sativus stigma carotenoids",
            ],
            "mechanism_of_action": "Cognitive mechanisms under investigation include antioxidant carotenoid activity, modulation of <strong>amyloid-beta</strong> aggregation, and cholinergic effects relevant to <strong>acetylcholinesterase</strong> [1][2]. Crocin and crocetin are studied for reduction of oxidative stress and inflammatory signaling through pathways such as <strong>NF-kB</strong> and <strong>Nrf2</strong>, primarily in preclinical models [1][2]. Comparator trials in Alzheimer's disease provide clinical outcome signals but do not prove disease modification [3][5].",
            "pharmacokinetics": {
                "absorption": "Human pharmacokinetic data for saffron extract as a whole are limited. Crocin is poorly absorbed intact and is hydrolyzed in the intestine to crocetin, which is more readily absorbed; cognition trials generally do not provide detailed plasma concentration data [1][2].",
                "distribution": "Human tissue-distribution data are insufficient. Crocetin is more lipophilic than crocin and may distribute systemically after absorption, but direct human brain-distribution data for saffron extract are not established [1][2].",
                "metabolism": "Crocin undergoes intestinal hydrolysis to crocetin followed by conjugation reactions. Safranal is expected to undergo hepatic metabolism; clinically relevant CYP450 interaction data for standard saffron extract doses are not established [1][2].",
                "excretion": "Conjugated metabolites are expected to be eliminated through urinary and biliary routes. Human elimination half-life values for cognition-relevant saffron extract constituents are not established in the cited cognitive trials [1][2].",
            },
            "safety_and_interactions": {
                "drug_interactions": "No clinically graded interaction trials were identified for saffron in cognitive-disorder populations. Precautionary concerns include additive effects with anticoagulant or antiplatelet drugs, CNS-active drugs, and antihypertensives; these are based on pharmacology rather than direct interaction trials [1][2].",
                "toxicity": "Clinical trials commonly used 30 mg/day for 16 to 52 weeks and did not report a consistent serious adverse-event excess [1][3][4][5]. Long-term high-dose use outside studied ranges is not characterized by these trials, and medicinal-dose use in pregnancy is not supported.",
            },
            "special_precautions": {
                "pregnancy": "Insufficient pregnancy data for medicinal-dose saffron extract. Avoid medicinal doses because pregnant participants were not studied and uterotonic concerns exist outside the cognition-trial literature.",
                "lactation": "Insufficient data on saffron constituents in human milk. Avoid medicinal-dose preparations during lactation as a precaution.",
                "hepatic_impairment": "No formal hepatic-impairment studies. Use caution in significant liver disease because safranal and carotenoid metabolites undergo hepatic processing.",
                "renal_impairment": "No formal renal-impairment studies. No dose-adjustment guidance has been established.",
            },
        },
    },
    {
        "scientific_name": "Paullinia cupana",
        "common_name": "Guarana",
        "type": "Plant",
        "article_count": 207,
        "primary_categories": [
            "Cognitive Function Research",
            "Stimulant Research",
            "Fatigue & Energy Research",
            "Attention Research",
        ],
        "sources": {
            "top_studies_urls": [
                "https://pubmed.ncbi.nlm.nih.gov/36678305/",
                "https://pubmed.ncbi.nlm.nih.gov/15582012/",
                "https://pubmed.ncbi.nlm.nih.gov/18077056/",
                "https://pubmed.ncbi.nlm.nih.gov/38931247/",
                "https://pubmed.ncbi.nlm.nih.gov/27720901/",
            ],
            "cited_references": [
                "[1] - Hack B et al. Effect of Guarana (Paullinia cupana) on Cognitive Performance: A Systematic Review and Meta-Analysis. Nutrients, 2023. PMID: 36678305",
                "[2] - Kennedy DO et al. Improved cognitive performance in human volunteers following administration of guarana (Paullinia cupana) extract: comparison and interaction with Panax ginseng. Pharmacol Biochem Behav, 2004. PMID: 15582012",
                "[3] - Kennedy DO et al. Improved cognitive performance and mental fatigue following a multi-vitamin and mineral supplement with added guaraná (Paullinia cupana). Appetite, 2008. PMID: 18077056",
                "[4] - Talik TN et al. Effects of Acute Guarana (Paullinia cupana) Ingestion on Mental Performance and Vagal Modulation Compared to a Low Dose of Caffeine. Nutrients, 2024. PMID: 38931247",
                "[5] - Ruchel JB et al. Guarana (Paullinia cupana) ameliorates memory impairment and modulates acetylcholinesterase activity in Poloxamer-407-induced hyperlipidemia in rat brain. Physiol Behav, 2017. PMID: 27720901",
            ],
        },
        "narrative_summary": {
            "historical_use": "Guarana is an Amazonian Sapindaceae liana traditionally used by Indigenous communities, including the Sateré-Mawé, whose roasted seed preparations were used as stimulant beverages and cultural medicines. Historical use centers on wakefulness, endurance, and appetite or fatigue states; this is traditional evidence rather than proof of cognitive efficacy.",
            "modern_application": "Modern cognitive research is mostly acute healthy-volunteer testing of guarana seed extracts or guarana-containing beverages. A 2023 systematic review and meta-analysis of eight placebo-controlled acute studies found a small response-time benefit but no consistent accuracy improvement or clear dose-response [1]. A controlled human trial reported attention and serial-subtraction improvements after 75 mg dried ethanolic guarana extract, alone and compared with Panax ginseng combinations [2]. Combination drink studies are confounded by vitamins, minerals, caffeine, and other ingredients, so they should not be attributed to guarana alone [3]. A 2024 trial comparing guarana with caffeine did not find consistent cognitive benefit, reinforcing that the evidence is mixed [4].",
            "side_effects": "Adverse effects are mainly stimulant-like and caffeine-related: insomnia, nervousness, anxiety, tremor, palpitations, gastrointestinal discomfort, and headache may occur, especially in caffeine-sensitive individuals. Acute cognition studies are short and do not define long-term tolerability. Guarana seed extracts can contain substantial caffeine, so total daily caffeine intake matters.",
            "contraindications": "Avoid high-caffeine guarana preparations in uncontrolled hypertension, significant arrhythmia, severe anxiety, insomnia, and known caffeine sensitivity. Use caution with stimulant medications, other caffeine sources, sympathomimetics, and monoamine oxidase inhibitors. Avoid medicinal-dose guarana during pregnancy and lactation unless caffeine exposure is specifically assessed and medically supervised.",
        },
        "clinical_data": {
            "used_part": "Seed; studies use dried seed extract, seed powder, or guarana-containing beverages. Cognitive interpretation must separate guarana-only studies from combination products.",
            "primary_active_compounds": [
                "Caffeine",
                "Theobromine",
                "Theophylline",
                "Catechin",
                "Epicatechin",
                "Procyanidins",
                "Tannins",
            ],
            "mechanism_of_action": "The primary acute mechanism is methylxanthine antagonism of <strong>adenosine A1</strong> and <strong>adenosine A2A</strong> receptors, increasing wakefulness and altering attention-related performance [1][2]. Caffeine also increases catecholaminergic signaling indirectly through <strong>dopamine</strong> and <strong>noradrenaline</strong> systems, while polyphenols may contribute antioxidant and vascular effects [1]. Preclinical work reports modulation of <strong>acetylcholinesterase</strong> activity in a rat hyperlipidemia memory-impairment model, but this does not establish human cognitive efficacy [5].",
            "pharmacokinetics": {
                "absorption": "Caffeine from guarana is rapidly absorbed orally, though the tannin-rich seed matrix may alter release kinetics compared with pure caffeine. Human guarana cognition trials do not provide a complete pharmacokinetic curve for the full extract [1][2].",
                "distribution": "Caffeine distributes widely, crosses the blood-brain barrier, and is present in saliva and breast milk. Distribution data for guarana polyphenol fractions as a complete extract are limited [1].",
                "metabolism": "Caffeine is primarily metabolized by hepatic <strong>CYP1A2</strong> to paraxanthine, theobromine, and theophylline. CYP1A2 inhibitors, smoking status, oral contraceptives, and genetic variability can change exposure [1].",
                "excretion": "Caffeine metabolites are eliminated mainly in urine. Half-life varies widely, commonly several hours in adults and longer in pregnancy, hepatic impairment, and some medication contexts [1].",
            },
            "safety_and_interactions": {
                "drug_interactions": "Potential interactions follow caffeine pharmacology: additive stimulation with sympathomimetics and ADHD stimulants, increased caffeine exposure with <strong>CYP1A2</strong> inhibitors such as fluvoxamine or ciprofloxacin, reduced exposure with smoking or CYP1A2 induction, and additive cardiovascular effects with decongestants [1]. Guarana may counteract sedatives and can add to total caffeine from coffee, tea, energy drinks, and supplements.",
                "toxicity": "Short acute cognition studies do not define chronic toxicity. Excess caffeine exposure can cause anxiety, insomnia, tachycardia, hypertension, tremor, vomiting, and in extreme overdose seizures or arrhythmias. Guarana products vary widely in caffeine content, making product standardization a central quality-control issue [1][4].",
            },
            "special_precautions": {
                "pregnancy": "Insufficient data for medicinal-dose guarana. Because caffeine crosses the placenta and pregnancy prolongs caffeine half-life, avoid high-caffeine guarana preparations and account for total caffeine exposure.",
                "lactation": "Caffeine enters breast milk. Avoid high-dose guarana and monitor infant irritability or sleep disturbance if caffeine-containing products are used.",
                "hepatic_impairment": "Caffeine clearance may be reduced in hepatic impairment. Use caution with high-caffeine guarana preparations.",
                "renal_impairment": "Caffeine metabolites are renally eliminated, but specific guarana dose-adjustment guidance is not established. Use caution in severe renal impairment.",
            },
        },
    },
    {
        "scientific_name": "Theobroma cacao",
        "common_name": "Cacao / Cocoa",
        "type": "Plant",
        "article_count": 1108,
        "primary_categories": [
            "Cognitive Function Research",
            "Vascular & Cerebral Blood Flow Research",
            "Flavanol Research",
            "Metabolic Research",
        ],
        "sources": {
            "top_studies_urls": [
                "https://pubmed.ncbi.nlm.nih.gov/36102337/",
                "https://pubmed.ncbi.nlm.nih.gov/22892813/",
                "https://pubmed.ncbi.nlm.nih.gov/25733639/",
                "https://pubmed.ncbi.nlm.nih.gov/25344629/",
                "https://pubmed.ncbi.nlm.nih.gov/33589674/",
            ],
            "cited_references": [
                "[1] - Baker LD et al. Effects of cocoa extract and a multivitamin on cognitive function: A randomized clinical trial. Alzheimers Dement, 2023. PMID: 36102337",
                "[2] - Desideri G et al. Benefits in cognitive function, blood pressure, and insulin resistance through cocoa flavanol consumption in elderly subjects with mild cognitive impairment. Hypertension, 2012. PMID: 22892813",
                "[3] - Mastroiacovo D et al. Cocoa flavanol consumption improves cognitive function, blood pressure control, and metabolic profile in elderly subjects: the Cocoa, Cognition, and Aging (CoCoA) Study. Am J Clin Nutr, 2015. PMID: 25733639",
                "[4] - Brickman AM et al. Enhancing dentate gyrus function with dietary flavanols improves cognition in older adults. Nat Neurosci, 2014. PMID: 25344629",
                "[5] - Sloan RP et al. Insights into the role of diet and dietary flavanols in cognitive aging: results of a randomized controlled trial. Sci Rep, 2021. PMID: 33589674",
            ],
        },
        "narrative_summary": {
            "historical_use": "Cacao is a Mesoamerican tree whose fermented seed preparations were used as food, ritual beverage, and trade material by Maya, Aztec, and other Indigenous cultures. Traditional cacao use is culturally and nutritionally important, but it should not be treated as clinical evidence for cognitive enhancement.",
            "modern_application": "Cognitive research on Theobroma cacao is best understood as research on cocoa flavanol extracts or flavanol-rich chocolate, not ordinary chocolate products. Several short RCTs in older adults or mild cognitive impairment reported improvements in selected executive-function, memory, or vascular outcomes after high-flavanol cocoa interventions [2][3][4][5]. However, the large COSMOS-Mind randomized trial found no global cognitive benefit from cocoa extract over 3 years, while the multivitamin arm showed benefit in that study [1]. The archive interpretation should therefore remain preparation-specific and cautious.",
            "side_effects": "Cocoa flavanol interventions in trials are generally food-derived, but tolerability depends strongly on product form, methylxanthine content, sugar, fat, and serving size. Possible adverse effects include gastrointestinal discomfort, reflux, headache or migraine triggering in susceptible individuals, insomnia or palpitations from caffeine/theobromine, and weight or glycemic concerns with sweetened chocolate products. Trial evidence for concentrated flavanol extracts does not generalize to all commercial chocolate.",
            "contraindications": "Use caution in severe reflux disease, migraine sensitivity, stimulant sensitivity, uncontrolled cardiovascular symptoms, and strict glycemic or weight-management contexts when products contain sugar and fat. Cocoa allergy is uncommon but possible. Interaction caution is warranted with stimulant medications and high total caffeine intake; anticoagulant concerns are theoretical and not clinically graded in the cited cognition trials.",
        },
        "clinical_data": {
            "used_part": "Seed/bean-derived cocoa powder, cocoa extract, cocoa flavanol drinks, or flavanol-rich chocolate. Processing level and flavanol dose determine relevance.",
            "primary_active_compounds": [
                "(-)-Epicatechin",
                "(+)-Catechin",
                "Procyanidin oligomers",
                "Theobromine",
                "Caffeine",
                "Quercetin glycosides",
                "Cocoa polyphenols",
            ],
            "mechanism_of_action": "Cocoa flavanols are investigated for vascular mechanisms, including increased endothelial <strong>nitric oxide</strong> bioavailability and improved flow-mediated dilation, which may influence cerebral perfusion [2][3]. Neurocognitive studies also discuss effects on dentate gyrus function, insulin sensitivity, and oxidative stress pathways such as <strong>Nrf2</strong>, though clinical cognitive outcomes are mixed [1][4][5]. Methylxanthines such as theobromine and caffeine can affect alertness through <strong>adenosine receptor</strong> antagonism, but they are not the sole explanation for flavanol-focused trial designs [2][5].",
            "pharmacokinetics": {
                "absorption": "Cocoa flavanol monomers such as epicatechin are orally absorbed and undergo rapid conjugation; oligomeric procyanidins are less readily absorbed intact and are metabolized by gut microbiota. Trial products vary substantially in flavanol dose and matrix [2][3][5].",
                "distribution": "Epicatechin metabolites circulate systemically and may affect vascular endothelium. Direct human brain tissue-distribution data for cocoa flavanol preparations are not established, though neuroimaging outcomes have been studied in older adults [4].",
                "metabolism": "Epicatechin and catechin undergo phase II metabolism, including glucuronidation, sulfation, and methylation. Gut microbiota convert larger procyanidins into smaller phenolic metabolites. Theobromine and caffeine undergo hepatic methylxanthine metabolism, including <strong>CYP1A2</strong>-dependent pathways for caffeine [5].",
                "excretion": "Flavanol conjugates and microbial phenolic metabolites are eliminated primarily in urine, with biliary and fecal routes contributing. Methylxanthine metabolites are renally eliminated; exact half-lives depend on compound and host factors.",
            },
            "safety_and_interactions": {
                "drug_interactions": "No clinically graded interaction trials were identified for cocoa flavanols in cognitive research. Potential interactions include additive stimulant effects with caffeine-containing products or sympathomimetics and exposure changes through <strong>CYP1A2</strong> modifiers for caffeine-containing products. Product sugar, fat, and oxalate content may be clinically relevant in metabolic disease or kidney-stone risk, depending on preparation.",
                "toxicity": "The large COSMOS cocoa-extract trial and smaller flavanol trials did not establish a consistent serious toxicity signal at studied doses [1][2][3][5]. High intake of commercial chocolate can add calories, sugar, saturated fat, methylxanthines, and contaminants depending on product quality; concentrated extract tolerability should not be inferred from ordinary food use alone.",
            },
            "special_precautions": {
                "pregnancy": "Food-level cacao intake is distinct from high-dose extract use. Insufficient data exist for medicinal-dose cocoa flavanol extracts during pregnancy; account for total caffeine and sugar exposure.",
                "lactation": "Caffeine and theobromine may enter breast milk. Use caution with high-methylxanthine cacao products and monitor infant sleep or irritability.",
                "hepatic_impairment": "No formal studies in hepatic impairment. Methylxanthine clearance and flavanol conjugation may be altered in significant liver disease.",
                "renal_impairment": "No formal renal-impairment guidance exists. Consider oxalate burden, potassium content, and renal elimination of metabolites in severe renal disease depending on preparation.",
            },
        },
    },
    {
        "scientific_name": "Polygala tenuifolia",
        "common_name": "Yuan Zhi / Chinese Polygala Root",
        "type": "Plant",
        "article_count": 315,
        "primary_categories": [
            "Cognitive Function Research",
            "Memory Research",
            "Neurological & Cognitive Research",
            "Traditional Chinese Medicine Research",
        ],
        "sources": {
            "top_studies_urls": [
                "https://pubmed.ncbi.nlm.nih.gov/19429065/",
                "https://pubmed.ncbi.nlm.nih.gov/19699261/",
                "https://pubmed.ncbi.nlm.nih.gov/38283842/",
                "https://pubmed.ncbi.nlm.nih.gov/39050746/",
                "https://pubmed.ncbi.nlm.nih.gov/30576772/",
            ],
            "cited_references": [
                "[1] - Lee JY et al. Effects of BT-11 on memory in healthy humans. Neurosci Lett, 2009. PMID: 19429065",
                "[2] - Shin KY et al. BT-11 is effective for enhancing cognitive functions in the elderly humans. Neurosci Lett, 2009. PMID: 19699261",
                "[3] - Zhang Y et al. Polygala tenuifolia and Acorus tatarinowii in the treatment of Alzheimer's disease: a systematic review and meta-analysis. Front Pharmacol, 2023. PMID: 38283842",
                "[4] - Li S et al. Saponin components in Polygala tenuifolia as potential candidate drugs for treating dementia. Front Pharmacol, 2024. PMID: 39050746",
                "[5] - Park CH et al. Study on the safety of Polygala tenuifolia Willdenow root extract powder (BT-11) in young person aged from 9 to 19 years old. J Ethnopharmacol, 2019. PMID: 30576772",
            ],
        },
        "narrative_summary": {
            "historical_use": "Polygala tenuifolia root is known in Traditional Chinese Medicine as Yuan Zhi, traditionally used in formulas for forgetfulness, restlessness, sleep disturbance, and spirit-calming indications. These uses are traditional and formula-based, and they do not establish isolated-species clinical efficacy.",
            "modern_application": "Human cognitive research is concentrated on BT-11, a Polygala tenuifolia root extract, with small randomized studies in healthy adults and elderly adults reporting improvements in verbal learning, recognition, and memory-related test batteries [1][2]. A 2024 meta-analysis evaluated the Polygala tenuifolia-Acorus tatarinowii herb pair as an adjunct in Alzheimer's disease, but this evidence is combination-based and rated low or very low quality, so it cannot be attributed to Polygala alone [3]. Mechanistic reviews emphasize saponins and related constituents in dementia models, but much of that literature is preclinical [4]. A separate clinical study in adolescents provides some product-specific tolerability information for BT-11 rather than adult long-term efficacy [5].",
            "side_effects": "Saponin-rich Polygala root preparations may cause gastrointestinal irritation, nausea, abdominal discomfort, or throat irritation. Human BT-11 studies were small and do not establish long-term adult tolerability. Combination TCM studies cannot isolate Polygala-specific adverse effects.",
            "contraindications": "Avoid in known allergy to Polygala species. Use caution in active gastritis, peptic ulcer disease, severe reflux, or high GI sensitivity because saponins can irritate mucosa. Use caution with CNS-active medications and cholinergic agents because cognitive mechanisms under investigation include neurotrophic and cholinergic pathways, but clinically graded interaction data are lacking.",
        },
        "clinical_data": {
            "used_part": "Dried root; BT-11 root extract in human memory studies. Traditional formulas may combine Polygala with Acorus and other herbs.",
            "primary_active_compounds": [
                "Tenuifolin",
                "Tenuigenin",
                "Polygalasaponins",
                "Onjisaponin B",
                "Senegenin",
                "3,6'-disinapoyl sucrose",
                "Xanthone glycosides",
            ],
            "mechanism_of_action": "Polygala root constituents are investigated for effects on <strong>BDNF</strong>, <strong>CREB</strong>, synaptic plasticity, and cholinergic signaling in memory models [4]. Saponins such as tenuifolin and onjisaponins are studied for modulation of <strong>acetylcholinesterase</strong>, neuroinflammation, and amyloid-related pathways, primarily in preclinical systems [4]. Human BT-11 trials provide cognitive test signals but do not establish a complete mechanism in humans [1][2].",
            "pharmacokinetics": {
                "absorption": "No comprehensive human pharmacokinetic dataset exists for Polygala tenuifolia root extract. Saponins are generally poorly absorbed intact and may be transformed by intestinal microbiota; sucrose esters and xanthones may have different absorption profiles [4].",
                "distribution": "Human distribution data are insufficient. Preclinical studies suggest some Polygala-derived metabolites may affect central nervous system pathways, but direct human brain distribution for BT-11 or root extract is not established [4].",
                "metabolism": "Saponins may undergo deglycosylation by gut microbiota followed by hepatic conjugation of absorbed aglycones. Human CYP450 interaction data for Polygala tenuifolia are not established [4].",
                "excretion": "Elimination routes and half-lives for BT-11 and Polygala root saponins are not defined in humans. Metabolites are expected to be eliminated through urinary and biliary pathways after conjugation [4].",
            },
            "safety_and_interactions": {
                "drug_interactions": "No clinically graded herb-drug interaction studies were identified. Precautionary concerns include additive CNS effects with sedatives or stimulants and theoretical interaction with cholinergic or anticholinergic drugs, based on cognitive and cholinergic mechanisms under investigation [1][4].",
                "toxicity": "Human clinical tolerability data are limited to small BT-11 studies and a product-specific adolescent tolerability study [1][2][5]. Saponin-rich preparations can irritate the gastrointestinal tract; chronic high-dose toxicity in adults is not adequately characterized by the cited literature.",
            },
            "special_precautions": {
                "pregnancy": "Insufficient human data for Polygala tenuifolia during pregnancy. Avoid medicinal-dose root preparations as a precaution.",
                "lactation": "Insufficient data on transfer into human milk. Avoid medicinal-dose preparations during lactation as a precaution.",
                "hepatic_impairment": "No formal hepatic-impairment studies. Use caution because absorbed constituents likely undergo hepatic metabolism.",
                "renal_impairment": "No formal renal-impairment studies and no dose-adjustment guidance. Use caution in severe renal impairment.",
            },
        },
    },
    {
        "scientific_name": "Huperzia serrata",
        "common_name": "Chinese Club Moss / Toothed Clubmoss",
        "type": "Plant",
        "article_count": 225,
        "primary_categories": [
            "Cognitive Function Research",
            "Cholinergic Research",
            "Neurological & Cognitive Research",
            "Alkaloid Research",
        ],
        "sources": {
            "top_studies_urls": [
                "https://pubmed.ncbi.nlm.nih.gov/24086396/",
                "https://pubmed.ncbi.nlm.nih.gov/18425924/",
                "https://pubmed.ncbi.nlm.nih.gov/21502597/",
                "https://pubmed.ncbi.nlm.nih.gov/23235666/",
                "https://pubmed.ncbi.nlm.nih.gov/34526893/",
            ],
            "cited_references": [
                "[1] - Yang G et al. Huperzine A for Alzheimer's disease: a systematic review and meta-analysis of randomized clinical trials. PLoS One, 2013. PMID: 24086396",
                "[2] - Li J et al. Huperzine A for Alzheimer's disease. Cochrane Database Syst Rev, 2008. PMID: 18425924",
                "[3] - Rafii MS et al. A phase II trial of huperzine A in mild to moderate Alzheimer disease. Neurology, 2011. PMID: 21502597",
                "[4] - Yue J et al. Huperzine A for mild cognitive impairment. Cochrane Database Syst Rev, 2012. PMID: 23235666",
                "[5] - Callizot N et al. Huperzia serrata extract NSP01 with neuroprotective effects: potential synergies of huperzine A and polyphenols. Front Pharmacol, 2021. PMID: 34526893",
            ],
        },
        "narrative_summary": {
            "historical_use": "Huperzia serrata is a Lycopodiaceae species used in Chinese materia medica sources under names associated with club mosses. Traditional use should be interpreted cautiously because common names such as club moss may refer to multiple Lycopodiaceae taxa.",
            "modern_application": "The strongest human cognitive evidence is for isolated huperzine A, an alkaloid originally identified from Huperzia serrata, rather than for whole-plant preparations. Systematic reviews of huperzine A in Alzheimer's disease reported cognitive outcome improvements but emphasized methodological limitations and high risk of bias in many trials [1][2]. A U.S. phase II trial in mild-to-moderate Alzheimer's disease did not meet the primary ADAS-cog endpoint at 200 mcg twice daily, though 400 mcg twice daily showed some secondary cognitive signal [3]. A Cochrane review found no eligible placebo-controlled RCT evidence for huperzine A in mild cognitive impairment at that time [4]. Whole Huperzia serrata extract research remains mostly preclinical or mechanistic [5].",
            "side_effects": "Huperzine A can produce cholinergic adverse effects, including nausea, vomiting, diarrhea, sweating, salivation, dizziness, bradycardia, insomnia, vivid dreams, and muscle cramps. Whole Huperzia extracts may vary in alkaloid content and are not interchangeable with purified huperzine A trials. Long-term tolerability and product-standardization data remain limited.",
            "contraindications": "Avoid combining with cholinesterase inhibitors such as donepezil, rivastigmine, or galantamine unless medically supervised because of additive cholinergic effects. Use caution or avoid in bradycardia, conduction disorders, asthma/COPD with cholinergic sensitivity, seizure disorders, peptic ulcer disease, and urinary obstruction. Pregnancy and lactation use is not supported by human evidence.",
        },
        "clinical_data": {
            "used_part": "Whole herb/aerial material as botanical source; human dementia trials primarily use isolated huperzine A rather than crude Huperzia serrata extract.",
            "primary_active_compounds": [
                "Huperzine A",
                "Huperzine B",
                "Lycopodium alkaloids",
                "Serratane-type triterpenoids",
                "Polyphenols in standardized extracts",
            ],
            "mechanism_of_action": "Huperzine A is a reversible inhibitor of <strong>acetylcholinesterase</strong>, increasing synaptic acetylcholine in a mechanism related to approved cholinesterase-inhibitor drugs [1][2]. Preclinical research also investigates effects on <strong>NMDA receptor</strong>-mediated excitotoxicity, oxidative stress, and neuroinflammatory pathways, but those mechanisms should not be treated as established clinical disease modification [1][5]. Whole-extract NSP01 research suggests possible synergy between huperzine A and polyphenols in cell and animal models, not confirmed human cognitive efficacy [5].",
            "pharmacokinetics": {
                "absorption": "Human clinical trials use oral huperzine A doses in the microgram range, indicating systemic oral activity, but botanical whole-extract pharmacokinetics are not equivalent to purified huperzine A [1][3]. Detailed extract-level absorption data are insufficient.",
                "distribution": "Huperzine A is sufficiently lipophilic to cross the blood-brain barrier, consistent with central cholinesterase inhibition. Human tissue-distribution data for complete Huperzia serrata extract are not established [1][5].",
                "metabolism": "Metabolic pathways for huperzine A in humans are incompletely characterized in the cited clinical literature. CYP450 interaction data for Huperzia serrata extracts are not clinically established.",
                "excretion": "Elimination data for purified huperzine A and whole Huperzia serrata extract are incomplete in the cited clinical literature. No dose-adjustment guidance is established for renal or hepatic impairment.",
            },
            "safety_and_interactions": {
                "drug_interactions": "Major precautionary pharmacodynamic concern: additive cholinergic effects with donepezil, rivastigmine, galantamine, bethanechol, or other cholinergic agents. Antagonism with anticholinergic drugs is also plausible. Clinically graded interaction trials for Huperzia serrata products were not identified [1][3].",
                "toxicity": "Purified huperzine A trials report cholinergic adverse effects but generally studied short-to-moderate durations [1][3]. Whole-plant extracts vary in alkaloid content; quality-control failures could increase toxicity risk. Long-term crude-extract toxicity is not adequately characterized.",
            },
            "special_precautions": {
                "pregnancy": "Insufficient human data for huperzine A or Huperzia serrata during pregnancy. Avoid medicinal-dose use.",
                "lactation": "Insufficient data on transfer into breast milk. Avoid medicinal-dose use during lactation.",
                "hepatic_impairment": "No formal hepatic-impairment studies. Use caution because metabolism and clearance are incompletely characterized.",
                "renal_impairment": "No formal renal-impairment studies and no dose-adjustment guidance. Use caution in severe renal impairment.",
            },
        },
    },
]


def main():
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)

    existing = {entry["scientific_name"] for entry in data}
    to_add = [entry for entry in NEW_ENTRIES if entry["scientific_name"] not in existing]
    skipped = [entry["scientific_name"] for entry in NEW_ENTRIES if entry["scientific_name"] in existing]

    data.extend(to_add)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Added {len(to_add)} entries; skipped {len(skipped)} existing entries.")
    if skipped:
        print("Skipped:", ", ".join(skipped))
    print(f"Total entries: {len(data)}")


if __name__ == "__main__":
    main()
