#!/usr/bin/env python3
"""Batch 4 — Curcuma longa, Zingiber officinale, Boswellia serrata, Salix alba"""
import json

PLANTS = [
  {
    "scientific_name": "Curcuma longa",
    "common_name": "Turmeric",
    "type": "Plant",
    "article_count": 6753,
    "primary_categories": ["Anti-inflammatory", "Neuroprotection", "Oncology support", "Antioxidant"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42152667/",
        "https://pubmed.ncbi.nlm.nih.gov/42142792/",
        "https://pubmed.ncbi.nlm.nih.gov/42136296/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Turmeric has been used in Ayurvedic and traditional Chinese medicine for over 4,000 years. In Ayurveda it is known as 'haridra' or 'kanchani' (golden goddess) and is classified as a bitter tonic, blood purifier, and wound healer. Used extensively in Unani medicine and throughout South and Southeast Asia as a culinary spice, dye, and medicine for liver conditions, skin disorders, and inflammation. Marco Polo noted its similarities to saffron during his travels through China in 1280 CE.",
      "modern_application": "Curcumin — the principal curcuminoid — is one of the most extensively studied plant compounds in biomedical research, with over 6,000 PubMed publications. Despite extraordinary preclinical breadth (anti-inflammatory, neuroprotective, anti-cancer, antidiabetic), clinical translation has been limited by extremely poor oral bioavailability (<1%). Advanced delivery systems (BCM-95, Theracurmin, Meriva phospholipid complex, nano-curcumin) achieve 10–20-fold higher plasma concentrations and have shown clinical benefit in osteoarthritis (non-inferior to ibuprofen in two RCTs), ulcerative colitis, depression (adjunct to antidepressants), and metabolic syndrome.",
      "side_effects": "Generally very safe at culinary doses. At high supplemental doses (>8 g/day): GI upset, nausea, diarrhoea, flatulence. Rare: contact dermatitis. High-dose piperine combinations may cause GI irritation. Potential pro-oxidant at very high doses. Yellow staining of skin and stool. Oxalate content — high-dose chronic use may increase kidney stone risk in susceptible individuals.",
      "contraindications": "Caution with anticoagulants (warfarin, heparin, aspirin) — curcumin has antiplatelet activity; INR monitoring required. Avoid high doses in cholelithiasis (gallstones) — curcumin stimulates bile duct contraction. Caution before surgery (antiplatelet effects). Avoid high doses in pregnancy (uterotonic at pharmacological doses). Caution with iron supplementation — curcumin chelates iron."
    },
    "clinical_data": {
      "used_part": "Rhizome (dried and powdered; standardised curcuminoid extract)",
      "primary_active_compounds": [
        "Curcumin (diferuloylmethane; primary curcuminoid — 77% of curcuminoid content)",
        "Demethoxycurcumin (17% of curcuminoids)",
        "Bisdemethoxycurcumin (6% of curcuminoids)",
        "Ar-turmerone, α-turmerone, β-turmerone (sesquiterpene ketones in volatile oil)",
        "Cyclocurcumin (minor curcuminoid)",
        "Zingiberene (sesquiterpene shared with ginger)"
      ],
      "mechanism_of_action": "Curcumin inhibits <strong>NF-κB</strong> transcription factor by preventing IκBα phosphorylation and proteasomal degradation, suppressing expression of <strong>COX-2</strong>, <strong>iNOS</strong>, <strong>TNF-α</strong>, <strong>IL-1β</strong>, and <strong>IL-6</strong>. Inhibits the <strong>JAK/STAT3</strong> signalling pathway, relevant to cancer cell survival and immune evasion. Activates <strong>Nrf2/HO-1</strong> antioxidant response element, upregulating superoxide dismutase and glutathione. Inhibits amyloid-β (<strong>Aβ</strong>) aggregation and tau phosphorylation via <strong>GSK-3β</strong> inhibition — neuroprotective in Alzheimer's models. Promotes cancer cell apoptosis via modulation of the <strong>Bcl-2/Bax</strong> ratio and inhibition of <strong>EGFR</strong> and <strong>VEGF</strong> receptor signalling. Upregulates <strong>BDNF</strong>, contributing to antidepressant effects.",
      "pharmacokinetics": {
        "absorption": "Native curcumin has extremely poor oral bioavailability (<1%) due to low aqueous solubility, poor intestinal absorption, and rapid first-pass metabolism. Enhanced formulations: BCM-95 (curcumin with turmeric volatile oils) achieves 7-fold improvement; Theracurmin (nano-colloidal dispersion) 27-fold; Meriva (phospholipid complex) 29-fold; piperine (20 mg) co-administration achieves 20-fold increase. Cmax at 1–2 hours post-dose with enhanced formulations.",
        "distribution": "Poorly distributed systemically due to rapid metabolism. With enhanced formulations, curcumin and metabolites reach liver, colon, kidney, and brain. Curcumin crosses the blood-brain barrier. Plasma protein binding >99% (albumin). Accumulates in GI mucosa — relevant to local anti-inflammatory effects.",
        "metabolism": "Extensive and rapid hepatic and intestinal metabolism. Phase I: reduction to dihydrocurcumin, tetrahydrocurcumin (THC) by aldo-keto reductases. Phase II: glucuronidation (UGT1A1, UGT1A8) and sulfation. THC is itself biologically active. Curcumin also degrades rapidly in alkaline pH (>7.4) via non-enzymatic hydrolysis.",
        "excretion": "Primarily biliary/faecal (>85%); urinary excretion of glucuronide conjugates minimal. Half-life of native curcumin in plasma ~1–2 hours; THC metabolites longer-lived. Enhanced formulations show plasma half-lives of 4–8 hours."
      },
      "safety_and_interactions": {
        "drug_interactions": "Anticoagulants (warfarin, heparin) — antiplatelet activity and possible CYP2C9 inhibition; monitor INR. Antiplatelet drugs (aspirin, clopidogrel) — additive bleeding risk. Chemotherapy agents (doxorubicin, cyclophosphamide) — preclinical evidence of both sensitisation and antagonism; clinical data insufficient; consult oncologist. Iron supplements — curcumin chelates iron, reducing absorption; separate by ≥2 hours. Piperine combinations — 20-fold increase in curcumin bioavailability also increases bioavailability of co-administered drugs (important drug interaction risk amplifier). CYP3A4, CYP2C9, CYP1A2 substrates — curcumin inhibits multiple CYPs at high doses.",
        "toxicity": "LD50 >10 g/kg in mice (oral). Phase I clinical trials demonstrated tolerability up to 12 g/day. GI side effects dose-limiting at very high doses. Oxalate content in turmeric powder: ~91 mg per 100 g — high-dose chronic use increases urinary oxalate and stone risk in susceptible individuals. No clinically significant hepatotoxicity documented."
      },
      "special_precautions": {
        "pregnancy": "Culinary quantities are safe. High supplemental doses (≥500 mg curcumin extracts) should be avoided — uterotonic activity at pharmacological doses and insufficient safety data.",
        "lactation": "No evidence of harm at dietary intake. High-dose extracts not studied; avoid during breastfeeding.",
        "hepatic_impairment": "Hepatoprotective at standard doses. Caution at very high doses — extensive hepatic metabolism may be impaired. No formal dose adjustment guidelines. Monitor if using with other hepatically metabolised drugs.",
        "renal_impairment": "High oxalate content in turmeric powder poses kidney stone risk with chronic high-dose use in CKD or stone-formers. Use purified curcumin extracts (low oxalate) rather than whole turmeric powder in renal impairment."
      }
    },
    "consumer_view": {
      "tagline": "Powerful anti-inflammatory — but only works if you take the right form",
      "what_it_does": "Turmeric is one of nature's most potent anti-inflammatory compounds, shown in trials to rival ibuprofen for joint pain — without GI bleeding risk. The catch: regular turmeric powder is almost completely unabsorbed. You must use a bioavailability-enhanced form (with piperine, phospholipids, or nano-particle technology) to get meaningful blood levels.",
      "typical_uses": [
        "Osteoarthritis and joint pain",
        "Inflammatory bowel conditions (Crohn's, UC)",
        "Adjunct support in depression",
        "Metabolic syndrome and blood sugar regulation",
        "General anti-inflammatory and antioxidant support"
      ],
      "suggested_dose": "400–600 mg of curcumin (not turmeric) from an enhanced-bioavailability form: BCM-95, Theracurmin, Meriva, or standard curcumin + 20 mg piperine (black pepper extract), 2–3 times daily with food. Avoid plain turmeric powder capsules — they are largely inactive.",
      "onset": "Acute anti-inflammatory effects: 2–4 weeks. Joint pain relief and metabolic effects: 6–8 weeks of consistent use.",
      "safety_snapshot": [
        "Avoid high doses with blood thinners (warfarin, aspirin)",
        "Do not take before surgery",
        "If prone to kidney stones, use purified curcumin extract not whole turmeric powder"
      ]
    }
  },
  {
    "scientific_name": "Zingiber officinale",
    "common_name": "Ginger",
    "type": "Plant",
    "article_count": 3808,
    "primary_categories": ["Anti-inflammatory", "Antiemetic", "GI support", "Analgesic"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42153012/",
        "https://pubmed.ncbi.nlm.nih.gov/42128790/",
        "https://pubmed.ncbi.nlm.nih.gov/42126587/"
      ]
    },
    "narrative_summary": {
      "historical_use": "One of the most ancient and globally distributed medicinal spices, cultivated for over 5,000 years. First described in the Chinese pharmacopoeia Shennong Ben Cao Jing (c. 100 CE). The name 'ginger' derives from the Sanskrit 'srngaveram' (horn root). Traded along the Silk Road and Arab spice routes for millennia. In medieval Europe it was so highly valued it was used to pay rent and taxes. Hippocrates and Dioscorides both described its GI and warming properties. Ayurveda calls it 'vishwabhesaj' (universal medicine).",
      "modern_application": "Among the best-evidenced herbal medicines for nausea and vomiting. A 2014 Cochrane review confirmed efficacy for nausea and vomiting of pregnancy (NVP) with a safety profile comparable to vitamin B6. Multiple RCTs confirm benefit for chemotherapy-induced nausea (CINV) as an adjunct to standard antiemetics. For pain, a 2015 systematic review of 5 RCTs found significant reduction in dysmenorrhoea; anti-inflammatory effects in osteoarthritis are equivalent to ibuprofen in some RCTs. Effective dose: 1–2 g of dried ginger or 250 mg of standardised extract (5% gingerols) twice daily.",
      "side_effects": "Heartburn and gastric reflux are the most common complaints, especially at doses >2 g. Mouth and throat irritation from fresh ginger. Diarrhoea at high doses. Increased bleeding time (antiplatelet effect). Rare: allergic reactions. May potentiate hypoglycaemia in combination with antidiabetic drugs. Excessive consumption during pregnancy debated — therapeutic doses appear safe but very high doses should be avoided.",
      "contraindications": "Caution with anticoagulants and antiplatelet drugs (additive bleeding risk). Avoid high doses (>4 g/day) in pregnancy. Caution in patients with active peptic ulcer disease or severe GERD (gastric irritation). Caution before surgery (antiplatelet activity — discontinue ≥1 week pre-operatively at high doses)."
    },
    "clinical_data": {
      "used_part": "Rhizome (fresh — zingiber recens; dried — zingiber siccum; steam-distilled essential oil)",
      "primary_active_compounds": [
        "6-Gingerol (primary pungent compound in fresh ginger; anti-inflammatory, antiemetic)",
        "8-Gingerol and 10-gingerol (homologous gingerols)",
        "6-Shogaol (dehydrated gingerol; formed on drying/heating; more potent anti-inflammatory than gingerol)",
        "Zingerone (formed from 6-gingerol on heating; milder, less pungent)",
        "6-Paradol (formed from gingerols; antimicrobial)",
        "Zingiberene and bisabolene (sesquiterpenes in essential oil)",
        "Galanolactone (diterpenoid; 5-HT3 antagonist)"
      ],
      "mechanism_of_action": "6-Gingerol and 6-shogaol dually inhibit <strong>COX-1</strong>/<strong>COX-2</strong> and <strong>5-LOX</strong> (lipoxygenase), reducing both prostaglandin E2 and leukotriene B4 synthesis — a combined anti-inflammatory mechanism distinct from NSAIDs (COX-only). Antiemetic activity via peripheral <strong>5-HT3 receptor</strong> antagonism in the gut (reducing afferent vagal signalling to the vomiting centre) and weak <strong>D2 receptor</strong> antagonism. Galanolactone is a competitive <strong>5-HT3</strong> antagonist. Gastric prokinetic via <strong>motilin receptor</strong> agonism, accelerating gastric emptying. Thermogenic via activation of <strong>TRPV1</strong> (transient receptor potential vanilloid 1 channel). Antiplatelet via suppression of <strong>thromboxane A2 (TXA2)</strong> synthesis and inhibition of <strong>COX-1</strong>-dependent platelet activation.",
      "pharmacokinetics": {
        "absorption": "6-Gingerol is rapidly absorbed from the upper GI tract; Cmax at 30–60 minutes. 6-Shogaol forms from gingerols during drying and heating and is more bioavailable from dried preparations. Bioavailability enhanced when taken with food. Fresh and dried ginger have different active compound profiles.",
        "distribution": "Gingerols and shogaols distribute widely to GI mucosa, liver, and peripheral inflammatory tissues. 6-Shogaol crosses the blood-brain barrier (rodent data). Plasma protein binding estimated at 70–80%. Volume of distribution not well characterised in humans.",
        "metabolism": "Extensive hepatic conjugation. 6-Gingerol undergoes glucuronidation and sulfation; also reduced to 6-gingerdiols and oxidised to 6-oxogingero by hepatic reductases and oxidases. 6-Shogaol is more stable metabolically. CYP1A2 and CYP3A4 involvement documented. Short half-life of 1–2 hours necessitates multiple daily dosing.",
        "excretion": "Urinary excretion of glucuronide and sulfate conjugates. Biliary excretion of metabolites. Half-life of 6-gingerol approximately 1.5 hours; 6-shogaol ~2 hours. Enterohepatic recirculation minor."
      },
      "safety_and_interactions": {
        "drug_interactions": "Anticoagulants (warfarin, heparin) — additive antiplatelet activity (TXA2 inhibition); monitor INR, especially at doses >2 g/day. Antiplatelet drugs (aspirin, clopidogrel) — additive bleeding risk. Antidiabetic agents (insulin, metformin, sulfonylureas) — additive glucose-lowering via AMPK pathway; hypoglycaemia risk. Antihypertensives — additive BP reduction via vasodilatory effects. Calcium channel blockers — 6-shogaol inhibits vascular smooth muscle Ca²⁺ channels; potentiation possible. Chemotherapy antiemetics (ondansetron) — additive 5-HT3 antagonism; potentially beneficial combination.",
        "toxicity": "LD50 >5,000 mg/kg in mice (oral). No clinically significant toxicity at therapeutic doses (<4 g/day). GI irritation (heartburn, ulceration) at very high doses in susceptible individuals. No hepatotoxicity or nephrotoxicity documented. Mutagenicity assays negative for gingerols at therapeutic concentrations."
      },
      "special_precautions": {
        "pregnancy": "Therapeutic doses (1 g/day) are considered safe and effective for NVP based on multiple RCTs. Avoid doses >2 g/day during pregnancy; very high doses may have uterotonic effects. First trimester exposure in large observational studies shows no increased malformation risk.",
        "lactation": "No documented harm at dietary or standard therapeutic doses. Excreted in breast milk in small amounts. Considered compatible with breastfeeding by most authorities.",
        "hepatic_impairment": "Hepatoprotective effects documented in NAFLD models. No contraindication at therapeutic doses. Hepatic CYP1A2 and CYP3A4 involvement; drug interaction risk higher in severe liver disease.",
        "renal_impairment": "No specific contraindication. Metabolites renally excreted; no dose adjustment guidelines established. Monitor in severe renal impairment."
      }
    },
    "consumer_view": {
      "tagline": "Relieves nausea, eases joint pain, and fights inflammation — naturally and safely",
      "what_it_does": "Ginger is one of the most versatile and best-evidenced herbal medicines available. Clinical trials confirm it works for morning sickness, chemotherapy nausea, period pain, and arthritis. Unlike NSAIDs, it reduces inflammation through two separate pathways simultaneously, and it is safe enough to use during pregnancy.",
      "typical_uses": [
        "Nausea and vomiting (morning sickness, travel, chemotherapy)",
        "Period pain (dysmenorrhoea)",
        "Osteoarthritis and joint inflammation",
        "Bloating, indigestion, and slow digestion",
        "Cold and flu symptom relief"
      ],
      "suggested_dose": "Nausea: 1–1.5 g of dried ginger powder per day in divided doses. Pain and inflammation: 250 mg of standardised extract (5% gingerols) 2–4 times daily with food. Fresh ginger: 2–4 g of grated root daily. Capsules are preferred for anti-inflammatory use; tea or syrup for nausea.",
      "onset": "Nausea relief: 30–60 minutes for acute use. Anti-inflammatory and pain effects: 2–4 weeks of regular use.",
      "safety_snapshot": [
        "Can cause heartburn at high doses — take with food",
        "Avoid more than 1 g/day in the first trimester without medical advice",
        "May increase bleeding — stop 1 week before surgery"
      ]
    }
  },
  {
    "scientific_name": "Boswellia serrata",
    "common_name": "Indian frankincense / Shallaki / Salai guggul",
    "type": "Plant",
    "article_count": 1149,
    "primary_categories": ["Anti-inflammatory", "Analgesic", "Neuroprotection", "Respiratory"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42130642/",
        "https://pubmed.ncbi.nlm.nih.gov/42102034/",
        "https://pubmed.ncbi.nlm.nih.gov/42057627/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Boswellia resin (frankincense) has been valued for millennia in Ayurvedic, Unani, and traditional African and Middle Eastern medicine. Among the world's oldest traded commodities — ancient Egyptian hieroglyphs document frankincense trade routes from the Punt region (present-day Somalia). In Ayurveda, Boswellia serrata (Shallaki) has been used for over 3,000 years for joint conditions, diarrhoea, skin diseases, and as a lung tonic. Mentioned in the Sushruta Samhita for musculoskeletal pain. Frankincense was one of the gifts brought to the infant Jesus — reflecting its immense historical value.",
      "modern_application": "The most clinically distinctive feature of Boswellia is its selective inhibition of 5-lipoxygenase (5-LOX) — the enzyme responsible for leukotriene synthesis — rather than COX enzymes targeted by NSAIDs. This explains its efficacy without GI bleeding risk. A 2003 RCT (Kimmatkar et al.) demonstrated significant reduction in knee OA pain, swelling, and walking distance versus placebo. A 2011 RCT showed AKBA-enriched Boswellia extract (5-Loxin) superior to celecoxib for knee OA at 90 days. Evidence also supports benefit in asthma, Crohn's disease, and ulcerative colitis. Standardised extracts enriched in AKBA (3-O-acetyl-11-keto-β-boswellic acid) are the most clinically validated.",
      "side_effects": "Well tolerated in clinical trials. GI discomfort (nausea, acid reflux) most common — reduced when taken with food. Diarrhoea and skin rash reported infrequently. No significant haematological, hepatic, or renal adverse effects in RCTs of up to 6 months. Less GI toxicity than NSAIDs at equivalent anti-inflammatory doses — a key clinical advantage.",
      "contraindications": "Caution with anticoagulants — boswellic acids may have antiplatelet activity. Caution before surgery. Limited pregnancy data — avoid high-dose supplemental use in pregnancy (traditional use suggests safety at culinary exposure). Caution in patients with peptic ulcer or severe GERD at high doses."
    },
    "clinical_data": {
      "used_part": "Oleo-gum resin (exudate from trunk incisions); standardised extract (enriched boswellic acids)",
      "primary_active_compounds": [
        "3-O-Acetyl-11-keto-β-boswellic acid (AKBA — most potent 5-LOX inhibitor)",
        "11-Keto-β-boswellic acid (KBA)",
        "α-Boswellic acid and β-boswellic acid (principal boswellic acids by mass)",
        "3-O-Acetyl-α-boswellic acid (AABA)",
        "Incensole acetate (diterpene; anti-inflammatory, neuroprotective; TRPV3 agonist)",
        "Lupeolic acid (triterpenoid)"
      ],
      "mechanism_of_action": "AKBA is a selective, non-competitive inhibitor of <strong>5-lipoxygenase (5-LOX)</strong>, blocking conversion of arachidonic acid to leukotriene A4 and downstream pro-inflammatory leukotrienes (LTB4, LTC4, LTD4). Unlike NSAIDs, Boswellia does not inhibit <strong>COX-1</strong> or <strong>COX-2</strong> — preserving gastric prostaglandin production and explaining its GI safety advantage. Also inhibits <strong>microsomal prostaglandin E synthase-1 (mPGES-1)</strong>, reducing PGE2. Prevents cartilage degradation by inhibiting <strong>matrix metalloprotease-3 (MMP-3)</strong> and <strong>MMP-13</strong>. Incensole acetate activates <strong>TRPV3</strong> receptor and modulates <strong>NF-κB</strong> signalling, with additional neuroprotective and anxiolytic activity in animal models. Inhibits complement activation via <strong>C3-convertase</strong> suppression.",
      "pharmacokinetics": {
        "absorption": "Boswellic acids are poorly absorbed due to high lipophilicity and large molecular size. Bioavailability is substantially enhanced by co-administration with a high-fat meal (up to 10-fold) or phospholipid complexation (Casperome/Phytosome). Plasma protein binding >95% for AKBA. Cmax of AKBA at 4–5 hours post-dose with standard extract.",
        "distribution": "Distributes to synovial fluid and joint tissue (target organ for arthritis), lung tissue, and intestinal mucosa. High plasma protein binding limits free fraction. Accumulates in inflamed tissues due to increased vascular permeability. Incensole acetate crosses the blood-brain barrier.",
        "metabolism": "Hepatic glucuronidation (UGT enzymes) is the primary metabolic pathway. β-Oxidation of the pentacyclic triterpenoid backbone. CYP3A4 minor involvement. Half-life of AKBA estimated at 5–7 hours (formulation-dependent). Enterohepatic recirculation extends effective exposure.",
        "excretion": "Primarily biliary and faecal. Urinary excretion of glucuronide conjugates minor. Half-life of boswellic acid glucuronides ~6 hours. Slow accumulation over repeated dosing due to enterohepatic recirculation."
      },
      "safety_and_interactions": {
        "drug_interactions": "Anticoagulants (warfarin) — possible additive antiplatelet activity; monitor INR. NSAIDs — additive anti-inflammatory effect via complementary pathways (COX + 5-LOX inhibition); combination may enhance efficacy with reduced NSAID dose requirements. P-glycoprotein substrates — boswellic acids inhibit P-gp; possible increased absorption of co-administered P-gp substrates (digoxin, loperamide, certain chemotherapy agents). CYP3A4 substrates — minor inhibition; clinically relevant at high doses only.",
        "toxicity": "LD50 >5,000 mg/kg in rodents (oral). No clinically significant toxicity in RCTs of up to 6 months at 1,000–3,600 mg/day. No haematological, hepatic, or renal toxicity documented. GI side effects dose-dependent and manageable."
      },
      "special_precautions": {
        "pregnancy": "Insufficient clinical safety data. Traditionally used in Ayurvedic medicine during pregnancy, but high-dose extracts not validated for safety. Avoid concentrated AKBA-enriched supplements in pregnancy.",
        "lactation": "No data on excretion in breast milk. Avoid high-dose supplements during breastfeeding.",
        "hepatic_impairment": "UGT-mediated glucuronidation impaired in severe liver disease; boswellic acid exposure may increase. No formal dose adjustment guidelines. Use with monitoring.",
        "renal_impairment": "No specific renal toxicity documented. Glucuronide conjugates partly renally excreted. No dose adjustment guidelines established; standard monitoring in severe renal impairment."
      }
    },
    "consumer_view": {
      "tagline": "Anti-inflammatory that protects your joints and gut — without the stomach side effects of NSAIDs",
      "what_it_does": "Boswellia is frankincense — the ancient resin prized for millennia — and modern science has shown it is one of the most effective natural anti-inflammatories available. Unlike ibuprofen and similar drugs, it targets a completely different inflammation pathway, making it safe on the stomach and suitable for long-term use. Clinical trials show real benefit for arthritis, asthma, and inflammatory bowel disease.",
      "typical_uses": [
        "Osteoarthritis and joint pain",
        "Asthma and chronic respiratory inflammation",
        "Inflammatory bowel disease (Crohn's, UC)",
        "Back pain and musculoskeletal inflammation",
        "Long-term anti-inflammatory support"
      ],
      "suggested_dose": "300–500 mg of standardised Boswellia extract (containing ≥30% boswellic acids, ≥10% AKBA) 2–3 times daily, taken with a meal containing fat (essential for absorption). Allow 4–8 weeks for full anti-inflammatory effect.",
      "onset": "Pain and swelling reduction: 2–4 weeks. Cartilage protection and sustained relief: 6–12 weeks of regular use.",
      "safety_snapshot": [
        "Must be taken with food containing fat — absorption is negligible without it",
        "Generally safe for long-term use unlike NSAIDs — no stomach lining damage",
        "Tell your doctor if taking blood thinners or P-gp-dependent medications"
      ]
    }
  },
  {
    "scientific_name": "Salix alba",
    "common_name": "White willow / Willow bark",
    "type": "Plant",
    "article_count": 4072,
    "primary_categories": ["Analgesic", "Anti-inflammatory", "Antipyretic"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42148282/",
        "https://pubmed.ncbi.nlm.nih.gov/42142901/",
        "https://pubmed.ncbi.nlm.nih.gov/42130174/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Willow bark is one of the oldest analgesics known to humanity. Papyrus texts from ancient Egypt (c. 1550 BCE) describe its use for fever and pain. Hippocrates recommended it for fever and labour pains. The active principle, salicin, was first isolated in 1828 by French pharmacist Henri Leroux and purified by Italian chemist Raffaele Piria. Felix Hoffmann at Bayer then synthesised the acetylated derivative — acetylsalicylic acid — in 1897, giving birth to aspirin. Willow bark is thus the direct progenitor of one of the most prescribed drugs in history.",
      "modern_application": "Multiple high-quality RCTs support willow bark extract for low back pain (2000, Chrubasik et al. — equivalent to rofecoxib), osteoarthritis, and headache. A standardised extract providing 240 mg salicin daily is the most studied dose. An important advantage over aspirin: willow bark's multicomponent salicylate matrix does not acetylate COX enzymes and causes significantly less GI mucosal damage, making it suitable for patients who cannot tolerate aspirin. ESCOP (European Scientific Cooperative on Phytotherapy) recognises willow bark for low back pain and feverish conditions.",
      "side_effects": "GI intolerance (nausea, heartburn, diarrhoea) less common than with aspirin. Allergic reactions in aspirin-hypersensitive individuals (cross-reactivity — avoid in aspirin allergy). Rare: renal impairment with high-dose chronic use (salicylate nephropathy). Increased bleeding time. Reye's syndrome risk in children with viral illness (salicylate class effect — avoid in under-16s during viral illness). No antiplatelet effect as strong as aspirin.",
      "contraindications": "Contraindicated in aspirin or salicylate hypersensitivity. Avoid in children under 16 with viral illness (Reye's syndrome risk — salicylate class). Avoid with anticoagulants (additive bleeding risk). Avoid in peptic ulcer disease and severe GERD. Caution before surgery. Avoid in third trimester of pregnancy (premature ductus arteriosus closure)."
    },
    "clinical_data": {
      "used_part": "Bark of young branches (dried; aqueous or hydroethanolic extract)",
      "primary_active_compounds": [
        "Salicin (phenolic glycoside — primary prodrug; 1–12% in bark)",
        "Salicortin and tremulacin (salicin esters; more potent anti-inflammatory than salicin alone)",
        "Fragilin and populin (related phenolic glycosides)",
        "Quercetin, naringenin, catechin, and epicatechin (flavonoids — contribute COX-2 and 5-LOX inhibition)",
        "Chlorogenic acid and caffeic acid (phenolic acids)",
        "Tannins (condensed proanthocyanidins)"
      ],
      "mechanism_of_action": "Salicin is hydrolysed in the gut by β-glucosidase to saligenin (salicyl alcohol), which is then hepatically oxidised to salicylic acid — the primary active metabolite. Salicylic acid inhibits <strong>COX-1</strong> and <strong>COX-2</strong> non-selectively (unlike aspirin, without acetylation), reducing prostaglandin synthesis and producing analgesic, antipyretic, and anti-inflammatory effects. Inhibits <strong>NF-κB</strong> directly (aspirin-independent pathway) — reduces <strong>IL-6</strong>, <strong>TNF-α</strong>. Flavonoid fraction (quercetin, catechin) provides complementary <strong>COX-2</strong> and <strong>5-LOX</strong> inhibition, explaining the broader anti-inflammatory profile compared to purified salicylate alone. Tannins provide astringent and antipyretic effects at mucosal surfaces.",
      "pharmacokinetics": {
        "absorption": "Salicin is rapidly hydrolysed in the small intestine and colon; saligenin absorbed and converted to salicylic acid in liver. Salicylic acid Cmax at 1.5–2.5 hours after willow bark extract. Bioavailability of salicylate from willow bark is lower than equivalent aspirin dose, explaining reduced GI toxicity but also reduced antiplatelet potency. Flavonoids absorbed with moderate bioavailability.",
        "distribution": "Salicylic acid distributes widely; plasma protein binding 80–90% (concentration-dependent). Crosses the blood-brain barrier (antipyretic CNS effect). Distributes to synovial fluid in inflamed joints. Volume of distribution ~0.15 L/kg (salicylate).",
        "metabolism": "Hepatic. Salicylic acid undergoes conjugation with glycine (salicyluric acid — primary route, saturable), glucuronidation (UGT enzymes), and oxidation to gentisic acid and catechol. Saturation of glycine conjugation at high doses causes non-linear pharmacokinetics at therapeutic doses. Flavonoids conjugated by UGT1A1 and sulfotransferases.",
        "excretion": "Urinary excretion of salicyluric acid (75%), salicylate glucuronides (10%), free salicylate (10%). Half-life of salicylate 2–3 hours at low doses; extends to 15–30 hours at high doses (non-linear). Urinary pH significantly affects salicylate excretion (alkaline pH increases renal clearance)."
      },
      "safety_and_interactions": {
        "drug_interactions": "Anticoagulants (warfarin, heparin) — additive antiplatelet and anti-inflammatory effects; increased bleeding risk; monitor INR. Antiplatelet drugs (aspirin, clopidogrel) — additive bleeding; avoid combination. NSAIDs (ibuprofen, naproxen, diclofenac) — additive GI toxicity and nephrotoxicity. Methotrexate — salicylates reduce methotrexate renal clearance; toxicity risk. ACE inhibitors and antihypertensives — salicylates may blunt antihypertensive effect (renal prostaglandin inhibition). Uricosuric drugs (probenecid, sulfinpyrazone) — salicylates antagonise urate excretion at low doses.",
        "toxicity": "Salicylate poisoning (salicylism) at high doses: tinnitus, nausea, hyperventilation, metabolic acidosis. Reye's syndrome (rare, potentially fatal encephalopathy and liver failure) with salicylate use in children during viral illness — class effect. Aspirin cross-sensitivity reactions: urticaria, bronchospasm, anaphylaxis in susceptible individuals. Chronic high-dose salicylate nephropathy possible with prolonged use."
      },
      "special_precautions": {
        "pregnancy": "Avoid in the third trimester — salicylates cause premature closure of the ductus arteriosus and may prolong labour. Use in early pregnancy only under medical supervision.",
        "lactation": "Salicylate excreted in breast milk. Occasional use at low doses generally considered safe; avoid regular high-dose use during breastfeeding.",
        "hepatic_impairment": "Salicylate conjugation (glycine, glucuronide) impaired in liver disease; accumulation risk. Reduce dose and monitor plasma salicylate levels in severe hepatic impairment.",
        "renal_impairment": "Salicylate primarily renally excreted; significant accumulation in renal failure. NSAIDs and salicylates reduce renal prostaglandin synthesis — may precipitate acute kidney injury. Avoid in moderate-to-severe renal impairment."
      }
    },
    "consumer_view": {
      "tagline": "The original aspirin — natural pain and fever relief from the bark that inspired the drug",
      "what_it_does": "White willow bark is where aspirin came from. The salicin in the bark converts to salicylic acid in your body — the same anti-inflammatory compound — but works more gently, with less stomach irritation. Clinical trials show it is effective for back pain, arthritis, and headache. Unlike aspirin, it does not strongly thin the blood.",
      "typical_uses": [
        "Low back pain",
        "Osteoarthritis and joint pain",
        "Headache and migraine",
        "Fever and flu symptoms",
        "Menstrual pain"
      ],
      "suggested_dose": "Extract standardised to deliver 240 mg salicin per day (typically 400–800 mg dried bark extract), divided into 2–3 doses with food. Allow 1–2 weeks for full anti-inflammatory effects to develop.",
      "onset": "Fever and acute pain: 1–2 hours. Chronic inflammatory pain (OA, back pain): 1–2 weeks of regular use.",
      "safety_snapshot": [
        "Avoid if you are allergic to aspirin — cross-reactivity is common",
        "Do not give to children under 16 during a fever or viral illness (Reye's syndrome risk)",
        "Avoid in the last 3 months of pregnancy"
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
