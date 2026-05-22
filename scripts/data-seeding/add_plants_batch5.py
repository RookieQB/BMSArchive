#!/usr/bin/env python3
"""Batch 5 — Berberis vulgaris, Silybum marianum, Allium sativum, Cinnamomum verum"""
import json

PLANTS = [
  {
    "scientific_name": "Berberis vulgaris",
    "common_name": "Barberry / European barberry",
    "type": "Plant",
    "article_count": 280,
    "primary_categories": ["Antidiabetic", "Cardiovascular", "Antimicrobial", "Hepatoprotection"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42030670/",
        "https://pubmed.ncbi.nlm.nih.gov/41897491/",
        "https://pubmed.ncbi.nlm.nih.gov/41863266/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Barberry has been used medicinally for over 2,500 years across Persia, India, China, and Europe. Ancient Egyptians used it in combination with fennel to prevent plague. In Ayurveda, Berberis aristata (closely related) is known as 'daruharidra' and used for skin conditions, eye infections, and fever. Traditional Persian and Unani medicine employed barberry bark and root for liver disease, jaundice, and as a bitter tonic. The primary alkaloid berberine was first isolated in 1826 and has since become one of the most studied plant alkaloids in pharmacology.",
      "modern_application": "Berberine — the primary isoquinoline alkaloid — has accumulated substantial clinical evidence as a metabolic medicine. A landmark 2008 RCT (Zhang et al., Metabolism) found berberine 500 mg three times daily reduced HbA1c, fasting and postprandial glucose, and triglycerides in type 2 diabetes as effectively as metformin. A 2015 meta-analysis of 27 RCTs confirmed significant reductions in fasting blood glucose, HbA1c, and LDL-C. Berberine's PCSK9 inhibitory mechanism for LDL reduction is mechanistically distinct from statins, making it valuable for statin-intolerant patients. Emerging evidence for gut microbiome modulation and NAFLD treatment.",
      "side_effects": "GI side effects are the main tolerability concern: nausea, constipation, diarrhoea, and abdominal cramping — most pronounced in the first 1–2 weeks. Generally resolves with dose titration. Bitter taste. Rare: headache. Berberine crosses the placenta — contraindicated in pregnancy (neonatal jaundice risk via bilirubin displacement). Yellow discolouration of skin and mucous membranes at very high doses.",
      "contraindications": "Contraindicated in pregnancy (risk of neonatal jaundice; bilirubin displacement from albumin in neonates). Contraindicated in neonates and infants. Caution with antidiabetic drugs (additive hypoglycaemia). Caution with CYP3A4-metabolised drugs (significant inhibition). Avoid with cyclosporin (increased plasma levels). Caution with antibiotics — berberine inhibits gut bacteria including probiotic species."
    },
    "clinical_data": {
      "used_part": "Root bark and stem bark (dried; standardised extract or isolated berberine HCl)",
      "primary_active_compounds": [
        "Berberine (isoquinoline alkaloid — primary active; 0.5–6% in bark)",
        "Berbamine (bisbenzylisoquinoline alkaloid; immunosuppressive, anti-arrhythmic)",
        "Oxyacanthine (bisbenzylisoquinoline alkaloid)",
        "Palmatine and columbamine (protoberberine alkaloids)",
        "Chelidonic acid",
        "Tannins and resinous matter"
      ],
      "mechanism_of_action": "Berberine activates <strong>AMPK (AMP-activated protein kinase)</strong> via inhibition of mitochondrial complex I, increasing AMP:ATP ratio — a mechanism shared with metformin that improves insulin sensitivity, reduces hepatic glucose output, and promotes β-oxidation of fatty acids. Inhibits <strong>PTP1B (protein tyrosine phosphatase 1B)</strong>, enhancing insulin receptor signalling. Reduces LDL-cholesterol via dual mechanism: inhibition of <strong>PCSK9</strong> (proprotein convertase subtilisin/kexin type 9) transcription and upregulation of <strong>LDL receptor (LDLR)</strong> expression in hepatocytes. Antimicrobial via inhibition of <strong>bacterial DNA gyrase</strong> and <strong>topoisomerase IV</strong>. Mild inhibition of <strong>MAO-A</strong> and <strong>MAO-B</strong> may contribute to mood-stabilising effects. Modulates gut microbiome by selectively suppressing pathogenic bacteria and enriching short-chain fatty acid–producing species.",
      "pharmacokinetics": {
        "absorption": "Berberine has very poor oral bioavailability (~5%) due to active efflux by P-glycoprotein (P-gp) and multidrug resistance protein 1 (MRP1) at the intestinal wall. Despite low systemic levels, high local GI concentrations are therapeutically relevant for gut microbiome effects. Absorption enhanced by P-gp inhibitors (piperine 20 mg increases berberine bioavailability ~2-fold).",
        "distribution": "Widely distributed to liver, kidney, intestine, and muscle — key metabolic target organs. Berberine crosses the blood-brain barrier and accumulates in brain tissue. Plasma protein binding ~45%. Volume of distribution large (~44 L/kg) indicating extensive tissue binding.",
        "metabolism": "Primarily intestinal and hepatic. Berberine undergoes demethylation to berberrubine and thalifendine, reduction to dihydroberberine (more bioavailable form — preclinical), and glucuronidation/sulfation. Significant CYP2D6 and CYP3A4 inhibition — clinically relevant drug interaction risk. Enterohepatic recirculation extends effective exposure despite short plasma half-life.",
        "excretion": "Biliary excretion predominates. Urinary excretion of metabolites minor (~5%). Half-life of berberine approximately 3–6 hours. Dihydroberberine has longer half-life. Faecal excretion of unabsorbed berberine is high."
      },
      "safety_and_interactions": {
        "drug_interactions": "Antidiabetic agents (metformin, insulin, sulfonylureas, GLP-1 agonists) — additive glucose lowering; hypoglycaemia risk; monitor blood glucose carefully. Cyclosporin — CYP3A4 and P-gp inhibition significantly increases cyclosporin AUC; contraindicated or requires dose reduction with close monitoring. Warfarin — CYP2C9 inhibition may increase INR; monitor. Macrolide antibiotics (erythromycin, clarithromycin) — additive CYP3A4 inhibition and potential cardiac QT prolongation. Statins — berberine inhibits CYP3A4 (simvastatin, atorvastatin metabolism impaired); myopathy risk; use lower statin doses.",
        "toxicity": "LD50 ~25 mg/kg IV in mice; >1,000 mg/kg oral (large therapeutic window by oral route). GI side effects are dose-limiting. Neonatal jaundice (kernicterus) risk — berberine displaces bilirubin from albumin in neonates with immature blood-brain barrier; never use in neonates or during pregnancy at term. High-dose cardiac effects (QT prolongation) reported in vitro at supra-therapeutic concentrations."
      },
      "special_precautions": {
        "pregnancy": "Contraindicated throughout pregnancy. Berberine crosses the placenta and can cause neonatal jaundice (bilirubin displacement) and uterine contractions. Historically used as an abortifacient in traditional medicine.",
        "lactation": "Excreted in breast milk. Contraindicated during breastfeeding — neonatal jaundice risk persists in newborns fed breast milk containing berberine.",
        "hepatic_impairment": "Hepatoprotective effects at standard doses. Severe hepatic impairment impairs CYP2D6 and CYP3A4 metabolism; berberine plasma levels may increase. Drug interaction risks amplified. Use with caution and dose reduction.",
        "renal_impairment": "No specific contraindication at therapeutic doses. Metabolites partially renally excreted; accumulation in severe CKD possible. Monitor renal function."
      }
    },
    "consumer_view": {
      "tagline": "Natural metformin alternative — lowers blood sugar and cholesterol through the same cellular pathway",
      "what_it_does": "Berberine from barberry activates the same enzyme as metformin (the most prescribed diabetes drug) — making it one of the few herbal compounds with a well-understood mechanism comparable to a pharmaceutical. Clinical trials confirm it lowers blood sugar, HbA1c, and LDL cholesterol effectively, with the added benefit of improving gut bacteria.",
      "typical_uses": [
        "Type 2 diabetes and insulin resistance",
        "High LDL cholesterol (especially statin-intolerant patients)",
        "Metabolic syndrome",
        "NAFLD (non-alcoholic fatty liver disease)",
        "Gut dysbiosis and intestinal infections"
      ],
      "suggested_dose": "500 mg of berberine HCl 2–3 times daily with meals (total 1,000–1,500 mg/day). Start with a lower dose (500 mg/day) and titrate up over 2 weeks to reduce GI side effects. Combining with 20 mg piperine (black pepper extract) significantly improves absorption.",
      "onset": "Blood sugar effects: 1–2 weeks. Cholesterol reduction: 4–8 weeks. Full metabolic benefits: 12 weeks.",
      "safety_snapshot": [
        "Never take during pregnancy — risk of jaundice in newborns",
        "Monitor blood sugar carefully if on diabetes medication — strong additive effect",
        "May significantly raise levels of cyclosporin and some statins — check with your doctor"
      ]
    }
  },
  {
    "scientific_name": "Silybum marianum",
    "common_name": "Milk thistle / Silymarin",
    "type": "Plant",
    "article_count": 1483,
    "primary_categories": ["Hepatoprotection", "Antioxidant", "Oncology support", "Detoxification"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42129636/",
        "https://pubmed.ncbi.nlm.nih.gov/42123598/",
        "https://pubmed.ncbi.nlm.nih.gov/42089718/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Milk thistle has been used medicinally for over 2,000 years. Dioscorides (c. 77 CE) described it as a remedy for serpent bites. In medieval Europe it was widely cultivated in monastery gardens and prescribed by herbalists including John Gerard (1597) specifically for liver and gallbladder conditions. Nicholas Culpeper (1653) noted it 'opens obstructions of the liver and spleen.' The common name derives from the milky white variegation of the leaves, legendarily caused by drops of the Virgin Mary's milk. Introduced to North American settlers as a liver tonic and galactagogue.",
      "modern_application": "Milk thistle (standardised silymarin complex) is one of the most evidence-based hepatoprotective agents in phytomedicine. German Commission E approved it for toxic liver damage, inflammatory liver conditions, and as supportive therapy in chronic hepatitis and cirrhosis. A defining study confirmed silymarin as the specific antidote to Amanita phalloides (death cap mushroom) poisoning via IV silibinin (Legalon SIL) — administered in European emergency medicine. Multiple RCTs support benefit in NAFLD, alcoholic liver disease, viral hepatitis (adjunct), and drug-induced liver injury. Emerging evidence for breast and prostate cancer support.",
      "side_effects": "Exceptionally well tolerated. Mild and transient GI effects (loose stools, nausea, bloating) in ~1% of users — attributed to bile-stimulating activity. Rare allergic reactions in Asteraceae-sensitive individuals. Mild laxative effect (bile flow stimulation). No significant hepatotoxicity, nephrotoxicity, or haematological effects documented in any clinical trial.",
      "contraindications": "Known Asteraceae/Compositae allergy. Caution with hormone-sensitive conditions — silibinin has mild oestrogenic activity (binds ERα weakly); use cautiously in ER-positive breast cancer (evidence is mixed — silibinin may actually be anti-oestrogenic at pharmacological doses). Caution with drugs metabolised by CYP2C9, CYP3A4, and UGT1A1 (silymarin inhibits all three). Avoid very high doses in acute biliary obstruction."
    },
    "clinical_data": {
      "used_part": "Seed (achene; standardised silymarin complex from seed extract)",
      "primary_active_compounds": [
        "Silibinin A and B (primary flavonolignans; most pharmacologically active; also called silybin)",
        "Isosilybin A and B (diastereomers of silibinin)",
        "Silydianin",
        "Silychristin and isosilychristin",
        "Taxifolin (dihydroquercetin; flavonoid precursor to lignan formation)",
        "Fatty acids: linoleic acid (60%), oleic acid (30%) in seed oil"
      ],
      "mechanism_of_action": "Silibinin competitively inhibits uptake of hepatotoxins (amatoxins, phalloidin, microcystins) via hepatic <strong>OATP1B3</strong> (organic anion-transporting polypeptide), preventing cellular uptake — the mechanism behind its antidote role in Amanita poisoning. Potent antioxidant via <strong>Nrf2/HO-1</strong> activation, increasing glutathione, superoxide dismutase, and catalase. Inhibits <strong>NF-κB</strong>, reducing hepatic stellate cell activation and <strong>TGF-β1</strong>-driven collagen synthesis (anti-fibrotic). Promotes hepatocyte regeneration by stimulating <strong>RNA polymerase I</strong> and ribosomal RNA synthesis. Inhibits <strong>CYP2E1</strong>-mediated oxidative metabolism — reducing reactive metabolite formation from alcohol and hepatotoxic drugs. Anti-tumour via <strong>EGFR</strong> inhibition, <strong>STAT3</strong> suppression, and induction of apoptosis via <strong>caspase-3/7</strong>.",
      "pharmacokinetics": {
        "absorption": "Silymarin complex has poor aqueous solubility; oral bioavailability of silibinin is ~23–47% (variable). Phospholipid complexation (Siliphos/Phytosome) increases bioavailability 4–10-fold. Food significantly enhances absorption. Cmax at 2–4 hours post-dose. Silibinin A and B are absorbed at similar rates.",
        "distribution": "Distributes preferentially to liver (target organ) — hepatic concentrations significantly exceed plasma levels. Also found in kidney, lung, and intestinal mucosa. Plasma protein binding ~99% (albumin and α1-acid glycoprotein). Low CNS penetration.",
        "metabolism": "Extensive hepatic phase II conjugation: glucuronidation (UGT1A1, UGT1A3) and sulfation (SULT1A1). Undergoes enterohepatic recirculation of conjugates — extends effective exposure. Silibinin inhibits CYP2C9, CYP3A4, CYP2D6, and UGT1A1 — clinically relevant drug interaction potential at high doses.",
        "excretion": "Primarily biliary (>80%); urinary excretion of glucuronide and sulfate conjugates minor. Half-life of silibinin ~6 hours. Significant enterohepatic recirculation prolongs effective half-life to approximately 12–16 hours."
      },
      "safety_and_interactions": {
        "drug_interactions": "Indinavir and HIV antiretrovirals (CYP3A4 substrates) — silibinin inhibition may increase plasma levels; monitor. Irinotecan (chemotherapy) — UGT1A1 inhibition increases active SN-38 metabolite; toxicity risk; consult oncologist. Warfarin — CYP2C9 inhibition possible; monitor INR. Metronidazole and other hepatically metabolised antibiotics — potential interaction. Oestrogen-containing contraceptives — theoretical oestrogenic interaction; not confirmed clinically at standard doses.",
        "toxicity": "LD50 >5,000 mg/kg in rodents (oral). Exceptionally safe profile — no serious adverse events in any published clinical trial. IV silibinin (Legalon SIL) for Amanita poisoning: transient mild haemolysis reported at very high parenteral doses. No carcinogenicity, mutagenicity, or reproductive toxicity documented."
      },
      "special_precautions": {
        "pregnancy": "Insufficient human safety data. Mild oestrogenic activity — avoid high-dose supplemental use during pregnancy. Traditional use as a galactagogue (milk promoter) historically considered safe at low doses.",
        "lactation": "Traditionally used to promote milk production. Limited safety data on neonatal exposure via breast milk at supplemental doses. Culinary use considered safe; avoid concentrated extracts.",
        "hepatic_impairment": "The primary indication. Hepatoprotective and regenerative at therapeutic doses. Consider dose reduction in severe cirrhosis (reduced first-pass metabolism increases plasma exposure). Generally well tolerated even in advanced liver disease.",
        "renal_impairment": "Minor renal excretion of metabolites. No specific contraindication. No dose adjustment guidelines established. Safe at standard doses in moderate renal impairment."
      }
    },
    "consumer_view": {
      "tagline": "The gold standard herbal liver protector — backed by strong evidence and an antidote application",
      "what_it_does": "Milk thistle is the most evidence-backed herbal medicine for liver health. Its active compound silibinin literally blocks liver toxins from entering liver cells — so effectively that it is used intravenously in European hospitals as the antidote to death cap mushroom poisoning. It also protects against alcohol damage, fatty liver disease, and supports liver regeneration.",
      "typical_uses": [
        "Fatty liver disease (NAFLD/NASH)",
        "Alcoholic liver disease and liver recovery",
        "Medication-induced liver stress (statins, NSAIDs)",
        "Viral hepatitis support",
        "General liver detoxification and protection"
      ],
      "suggested_dose": "200–400 mg of standardised silymarin (70–80% silymarin complex) 2–3 times daily. For maximum absorption use a phospholipid-complexed form (Siliphos/Phytosome) or take standard capsules with a fatty meal. Long-term daily use is safe and well studied.",
      "onset": "Liver enzyme (ALT/AST) improvement: 4–8 weeks. Symptom relief in fatty liver and hepatitis: 8–12 weeks. Protective effects begin from first dose.",
      "safety_snapshot": [
        "Avoid if allergic to ragweed, daisies, or artichokes",
        "May interact with some HIV medications and chemotherapy — consult your doctor",
        "One of the safest herbal medicines available for long-term use"
      ]
    }
  },
  {
    "scientific_name": "Allium sativum",
    "common_name": "Garlic",
    "type": "Plant",
    "article_count": 9782,
    "primary_categories": ["Cardiovascular", "Antimicrobial", "Antihypertensive", "Antidiabetic"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42143523/",
        "https://pubmed.ncbi.nlm.nih.gov/42143351/",
        "https://pubmed.ncbi.nlm.nih.gov/42142775/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Garlic is among the most ancient of all medicinal plants, with documented use spanning over 5,000 years across virtually every major civilisation. Mentioned in the Ebers Papyrus (c. 1550 BCE) for treating heart disease, tumours, and worms. Egyptian pyramid builders were fed garlic to maintain strength. Hippocrates prescribed it for respiratory conditions, GI disorders, and fatigue. Roman soldiers ate it for endurance. Louis Pasteur confirmed its antibacterial properties in 1858. During WWI and WWII it was used as an antiseptic for wounds when conventional antibiotics were unavailable.",
      "modern_application": "One of the most extensively studied food-medicines globally with nearly 10,000 PubMed publications. Meta-analyses of RCTs confirm clinically significant reductions in systolic (7–10 mmHg) and diastolic (3–5 mmHg) blood pressure in hypertension. A 2016 Cochrane review found modest LDL-C reduction (~10 mg/dL). Aged garlic extract (AGE — standardised to S-allylcysteine) has the most consistent clinical evidence for cardiovascular benefit. Antimicrobial RCTs show reduced frequency and duration of common colds. Emerging evidence for H. pylori eradication adjunct therapy and colorectal cancer risk reduction.",
      "side_effects": "Halitosis (garlic breath) and body odour — the most common and socially limiting effects. GI irritation (heartburn, nausea, flatulence), particularly from raw garlic. Antiplatelet effects — increased bleeding time. Contact dermatitis (topical). Rare: anaphylaxis (IgE-mediated allergy). Garlic allergy is distinct from Allium/leek allergy. Diallyl disulfide can cause haemolytic anaemia in cats and dogs (not humans at dietary doses).",
      "contraindications": "Anticoagulant or antiplatelet therapy — additive bleeding risk; clinical monitoring required. Discontinue high-dose supplements ≥1 week before surgery. HIV medications (saquinavir, ritonavir) — garlic extract significantly reduces saquinavir plasma levels (CYP3A4 and P-gp induction). Thyroid medications — garlic at high doses may affect thyroid hormone metabolism. Caution in pemphigus (inflammatory skin condition — case reports of exacerbation)."
    },
    "clinical_data": {
      "used_part": "Bulb (clove; fresh, dried powder, aged garlic extract, or garlic oil)",
      "primary_active_compounds": [
        "Allicin (allyl 2-propenethiosulfinate — formed from alliin by alliinase on crushing; primary antimicrobial compound; unstable)",
        "S-Allylcysteine (SAC — stable; primary active in aged garlic extract; cardioprotective)",
        "S-Allylmercaptocysteine (SAMC)",
        "Diallyl disulfide (DADS) and diallyl trisulfide (DATS — primary anticancer thiosulfinates)",
        "Ajoene (antiplatelet, antifungal; formed from allicin in oil)",
        "Alliin (stable precursor; inactive until enzymatic conversion by alliinase)",
        "Fructooligosaccharides (prebiotic; gut microbiome-modulating)"
      ],
      "mechanism_of_action": "Allicin and organosulfur compounds (DADS, DATS) inhibit <strong>HMG-CoA reductase</strong>, reducing hepatic cholesterol synthesis. Antihypertensive via enzymatic production of <strong>hydrogen sulfide (H₂S)</strong> from allicin metabolites — H₂S activates vascular <strong>KATP channels</strong>, hyperpolarising vascular smooth muscle, causing vasodilation. Also inhibits <strong>ACE (angiotensin-converting enzyme)</strong>, reducing angiotensin II–mediated vasoconstriction. Antiplatelet via inhibition of <strong>TXA2</strong> synthesis and <strong>COX-1</strong>-dependent arachidonate metabolism, and direct inhibition of fibrinogen binding to GPIIb/IIIa receptor. SAC upregulates <strong>Nrf2/HO-1</strong> antioxidant pathway. DATS induces tumour cell apoptosis via reactive sulfur species generating mitochondrial oxidative stress in cancer cells. Antimicrobial: allicin covalently modifies <strong>cysteine proteases</strong> and <strong>thiol-containing enzymes</strong> in pathogens.",
      "pharmacokinetics": {
        "absorption": "Allicin is rapidly formed on crushing and absorbed from the upper GI tract; however, allicin itself is highly unstable and rapidly converted to diallyl sulfides, ajoene, and vinyldithiins. SAC (from aged garlic extract) is stable and has near-complete oral bioavailability (~98%). Cmax of allicin metabolites at 1–2 hours.",
        "distribution": "Organosulfur compounds distribute widely to all tissues including liver, lung, kidney, and blood vessels. Allicin metabolites detected in exhaled breath (explains garlic odour). SAC enters the CNS — neuroprotective effects documented in animal models. DADS distributes to intestinal mucosa (relevant to anticancer effects).",
        "metabolism": "Allicin rapidly and non-enzymatically decomposes in vivo to DADS, DATS, and ajoene. SAC undergoes N-acetylation in the liver to N-acetyl-SAC. DADS and DATS metabolised by hepatic CYP2E1 and CYP3A4. Garlic is a known inducer of CYP3A4 and P-glycoprotein at high doses — clinically relevant for antiretroviral interactions.",
        "excretion": "Urinary excretion of N-acetyl-SAC and other thiol conjugates. Pulmonary excretion of volatile DADS (garlic breath). Half-life of SAC ~10 hours. DADS and DATS metabolites excreted in urine and bile within 24 hours."
      },
      "safety_and_interactions": {
        "drug_interactions": "Warfarin and anticoagulants — additive antiplatelet effects (TXA2 inhibition); INR elevation documented in case reports; monitor closely. Antiplatelet drugs (aspirin, clopidogrel) — additive bleeding risk. Saquinavir (HIV protease inhibitor) — garlic extract reduces saquinavir AUC by up to 51% via CYP3A4 and P-gp induction; contraindicated with ritonavir-boosted regimens. Other HIV antiretrovirals — potential CYP3A4 induction; monitor drug levels. Isoniazid (TB treatment) — reduced absorption when taken together. Insulin and antidiabetic drugs — modest additive glucose-lowering effect.",
        "toxicity": "LD50 >30 mL/kg (garlic oil) in rodents. No significant human toxicity at dietary or supplemental doses. Topical allicin can cause chemical burns and blistering on skin (reports of self-treatment with raw garlic). GI haemorrhage risk at very high doses in combination with anticoagulants. Diallyl sulfide is a CYP2E1 substrate and may modestly modify acetaminophen hepatotoxicity at high doses."
      },
      "special_precautions": {
        "pregnancy": "Culinary use is universally considered safe in pregnancy. High-dose supplements (>900 mg garlic extract/day) not formally studied; avoid as a precaution given antiplatelet activity.",
        "lactation": "Garlic flavour transfers to breast milk and may affect infant feeding behaviour — some infants feed more readily, others refuse. Culinary quantities considered safe.",
        "hepatic_impairment": "Hepatoprotective at standard doses. CYP3A4 induction by high-dose garlic may alter metabolism of co-administered hepatically cleared drugs. No direct hepatotoxicity documented.",
        "renal_impairment": "No specific contraindication. Thiol metabolites renally excreted; accumulation possible in severe CKD. No dose adjustment guidelines established."
      }
    },
    "consumer_view": {
      "tagline": "Lowers blood pressure and cholesterol, fights infections — the best-studied food-medicine in the world",
      "what_it_does": "Garlic is where cooking and medicine overlap. Clinical trials show it meaningfully lowers blood pressure (by about 7–10 mmHg systolic), reduces LDL cholesterol, fights bacterial and viral infections, and reduces the risk of heart disease. The catch: supplements vary enormously in quality. You need a preparation that actually releases active compounds.",
      "typical_uses": [
        "High blood pressure",
        "High cholesterol and cardiovascular risk reduction",
        "Recurrent colds and infections",
        "Atherosclerosis prevention",
        "H. pylori infection (adjunct support)"
      ],
      "suggested_dose": "Aged garlic extract (AGE): 600–1,200 mg/day standardised to S-allylcysteine. Allicin-releasing tablets: equivalent to 3–5 g fresh garlic daily. Fresh garlic: 2–5 g (1–2 cloves) per day, crushed and rested 10 minutes before use (activates alliinase). Enteric-coated supplements reduce garlic breath.",
      "onset": "Blood pressure reduction: 4–8 weeks. Cholesterol reduction: 8–12 weeks. Immune effects: 1–2 weeks.",
      "safety_snapshot": [
        "Avoid high-dose supplements with blood thinners — significant bleeding risk",
        "Do not combine with HIV medications (saquinavir) without medical supervision",
        "Stop high-dose garlic supplements 1 week before surgery"
      ]
    }
  },
  {
    "scientific_name": "Cinnamomum verum",
    "common_name": "Ceylon cinnamon / True cinnamon",
    "type": "Plant",
    "article_count": 1865,
    "primary_categories": ["Antidiabetic", "Anti-inflammatory", "Antimicrobial", "Cardiovascular"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42116688/",
        "https://pubmed.ncbi.nlm.nih.gov/42075729/",
        "https://pubmed.ncbi.nlm.nih.gov/42073199/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Ceylon cinnamon is one of the world's oldest traded spices, mentioned in Chinese writing as early as 2700 BCE and in the Ebers Papyrus (c. 1550 BCE). Among the first commodities traded on spice routes from Sri Lanka (formerly Ceylon) to Egypt, Arabia, and Rome. So highly valued in ancient times that it was presented as gifts to kings and gods. Pliny the Elder (77 CE) noted its extraordinary price. In medieval Europe it flavoured food, masked the smell of decay, and was used medicinally for digestive complaints, fever, and menstrual problems. The distinction between true Ceylon cinnamon (C. verum) and Cassia cinnamon (C. aromaticum or C. cassia) is medically important due to dramatically different coumarin content.",
      "modern_application": "Clinical evidence for metabolic effects is growing: a 2019 systematic review and meta-analysis of 18 RCTs found significant reductions in fasting blood glucose, HbA1c, and triglycerides in type 2 diabetes. Key advantage of C. verum over C. cassia: coumarin content is only 0.004% vs. 0.31–6.97% in cassia — making Ceylon cinnamon safe for daily long-term use where cassia carries hepatotoxicity risk. A 2020 RCT demonstrated significant reduction in insulin resistance (HOMA-IR) at 3 g/day over 8 weeks. Antimicrobial RCTs confirm activity against Candida, H. pylori, and E. coli. ESCOP recognises it for loss of appetite and mild GI spasms.",
      "side_effects": "Ceylon cinnamon is very safe at culinary and therapeutic doses. GI irritation at high doses. Allergic contact stomatitis and cheilitis (topical cinnamon allergy — from cinnamon oil in toothpastes, gum). Cinnamaldehyde is a sensitiser — occupational dermatitis in bakery workers. Coumarin content in Ceylon cinnamon is negligible; hepatotoxicity from cassia cinnamon (NOT C. verum) is the relevant concern. Drug interactions are the main clinical consideration.",
      "contraindications": "Caution with antidiabetic medications (additive glucose lowering; hypoglycaemia risk). Caution with anticoagulants. Avoid high doses in pregnancy (uterotonic activity of cinnamaldehyde at pharmacological doses). Caution with CYP2A6 substrates (cinnamaldehyde inhibits CYP2A6). Important: do not substitute cassia cinnamon for Ceylon in high-dose supplementation — hepatotoxic coumarin content."
    },
    "clinical_data": {
      "used_part": "Inner bark of young shoots (quills/sticks; dried and powdered; essential oil by steam distillation)",
      "primary_active_compounds": [
        "Cinnamaldehyde (trans-cinnamaldehyde; 55–90% of essential oil; primary anti-inflammatory and antimicrobial compound)",
        "Eugenol (phenylpropanoid; anti-inflammatory, analgesic; higher in C. verum than cassia)",
        "Cinnamic acid and methyl cinnamate",
        "Cinnamate esters (2-methoxycinnamaldehyde)",
        "Proanthocyanidins (type A and B; insulin-sensitising)",
        "Coumarin (hepatotoxic at high doses — present at <0.004% in C. verum; 0.3–6.97% in C. cassia — critical safety distinction)"
      ],
      "mechanism_of_action": "Cinnamaldehyde activates <strong>TRPA1 (transient receptor potential ankyrin 1)</strong> channels, producing anti-inflammatory signalling and modulating pain perception. Insulin-sensitising mechanisms: inhibits <strong>PTP1B</strong> (protein tyrosine phosphatase 1B), restoring insulin receptor β-subunit autophosphorylation; upregulates <strong>GLUT4</strong> expression and translocation in skeletal muscle; activates <strong>AMPK</strong> — converging on the same pathway as berberine and metformin. Postprandial glucose reduction via inhibition of intestinal <strong>α-glucosidase</strong> and <strong>α-amylase</strong>, slowing carbohydrate digestion. Antimicrobial: cinnamaldehyde disrupts bacterial cell membranes via thiol-reactivity and inhibits biofilm formation by <strong>quorum sensing</strong> interference. Anti-inflammatory via <strong>NF-κB</strong> inhibition and <strong>COX-2</strong> suppression.",
      "pharmacokinetics": {
        "absorption": "Cinnamaldehyde is rapidly absorbed from the GI tract; first-pass metabolism to cinnamic acid is extensive. Cmax at 30–60 minutes. Bioavailability of cinnamaldehyde itself is low due to rapid conversion; cinnamic acid is the primary circulating metabolite. Proanthocyanidins absorbed after gut depolymerisation.",
        "distribution": "Cinnamic acid distributes widely; crosses the blood-brain barrier (anti-inflammatory CNS effects). Cinnamaldehyde rapidly partitions into intestinal mucosa and liver. Eugenol distributes to lipid-rich tissues. Plasma protein binding moderate (~70%).",
        "metabolism": "Cinnamaldehyde rapidly oxidised to cinnamic acid by aldehyde oxidase; cinnamic acid further β-oxidised to benzoic acid and then conjugated with glycine to form hippuric acid — the primary urinary metabolite. CYP2A6 inhibition documented. Eugenol conjugated by hepatic UGT enzymes.",
        "excretion": "Urinary excretion of hippuric acid (primary metabolite of cinnamaldehyde via cinnamic acid), glucuronic acid conjugates of cinnamic acid and eugenol. Half-life of cinnamic acid ~1 hour. Complete excretion within 24 hours of a single dose."
      },
      "safety_and_interactions": {
        "drug_interactions": "Antidiabetic agents (metformin, insulin, sulfonylureas, SGLT2 inhibitors, GLP-1 agonists) — additive glucose lowering; hypoglycaemia risk; monitor blood glucose. Anticoagulants (warfarin) — coumarin interaction only relevant with cassia cinnamon; Ceylon cinnamon has negligible coumarin; cinnamaldehyde has mild antiplatelet activity — monitor INR. CYP2A6 substrates (nicotine, letrozole, some cancer drugs) — cinnamaldehyde inhibition may alter drug metabolism. Antibiotics (for H. pylori) — cinnamaldehyde has additive antimicrobial activity; potential synergy.",
        "toxicity": "Cinnamaldehyde is the primary sensitiser and causes contact allergy (skin and oral mucosa) — not systemic toxicity. LD50 of cinnamaldehyde ~1.85 g/kg (rodent oral). The critical safety issue for cinnamon supplementation is coumarin: C. cassia contains up to 6.97% coumarin (hepatotoxic threshold 0.1 mg/kg/day in humans); C. verum is safe (<0.004% coumarin). European Food Safety Authority warns against daily high-dose cassia supplementation."
      },
      "special_precautions": {
        "pregnancy": "Culinary use of Ceylon cinnamon is considered safe throughout pregnancy. High-dose supplemental cinnamaldehyde (>3 g/day equivalent) avoided due to theoretical uterotonic activity. Cassia cinnamon high-dose use contraindicated.",
        "lactation": "No documented harm at culinary or standard therapeutic doses. Cinnamic acid excreted in breast milk in small quantities. Considered compatible with breastfeeding.",
        "hepatic_impairment": "Ceylon cinnamon: safe at therapeutic doses; hepatoprotective properties documented. Cassia cinnamon: coumarin is directly hepatotoxic at high doses — do not use cassia supplements in hepatic impairment.",
        "renal_impairment": "Hippuric acid (primary urinary metabolite) accumulates in renal failure. No specific contraindication established for standard doses. High-dose use not studied in severe CKD."
      }
    },
    "consumer_view": {
      "tagline": "Blood sugar control and antimicrobial benefits — but only if you use the right type of cinnamon",
      "what_it_does": "Ceylon cinnamon (true cinnamon) improves how your body handles blood sugar by targeting the same pathways as diabetes medications. It is also antimicrobial, anti-inflammatory, and cardiovascular-protective. The important thing: most cinnamon sold is cassia — a different species that can damage your liver at high doses. Ceylon is the safe choice for daily supplementation.",
      "typical_uses": [
        "Blood sugar control and insulin resistance",
        "Type 2 diabetes support",
        "High triglycerides and cardiovascular risk",
        "Antimicrobial support (H. pylori, Candida)",
        "Anti-inflammatory and metabolic syndrome"
      ],
      "suggested_dose": "1–3 g of Ceylon cinnamon powder per day (½–1 teaspoon), or 250–500 mg of standardised extract (standardised to ≥3% cinnamaldehyde). Ensure the label says Cinnamomum verum or C. zeylanicum — NOT C. cassia or C. aromaticum. Take with meals.",
      "onset": "Blood sugar and HbA1c effects: 4–8 weeks. Antimicrobial effects: 1–2 weeks.",
      "safety_snapshot": [
        "Only use Ceylon cinnamon (C. verum/zeylanicum) for daily supplementation — cassia can damage your liver",
        "Monitor blood sugar closely if on diabetes medication",
        "Avoid high doses during pregnancy"
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
