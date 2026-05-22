#!/usr/bin/env python3
"""Batch 1 — Ginkgo biloba, Panax ginseng, Bacopa monnieri, Rhodiola rosea"""
import json

PLANTS = [
  {
    "scientific_name": "Ginkgo biloba",
    "common_name": "Ginkgo / Maidenhair tree",
    "type": "Plant",
    "article_count": 5758,
    "primary_categories": ["Cognitive enhancement", "Neuroprotection", "Peripheral circulation"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42150674/",
        "https://pubmed.ncbi.nlm.nih.gov/42149066/",
        "https://pubmed.ncbi.nlm.nih.gov/42143819/"
      ]
    },
    "narrative_summary": {
      "historical_use": "One of the oldest living tree species on Earth (>200 million years old), revered in China for over 5,000 years as 'yin xing' (silver apricot). Leaves and seeds used in Traditional Chinese Medicine for respiratory conditions, urinary dysfunction, and memory decline. Introduced to Western pharmacology in the 1960s; the standardised extract EGb 761 was developed by Willmar Schwabe GmbH and remains the most extensively studied phytomedicine in Europe.",
      "modern_application": "EGb 761 (standardised to 24% flavonol glycosides and 6% terpene lactones) is approved in Germany for symptomatic treatment of dementia and peripheral arterial disease. Multiple RCTs show modest improvement in cognitive scores in mild-to-moderate Alzheimer's disease. A Cochrane review found inconsistent evidence for dementia prevention in healthy adults. Strongest evidence is for symptom management in existing cognitive impairment, tinnitus, and intermittent claudication.",
      "side_effects": "GI upset (nausea, diarrhoea), headache, dizziness, and palpitations. Skin hypersensitivity reactions possible (cross-reactivity with urushiol in poison ivy). Rarely: spontaneous bleeding events including subdural haematoma and vitreous haemorrhage (case reports). Ginkgolic acids in crude preparations are nephrotoxic and potentially carcinogenic; pharmaceutical extracts limit these to <5 ppm.",
      "contraindications": "Contraindicated with anticoagulants (warfarin, heparin) and antiplatelet drugs (aspirin, clopidogrel, NSAIDs). Discontinue ≥36 hours before surgery. Contraindicated with MAO inhibitors. Avoid in patients with a seizure history (ginkgotoxin lowers seizure threshold in overdose). Avoid unpurified leaf preparations."
    },
    "clinical_data": {
      "used_part": "Leaf (standardised extract EGb 761); seed (limited — nephrotoxic raw)",
      "primary_active_compounds": [
        "Ginkgo flavonol glycosides (quercetin-3-rutinoside, kaempferol-3-rutinoside, isorhamnetin glycosides)",
        "Ginkgolides A, B, C, J (diterpene lactones)",
        "Bilobalide (sesquiterpene lactone)",
        "Ginkgolic acids (alkyl/alkenyl phenols — limited to <5 ppm in EGb 761)",
        "Proanthocyanidins"
      ],
      "mechanism_of_action": "Ginkgolides A and B are potent, selective antagonists at the <strong>platelet-activating factor (PAF) receptor</strong>, inhibiting platelet aggregation and reducing arterial thrombosis risk. Bilobalide is a non-competitive antagonist at the <strong>GABA-A receptor</strong> (glycine-binding site), providing neuroprotection against ischaemia-induced excitotoxicity. Flavonols scavenge reactive oxygen species and upregulate <strong>Nrf2/HO-1</strong> antioxidant genes. The whole extract increases cerebral blood flow via <strong>eNOS</strong>-mediated nitric oxide production and mildly inhibits <strong>MAO-A</strong> and <strong>MAO-B</strong>, contributing to mood stabilisation.",
      "pharmacokinetics": {
        "absorption": "Flavonol glycosides are well absorbed (bioavailability ~80%) after enzymatic deglycosylation in the gut. Ginkgolides A and B reach Cmax at 2–3 hours; bilobalide Cmax at 1–2 hours. Food has minimal effect on absorption.",
        "distribution": "Crosses the blood-brain barrier readily; high affinity for brain, retinal, and cochlear tissue. Plasma protein binding of flavonoids ~98%. Volume of distribution of ginkgolides estimated at 0.5–1 L/kg.",
        "metabolism": "Hepatic. Flavonol glycosides hydrolysed to aglycones (quercetin, kaempferol, isorhamnetin) then conjugated via UGT glucuronidation and sulfation. Ginkgolides are substrates of CYP2C9 and CYP3A4. Quercetin undergoes bacterial ring-fission in the large intestine.",
        "excretion": "Urinary (conjugated metabolites) and biliary. Ginkgolide B half-life ~4 hours; bilobalide ~3 hours; quercetin metabolites ~2–3 hours."
      },
      "safety_and_interactions": {
        "drug_interactions": "Anticoagulants (warfarin, acenocoumarol) — INR elevation via PAF antagonism and mild antiplatelet activity; monitor closely. Antiplatelet agents (aspirin, clopidogrel, NSAIDs) — additive bleeding risk. CYP2C9 substrates (phenytoin, ibuprofen) — CYP2C9 inhibition increases plasma levels. SSRIs/SNRIs — rare serotonin syndrome reports. MAO inhibitors — theoretical potentiation; contraindicated. Insulin and oral antidiabetics — possible additive hypoglycaemia.",
        "toxicity": "LD50 >7,750 mg/kg in rats (oral). Ginkgolic acids are nephrotoxic and genotoxic — pharmaceutical extracts limit to <5 ppm. Ginkgotoxin (4'-O-methylpyridoxine) in seeds is seizurogenic (pyridoxine-responsive); leaf extracts contain minimal amounts. High-dose chronic rodent studies showed hepatocellular adenoma (NTP); clinical relevance uncertain."
      },
      "special_precautions": {
        "pregnancy": "Insufficient human safety data. Ginkgolic acids are potentially teratogenic. Avoid during pregnancy.",
        "lactation": "Excretion in breast milk unknown. Avoid due to insufficient safety data.",
        "hepatic_impairment": "CYP2C9 and CYP3A4 are hepatically expressed; impaired metabolism expected in liver disease. No formal dose adjustment studies available. Use with caution and monitor.",
        "renal_impairment": "Water-soluble conjugated metabolites are renally excreted. Accumulation possible in severe renal impairment. No formal dose adjustment guidelines established."
      }
    },
    "consumer_view": {
      "tagline": "Sharpens memory and improves blood flow to the brain and limbs",
      "what_it_does": "Ginkgo increases blood flow to the brain, protects nerve cells from damage, and prevents blood from clumping in small vessels. Most people use it to support memory, concentration, and mental sharpness — especially with age. It is also widely used for tinnitus and cold hands and feet.",
      "typical_uses": [
        "Age-related memory decline",
        "Tinnitus (ringing in the ears)",
        "Poor circulation in hands and feet",
        "Concentration and mental clarity",
        "Mild dementia symptom support"
      ],
      "suggested_dose": "120–240 mg of standardised extract (EGb 761; 24% flavonol glycosides, 6% terpene lactones) per day, split into 2 doses with meals. Allow 4–8 weeks for cognitive effects.",
      "onset": "Circulation and alertness: 1–2 weeks. Memory and cognitive benefits: 4–8 weeks of consistent use.",
      "safety_snapshot": [
        "Do not take with blood thinners (warfarin, aspirin, clopidogrel)",
        "Stop at least 36 hours before any surgery",
        "Avoid if you have a history of seizures or are taking MAO inhibitors"
      ]
    }
  },
  {
    "scientific_name": "Panax ginseng",
    "common_name": "Asian ginseng / Korean red ginseng",
    "type": "Plant",
    "article_count": 11595,
    "primary_categories": ["Adaptogen", "Cognitive enhancement", "Immune support", "Energy & vitality"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42152269/",
        "https://pubmed.ncbi.nlm.nih.gov/42152268/",
        "https://pubmed.ncbi.nlm.nih.gov/42148289/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Used in Traditional Chinese Medicine for over 2,000 years, Panax ginseng — from the Greek 'pan-akos' (all-healing) — is classified in the Shen Nong Ben Cao Jing (c. 100 CE) as a superior tonic to tonify Qi, calm the mind, and prolong life. Red ginseng is prepared by steaming and drying 6-year-old roots, which transforms the ginsenoside profile (creating Rg3, Rh2, compound K) and has been commercially cultivated in Korea for over 500 years.",
      "modern_application": "Extensively studied as an adaptogen. RCTs demonstrate improved cognitive performance (working memory, attention), reduced fatigue, and enhanced physical endurance. Korean red ginseng shows consistent evidence for improving erectile dysfunction and glycaemic control in type 2 diabetes. A 2020 Cochrane review found KRG reduced incidence and duration of common cold. Most trials use standardised extracts with ≥5% ginsenosides at 200–400 mg/day.",
      "side_effects": "Insomnia and nervousness are the most common, dose-dependent effects. GI disturbance (nausea, diarrhoea). Headache and blood pressure elevation at high doses. 'Ginseng abuse syndrome' at >3 g/day: hypertension, oedema, insomnia, skin eruptions. Mastalgia and postmenopausal uterine bleeding from oestrogenic ginsenoside activity.",
      "contraindications": "Avoid at high doses in hypertension. Contraindicated with MAO inhibitors (hypertensive crisis). Use with extreme caution in hormone-sensitive conditions (ER-positive breast cancer, endometrial cancer). Contraindicated during acute infections with high fever. Cycle use: maximum 12 weeks continuous, then a 4-week break."
    },
    "clinical_data": {
      "used_part": "Root (6+ years old); white ginseng (air-dried) and red ginseng (steamed and dried)",
      "primary_active_compounds": [
        "Ginsenoside Rb1 (sedative/neuroprotective; high in white ginseng)",
        "Ginsenoside Rg1 (stimulant-like, oestrogenic)",
        "Ginsenoside Re (antidiabetic, cardioprotective)",
        "Ginsenoside Rg3 and Rh2 (anti-tumour; enriched in red ginseng)",
        "Compound K (primary bioactive metabolite; formed from Rb1 by gut bacteria)",
        "Panaxans A–E (polysaccharide hypoglycaemics)",
        "Gintonin (lysophosphatidic acid receptor ligand)"
      ],
      "mechanism_of_action": "Ginsenosides modulate the <strong>hypothalamic-pituitary-adrenal (HPA) axis</strong>, attenuating stress-induced cortisol hypersecretion. Rg1 acts as a partial <strong>glucocorticoid receptor</strong> agonist; Rb1 suppresses hypothalamic <strong>CRH</strong> release. Rg1 upregulates <strong>BDNF</strong> and promotes hippocampal neurogenesis via <strong>ERK1/2</strong> signalling. Neuroprotection via inhibition of <strong>NMDA receptor</strong>-mediated excitotoxicity. Vasodilation via <strong>eNOS</strong> upregulation and nitric oxide production (relevant to erectile function). Immunomodulation via <strong>NK cell</strong> activation and <strong>TLR-4</strong> engagement by panaxan polysaccharides.",
      "pharmacokinetics": {
        "absorption": "Ginsenosides are poorly absorbed as intact glycosides due to high molecular weight and poor membrane permeability. Gut microbiota deglycosylate them to compound K, 20(S)-protopanaxadiol, and Rh1 — the bioactive circulating forms. Cmax of compound K at 3–5 hours after standardised extract. Significant inter-individual PK variability driven by gut microbiome composition.",
        "distribution": "Compound K crosses the blood-brain barrier; high tissue affinity for gonads, adrenal glands, liver, and spleen. Ginsenoside Rg1 crosses the BBB rapidly (Tmax ~30 min after IV in animal models). Plasma protein binding ~80% for most ginsenosides.",
        "metabolism": "Extensive first-pass and gut metabolism. Parent ginsenosides → gut bacterial β-glucosidase → compound K, Rh1, Rh2 → hepatic glucuronidation via UGT enzymes. CYP3A4 mediates triterpenoid oxidation. Red ginseng ginsenosides (Rg3, Rh2) are more directly bioavailable than white ginseng equivalents.",
        "excretion": "Biliary (primary route) and urinary. Compound K half-life ~10–15 hours. Intact ginsenosides predominantly excreted in faeces. Enterohepatic recirculation documented for some ginsenosides."
      },
      "safety_and_interactions": {
        "drug_interactions": "Warfarin — case reports of both decreased INR (CYP2C9 induction) and increased INR (antiplatelet activity); close monitoring required. MAO inhibitors (phenelzine, tranylcypromine) — hypertensive crisis; contraindicated. Antidiabetic drugs — additive hypoglycaemia (documented in RCTs). Immunosuppressants (cyclosporin) — CYP3A4 induction may reduce cyclosporin levels. Stimulants (caffeine, amphetamines) — additive CNS stimulation, insomnia, hypertension.",
        "toxicity": "LD50 >5 g/kg in mice (oral). Ginseng abuse syndrome at >3 g/day chronic dosing. Rare hepatotoxicity in case reports — likely adulterated products. Mastalgia and uterine bleeding from oestrogenic ginsenoside fractions."
      },
      "special_precautions": {
        "pregnancy": "Ginsenoside Rb1 shows embryotoxicity in animal models at high doses. Avoid during pregnancy, particularly in the first trimester.",
        "lactation": "Ginsenoside excretion in breast milk has not been characterised. Avoid during breastfeeding.",
        "hepatic_impairment": "Significant hepatic metabolism; dose reduction warranted in severe impairment. Monitor liver enzymes. Rare hepatotoxicity reported.",
        "renal_impairment": "Ginsenoside metabolites are renally excreted; accumulation possible in severe renal failure. No formal dose adjustment guidelines. Use with monitoring."
      }
    },
    "consumer_view": {
      "tagline": "Boosts energy, sharpens focus, and helps your body handle stress",
      "what_it_does": "Asian ginseng is one of the world's most thoroughly studied adaptogen herbs — it helps your body cope with physical and mental stress more effectively. It can improve energy levels, mental clarity, and immune resilience, and has solid evidence for supporting sexual health in men.",
      "typical_uses": [
        "Mental fatigue and brain fog",
        "Low energy and physical endurance",
        "Stress resilience and burnout recovery",
        "Immune support and cold prevention",
        "Erectile dysfunction"
      ],
      "suggested_dose": "200–400 mg of standardised extract (≥5% ginsenosides) per day, in the morning. Cycle use: 8–12 weeks on, then a 4-week break. Red ginseng is preferred for energy and sexual health; white ginseng for gentler, calming effects.",
      "onset": "Energy and focus: 1–2 weeks. Immune, cognitive, and sexual health benefits: 4–8 weeks.",
      "safety_snapshot": [
        "Never combine with MAO inhibitors — serious blood pressure reaction",
        "Can cause insomnia — take in the morning only",
        "Consult a doctor if on warfarin, diabetes medication, or hormone-sensitive treatments"
      ]
    }
  },
  {
    "scientific_name": "Bacopa monnieri",
    "common_name": "Brahmi / Water hyssop",
    "type": "Plant",
    "article_count": 544,
    "primary_categories": ["Cognitive enhancement", "Neuroprotection", "Adaptogen", "Anxiolytic"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42105315/",
        "https://pubmed.ncbi.nlm.nih.gov/42102930/",
        "https://pubmed.ncbi.nlm.nih.gov/42074246/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Used for over 3,000 years in Ayurvedic medicine, described in the Charaka Samhita (c. 6th century BCE) as a 'medhya rasayana' — an intellect-promoting tonic. Traditionally prescribed to enhance memory acquisition and retention in Vedic scholars and students of sacred texts. Also used historically as a nervine tonic for epilepsy, anxiety, and mental disorders.",
      "modern_application": "Among the most rigorously studied nootropic plants. Meta-analyses of 9 RCTs demonstrate statistically significant improvements in memory acquisition and retention in healthy adults and older populations. Most trials use standardised CDRI-08 extract (Keenmind) at 300–450 mg/day for 12 weeks. Evidence also supports anxiolytic activity with reduced cortisol in chronic stress, and a neuroprotective effect in models of amyloid-β toxicity relevant to Alzheimer's disease.",
      "side_effects": "GI side effects are the most common and clinically significant: nausea, abdominal cramping, loose stools, and bloating — substantially reduced when taken with food. Dry mouth and mild fatigue reported at high doses. No serious adverse events reported in RCTs at therapeutic doses. Long-term safety beyond 12 weeks is not well characterised in human studies.",
      "contraindications": "Avoid concurrent use with AChE inhibitors (donepezil, rivastigmine, galantamine) — pharmacodynamic overlap risks cholinergic toxicity. Caution with antidepressants targeting the serotonin system. Bradycardia risk: avoid with β-blockers, calcium channel blockers, and digoxin. Potential thyroid interaction: may reduce T4 levels; monitor in hypothyroid patients on replacement therapy."
    },
    "clinical_data": {
      "used_part": "Whole aerial plant (leaves and stem); standardised ethanolic extract (45% bacosides)",
      "primary_active_compounds": [
        "Bacoside A (Bacoside A3 + Bacopasaponin C + Bacopaside II)",
        "Bacopasides I–XII (dammarane-type triterpenoid saponins)",
        "Bacopaside N2",
        "Apigenin and luteolin (flavone aglycones)",
        "Brahmine (alkaloid)",
        "D-mannitol and betulinic acid"
      ],
      "mechanism_of_action": "Bacosides enhance dendritic branching and synaptic plasticity via the <strong>MAPK/ERK</strong> signalling pathway, increasing protein kinase C (PKC) activity in the hippocampus. Inhibit <strong>acetylcholinesterase (AChE)</strong> and <strong>butyrylcholinesterase (BuChE)</strong>, raising synaptic acetylcholine concentrations. Upregulate hippocampal <strong>BDNF</strong> and neurotrophin-3, supporting long-term potentiation. Reduce <strong>5-HT</strong> turnover via tryptophan hydroxylase inhibition, contributing to anxiolysis. Potent antioxidant via <strong>Nrf2/HO-1</strong> pathway, reducing amyloid-β aggregation (Alzheimer's neuroprotection). Modulate the <strong>HPA axis</strong>, reducing cortisol response to stress.",
      "pharmacokinetics": {
        "absorption": "Bacosides are absorbed after hydrolysis by intestinal enzymes. Cmax at approximately 2 hours post-dose for bacoside aglycones. Bioavailability is moderate; lipid-based formulations enhance absorption. Standard therapeutic dose is 300 mg extract with meals.",
        "distribution": "Crosses the blood-brain barrier; preferentially accumulates in hippocampus and frontal cortex, consistent with observed cognitive effects. Plasma protein binding estimated at ~60%. Spermatogenic tissue distribution has been noted in rodent studies.",
        "metabolism": "Hepatic metabolism via CYP3A4 and CYP2D6. Triterpenoid saponins partially hydrolysed in the gut before absorption; aglycone forms (ebelin lactone, jujubogenin) are the primary absorbed entities. Flavonoids undergo glucuronidation and sulfation.",
        "excretion": "Primarily biliary and faecal. Urinary excretion of glucuronide and sulfate conjugates. Half-life estimated at 2–4 hours for bacoside aglycones; multiple daily dosing required for sustained levels."
      },
      "safety_and_interactions": {
        "drug_interactions": "AChE inhibitors (donepezil, galantamine, rivastigmine) — additive cholinergic stimulation; risk of bradycardia, excessive secretions, GI hypermotility. Antidepressants (SSRIs, TCAs) — serotonin system modulation; caution required. Thyroid hormone replacement (levothyroxine) — Bacopa may reduce T4 conversion; monitor thyroid function. β-Blockers and calcium channel blockers — additive bradycardia via muscarinic mechanism.",
        "toxicity": "LD50 >5 g/kg in rodents. Spermatotoxic effects in male rats at high doses (>80 mg/kg); fully reversible on discontinuation; not confirmed in human studies. GI side effects are dose-dependent and the primary tolerability concern."
      },
      "special_precautions": {
        "pregnancy": "Insufficient human safety data. Potential uterotonic effects noted in animal studies at high doses. Avoid during pregnancy.",
        "lactation": "Traditional use in Ayurveda suggests relative safety, but no modern pharmacokinetic data on excretion in breast milk. Avoid concentrated extracts during breastfeeding.",
        "hepatic_impairment": "CYP3A4 substrate; reduced hepatic function may increase plasma exposure. No formal dose adjustment guidelines. Use with caution and reduce dose in severe impairment.",
        "renal_impairment": "Conjugated metabolites excreted renally. No specific contraindication established; standard monitoring recommended in severe renal impairment."
      }
    },
    "consumer_view": {
      "tagline": "Improves memory and learning — but patience is required: 8–12 weeks to full effect",
      "what_it_does": "Brahmi is an Ayurvedic herb that gradually strengthens the brain's ability to form and recall memories. Unlike caffeine, it doesn't give a quick boost — it works by improving the structure of brain cells over weeks. Regular use also reduces anxiety and helps with focus.",
      "typical_uses": [
        "Improving memory formation and recall",
        "Student and exam performance support",
        "Anxiety and stress reduction",
        "Protecting brain health with age",
        "ADHD-related focus difficulties"
      ],
      "suggested_dose": "300–450 mg of standardised extract (45% bacosides) once daily, taken with food. Effects require consistent daily use for 8–12 weeks. Do not take on an empty stomach.",
      "onset": "Reduced anxiety and mild focus improvement: 2–4 weeks. Full memory and learning benefits: 8–12 weeks.",
      "safety_snapshot": [
        "Always take with food — significant nausea on an empty stomach",
        "Avoid if on Alzheimer's medications (donepezil, rivastigmine)",
        "Not recommended during pregnancy or if trying to conceive (male)"
      ]
    }
  },
  {
    "scientific_name": "Rhodiola rosea",
    "common_name": "Golden root / Arctic root / Rose root",
    "type": "Plant",
    "article_count": 1508,
    "primary_categories": ["Adaptogen", "Anti-fatigue", "Mood support", "Mental performance"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42149803/",
        "https://pubmed.ncbi.nlm.nih.gov/42126218/",
        "https://pubmed.ncbi.nlm.nih.gov/42123940/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Used for over 3,000 years across Scandinavia, Siberia, and Central Asia. Viking seafarers used it to increase physical endurance and cold tolerance; Siberian hunters consumed it before long expeditions. Classified in the Soviet Pharmacopoeia and extensively (and largely classified) researched by Soviet scientists from the 1960s to 1980s as a performance-enhancing adaptogen for military personnel, athletes, and cosmonauts. Referenced in Chinese medicine as 'hong jing tian' (red-stalked sky herb).",
      "modern_application": "The European Medicines Agency (EMA, 2012) concluded 'well-established use' evidence for Rhodiola extract SHR-5 in temporary fatigue, exhaustion, and stress. Swedish RCTs (Darbinyan 2000; Shevtsov 2003) demonstrated significant improvements in mental work capacity, reaction time, and short-term memory in physicians on night duty and cadets under stress. A 2015 RCT (Lekomtseva et al.) demonstrated non-inferiority to sertraline in mild-to-moderate depression with a significantly better side effect profile. Standardised SHR-5 extract (3.6% rosavin, 1.6% salidroside) is the most clinically validated form.",
      "side_effects": "Generally well tolerated in clinical trials. Dizziness, dry mouth, and excessive saliva. Agitation, palpitations, and anxiety at high doses or in susceptible individuals. Insomnia if taken in the afternoon or evening (stimulant-like profile). Rarely: hypersensitivity reactions. Activating effect has precipitated hypomanic episodes in individuals with bipolar disorder.",
      "contraindications": "Avoid in bipolar disorder and mania (activating effect may precipitate hypomania). Contraindicated with MAO inhibitors. Avoid in uncontrolled hypertension. Do not take in the evening. Caution with antidepressants — additive serotonergic and dopaminergic activity increases serotonin syndrome risk."
    },
    "clinical_data": {
      "used_part": "Root and rhizome (dried; standardised extract SHR-5)",
      "primary_active_compounds": [
        "Rosavin (cinnamyl alcohol β-D-glucopyranoside; marker compound for standardisation)",
        "Rosarin and Rosin (related phenylpropanoid glycosides)",
        "Salidroside / Rhodioloside (tyrosol β-D-glucoside; primary active)",
        "p-Tyrosol (aglycone of salidroside; directly bioactive)",
        "Rosiridin (monoterpene glycoside)",
        "Triandrin and viridoside"
      ],
      "mechanism_of_action": "Salidroside and p-tyrosol activate <strong>AMPK (AMP-activated protein kinase)</strong>, promoting mitochondrial biogenesis and increasing cellular ATP production — the primary mechanism for anti-fatigue effects. Mild inhibition of <strong>MAO-A</strong> and <strong>MAO-B</strong> raises synaptic serotonin, dopamine, and norepinephrine levels. <strong>HPA axis</strong> modulation via glucocorticoid receptor sensitisation reduces cortisol hypersecretion under chronic stress. Upregulation of <strong>BDNF</strong> and <strong>5-HT1A</strong> receptor expression in the prefrontal cortex contributes to the antidepressant effect. Salidroside activates <strong>Nrf2/HO-1</strong> antioxidant defence. Rosavins stimulate <strong>β-endorphin</strong> release via opioidergic pathways, contributing to mood elevation.",
      "pharmacokinetics": {
        "absorption": "Salidroside is rapidly and well absorbed; Cmax at approximately 1 hour post-dose. Oral bioavailability of salidroside is ~70%. Rosavin absorption is lower; partially hydrolysed in the gut to rosaric acid. Food slightly delays but does not significantly reduce bioavailability.",
        "distribution": "Salidroside crosses the blood-brain barrier; detected in brain tissue within 30 minutes in rodent models. p-Tyrosol distributes to all tissues with confirmed CNS penetration. Plasma protein binding of salidroside is low (<30%), allowing a high free fraction for tissue distribution.",
        "metabolism": "Salidroside is hydrolysed to p-tyrosol and glucose by intestinal and hepatic β-glucosidase. p-Tyrosol is conjugated by hepatic UGT enzymes (glucuronidation, sulfation). Rosavins undergo ester hydrolysis. CYP3A4 involvement is minor.",
        "excretion": "Primarily urinary as glucuronide conjugates of p-tyrosol. Half-life of salidroside ~4.5 hours. Rosavin metabolites excreted via bile."
      },
      "safety_and_interactions": {
        "drug_interactions": "MAO inhibitors — pharmacodynamic potentiation of monoamine increase; hypertensive crisis risk; contraindicated. Antidepressants (SSRIs, SNRIs, bupropion) — additive serotonergic/noradrenergic activity; serotonin syndrome risk at high doses. Stimulants (caffeine, modafinil, methylphenidate) — additive CNS stimulation; tachycardia, hypertension. Antidiabetic agents — salidroside has intrinsic glucose-lowering properties; additive hypoglycaemia risk. P-glycoprotein substrates (digoxin, tacrolimus) — salidroside inhibits P-gp efflux transporter; plasma levels may increase.",
        "toxicity": "LD50 >3,000 mg/kg in mice (oral). No serious adverse events at therapeutic doses (200–600 mg/day) across all published clinical trials. Activating and stimulant-like properties may unmask hypomania in bipolar disorder."
      },
      "special_precautions": {
        "pregnancy": "No human safety data available. Animal studies show no teratogenicity at therapeutic doses, but insufficient evidence to recommend use. Avoid during pregnancy.",
        "lactation": "Excretion in breast milk unknown. Avoid due to insufficient safety data.",
        "hepatic_impairment": "UGT-mediated glucuronidation is the primary metabolic route; impaired glucuronidation in liver disease may increase p-tyrosol exposure. No formal dose adjustment guidelines. Use with caution.",
        "renal_impairment": "Conjugated metabolites are primarily renally excreted. Accumulation possible in CKD stage 4–5. Monitor renal function in severe impairment."
      }
    },
    "consumer_view": {
      "tagline": "Fights fatigue and lifts mood — one of the fastest-acting herbal adaptogens",
      "what_it_does": "Rhodiola is an Arctic herb that helps your body and mind recover from exhaustion and mental burnout. Unlike most herbal remedies, it can reduce fatigue noticeably within a few days. It also has mild antidepressant-like effects and is popular with students, professionals under pressure, and athletes.",
      "typical_uses": [
        "Mental and physical fatigue",
        "Burnout and work-related exhaustion",
        "Exam and performance stress",
        "Mild depression and low mood",
        "Athletic endurance and recovery"
      ],
      "suggested_dose": "200–400 mg of standardised extract (≥3% rosavins, ≥1% salidroside) once daily, taken in the morning or early afternoon. Do not take after 2 pm — it is activating. Start with 200 mg; increase to 400 mg after 1 week if well tolerated.",
      "onset": "Anti-fatigue and focus: 3–7 days. Mood stabilisation and stress resilience: 2–4 weeks.",
      "safety_snapshot": [
        "Take in the morning only — causes insomnia if taken late in the day",
        "Avoid if you have bipolar disorder",
        "Do not combine with antidepressants or MAO inhibitors without medical supervision"
      ]
    }
  }
]

DATA_FILE = "data.json"

with open(DATA_FILE, encoding="utf-8") as f:
    data = json.load(f)

existing = {d["scientific_name"] for d in data}
added = 0
for plant in PLANTS:
    if plant["scientific_name"] in existing:
        print(f"SKIP (already exists): {plant['scientific_name']}")
    else:
        data.append(plant)
        added += 1
        print(f"ADDED: {plant['scientific_name']}")

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nDone — {added} plants added. data.json now has {len(data)} entries.")
