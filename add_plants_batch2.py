#!/usr/bin/env python3
"""Batch 2 — Withania somnifera, Valeriana officinalis, Matricaria chamomilla, Passiflora incarnata"""
import json

PLANTS = [
  {
    "scientific_name": "Withania somnifera",
    "common_name": "Ashwagandha / Indian winter cherry",
    "type": "Plant",
    "article_count": 1974,
    "primary_categories": ["Adaptogen", "Stress & anxiety", "Reproductive health", "Thyroid support"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42143351/",
        "https://pubmed.ncbi.nlm.nih.gov/42130673/",
        "https://pubmed.ncbi.nlm.nih.gov/42129799/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Ashwagandha ('smell of horse' in Sanskrit — referring to the root's odour and its reputed ability to confer the strength and virility of a horse) has been central to Ayurvedic medicine for over 3,000 years. Classified as a 'rasayana' (rejuvenating tonic) in the Charaka Samhita and Ashtanga Hridayam, it was prescribed for debility, emaciation, nervous exhaustion, and as a male reproductive tonic. The specific epithet 'somnifera' (sleep-inducing) refers to its sedative and anxiolytic properties.",
      "modern_application": "Among the most commercially successful adaptogens globally. A 2021 systematic review and meta-analysis of 12 RCTs (Pratte et al. updated) found significant reductions in stress and anxiety scores and cortisol levels. KSM-66 and Sensoril (ashwagandha root and leaf extracts respectively) are the most studied standardised extracts. RCTs demonstrate improved maximal oxygen uptake (VO₂max), muscle strength, and recovery in athletes. A 2019 RCT found significant increases in testosterone and sperm quality in infertile men. Emerging evidence for TSH modulation and thyroid hormone support in subclinical hypothyroidism.",
      "side_effects": "Generally well tolerated. GI discomfort (nausea, loose stools) most common. Drowsiness at higher doses (>600 mg/day). Rare but documented: hepatotoxicity (case reports of cholestatic and hepatocellular injury, some requiring liver transplantation — likely rare idiosyncratic reactions). Thyroid hormone elevation (potential concern in hyperthyroid patients). Possible worsening of autoimmune conditions.",
      "contraindications": "Contraindicated in autoimmune diseases (rheumatoid arthritis, lupus, Hashimoto's thyroiditis) — immune-stimulating activity may exacerbate flares. Avoid in hyperthyroidism. Contraindicated with immunosuppressants (pharmacodynamic antagonism). Avoid with benzodiazepines and CNS depressants (additive sedation). Contraindicated during pregnancy (uterotonic alkaloids). Discontinue ≥2 weeks before surgery."
    },
    "clinical_data": {
      "used_part": "Root (primary therapeutic use); leaf (Sensoril extract); berry and seed (limited use)",
      "primary_active_compounds": [
        "Withanolides (withanolide A, withaferin A — steroidal lactones)",
        "Withanosides I–VII (glycosides of withanolides)",
        "Sitoindosides VII–X (acyl steryl glucosides)",
        "Alkaloids (somniferin, withanine, cuscohygrine)",
        "Withanoside IV and VI (neuroprotective)",
        "Oligosaccharides (immunomodulatory)"
      ],
      "mechanism_of_action": "Withanolides modulate the <strong>GABA-A receptor</strong> (positive allosteric modulation at the benzodiazepine site), producing anxiolytic and sedative effects without dependence risk. Withaferin A inhibits the <strong>NF-κB</strong> signalling pathway by covalently binding IκBα kinase (IKKβ), reducing pro-inflammatory cytokines (<strong>IL-6</strong>, <strong>TNF-α</strong>, <strong>COX-2</strong>). HPA axis regulation: withanolides reduce <strong>CRH</strong> expression and sensitise glucocorticoid receptors, normalising cortisol hypersecretion. Upregulate <strong>BDNF</strong> and promote axonal and dendritic growth (neuroprotective). Anabolic effects via <strong>LH</strong> stimulation and direct androgenic activity at the androgen receptor. Modest upregulation of <strong>TSH</strong> receptor sensitivity, supporting T3 and T4 production.",
      "pharmacokinetics": {
        "absorption": "Withanolides are lipophilic; oral bioavailability is moderate (~30–70%). KSM-66 root extract shows Cmax for withanolide A at approximately 2–4 hours. Co-administration with fat enhances absorption. Standard clinical doses: 300–600 mg extract twice daily.",
        "distribution": "Highly lipophilic withanolides distribute broadly to CNS, gonads, and adrenal glands — consistent with adaptogenic and reproductive effects. Accumulates in adipose tissue. Crosses the blood-brain barrier. Plasma protein binding estimated >85%.",
        "metabolism": "Hepatic CYP3A4 and CYP2C9 metabolism. Withanolides undergo hydroxylation and glucuronidation. Withaferin A has reactive α,β-unsaturated lactone moiety — covalently modifies protein thiols (IKKβ) as part of its mechanism. Gut microbiota further metabolise withanosides.",
        "excretion": "Biliary (primary for lipophilic withanolides) and urinary (polar metabolites). Half-life estimated at 4–6 hours for withanolide A. Multiple daily dosing required for sustained plasma levels."
      },
      "safety_and_interactions": {
        "drug_interactions": "Immunosuppressants (cyclosporin, tacrolimus, mycophenolate) — pharmacodynamic antagonism via immune stimulation; contraindicated. Thyroid medications (levothyroxine) — additive thyroid stimulation; risk of hyperthyroidism symptoms; monitor TSH. Benzodiazepines and CNS depressants (alcohol, barbiturates) — additive sedation via GABA-A potentiation. Antidiabetic agents — additive hypoglycaemia (insulin-sensitising effect documented). Warfarin — possible pharmacodynamic interaction; monitor INR.",
        "toxicity": "LD50 >2,000 mg/kg in mice (aqueous extract). Case reports of severe hepatotoxicity (cholestatic liver injury, acute liver failure) at standard doses — estimated incidence very low but potentially serious. Uterotonic alkaloids (somniferin) are responsible for pregnancy risk. High-dose chronic animal studies showed no significant organ toxicity."
      },
      "special_precautions": {
        "pregnancy": "Contraindicated. Uterotonic alkaloids (somniferin, withanine) can stimulate uterine contractions and increase miscarriage risk. Avoid throughout pregnancy.",
        "lactation": "Withanolide excretion in breast milk not characterised. Avoid during breastfeeding due to insufficient safety data.",
        "hepatic_impairment": "Rare idiosyncratic hepatotoxicity documented at standard doses. Avoid in patients with pre-existing hepatic disease. Monitor LFTs (ALT, AST, ALP, bilirubin) in all users at 8–12 weeks.",
        "renal_impairment": "No specific contraindication established. Polar metabolites excreted renally; accumulation possible in severe CKD. Use with caution and monitoring."
      }
    },
    "consumer_view": {
      "tagline": "Reduces stress and anxiety, builds strength, and supports restful sleep",
      "what_it_does": "Ashwagandha is the most popular Ayurvedic herb in the West — and for good reason. Clinical studies consistently show it lowers cortisol (the stress hormone), reduces anxiety, improves sleep quality, and supports muscle strength and recovery. It works best taken daily over several weeks.",
      "typical_uses": [
        "Chronic stress and anxiety",
        "Poor sleep quality",
        "Athletic performance and muscle recovery",
        "Low testosterone and male fertility",
        "Mental fatigue and burnout"
      ],
      "suggested_dose": "300–600 mg of standardised root extract (KSM-66 or Sensoril; ≥5% withanolides) once or twice daily with meals. Most studies show clear benefits after 8 weeks of daily use.",
      "onset": "Sleep improvement: 1–2 weeks. Anxiety and stress reduction: 2–4 weeks. Strength and hormonal effects: 8–12 weeks.",
      "safety_snapshot": [
        "Do not take during pregnancy — can cause miscarriage",
        "Avoid if you have an autoimmune disease (lupus, RA, Hashimoto's)",
        "Rare but serious liver reactions reported — stop if you develop jaundice or dark urine"
      ]
    }
  },
  {
    "scientific_name": "Valeriana officinalis",
    "common_name": "Valerian",
    "type": "Plant",
    "article_count": 1407,
    "primary_categories": ["Sedation & sleep", "Anxiolytic", "Antispasmodic"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42152921/",
        "https://pubmed.ncbi.nlm.nih.gov/42058246/",
        "https://pubmed.ncbi.nlm.nih.gov/41995686/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Used medicinally since at least ancient Greece and Rome; Hippocrates described its properties and Galen prescribed it for insomnia. The name 'valerian' may derive from the Latin 'valere' (to be strong/healthy) or from the Roman province of Valeria. Widely used in Europe throughout the medieval period as a sedative and antispasmodic. During World War I and II, valerian was used to treat shell shock and nerve tension in civilian populations.",
      "modern_application": "European Medicines Agency (EMA) has approved valerian as a traditional herbal medicine for temporary relief of mild symptoms of stress and sleep difficulties. Meta-analyses of RCTs show modest but consistent improvement in subjective sleep quality, sleep latency, and sleep architecture. Most robust evidence is for aqueous root extract at 400–900 mg taken 30–60 minutes before sleep. Evidence for anxiety is less consistent but positive in some RCTs. Often combined with hops (Humulus lupulus) for synergistic sedation.",
      "side_effects": "Generally well tolerated. Paradoxical stimulation (agitation, restlessness) in some individuals — particularly children and the elderly. Morning drowsiness ('hangover effect') at high doses. Headache and GI upset. Rare: hepatotoxicity with prolonged use of valepotriate-containing preparations (valepotriates are potentially alkylating — largely destroyed in aqueous extracts). Withdrawal effects reported after abrupt discontinuation following long-term use (insomnia rebound, anxiety).",
      "contraindications": "Avoid concomitant use with CNS depressants (benzodiazepines, barbiturates, opioids, alcohol) — additive sedation. Avoid in hepatic disease (hepatotoxicity risk with valepotriate-rich preparations). Do not take before driving or operating machinery. Avoid in children under 3 years. Caution with anaesthesia — taper and discontinue ≥2 weeks before surgery."
    },
    "clinical_data": {
      "used_part": "Root and rhizome (dried; aqueous or hydroethanolic extract)",
      "primary_active_compounds": [
        "Valerenic acid (sesquiterpene carboxylic acid; primary marker)",
        "Acetoxyvalerenol and hydroxyvalerenic acid (sesquiterpene metabolites)",
        "Valepotriates: valtrate, didrovaltrate, isovaltrate (iridoid monoterpenes — unstable in aqueous extract)",
        "Isovaleric acid (volatile; characteristic odour)",
        "Linarin and hesperidin (flavonoids)",
        "GABA (measurable amounts in root extract)"
      ],
      "mechanism_of_action": "Valerenic acid is a positive allosteric modulator of the <strong>GABA-A receptor</strong>, binding selectively to the β3 subunit and potentiating chloride influx — distinct from the benzodiazepine binding site, which explains the lack of dependence and tolerance. Valerenic acid also inhibits <strong>GABA transaminase (GABA-T)</strong>, the enzyme responsible for GABA degradation, raising synaptic GABA concentrations. Partial agonist activity at the <strong>5-HT5a receptor</strong> may contribute to anxiolytic and circadian rhythm-modulating effects. Linarin and hesperidin inhibit <strong>adenosine deaminase</strong>, increasing extracellular adenosine (sleep-promoting). Isovaleric acid modulates <strong>GABA-A</strong> receptor directly.",
      "pharmacokinetics": {
        "absorption": "Valerenic acid is absorbed rapidly; Cmax at approximately 1–2 hours after oral administration. Aqueous extract bioavailability is adequate for therapeutic effect. Valepotriates are poorly absorbed and largely hydrolysed in the gut to baldrinal (partially responsible for activity).",
        "distribution": "Valerenic acid crosses the blood-brain barrier. Distributes to CNS, liver, and kidney. Plasma protein binding estimated at ~60–80%. Lipophilic valepotriate metabolites accumulate in adipose tissue.",
        "metabolism": "Hepatic oxidative metabolism of valerenic acid (CYP2C9 and CYP3A4). Valepotriates hydrolysed in gut to homobaldrinal and baldrinal (partially bioactive). Isovaleric acid undergoes β-oxidation. Linarin undergoes hepatic glucuronidation.",
        "excretion": "Urinary excretion of valerenic acid metabolites. Half-life of valerenic acid ~1.1 hours; short half-life necessitates pre-sleep dosing. Baldrinal metabolites excreted in both bile and urine."
      },
      "safety_and_interactions": {
        "drug_interactions": "CNS depressants (benzodiazepines, barbiturates, opioids, zopiclone, alcohol) — additive sedation; respiratory depression risk at high combined doses. CYP3A4 substrates — possible mild inhibition increasing drug plasma levels. Antiepileptics (valproate) — theoretical GABA-T interaction; monitor. Loperamide and antispasmodics — additive GI motility reduction.",
        "toxicity": "LD50 >3,000 mg/kg in mice. Valepotriates show in vitro alkylating and cytotoxic activity but are largely destroyed in standard aqueous and hydroethanolic extracts. No serious adverse events in RCTs at therapeutic doses. Long-term use (>4–6 weeks) not well studied; taper gradually to avoid rebound insomnia."
      },
      "special_precautions": {
        "pregnancy": "Insufficient human safety data. Valepotriates show cytotoxic activity in vitro and potential mutagenicity. Avoid during pregnancy.",
        "lactation": "Excretion in breast milk unknown. Avoid due to insufficient data.",
        "hepatic_impairment": "Valepotriate-rich preparations associated with hepatotoxicity in animal studies. Use only aqueous extracts (valepotriate-poor) with caution in hepatic disease. Monitor LFTs.",
        "renal_impairment": "No specific contraindication. Urinary excretion of metabolites; monitoring recommended in severe renal impairment."
      }
    },
    "consumer_view": {
      "tagline": "Natural sleep aid that calms the nervous system without next-day grogginess",
      "what_it_does": "Valerian is one of the most widely used herbal sleep aids in Europe and North America. It works by boosting GABA — the brain's main calming signal — similar to how sleep medications work, but without the risk of dependence or strong morning drowsiness. It is best for difficulty falling asleep and restless, anxious minds at bedtime.",
      "typical_uses": [
        "Difficulty falling asleep",
        "Stress-related sleep disruption",
        "Mild anxiety and nervous tension",
        "Restless legs (in combination products)",
        "Menopausal sleep disturbance"
      ],
      "suggested_dose": "400–900 mg of aqueous root extract 30–60 minutes before bed. Results may take 2–4 weeks of nightly use to fully establish. Often combined with hops or lemon balm for enhanced effect.",
      "onset": "Some individuals notice effects from the first night; most see reliable improvement after 2–4 weeks of consistent use.",
      "safety_snapshot": [
        "Do not drive or operate machinery after taking",
        "Do not combine with prescription sleep aids, benzodiazepines, or alcohol",
        "Taper gradually after long-term use — abrupt stop can cause rebound insomnia"
      ]
    }
  },
  {
    "scientific_name": "Matricaria chamomilla",
    "common_name": "German chamomile",
    "type": "Plant",
    "article_count": 958,
    "primary_categories": ["Anxiolytic", "Anti-inflammatory", "GI support", "Wound healing"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42148629/",
        "https://pubmed.ncbi.nlm.nih.gov/42141424/",
        "https://pubmed.ncbi.nlm.nih.gov/42122886/"
      ]
    },
    "narrative_summary": {
      "historical_use": "One of the oldest and most widely used medicinal herbs in the world, with documented use stretching back to ancient Egypt, Greece, and Rome. The ancient Egyptians dedicated chamomile to their sun god Ra and used it as a fever remedy. In European folk medicine it was called 'alles zutraut' (capable of anything) in German tradition. Its name derives from the Greek 'chamaimelon' (ground apple) due to its apple-like fragrance.",
      "modern_application": "A 2016 RCT (Mao et al., University of Pennsylvania) demonstrated significant reduction in generalised anxiety disorder (GAD) symptoms over 26 weeks, including reduced relapse rates, making it one of the most clinically robust herbal anxiolytics. Well-established topical use for wound healing, inflammation, and eczema. GI applications supported by RCTs for infantile colic, dyspepsia, and IBS. European Pharmacopoeia-approved for internal and external use.",
      "side_effects": "Generally extremely well tolerated. Allergic reactions in individuals sensitised to Asteraceae/Compositae family plants (ragweed, chrysanthemum, marigold) — anaphylaxis reported rarely. Contact dermatitis with topical preparations (uncommon). Additive sedation with CNS depressants at high doses. GI upset in very high doses. Emmenagogue effects (stimulates menstruation) at high doses.",
      "contraindications": "Contraindicated in known Asteraceae allergy. Caution with anticoagulants (apigenin inhibits platelet aggregation). Avoid high-dose preparations during pregnancy (emmenagogue and theoretical uterotonic effects at high doses). Caution with benzodiazepines — GABA-A receptor modulation may potentiate sedation."
    },
    "clinical_data": {
      "used_part": "Flower head (capitulum); dried herb; essential oil (steam distillation)",
      "primary_active_compounds": [
        "Apigenin (flavone; primary anxiolytic compound)",
        "α-Bisabolol (sesquiterpene alcohol; anti-inflammatory, wound healing)",
        "Chamazulene (formed from matricine during steam distillation; deep blue; potent anti-inflammatory)",
        "Matricine (sesquiterpene lactone precursor to chamazulene)",
        "Luteolin and quercetin (flavone and flavonol)",
        "Mucilage polysaccharides (GI soothing)",
        "Spiro ether (en-yne-bicyclo[2.2.1]heptene derivatives)"
      ],
      "mechanism_of_action": "Apigenin is a partial agonist at the <strong>GABA-A receptor</strong> benzodiazepine binding site (Kd ~4 µM), producing anxiolysis without significant sedation, tolerance, or muscle relaxation at therapeutic doses. Apigenin also inhibits <strong>CYP1A2</strong> and <strong>CYP2C9</strong>. α-Bisabolol and chamazulene selectively inhibit <strong>COX-1</strong>, <strong>COX-2</strong>, and <strong>5-LOX</strong>, reducing prostaglandin E2 and leukotriene B4. Apigenin inhibits <strong>TNF-α</strong> transcription and <strong>NF-κB</strong> activation. GI antispasmodic effect via blockade of <strong>L-type Ca²⁺ channels</strong> in intestinal smooth muscle. Luteolin inhibits <strong>histamine</strong> release from mast cells.",
      "pharmacokinetics": {
        "absorption": "Apigenin well absorbed (bioavailability ~30% from glycoside forms after gut hydrolysis). Food slightly delays but does not reduce Cmax. α-Bisabolol absorbed transdermally and orally; Cmax at 1–2 hours. Chamazulene is present only in essential oil (formed from matricine by steam distillation).",
        "distribution": "Apigenin distributes to CNS; plasma protein binding >99% (primarily to albumin). Despite high protein binding, CNS penetration sufficient for anxiolytic effect. α-Bisabolol distributes to skin, liver, and adipose tissue.",
        "metabolism": "Apigenin undergoes extensive hepatic glucuronidation and sulfation (UGT1A1, UGT1A9, SULT1A1). Also undergoes bacterial ring-fission in large intestine producing bioactive phenolic metabolites. Inhibits CYP1A2, CYP2C9, and CYP3A4 — clinically relevant at high doses. α-Bisabolol hydroxylated by CYP enzymes.",
        "excretion": "Urinary excretion of glucuronide and sulfate conjugates. Half-life of apigenin ~1–4 hours (varies by formulation). Chamazulene and terpenoid metabolites excreted via bile."
      },
      "safety_and_interactions": {
        "drug_interactions": "Warfarin and anticoagulants — apigenin inhibits platelet aggregation and CYP2C9 (warfarin metabolism); elevated INR possible. Benzodiazepines and CNS depressants — additive sedation via GABA-A potentiation. CYP1A2 substrates (theophylline, clozapine, caffeine) — apigenin inhibition increases plasma levels. Oestrogen-containing contraceptives — weak phytoestrogenic activity of apigenin may interact theoretically.",
        "toxicity": "LD50 >5,000 mg/kg in rodents (aqueous extract). Anaphylaxis is the most serious risk (rare; in Asteraceae-sensitised individuals). Mutagenicity of chamazulene at very high concentrations in vitro (not clinically relevant at therapeutic doses). No hepatotoxicity documented."
      },
      "special_precautions": {
        "pregnancy": "Avoid high-dose preparations and concentrated extracts during pregnancy — emmenagogue and theoretical uterotonic effects at pharmacological doses. Chamomile tea at normal culinary quantities is generally considered safe.",
        "lactation": "No evidence of harm at normal consumption levels. High-dose extracts not recommended due to insufficient data.",
        "hepatic_impairment": "CYP2C9 inhibition may impair metabolism of co-administered drugs. No direct hepatotoxicity documented. Use with caution in severe hepatic impairment.",
        "renal_impairment": "No specific contraindication. Conjugated metabolites renally excreted; no dose adjustment established."
      }
    },
    "consumer_view": {
      "tagline": "Gentle daily calm — reduces anxiety, soothes digestion, and promotes sleep",
      "what_it_does": "German chamomile is one of the safest and most versatile herbal medicines available. It calms the nervous system similarly to low-dose anti-anxiety medications (but much more gently), soothes the digestive tract, and reduces inflammation both inside the body and on the skin. It is suitable for long-term daily use.",
      "typical_uses": [
        "Generalised anxiety and nervous tension",
        "Difficulty falling asleep",
        "Irritable bowel syndrome and bloating",
        "Skin inflammation and eczema (topical)",
        "Infant colic (chamomile tea)"
      ],
      "suggested_dose": "Anxiety and sleep: 220–1,100 mg of standardised extract (1.2% apigenin) daily. As tea: 1–3 g dried flowers per cup, steeped 10 minutes, up to 3 cups daily. For sleep, drink 30–45 minutes before bed.",
      "onset": "GI and mild sedative effects: within 30–60 minutes. Sustained anxiety reduction: 2–4 weeks of regular use.",
      "safety_snapshot": [
        "Avoid if you are allergic to ragweed, daisies, or chrysanthemums",
        "High-dose extracts are not recommended during pregnancy",
        "May increase the effect of blood thinners — check with your doctor"
      ]
    }
  },
  {
    "scientific_name": "Passiflora incarnata",
    "common_name": "Passionflower / Maypop",
    "type": "Plant",
    "article_count": 1323,
    "primary_categories": ["Anxiolytic", "Sedation & sleep", "Antispasmodic"],
    "sources": {
      "top_studies_urls": [
        "https://pubmed.ncbi.nlm.nih.gov/42129035/",
        "https://pubmed.ncbi.nlm.nih.gov/42123393/",
        "https://pubmed.ncbi.nlm.nih.gov/42083443/"
      ]
    },
    "narrative_summary": {
      "historical_use": "Native to the southeastern United States, Mexico, and Central America. Used extensively by indigenous peoples of North America (Cherokee, Houma, Algonquin) for insomnia, epilepsy, and as a general nerve tonic. Introduced to European medicine in the 17th century by Spanish explorers who named it for the symbolic resemblance of the flower parts to the instruments of Christ's Passion. Included in the US National Formulary from 1916–1936 as a sedative.",
      "modern_application": "European Medicines Agency (EMA) recognises passionflower for traditional use in mild anxiety and sleep disorders. A double-blind RCT (Akhondzadeh et al., 2001) found passionflower equivalent to oxazepam for generalised anxiety disorder with fewer job performance impairment side effects. Used pre-operatively: a 2011 RCT showed significant reduction in pre-surgical anxiety without sedation (unlike midazolam). Most often used in combination with valerian and hops in sleep and anxiety formulations.",
      "side_effects": "Generally mild and infrequent. Drowsiness and sedation (dose-dependent). Dizziness, confusion, and impaired coordination at high doses. GI discomfort (nausea, vomiting) occasionally. Rare: vasculitis reported in a case report. Rare hypersensitivity. Possible paradoxical agitation (similar to valerian).",
      "contraindications": "Avoid concomitant use with benzodiazepines, barbiturates, opioids, and alcohol (additive CNS depression). Contraindicated with MAO inhibitors — harmala alkaloid content (harmine, harmaline traces). Do not use before driving or operating machinery. Avoid in children under 6 years."
    },
    "clinical_data": {
      "used_part": "Aerial parts: leaf, stem, tendril, and flower (dried herb or hydroethanolic extract)",
      "primary_active_compounds": [
        "Chrysin (5,7-dihydroxyflavone; primary anxiolytic flavone)",
        "Vitexin (apigenin-8-C-glucoside)",
        "Isovitexin (apigenin-6-C-glucoside)",
        "Orientin and isoorientin (luteolin C-glycosides)",
        "Harmane alkaloids (harmine, harmol — trace quantities; MAO-inhibiting)",
        "Passiflorine (alkaloid)",
        "GABA (measurable in extract)"
      ],
      "mechanism_of_action": "Chrysin binds the <strong>GABA-A receptor</strong> at the benzodiazepine site as a partial agonist, producing anxiolysis with minimal sedation — lower intrinsic efficacy than full benzodiazepines reduces side effect risk. Vitexin and isovitexin inhibit <strong>MAO-B</strong>, mildly elevating dopamine and phenylethylamine. Flavone C-glycosides (orientin, isoorientin) modulate <strong>GABA-A</strong> receptor activity and inhibit <strong>5-HT₂</strong> receptor binding. Chrysin inhibits the peripheral benzodiazepine receptor (<strong>TSPO</strong>) in mitochondria, modulating neurosteroid synthesis (allopregnanolone). Passiflorine has mild antispasmodic activity via <strong>muscarinic receptor</strong> antagonism.",
      "pharmacokinetics": {
        "absorption": "Chrysin has very low oral bioavailability (<1%) due to extensive first-pass sulfation and glucuronidation — limiting systemic availability despite in vitro potency. Vitexin and isovitexin (C-glycosides) are better absorbed (~25–30%) and contribute significantly to clinical activity. Cmax at 1–2 hours for flavone C-glycosides.",
        "distribution": "Vitexin and isovitexin penetrate the CNS at pharmacologically relevant concentrations (rodent brain distribution confirmed). Chrysin is extensively protein-bound (>97% albumin), with limited free fraction for CNS activity despite lipophilicity. Harmane alkaloids (trace) rapidly enter CNS.",
        "metabolism": "Chrysin: extensive hepatic sulfation (SULT1A1) and glucuronidation (UGT1A1, UGT1A3). Vitexin and isovitexin undergo deglycosylation and phenolic ring hydroxylation. CYP3A4 involvement minor. Harmane alkaloids: MAO-A and MAO-B substrates; rapid hepatic metabolism.",
        "excretion": "Urinary excretion of sulfate and glucuronide conjugates. Half-life of vitexin ~2–3 hours. Chrysin metabolites excreted in both urine and bile. Harmane alkaloids have very short plasma half-life (<1 hour)."
      },
      "safety_and_interactions": {
        "drug_interactions": "Benzodiazepines (diazepam, lorazepam, alprazolam) — additive GABA-A potentiation; enhanced sedation and respiratory depression. MAO inhibitors — harmane alkaloid content; hypertensive crisis risk; contraindicated. Opioid analgesics — additive CNS and respiratory depression. Anticoagulants (warfarin) — chrysin inhibits CYP2C9; potential INR elevation. SSRIs — mild 5-HT₂ antagonism may interact pharmacodynamically.",
        "toxicity": "LD50 not established for P. incarnata extract in humans. Rodent oral LD50 >900 mg/kg for total extract. Vasculitis reported in one case (temporal association, causality unproven). No hepatotoxicity documented in clinical literature. Harmane alkaloid content too low for direct MAO inhibition at therapeutic doses but relevant in combination with MAOIs."
      },
      "special_precautions": {
        "pregnancy": "Insufficient human safety data. Historically used to stimulate menstruation (emmenagogue). Passiflorine has uterotonic potential. Avoid during pregnancy.",
        "lactation": "No data on excretion in breast milk. Avoid concentrated preparations during breastfeeding.",
        "hepatic_impairment": "CYP2C9 and UGT substrate; reduced clearance expected in liver disease. No formal dose adjustment guidelines. Use with caution.",
        "renal_impairment": "Conjugated metabolites excreted renally. No specific dose adjustment established; monitoring recommended in severe renal impairment."
      }
    },
    "consumer_view": {
      "tagline": "Fast-acting natural anxiety relief without making you drowsy or dependent",
      "what_it_does": "Passionflower calms anxiety and reduces mental restlessness by working on the same brain pathway as anti-anxiety medications — but more gently, without the addiction risk or heavy sedation. Clinical trials have compared it favourably to oxazepam (a benzodiazepine) for generalised anxiety. It is also used before stressful events or surgery.",
      "typical_uses": [
        "Generalised anxiety and nervous tension",
        "Situational anxiety (pre-exam, pre-procedure)",
        "Sleep difficulties due to racing thoughts",
        "Mild withdrawal support (in combination products)",
        "Irritable bowel syndrome with anxiety component"
      ],
      "suggested_dose": "250–500 mg of standardised dried herb extract up to 3 times daily for anxiety, or 500–1,000 mg 30–60 minutes before bed for sleep. Also widely available as a liquid tincture (1:5, 45% ethanol): 1–4 ml up to 3 times daily.",
      "onset": "Acute anxiety relief: 30–60 minutes. Sleep improvement and sustained anxiety reduction: 1–2 weeks.",
      "safety_snapshot": [
        "Do not drive after taking — can cause drowsiness at higher doses",
        "Never combine with MAO inhibitors",
        "Avoid during pregnancy"
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
