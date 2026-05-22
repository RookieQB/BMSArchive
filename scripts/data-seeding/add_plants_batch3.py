#!/usr/bin/env python3
"""Batch 3 — Nigella sativa, Echinacea purpurea, Sambucus nigra, Astragalus propinquus"""
import json

PLANTS = [
  {
    "scientific_name": "Nigella sativa",
    "common_name": "Black seed / Black cumin / Kalonji",
    "type": "Plant",
    "article_count": 2535,
    "primary_categories": ["Immunomodulation", "Anti-inflammatory", "Respiratory", "Antidiabetic"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42124081/",
        "https://pubmed.ncbi.nlm.nih.gov/42121497/",
        "https://pubmed.ncbi.nlm.nih.gov/42091563/"
      ]
    },
    "narrative_summary": {
      "historical_use": "One of the most revered medicinal plants in Islamic medicine; the Prophet Muhammad reportedly stated 'Use this black seed, it is a remedy for every disease except death' (Sahih al-Bukhari). Seeds and oil have been found in the tomb of Tutankhamun (c. 1325 BCE), attesting to Egyptian use. Extensively described in Ibn Sina's Canon of Medicine (1025 CE) for respiratory conditions, headaches, and as a diuretic and anthelmintic. Known in Arabic as 'habbatus sawda' (seed of blessing) and used across the Islamic world for over 1,400 years.",
      "modern_application": "Thymoquinone — the primary active constituent — has been studied extensively in preclinical models for anti-cancer, anti-inflammatory, antidiabetic, and hepatoprotective activities. Clinical RCTs demonstrate: significant reduction in fasting blood glucose and HbA1c in type 2 diabetes (meta-analysis, 2017); improvement in asthma control and reduction in bronchodilator use; reduction in blood pressure; and lipid-lowering effects (LDL reduction, HDL increase). A 2021 RCT showed significant reduction in COVID-19 severity and viral load. Seed oil standardised to ≥2% thymoquinone is the most studied preparation.",
      "side_effects": "Generally well tolerated at recommended doses. GI discomfort (bloating, nausea) most common. Allergic contact dermatitis with topical application. Seed oil may cause hypoglycaemia in combination with antidiabetic drugs. Potential nephrotoxicity at very high doses (animal data). Hepatotoxic at supratherapeutic doses in rodents — not confirmed in human RCTs. Antifertility effects in male rodents at high doses (reversible).",
      "contraindications": "Avoid during pregnancy (documented uterotonic activity; historically used as an abortifacient). Caution in hypoglycaemia-prone patients on insulin or sulfonylureas. Caution before surgery (antiplatelet activity). Avoid in severe renal impairment at high doses."
    },
    "clinical_data": {
      "used_part": "Seed and fixed seed oil (cold-pressed)",
      "primary_active_compounds": [
        "Thymoquinone (TQ — volatile oil; primary pharmacologically active constituent)",
        "Thymohydroquinone (reduced form of TQ)",
        "Thymol and carvacrol (monoterpene phenols)",
        "Nigellone (dimer of thymoquinone; antihistaminic)",
        "Alpha-hederin (saponin; immunostimulant)",
        "Fixed oils: linoleic acid (50–60%), oleic acid, palmitic acid",
        "Nigellidine and nigellicine (alkaloids)"
      ],
      "mechanism_of_action": "Thymoquinone inhibits <strong>NF-κB</strong> activation by preventing IκBα phosphorylation and degradation, suppressing downstream pro-inflammatory mediators (<strong>TNF-α</strong>, <strong>IL-1β</strong>, <strong>IL-6</strong>, <strong>COX-2</strong>, <strong>iNOS</strong>). Activates the <strong>Nrf2/HO-1</strong> antioxidant pathway, increasing superoxide dismutase and catalase activity. Antidiabetic effects via <strong>PPAR-γ</strong> activation, <strong>GLUT4</strong> upregulation, and inhibition of intestinal α-glucosidase. Bronchodilatory activity via <strong>β₂-adrenergic receptor</strong> stimulation and <strong>PDE4</strong> inhibition (raising cAMP). Anti-proliferative activity via <strong>p53</strong> pathway activation and <strong>Bcl-2</strong> suppression. Nigellone inhibits <strong>histamine</strong> release from mast cells, explaining antiallergic activity.",
      "pharmacokinetics": {
        "absorption": "Thymoquinone is moderately absorbed orally; lipid formulations (seed oil) significantly enhance bioavailability compared to aqueous extracts. Cmax at 2–3 hours post-dose. Bioavailability enhanced by co-administration with piperine or fat.",
        "distribution": "Highly lipophilic; distributes to liver, kidney, lung, and adipose tissue. Crosses the blood-brain barrier in rodent models. Plasma protein binding estimated at 60–80%. Accumulates in immune-rich tissues (spleen, lymph nodes).",
        "metabolism": "Hepatic; thymoquinone undergoes reduction to thymohydroquinone by hepatic reductases and conjugation via glutathione-S-transferase. CYP3A4 and CYP2D6 are involved. Thymoquinone is itself a Michael acceptor — reacts with protein thiol groups. Half-life approximately 2–3 hours.",
        "excretion": "Primarily biliary (conjugated metabolites) and urinary. Thymol and carvacrol excreted in urine as glucuronide conjugates. Enterohepatic recirculation of thymoquinone conjugates documented."
      },
      "safety_and_interactions": {
        "drug_interactions": "Antidiabetic agents (insulin, metformin, sulfonylureas) — additive glucose-lowering effect; hypoglycaemia risk. Anticoagulants (warfarin) — thymoquinone inhibits platelet aggregation and may inhibit CYP2C9; monitor INR. Antihypertensives — additive blood pressure reduction; monitor. Immunosuppressants (cyclosporin) — potential CYP3A4 interaction; immunostimulant activity may oppose immunosuppression. Chemotherapy agents — thymoquinone shows synergistic cytotoxicity in preclinical models but clinical interaction data are absent.",
        "toxicity": "LD50 of thymoquinone 57 mg/kg IV in mice; 870 mg/kg oral (much safer). Oral seed oil LD50 >2 mL/kg in rodents. High-dose nephrotoxicity documented in rats; not confirmed at therapeutic human doses. Antifertility effects in male animals at supratherapeutic doses."
      },
      "special_precautions": {
        "pregnancy": "Contraindicated. Documented uterotonic and abortifacient activity at therapeutic doses. Historically used deliberately for pregnancy termination in traditional medicine.",
        "lactation": "Thymoquinone excretion in breast milk not characterised. Traditional use suggests moderate safety; avoid concentrated oil supplements during breastfeeding.",
        "hepatic_impairment": "Hepatotoxicity at supratherapeutic doses in animal models. At therapeutic doses, hepatoprotective effects documented in RCTs. Use with monitoring in pre-existing liver disease.",
        "renal_impairment": "High-dose nephrotoxicity in animal studies. Avoid at high doses in moderate-to-severe renal impairment. Therapeutic doses appear safe based on clinical trial data."
      }
    },
    "consumer_view": {
      "tagline": "Ancient immune and anti-inflammatory seed oil with wide-ranging clinical evidence",
      "what_it_does": "Black seed oil is one of the most studied natural medicines from the Islamic world. It reduces inflammation across the body, supports immune defences, improves blood sugar control, and opens the airways in asthma. It works across multiple body systems simultaneously, making it unusually versatile.",
      "typical_uses": [
        "Immune support and infection resistance",
        "Asthma and allergic respiratory conditions",
        "Blood sugar control in type 2 diabetes",
        "High blood pressure and cholesterol",
        "General anti-inflammatory support"
      ],
      "suggested_dose": "500 mg–2 g of cold-pressed black seed oil per day (standardised to ≥2% thymoquinone), divided into 2 doses with meals. Or 1–2 teaspoons of whole cold-pressed oil daily. Allow 4–8 weeks for metabolic effects.",
      "onset": "Blood pressure and respiratory effects: 2–4 weeks. Blood sugar and lipid effects: 6–8 weeks.",
      "safety_snapshot": [
        "Do not take during pregnancy — can cause miscarriage",
        "Watch for low blood sugar if on diabetes medication",
        "Avoid high doses if you have kidney disease"
      ]
    }
  },
  {
    "scientific_name": "Echinacea purpurea",
    "common_name": "Purple coneflower / Echinacea",
    "type": "Plant",
    "article_count": 1645,
    "primary_categories": ["Immune support", "Antiviral", "Anti-inflammatory"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42125221/",
        "https://pubmed.ncbi.nlm.nih.gov/42118563/",
        "https://pubmed.ncbi.nlm.nih.gov/42115237/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Used by at least 14 Native American tribes of the Great Plains for a wider range of conditions than perhaps any other plant — including wound healing, snake bites, toothache, sore throat, and infection. The Lakota, Cheyenne, and Comanche used it as an analgesic and anti-infective. Introduced to European-American medicine in the 1880s by the eclectic physician Dr H.C.F. Meyer, who marketed it as a remedy for rattlesnake bite. By the early 20th century it was the best-selling plant medicine in the United States.",
      "modern_application": "One of the most commercially significant herbal medicines in the world. A 2015 Cochrane review (Karsch-Völk et al.) of 24 RCTs concluded Echinacea preparations may reduce the incidence and duration of the common cold, with some preparations showing significant effects. A 2007 meta-analysis (Shah et al., Lancet Infectious Diseases) found a 58% reduction in cold incidence and 1.4-day reduction in duration. EchinilinTM (juice of E. purpurea herb standardised to alkylamides and polysaccharides) is one of the best-studied preparations.",
      "side_effects": "Generally very well tolerated for short-term use (≤8 weeks). Allergic reactions in Asteraceae-sensitised individuals (urticaria, rash, rarely anaphylaxis). GI upset (nausea, diarrhoea). Unpleasant tingling sensation on the tongue (from alkylamides — actually a sign of quality). Rare: worsening of autoimmune conditions. Theoretical concern about long-term continuous use depleting immune function (overcycling).",
      "contraindications": "Contraindicated in autoimmune diseases (RA, lupus, MS, psoriasis) — immune stimulation may exacerbate. Contraindicated with immunosuppressants (tacrolimus, cyclosporin, corticosteroids). Avoid in known Asteraceae allergy. Limit continuous use to ≤8 weeks; allow a 2-week break before restarting. Avoid in HIV/AIDS (uncertain effect on viral replication)."
    },
    "clinical_data": {
      "used_part": "Aerial parts (herb, leaf, flower) — E. purpurea; root — E. angustifolia and E. pallida (related species with different active profiles)",
      "primary_active_compounds": [
        "Alkylamides (isobutylamides; N-alkylamides) — primary immunomodulatory compounds",
        "Cichoric acid (caffeic acid derivative; antiviral, immunostimulant)",
        "Echinacoside (caffeic acid glycoside — primarily in E. angustifolia root)",
        "Arabinogalactans (polysaccharides; TLR-4 agonists)",
        "Glycoproteins (120 kDa; macrophage activating)",
        "Polysaccharide PS I and PS II (β-fructans)"
      ],
      "mechanism_of_action": "Alkylamides bind the <strong>cannabinoid type 2 receptor (CB2)</strong>, modulating macrophage cytokine production and suppressing excessive <strong>TNF-α</strong> and <strong>IL-6</strong> release (anti-inflammatory and immunomodulatory). Arabinogalactans and glycoproteins activate macrophages and dendritic cells via <strong>TLR-4</strong> and <strong>Dectin-1</strong>, stimulating phagocytosis and innate immune activity. Cichoric acid inhibits viral hyaluronidase and integrase — direct antiviral activity against rhinovirus and influenza. Upregulates <strong>IFN-α</strong> and <strong>IFN-β</strong> (interferons), reinforcing antiviral innate immunity. <strong>NK cell</strong> activity is significantly enhanced, increasing cytotoxic surveillance.",
      "pharmacokinetics": {
        "absorption": "Alkylamides are rapidly and well absorbed; Cmax at 20–30 minutes post-dose. Bioavailability is high (~80%) due to moderate lipophilicity. Cichoric acid is poorly absorbed (<5%). Polysaccharides and glycoproteins act locally in the GI tract and are not systemically absorbed to a clinically significant degree.",
        "distribution": "Alkylamides distribute rapidly to CB2-rich tissues: spleen, immune cells, and inflammatory foci. Extensive binding to plasma proteins and tissue CB2 receptors. Low CNS penetration. Cichoric acid remains in mucosal compartments.",
        "metabolism": "Alkylamides metabolised by CYP3A4, CYP1A2, and amidases. N-dealkylation and hydroxylation are primary metabolic routes. Half-life of alkylamides ~2 hours. Cichoric acid hydrolysed by gut esterases to caffeic acid.",
        "excretion": "Alkylamide metabolites excreted in urine and faeces. Half-life of alkylamides ~2 hours. Caffeic acid metabolites excreted in urine. Polysaccharides excreted in faeces unabsorbed."
      },
      "safety_and_interactions": {
        "drug_interactions": "Immunosuppressants (cyclosporin, tacrolimus, azathioprine, corticosteroids) — pharmacodynamic antagonism; may reduce efficacy of transplant antirejection drugs; contraindicated. CYP3A4 substrates — mild CYP3A4 inhibition by alkylamides; modest plasma level increases possible. Caffeine — alkylamides inhibit CYP1A2; caffeine plasma levels may rise. HIV antiretrovirals — theoretical concern about immune stimulation in HIV; avoid.",
        "toxicity": "LD50 >5,000 mg/kg in mice (oral aqueous extract). Allergic reactions (including rare anaphylaxis) are the most serious adverse events. Autoimmune exacerbation documented in case reports. No hepatotoxicity or organ toxicity at therapeutic doses."
      },
      "special_precautions": {
        "pregnancy": "Limited human safety data. Short-term use in the first trimester studied in one cohort (n=206) with no increased malformation risk. However, avoid high-dose preparations during pregnancy as a precaution.",
        "lactation": "No documented harm at normal use. Alkylamide excretion in breast milk not quantified. Use cautiously for short-term cold treatment.",
        "hepatic_impairment": "No specific contraindication. CYP3A4 metabolism may be impaired in severe liver disease; monitor for drug interactions. No direct hepatotoxicity documented.",
        "renal_impairment": "No specific contraindication at therapeutic doses. Metabolites renally excreted; standard monitoring in severe renal impairment."
      }
    },
    "consumer_view": {
      "tagline": "Shortens colds and boosts immune defences — best taken at first sign of illness",
      "what_it_does": "Echinacea is the world's most popular herbal immune supplement. Clinical evidence shows it can reduce your chance of catching a cold by around half and cut its duration by 1–2 days when taken at the first symptoms. It works by activating your innate immune system — the body's first line of defence against viruses.",
      "typical_uses": [
        "Preventing and shortening the common cold",
        "Upper respiratory tract infections",
        "General immune support in winter",
        "Post-illness recovery"
      ],
      "suggested_dose": "Prevention: 400–900 mg of standardised extract (containing alkylamides + cichoric acid) daily for up to 8 weeks. Acute treatment: higher doses at first sign of illness (e.g. 2,400 mg/day for 3 days, then standard dose). Take a 2-week break after every 8 weeks.",
      "onset": "Immune activation: within hours of first dose. Clinical effects on cold duration and severity: 1–3 days.",
      "safety_snapshot": [
        "Avoid if you have an autoimmune disease (lupus, RA, MS)",
        "Do not take with transplant or immunosuppressant medication",
        "Avoid if allergic to ragweed or daisies"
      ]
    }
  },
  {
    "scientific_name": "Sambucus nigra",
    "common_name": "Elderberry / Black elder",
    "type": "Plant",
    "article_count": 1132,
    "primary_categories": ["Antiviral", "Immune support", "Anti-inflammatory"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42106747/",
        "https://pubmed.ncbi.nlm.nih.gov/42101670/",
        "https://pubmed.ncbi.nlm.nih.gov/42075018/"
      ]
    },
    "narrative_summary": {
      "historical_use": "The elder tree has occupied a central place in European folk medicine, mythology, and culture for millennia. Called 'the medicine chest of the country people' by the herbalist John Evelyn (1664). Hippocrates referred to elder as his 'medicine chest.' Both the flowers and berries were used extensively in traditional European medicine for colds, flu, fever, rheumatism, and skin conditions. The tree was sacred in Norse, Celtic, and Slavic traditions — in Denmark, the elder tree was inhabited by 'Hyldemor' (Elder Mother), a protective spirit.",
      "modern_application": "A 2016 randomised, double-blind, placebo-controlled trial (Tiralongo et al.) showed standardised elderberry extract significantly reduced cold duration and severity in air travellers. A 2004 RCT (Zakay-Rones et al.) demonstrated a 4-day faster recovery from influenza B with elderberry syrup (Sambucol) versus placebo. A 2019 meta-analysis of 4 RCTs confirmed significant reductions in upper respiratory symptom duration and severity. Standardised extracts (Sambucol, Isorel) with documented anthocyanin content are the most clinically validated preparations.",
      "side_effects": "Well tolerated when properly prepared. Raw unripe berries, bark, leaves, and seeds contain sambunigrin (a cyanogenic glycoside) — can cause nausea, vomiting, and diarrhoea if consumed raw. Commercially prepared extracts and cooked berries are safe. Potential excessive immune stimulation (cytokine storm amplification) is a theoretical concern in severe influenza — clinical evidence for this risk is not established. Rare allergic reactions in Asteraceae-sensitive individuals.",
      "contraindications": "Never consume raw unripe berries, leaves, or bark — cyanogenic glycoside poisoning. Caution in autoimmune conditions — immune stimulation may exacerbate. Avoid with immunosuppressants. Potential interaction with diuretics and laxatives (elderberry has mild diuretic properties)."
    },
    "clinical_data": {
      "used_part": "Ripe berry (fruit; cooked or standardised extract); flower (elderflower — diaphoretic, anti-inflammatory)",
      "primary_active_compounds": [
        "Cyanidin-3-O-glucoside (dominant anthocyanin; antiviral)",
        "Cyanidin-3-O-sambubioside (anthocyanin)",
        "Cyanidin-3-O-rutinoside and cyanidin-3,5-O-diglucoside",
        "Quercetin, kaempferol, and isorhamnetin (flavonols)",
        "Chlorogenic acids (caffeic acid esters; antioxidant)",
        "Sambunigrin (cyanogenic glycoside — raw plant only; eliminated by cooking/processing)",
        "Lectins (SNA-I, SNA-II; agglutinins — antiviral binding proteins)"
      ],
      "mechanism_of_action": "Anthocyanins (primarily cyanidin-3-glucoside) directly inhibit influenza viral <strong>hemagglutinin</strong>, preventing viral attachment and entry into respiratory epithelial cells. Flavonoids inhibit viral <strong>neuraminidase</strong> — the same target as oseltamivir (Tamiflu) — blocking viral release from infected cells. Lectins (SNA-I) bind sialic acid residues on viral surfaces. Stimulate early cytokine production (<strong>IL-6</strong>, <strong>TNF-α</strong>, <strong>IL-1β</strong>) in macrophages via <strong>TLR-4</strong> engagement, accelerating innate immune activation. Quercetin activates <strong>Nrf2/HO-1</strong> antioxidant pathway and inhibits <strong>NLRP3</strong> inflammasome assembly in later infection phases.",
      "pharmacokinetics": {
        "absorption": "Anthocyanins are absorbed from the small intestine by active transport; bioavailability is low (0.5–2%) but the colonic microbiome converts them to phenolic acid metabolites with higher bioavailability. Cmax for cyanidin glycosides at 1–2 hours. Quercetin bioavailability ~24% from glycoside forms after enzymatic hydrolysis.",
        "distribution": "Anthocyanin metabolites (protocatechuic acid, phloroglucinol aldehyde) distribute to plasma, liver, and kidney. Quercetin and kaempferol distribute to respiratory epithelium and immune tissues. Plasma protein binding of quercetin ~99%.",
        "metabolism": "Anthocyanins rapidly degraded in plasma (half-life ~2 hours); colonic bacteria produce protocatechuic acid, vanillic acid, and other phenolic metabolites as secondary active compounds. Quercetin conjugated by UGT1A1 and SULT1A1. CYP3A4 involvement minimal.",
        "excretion": "Urinary excretion of anthocyanin glucuronides and phenolic acid metabolites within 24 hours. Quercetin metabolites in urine and bile. Polyphenol metabolites excreted over 24–48 hours."
      },
      "safety_and_interactions": {
        "drug_interactions": "Immunosuppressants (cyclosporin, tacrolimus) — pharmacodynamic antagonism via immune stimulation; avoid concurrent use. Diuretics — additive diuretic effect. Antidiabetic agents — anthocyanins improve insulin sensitivity; monitor blood glucose. Antiviral drugs (oseltamivir) — theoretical synergy via complementary neuraminidase inhibition; not formally studied.",
        "toxicity": "Sambunigrin in raw berries, bark, and leaves: cyanide-equivalent doses cause nausea, vomiting, weakness (case series documented). Cooking or commercial preparation completely eliminates this risk. No toxicity documented with properly prepared commercial extracts."
      },
      "special_precautions": {
        "pregnancy": "Insufficient clinical safety data for high-dose supplements. Elderflower tea at culinary quantities is generally considered safe. Avoid concentrated berry extracts during pregnancy.",
        "lactation": "No documented harm at normal dietary quantities. High-dose supplemental extracts not studied; avoid concentrated preparations.",
        "hepatic_impairment": "No hepatotoxicity documented. Quercetin conjugation may be impaired in severe liver disease. No dose adjustment guidelines established.",
        "renal_impairment": "No specific contraindication. Phenolic acid metabolites are renally excreted. No dose adjustment established for moderate impairment."
      }
    },
    "consumer_view": {
      "tagline": "Proven antiviral — shortens flu and colds by directly blocking the virus",
      "what_it_does": "Elderberry is one of the few herbal remedies with direct antiviral evidence — its anthocyanins physically block influenza and cold viruses from entering your cells. Clinical trials show it reduces flu duration by up to 4 days and cold severity when taken at the onset of illness. It also stimulates the immune system to respond faster.",
      "typical_uses": [
        "Influenza (flu) — reducing severity and duration",
        "Common cold prevention and treatment",
        "Upper respiratory tract infections",
        "Travel immune support"
      ],
      "suggested_dose": "Syrup (standardised to ≥3.2% anthocyanins): 15 ml (1 tablespoon) 4 times daily for up to 5 days during illness. Capsules: 500–1,000 mg extract twice daily. Start at first sign of illness for best results. Never consume raw elderberries.",
      "onset": "Antiviral effects begin within hours of first dose. Clinical improvement typically seen within 2–3 days of starting treatment.",
      "safety_snapshot": [
        "Never eat raw elderberries, bark, or leaves — toxic until cooked or extracted",
        "Avoid if on transplant or autoimmune medication",
        "Pregnant women should stick to culinary (food) quantities only"
      ]
    }
  },
  {
    "scientific_name": "Astragalus propinquus",
    "common_name": "Astragalus / Huang Qi / Milk-vetch root",
    "type": "Plant",
    "article_count": 1476,
    "primary_categories": ["Immunomodulation", "Adaptogen", "Cardioprotection", "Anti-ageing"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42068430/",
        "https://pubmed.ncbi.nlm.nih.gov/42055533/",
        "https://pubmed.ncbi.nlm.nih.gov/42009593/"
      ]
    },
    "narrative_summary": {
      "historical_use": "One of the most important tonic herbs in Traditional Chinese Medicine (TCM), first described in the Shen Nong Ben Cao Jing (c. 100 CE) as a superior-grade tonic for tonifying 'Wei Qi' (defensive vital energy) — the TCM concept roughly equivalent to immune function. The name 'Huang Qi' means 'yellow leader,' referring to the yellow root and its status as a leading tonic herb. Used for over 2,000 years as an immune tonic, adaptogen, and treatment for fatigue, night sweats, and general debility.",
      "modern_application": "Clinically studied as an immunomodulatory adjunct in oncology — a meta-analysis of 34 RCTs (2006, Journal of Clinical Oncology) found astragalus injection combined with chemotherapy significantly improved survival in non-small cell lung cancer. Astragaloside IV (the primary saponin) received particular attention after the discovery that cycloastragenol (its aglycone, marketed as TA-65) activates telomerase, potentially extending cellular lifespan — studied in small human trials with preliminary positive results on immune cell telomere length. Widely used in integrative oncology and as a general immune tonic.",
      "side_effects": "Exceptionally well tolerated; among the safest adaptogens available. Mild GI upset (nausea, loose stools) at high doses. Rare allergic reactions. Autoimmune exacerbation possible (immune-stimulating activity). Theoretical concern about immune-stimulating activity promoting graft rejection in transplant patients.",
      "contraindications": "Contraindicated with immunosuppressants (transplant antirejection drugs) — pharmacodynamic antagonism. Caution in active autoimmune flares. Avoid with lithium (potential diuretic-like effect reducing renal clearance of lithium). Very high doses may interfere with blood pressure control (hypotensive at very high doses)."
    },
    "clinical_data": {
      "used_part": "Root (4–7 years old; dried slices, decoction, or standardised extract)",
      "primary_active_compounds": [
        "Astragalosides I–IV (lanostane-type triterpene saponins — primary active)",
        "Cycloastragenol (aglycone of astragaloside IV; telomerase activator; TA-65 base compound)",
        "Astragalus polysaccharides (APS — arabinogalactans, glucans; primary immunostimulant)",
        "Formononetin and calycosin (isoflavones; phytoestrogenic, cardioprotective)",
        "Astragalin (kaempferol-3-glucoside; antioxidant)",
        "Canavanine (non-protein amino acid — trace; immunomodulatory)"
      ],
      "mechanism_of_action": "Astragalus polysaccharides (APS) activate macrophages, dendritic cells, and <strong>NK cells</strong> via <strong>TLR-4</strong> and <strong>Dectin-1</strong> signalling, upregulating <strong>IL-2</strong>, <strong>IFN-γ</strong>, and <strong>TNF-α</strong> production. Astragaloside IV and cycloastragenol activate <strong>telomerase (hTERT)</strong> — the enzyme that maintains telomere length — by epigenetic derepression of the hTERT gene, potentially slowing cellular ageing. Cardioprotective via <strong>eNOS</strong> upregulation, NO production, and inhibition of cardiomyocyte apoptosis. Anti-tumour via <strong>NK cell</strong> activation and restoration of T-lymphocyte function suppressed by chemotherapy. APS modulate the <strong>Th1/Th2</strong> immune axis, correcting the Th2 dominance associated with chronic illness.",
      "pharmacokinetics": {
        "absorption": "Astragalosides are poorly absorbed intact due to high molecular weight and hydrophilicity. Cycloastragenol (deglycosylated form) is significantly more bioavailable. APS act primarily in the GI tract and at mucosal surfaces; systemic absorption is limited. Formononetin and calycosin are well absorbed and undergo hepatic metabolism.",
        "distribution": "Astragalosides distribute to lymphoid organs (spleen, thymus, lymph nodes), bone marrow, and liver — consistent with immunomodulatory and haematopoietic effects. Cycloastragenol penetrates immune cell nuclei (evidence from telomerase activation studies). APS concentrate in GALT and spleen.",
        "metabolism": "Astragalosides undergo gut microbial deglycosylation to cycloastragenol (primary bioactive form). Cycloastragenol is further hepatically hydroxylated. Formononetin converted to daidzein by gut bacteria; both conjugated in liver. Calycosin undergoes ring-opening.",
        "excretion": "Biliary (primary) and urinary. Cycloastragenol metabolites excreted in faeces via bile. Formononetin and calycosin metabolites in urine. Half-life of cycloastragenol metabolites not well established in humans."
      },
      "safety_and_interactions": {
        "drug_interactions": "Immunosuppressants (cyclosporin, tacrolimus, mycophenolate, prednisone) — pharmacodynamic antagonism; may lead to graft rejection in transplant patients; contraindicated. Cyclophosphamide and other chemotherapy agents — APS may reduce myelosuppression (protective effect); clinically studied. Lithium — possible reduction in renal lithium clearance; monitor lithium levels. Antihypertensives — mild vasodilatory activity may have additive effect at very high doses.",
        "toxicity": "LD50 >160 g/kg in mice (oral aqueous extract — extremely safe). No organ toxicity at therapeutic doses in any published clinical trial. Canavanine content in raw herb is negligible. Parenteral astragalus preparations (used in TCM hospitals) rarely associated with allergic reactions."
      },
      "special_precautions": {
        "pregnancy": "Insufficient human safety data. Isoflavone content (formononetin) suggests caution due to phytoestrogenic activity. Avoid during pregnancy.",
        "lactation": "No documented harm. Isoflavone excretion in breast milk is possible. Avoid high-dose standardised extracts during breastfeeding.",
        "hepatic_impairment": "No specific dose adjustment required. Hepatoprotective effects demonstrated in clinical trials for viral hepatitis. Safe at standard doses in liver disease.",
        "renal_impairment": "Mild diuretic-like activity at high doses; caution with lithium co-administration. No contraindication at standard therapeutic doses. Monitor renal function in severe CKD."
      }
    },
    "consumer_view": {
      "tagline": "Deep immune tonic that may also slow cellular ageing — safe for long-term use",
      "what_it_does": "Astragalus has been used as a daily immune tonic in China for thousands of years. Modern research shows it activates the immune system at a deep level — boosting natural killer cells and helping immune function recover after illness or chemotherapy. It is also being studied for its ability to activate telomerase, an enzyme linked to cellular longevity.",
      "typical_uses": [
        "Long-term immune strengthening and resilience",
        "Recovery from illness or chemotherapy",
        "Chronic fatigue and low vitality",
        "Adjunct support during cancer treatment (under medical supervision)",
        "Anti-ageing and cellular health"
      ],
      "suggested_dose": "500–1,500 mg of standardised root extract (containing ≥70% APS or ≥0.5% astragalosides) twice daily. Can also be taken as a traditional decoction (9–30 g dried root per day). Safe for long-term continuous use.",
      "onset": "Immune activation markers: 2–4 weeks. Clinical resilience and energy improvements: 4–8 weeks of regular use.",
      "safety_snapshot": [
        "Do not take if you are on transplant or immunosuppressant medication",
        "Avoid during active autoimmune flare-ups",
        "Safe for most people long-term — one of the safest adaptogens available"
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
