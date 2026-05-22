#!/usr/bin/env python3
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

PLANTS = [
    {
        "id": "crataegus-monogyna",
        "common_name": "Hawthorn",
        "scientific_name": "Crataegus monogyna",
        "category": "plant",
        "tags": ["cardiovascular", "antioxidant", "cardiotonic", "traditional"],
        "overview": {
            "description": "Crataegus monogyna (common hawthorn) is a thorny shrub native to Europe, North Africa, and western Asia. Its berries, leaves, and flowers have been used for centuries in European herbal medicine as a cardiac tonic. Rich in oligomeric proanthocyanidins (OPCs) and flavonoids, hawthorn is one of the most extensively studied herbs for heart health, with evidence supporting use in mild-to-moderate chronic heart failure and hypertension.",
            "traditional_use": "European and Chinese traditional medicine used hawthorn berries and flowers for 'weak heart,' palpitations, anxiety, and poor circulation. In TCM, Shan Zha (C. pinnatifida) treats food stagnation and blood stasis. Medieval European herbalists prescribed hawthorn for 'heart-strengthening' and dropsy (oedema).",
            "article_count": 1507
        },
        "bioactive_compounds": {
            "primary": ["Oligomeric proanthocyanidins (OPCs)", "Vitexin-2-O-rhamnoside", "Hyperoside", "Rutin", "Chlorogenic acid"],
            "secondary": ["Epicatechin", "Quercetin", "Ursolic acid", "Oleanolic acid", "Caffeic acid"],
            "mechanism_of_action": "<strong>Positive inotropic effect:</strong> OPCs inhibit phosphodiesterase, increasing intracellular cAMP and enhancing myocardial contractility without increasing oxygen demand. <strong>Vasodilation:</strong> Flavonoids stimulate endothelial nitric oxide synthase (eNOS), increasing NO-mediated vascular relaxation and reducing peripheral resistance. <strong>Antioxidant cardioprotection:</strong> OPCs and flavonoids scavenge ROS and reduce oxidative damage to cardiomyocytes. <strong>Anti-arrhythmic:</strong> Hawthorn prolongs the refractory period in cardiac tissue by modulating potassium channels (IKr inhibition), reducing susceptibility to arrhythmias. <strong>Lipid-lowering:</strong> Increases LDL receptor expression and inhibits cholesterol biosynthesis."
        },
        "pharmacokinetics": {
            "absorption": "OPCs and flavonoids are absorbed in the small intestine; bioavailability is moderate (~30–40%) due to first-pass metabolism and poor aqueous solubility of some glycosides.",
            "distribution": "Distributed to cardiovascular tissues, liver, and kidneys. Flavonoids show preferential accumulation in heart and vascular endothelium.",
            "metabolism": "Hepatic glucuronidation and sulfation of flavonoid aglycones. OPCs are partially hydrolysed by gut microbiota to monomeric catechins before absorption.",
            "elimination": "Primarily renal excretion of conjugated metabolites; some biliary elimination. Half-life of major flavonoids: 2–6 hours."
        },
        "clinical_evidence": {
            "strong": ["Mild-to-moderate CHF (NYHA II–III): SPICE trial — hawthorn extract WS 1442 900 mg/day reduced symptom burden; HERB CHF trial showed safety but did not meet primary endpoint in severe CHF", "Blood pressure reduction: Meta-analysis of 14 RCTs showed significant reductions in diastolic BP (~3 mmHg)", "Exercise tolerance improvement in CHF patients across multiple RCTs"],
            "moderate": ["Anxiety reduction via anxiolytic flavonoids", "Lipid-lowering effects in hypercholesterolaemic patients", "Atherosclerosis prevention in animal models — human data limited"],
            "weak_or_preliminary": ["Neuroprotective effects", "Anti-diabetic activity", "Anti-cancer properties in vitro"]
        },
        "safety_profile": {
            "common_side_effects": ["Nausea", "Dizziness", "Gastrointestinal discomfort", "Headache", "Palpitations at high doses"],
            "serious_risks": ["May potentiate cardiac glycosides (digoxin) — increased risk of toxicity", "SPICE trial showed possible harm in advanced heart failure (LVEF <25%) — contraindicated in severe CHF", "Hypotension risk when combined with antihypertensives"],
            "contraindications": ["Severe heart failure", "Concurrent use of digoxin without monitoring", "Pregnancy (insufficient safety data)"],
            "drug_interactions": ["Digoxin (potentiation)", "Antihypertensives (additive effect)", "Nitrates (additive vasodilation)", "Phosphodiesterase inhibitors (additive)"],
            "pregnancy_lactation": "Insufficient safety data — avoid in pregnancy and lactation."
        },
        "dosing": {
            "standard_dose": "Standardised extract (WS 1442 or LI 132): 450–900 mg/day in divided doses; Crude berry/flower: 4–5 g/day as tea or tincture",
            "onset_of_action": "Cardiovascular effects typically require 4–8 weeks of consistent use",
            "forms_available": ["Standardised dry extract (18.75% OPCs)", "Tincture (1:5)", "Whole dried berries/flowers", "Capsules", "Tea"],
            "dosing_notes": "Most clinical trials used WS 1442 extract at 900 mg/day; efficacy data for crude preparations is more limited."
        },
        "sources": {
            "article_count": 1507,
            "top_studies_urls": [
                "https://pubmed.ncbi.nlm.nih.gov/26378574/",
                "https://pubmed.ncbi.nlm.nih.gov/41599280/",
                "https://pubmed.ncbi.nlm.nih.gov/40315641/"
            ]
        },
        "consumer_view": {
            "tagline": "The heart herb — nature's cardiotonic",
            "what_it_does": "Hawthorn gently strengthens the heart, improves blood flow, and helps manage mild high blood pressure. It's one of the few herbal medicines with solid clinical trial evidence behind it.",
            "typical_uses": ["Mild heart failure symptoms (breathlessness, fatigue)", "Mildly elevated blood pressure", "Palpitations and heart rate irregularities", "General cardiovascular support"],
            "suggested_dose": "Standardised extract (WS 1442): 450–900 mg daily, split into 2–3 doses. Give it 6–8 weeks to notice effects.",
            "onset": "Gradual — most people notice changes after 4–8 weeks of daily use.",
            "safety_snapshot": "Generally safe for most adults. Do NOT combine with heart medications (especially digoxin) without doctor supervision. Avoid in severe heart failure. Check with your GP before starting if you have any heart condition."
        }
    },
    {
        "id": "vitex-agnus-castus",
        "common_name": "Chaste Tree",
        "scientific_name": "Vitex agnus-castus",
        "category": "plant",
        "tags": ["hormonal", "women's health", "premenstrual", "prolactin", "traditional"],
        "overview": {
            "description": "Vitex agnus-castus (chaste tree or chasteberry) is a flowering shrub native to the Mediterranean and Central Asia. Its dried fruit has been used since antiquity to modulate female reproductive hormones. It is unique among herbs as a dopaminergic agent — its iridoid glycosides and diterpenes act on pituitary dopamine D2 receptors to inhibit prolactin secretion, making it clinically relevant for premenstrual syndrome, mastalgia, and cycle irregularities associated with hyperprolactinaemia.",
            "traditional_use": "Ancient Greeks and Romans used chaste tree to promote chastity by suppressing libido (hence the name). Hippocrates recommended it for uterine inflammation. In medieval Europe it was used by monks to suppress sexual urges. Later herbalists recognised its use for menstrual irregularities and premenstrual tension.",
            "article_count": 1070
        },
        "bioactive_compounds": {
            "primary": ["Agnuside (iridoid glycoside)", "Aucubin", "Casticin (flavonoid)", "Diterpenes (rotundifuran, vitexilactone)", "Vitexin"],
            "secondary": ["Penduletin", "Orientin", "Isovitexin", "Linoleic acid", "Progesterone-like sterols"],
            "mechanism_of_action": "<strong>Dopamine D2 receptor agonism:</strong> Diterpenes (particularly clerodadienols) bind pituitary dopamine D2 receptors, inhibiting prolactin release from lactotrophs — the primary clinical mechanism. <strong>Prolactin suppression:</strong> Reduced prolactin normalises the luteal phase, restoring progesterone-to-oestrogen balance and reducing PMS/mastalgia symptoms. <strong>Opioid receptor modulation:</strong> Beta-endorphin-like activity via mu-opioid receptors may contribute to mood-stabilising effects. <strong>Weak oestrogenic/anti-oestrogenic activity:</strong> Casticin shows selective oestrogen receptor modulation (SERM-like) at ER-beta, contributing to breast tissue effects. <strong>FSH/LH modulation:</strong> Indirect effects on gonadotropin ratio via hypothalamic feedback."
        },
        "pharmacokinetics": {
            "absorption": "Oral bioavailability is moderate; lipophilic diterpenes require fatty meal for optimal absorption. Agnuside is well absorbed and detectable in plasma within 1–2 hours.",
            "distribution": "Distributes to pituitary, hypothalamus, and reproductive organs. Diterpenes cross the blood-brain barrier to access dopaminergic neurons.",
            "metabolism": "Hepatic CYP3A4-mediated oxidation of diterpenes. Iridoid glycosides undergo gut microbiota hydrolysis to active aglycones.",
            "elimination": "Renal excretion of conjugated metabolites. Half-life of primary actives: 4–8 hours; clinical effects accumulate with chronic use."
        },
        "clinical_evidence": {
            "strong": ["Premenstrual syndrome (PMS): Multiple RCTs and meta-analyses show significant reduction in PMS symptom scores vs placebo; ZE 440 and Agnolyt extracts most studied", "Premenstrual dysphoric disorder (PMDD): Comparable efficacy to fluoxetine in small head-to-head trials", "Cyclic mastalgia: Significant pain reduction in breast pain RCTs"],
            "moderate": ["Luteal phase defect and cycle irregularities associated with latent hyperprolactinaemia", "Fertility support in women with luteal insufficiency", "Perimenopausal symptom management"],
            "weak_or_preliminary": ["Uterine fibroid management", "Acne related to hormonal fluctuations", "Hyperprolactinaemia of non-pituitary origin"]
        },
        "safety_profile": {
            "common_side_effects": ["Headache", "Nausea", "Acne-like skin reactions", "Menstrual irregularity (initial)", "Gastrointestinal upset", "Dizziness"],
            "serious_risks": ["Contraindicated in hormone-sensitive cancers (breast, uterine) due to oestrogenic activity", "May antagonise dopamine agonists (bromocriptine, cabergoline)", "Risk of ovarian hyperstimulation in fertility treatments"],
            "contraindications": ["Pregnancy and lactation (inhibits prolactin needed for breastfeeding)", "Hormone-sensitive cancers", "Concurrent use of dopamine antagonists (antipsychotics)", "IVF/ART cycles"],
            "drug_interactions": ["Dopamine antagonists/antipsychotics (mutual antagonism)", "Hormonal contraceptives (potential interaction)", "Bromocriptine/cabergoline (additive prolactin suppression)"],
            "pregnancy_lactation": "Contraindicated in pregnancy (insufficient safety data) and lactation (reduces milk supply via prolactin suppression)."
        },
        "dosing": {
            "standard_dose": "Standardised extract (0.5% agnuside): 20–40 mg/day as single morning dose; Crude dried fruit: 30–40 mg/day",
            "onset_of_action": "Hormonal effects emerge after 2–3 menstrual cycles; symptom improvement typically noted by cycle 2–3",
            "forms_available": ["Standardised capsules (ZE 440, Agnolyt)", "Tincture (1:5 in 60% ethanol)", "Dried whole berries", "Tablets"],
            "dosing_notes": "Best taken in the morning as a single dose. Must be used consistently for at least 3 months to assess efficacy. Do not combine with hormonal contraceptives without medical advice."
        },
        "sources": {
            "article_count": 1070,
            "top_studies_urls": [
                "https://pubmed.ncbi.nlm.nih.gov/23136064/",
                "https://pubmed.ncbi.nlm.nih.gov/38075075/",
                "https://pubmed.ncbi.nlm.nih.gov/29063202/"
            ]
        },
        "consumer_view": {
            "tagline": "The women's cycle herb — natural PMS and hormone support",
            "what_it_does": "Chaste tree helps balance female hormones by gently reducing a hormone called prolactin, which can be too high in some women. This can ease PMS symptoms, breast pain, and cycle irregularities.",
            "typical_uses": ["Premenstrual syndrome (mood swings, bloating, cramps)", "Cyclic breast pain", "Irregular menstrual cycles", "Hormonal acne"],
            "suggested_dose": "20–40 mg standardised extract daily, taken as a single morning dose. Use for at least 3 full menstrual cycles before judging effectiveness.",
            "onset": "Allow 2–3 months — hormonal herbs work slowly and need consistent daily use.",
            "safety_snapshot": "Do NOT use during pregnancy or breastfeeding. Avoid if you have hormone-sensitive cancer. Not suitable if taking antipsychotic medications. Otherwise well-tolerated by most women."
        }
    },
    {
        "id": "serenoa-repens",
        "common_name": "Saw Palmetto",
        "scientific_name": "Serenoa repens",
        "category": "plant",
        "tags": ["men's health", "prostate", "BPH", "anti-androgenic", "traditional"],
        "overview": {
            "description": "Serenoa repens (saw palmetto) is a small palm native to the southeastern United States. Its lipophilic berry extract is the most widely used phytomedicine for benign prostatic hyperplasia (BPH) globally. The lipid-sterol fraction inhibits 5-alpha-reductase and exhibits anti-inflammatory and anti-androgenic activity, making it relevant for urinary symptoms associated with prostate enlargement. It remains one of the most commercially successful herbal medicines in the US and Europe.",
            "traditional_use": "Native American tribes (Seminole, Cherokee) used saw palmetto berries as food and medicine for urinary and reproductive complaints in men. 19th-century Eclectic physicians prescribed it for 'atrophied testes,' low libido, and prostatitis. Modern use for BPH became mainstream in Europe by the 1970s–80s, predating finasteride.",
            "article_count": 576
        },
        "bioactive_compounds": {
            "primary": ["Free fatty acids (lauric, oleic, myristic acids)", "Beta-sitosterol", "Campesterol", "Stigmasterol", "Fatty acid esters"],
            "secondary": ["Flavonoids (isoquercitrin, rutin)", "Polysaccharides", "Triterpenes (oleanolic, ursolic acid)", "Aliphatic alcohols"],
            "mechanism_of_action": "<strong>5-alpha-reductase inhibition:</strong> The lipid-sterol fraction inhibits both type I and type II 5α-reductase isoenzymes, reducing conversion of testosterone to the more potent dihydrotestosterone (DHT) in prostate tissue — the primary driver of BPH. <strong>Androgen receptor antagonism:</strong> Beta-sitosterol and fatty acids compete with DHT for androgen receptor binding in prostatic cells. <strong>Anti-inflammatory activity:</strong> Inhibits COX-1/COX-2 and 5-LOX, reducing prostatic inflammation contributing to lower urinary tract symptoms. <strong>Anti-proliferative effect:</strong> Reduces prostatic epithelial and stromal cell proliferation via modulation of growth factor signalling (EGF-R, IGF-1R). <strong>Alpha-1 adrenergic receptor modulation:</strong> May relax smooth muscle in bladder neck and urethra, improving urine flow."
        },
        "pharmacokinetics": {
            "absorption": "Lipophilic extract is highly fat-soluble; bioavailability significantly enhanced when taken with food (fatty meal doubles absorption). Lauric acid detectable in plasma within 2–3 hours.",
            "distribution": "Preferentially distributes to prostatic tissue and adrenal glands. Beta-sitosterol achieves high concentrations in prostate after chronic dosing.",
            "metabolism": "Hepatic beta-oxidation of fatty acid components. Sterols are partially metabolised to bile acids. Minimal CYP450 involvement.",
            "elimination": "Biliary/faecal excretion predominates for sterols and fatty acids. Renal clearance for polar metabolites. Half-life of fatty acid actives: 6–10 hours."
        },
        "clinical_evidence": {
            "strong": ["Lower urinary tract symptoms (LUTS) in BPH: Initial positive RCTs (PERMIXON studies) showed improvements in peak urine flow and symptom scores", "Beta-sitosterol meta-analysis: Significant improvements in IPSS scores and peak flow rates"],
            "moderate": ["SAW study and CAMUS trial: No significant difference vs placebo for urinary symptoms in large well-powered RCTs — challenged earlier positive data", "Chronic prostatitis / pelvic pain syndrome: Small trials suggest benefit in symptom reduction", "Hair loss (androgenic alopecia): Pilot data suggests modest benefit in DHT-driven hair thinning"],
            "weak_or_preliminary": ["Prostate cancer prevention — no clinical evidence", "Libido enhancement in men", "Polycystic ovary syndrome (PCOS) — off-label, limited data"]
        },
        "safety_profile": {
            "common_side_effects": ["Nausea", "Abdominal pain", "Diarrhoea", "Headache", "Dizziness", "Decreased libido (rare)"],
            "serious_risks": ["Rare hepatotoxicity and pancreatitis case reports", "May interfere with PSA testing — can lower PSA by ~15%, masking prostate cancer", "Anti-androgenic effects may cause sexual dysfunction"],
            "contraindications": ["Hormone-sensitive cancers (theoretical — modulates androgens)", "Before PSA blood tests (inform clinician)", "Pregnancy and lactation (anti-androgenic effects on developing foetus)"],
            "drug_interactions": ["Warfarin and anticoagulants (possible potentiation via COX inhibition)", "Finasteride/dutasteride (additive 5AR inhibition — monitor for hypotension)", "Oral contraceptives/hormonal therapies (interaction possible)"],
            "pregnancy_lactation": "Contraindicated in pregnancy (anti-androgenic effects may affect male foetal development)."
        },
        "dosing": {
            "standard_dose": "Lipophilic extract (80–90% fatty acids and sterols): 160 mg twice daily (320 mg/day); or 320 mg once daily",
            "onset_of_action": "Urinary symptom improvement may require 4–6 weeks; peak effects at 3–6 months",
            "forms_available": ["Standardised lipophilic extract (PERMIXON, Prostasan)", "Softgel capsules", "Tincture", "Whole dried berry powder"],
            "dosing_notes": "Take with food to maximise absorption. Standardised lipophilic extracts (not whole berry powder) are required to match clinical trial evidence. Inform your doctor before taking if PSA testing is planned."
        },
        "sources": {
            "article_count": 576,
            "top_studies_urls": [
                "https://pubmed.ncbi.nlm.nih.gov/23298508/",
                "https://pubmed.ncbi.nlm.nih.gov/37345871/",
                "https://pubmed.ncbi.nlm.nih.gov/12137626/"
            ]
        },
        "consumer_view": {
            "tagline": "The prostate herb — America's most popular men's supplement",
            "what_it_does": "Saw palmetto may help with urinary symptoms caused by an enlarged prostate — like needing to urinate frequently at night or having a weak stream — by blocking the hormone that drives prostate growth.",
            "typical_uses": ["Frequent or urgent urination in men over 40", "Benign prostatic hyperplasia (enlarged prostate)", "Weak urine stream", "Androgenic hair thinning (off-label)"],
            "suggested_dose": "320 mg/day of standardised lipophilic extract (80–90% fatty acids), taken with food. Allow 4–6 weeks minimum, 3–6 months for full assessment.",
            "onset": "Urinary improvements begin around 4–6 weeks; full benefit takes 3–6 months.",
            "safety_snapshot": "Generally well-tolerated. Important: tell your doctor you're taking it if you're having a PSA (prostate cancer) blood test — it can lower PSA artificially and affect results. Not for use in women or children."
        }
    },
    {
        "id": "tribulus-terrestris",
        "common_name": "Puncture Vine",
        "scientific_name": "Tribulus terrestris",
        "category": "plant",
        "tags": ["men's health", "adaptogen", "testosterone", "athletic performance", "traditional"],
        "overview": {
            "description": "Tribulus terrestris (puncture vine) is a flowering plant widely distributed across warm temperate and tropical regions. Its fruit, root, and leaf extracts have been used in Ayurveda and TCM for centuries for male vitality, urinary health, and athletic endurance. Despite enormous commercial popularity as a 'testosterone booster,' the scientific evidence does not support increases in testosterone in healthy men; however, it shows genuine promise for erectile dysfunction, urinary complaints, and as an adaptogen under oxidative stress.",
            "traditional_use": "Ayurvedic medicine classifies Tribulus (Gokshura) as a Rasayana — a rejuvenating tonic for kidney, urinary tract, and male reproductive health. Chinese medicine used it for liver and kidney nourishment, eye disorders, and headaches. In Bulgaria and Eastern Europe, it gained fame in the 1970s as an athletic performance enhancer used by Soviet-era weightlifters.",
            "article_count": 669
        },
        "bioactive_compounds": {
            "primary": ["Protodioscin (steroidal saponin)", "Dioscin", "Tribulosin", "Tribulosaponin A–C", "Diosgenin"],
            "secondary": ["Quercetin", "Kaempferol", "Isorhamnetin", "Terrestriamide", "Harmine alkaloids (trace)", "Beta-sitosterol"],
            "mechanism_of_action": "<strong>LH-mediated testosterone modulation:</strong> Protodioscin may stimulate luteinizing hormone (LH) release from the pituitary, which in turn signals Leydig cells to produce testosterone — but this effect appears significant only in men with below-normal baseline LH/testosterone levels. <strong>Nitric oxide potentiation:</strong> Protodioscin is converted to DHEA and downstream androgens that enhance eNOS activity, improving penile smooth muscle relaxation and erectile function. <strong>Antioxidant protection:</strong> Flavonoids (quercetin, kaempferol) reduce oxidative damage in reproductive tissue and protect sperm from ROS. <strong>Diuretic and anti-urolithic activity:</strong> Saponins increase urine output and inhibit calcium oxalate crystal formation, relevant for kidney stone prevention. <strong>Adaptogenic stress response:</strong> Modulates HPA axis activity under physical stress, reducing cortisol excess."
        },
        "pharmacokinetics": {
            "absorption": "Steroidal saponins are poorly absorbed in native form; gut microbiota hydrolyse glycosides to more bioavailable aglycones (diosgenin). Protodioscin bioavailability is low (~10–15%) without enteric processing.",
            "distribution": "Saponin aglycones distribute to reproductive organs, liver, and kidney. Diosgenin is detected in testicular tissue in animal studies.",
            "metabolism": "Hepatic and intestinal biotransformation of saponins; diosgenin undergoes steroidogenic conversion. Flavonoids are glucuronidated and sulfated in the liver.",
            "elimination": "Renal and biliary excretion. Half-life of saponin metabolites: 4–8 hours; steady-state accumulation with 4–6 weeks of use."
        },
        "clinical_evidence": {
            "strong": ["Erectile dysfunction: Multiple RCTs demonstrate significant improvement in IIEF scores, particularly in men with mild-to-moderate ED and/or hypoactive sexual desire", "Urinary function: Improvement in urinary flow and symptom scores in men with lower urinary tract symptoms"],
            "moderate": ["Male infertility: Improvements in sperm motility and morphology in pilot studies", "Female sexual dysfunction: One RCT showed improved arousal and lubrication scores", "Kidney stone prevention: Reduces calcium oxalate crystallisation in vitro and animal models"],
            "weak_or_preliminary": ["Testosterone increase in healthy eugonadal men — NOT supported by well-controlled RCTs", "Athletic performance enhancement — not demonstrated in placebo-controlled trials", "Muscle mass or strength gains — no evidence in healthy trained athletes"]
        },
        "safety_profile": {
            "common_side_effects": ["Nausea", "Abdominal cramps", "Diarrhoea", "Sleep disturbance", "Gynecomastia (rare, at high doses)"],
            "serious_risks": ["Nephrotoxicity reported at very high doses in animal studies — caution in kidney disease", "Rare liver toxicity case reports", "May interact with diabetes medications"],
            "contraindications": ["Pregnancy (stimulates uterine contractions)", "Kidney disease (nephrotoxic at high doses)", "Hormone-sensitive cancers"],
            "drug_interactions": ["Antidiabetic drugs (hypoglycaemic potentiation)", "Antihypertensives (additive)", "Warfarin (possible interaction via flavonoid COX inhibition)", "Testosterone therapy (additive androgenic effects)"],
            "pregnancy_lactation": "Contraindicated in pregnancy. Insufficient data for lactation — avoid."
        },
        "dosing": {
            "standard_dose": "Standardised extract (40–45% saponins): 250–750 mg/day in divided doses; equivalent to 5–10 g/day dried herb",
            "onset_of_action": "Sexual function effects may appear within 4 weeks; urinary and other effects require 6–12 weeks",
            "forms_available": ["Standardised capsules (40–45% saponins)", "Tablets", "Powder", "Tincture"],
            "dosing_notes": "Saponin content varies widely across products — look for standardised extracts. Bulgarian varieties (aerial parts) differ in saponin profile from Indian varieties (fruit). Most sexual function trials used Bulgarian extract."
        },
        "sources": {
            "article_count": 669,
            "top_studies_urls": [
                "https://pubmed.ncbi.nlm.nih.gov/33602600/",
                "https://pubmed.ncbi.nlm.nih.gov/32736394/",
                "https://pubmed.ncbi.nlm.nih.gov/40219032/"
            ]
        },
        "consumer_view": {
            "tagline": "The vitality herb — traditional tonic for male health",
            "what_it_does": "Tribulus is popular as a testosterone booster, but research shows it's more effective for improving erectile function, urinary health, and general vitality. It does NOT reliably raise testosterone in healthy men.",
            "typical_uses": ["Mild-to-moderate erectile dysfunction", "Low sexual drive or libido", "Urinary flow problems in men", "General male vitality support"],
            "suggested_dose": "250–750 mg/day of standardised extract (40–45% saponins), split across 2–3 doses with meals. Allow 4–8 weeks.",
            "onset": "Sexual function improvements may begin around 4 weeks; other effects take 6–12 weeks.",
            "safety_snapshot": "Do not use during pregnancy. Use caution if you have kidney disease. If you're taking diabetes medication or blood thinners, check with your doctor first. Safe for most healthy adult men at recommended doses."
        }
    },
    {
        "id": "urtica-dioica",
        "common_name": "Stinging Nettle",
        "scientific_name": "Urtica dioica",
        "category": "plant",
        "tags": ["anti-inflammatory", "allergic rhinitis", "BPH", "joint health", "nutritional", "traditional"],
        "overview": {
            "description": "Urtica dioica (stinging nettle) is a perennial herb found across temperate regions worldwide. Despite its sting, nettle has been used medicinally for over 2,000 years. It is a nutritionally dense plant (high in iron, vitamin K, folate, calcium) and a remarkably versatile phytomedicine — with evidence-based applications ranging from allergic rhinitis and benign prostatic hyperplasia to rheumatoid arthritis and blood sugar management. Root and leaf extracts have distinct phytochemical profiles and clinical applications.",
            "traditional_use": "Ancient Greeks and Romans used nettle for joint pain, bleeding, and as a food source. Medieval European herbalists prescribed it as a diuretic, expectorant, and hair tonic. Native American tribes used topical nettle application (urtication) for arthritis pain relief — a practice still used in folk medicine. In Iran, nettle (gazaneh) is a traditional remedy for diabetes and hypertension.",
            "article_count": 965
        },
        "bioactive_compounds": {
            "primary": ["Beta-sitosterol (root)", "Lectins (UDA — Urtica dioica agglutinin)", "Polysaccharides", "Caffeic acid malic acid ester", "Chlorogenic acid"],
            "secondary": ["Quercetin", "Kaempferol", "Rutin", "Scopoletin", "Histamine, serotonin, formic acid (leaf hairs)", "Iron, calcium, vitamin K, folate"],
            "mechanism_of_action": "<strong>Anti-inflammatory (leaf):</strong> Quercetin and caffeic acid derivatives inhibit NF-κB signalling, suppressing pro-inflammatory cytokines (TNF-α, IL-1β, IL-6) and COX-2 — relevant for arthritis and rhinitis. <strong>Histamine modulation:</strong> Root polysaccharides and leaf flavonoids inhibit histamine release from mast cells; UDA lectin interferes with allergen-IgE interactions at the mast cell surface. <strong>5-alpha-reductase inhibition (root):</strong> Beta-sitosterol and root polysaccharides inhibit 5α-reductase and block androgen receptor in prostatic tissue, complementary to saw palmetto. <strong>SHBG binding (root):</strong> Root lignans and polysaccharides bind sex hormone-binding globulin (SHBG), potentially increasing free testosterone — unique mechanism among BPH herbs. <strong>Hypoglycaemic activity:</strong> Leaf polysaccharides stimulate insulin secretion and enhance peripheral glucose uptake via GLUT-4 translocation."
        },
        "pharmacokinetics": {
            "absorption": "Water-soluble polysaccharides and flavonoids are rapidly absorbed; UDA lectins are partially absorbed intact, surviving gastric acid. Fat-soluble beta-sitosterol has moderate absorption (~5–10%), enhanced by food.",
            "distribution": "Flavonoids distribute widely; beta-sitosterol concentrates in prostatic tissue. UDA shows distribution to lymphoid tissue and joint synovium.",
            "metabolism": "Hepatic glucuronidation and sulfation of flavonoids. Beta-sitosterol metabolised to bile acids. UDA is degraded proteolytically in the GI tract and liver.",
            "elimination": "Renal excretion of conjugated flavonoid metabolites. Sterol excretion primarily biliary/faecal. Half-life: 3–6 hours for major flavonoid actives."
        },
        "clinical_evidence": {
            "strong": ["Allergic rhinitis: Freeze-dried nettle leaf extract significantly reduced symptom severity vs placebo in a double-blind RCT (Mittman 1990); consistent with anti-histamine mechanism", "Benign prostatic hyperplasia: Multiple European RCTs show nettle root extract reduces IPSS scores and improves urinary flow, often combined with saw palmetto or pygeum"],
            "moderate": ["Rheumatoid arthritis: RCT showed nettle leaf extract (IDS 23) significantly reduced NSAID requirement when used adjunctively", "Blood pressure reduction: Small RCTs and observational studies show modest antihypertensive effects", "Blood glucose management in type 2 diabetes: Several controlled trials in Iran show reductions in fasting glucose and HbA1c"],
            "weak_or_preliminary": ["Iron deficiency anaemia support (nutritional rather than medicinal)", "Hair growth promotion", "Anti-cancer activity (in vitro only)"]
        },
        "safety_profile": {
            "common_side_effects": ["Gastrointestinal discomfort", "Skin rash (topical urtication — intentional or accidental)", "Mild diuresis", "Fluid retention (rare, paradoxical)"],
            "serious_risks": ["Additive hypoglycaemia with antidiabetic medications", "May potentiate anticoagulants (vitamin K content modulates warfarin effect)", "Allergy to latex — possible cross-reactivity"],
            "contraindications": ["Severe kidney disease (oxalate content)", "First trimester of pregnancy (uterotonic effects)", "Known urtica allergy"],
            "drug_interactions": ["Warfarin (vitamin K content; unpredictable effect — monitor INR)", "Antidiabetic drugs (additive hypoglycaemia)", "Antihypertensives (additive)", "Diuretics (additive — monitor electrolytes)", "Lithium (may reduce renal clearance)"],
            "pregnancy_lactation": "Avoid in first trimester (uterotonic in high doses). Limited data for lactation; nutritional leaf use as food likely safe."
        },
        "dosing": {
            "standard_dose": "Leaf extract: 300–600 mg/day (freeze-dried or standardised); Root extract: 300–600 mg/day (BPH); Leaf tea: 3–4 cups/day of infusion from 3–4 g dried herb",
            "onset_of_action": "Allergic rhinitis relief may occur within days; BPH effects require 4–8 weeks; anti-inflammatory effects 4–6 weeks",
            "forms_available": ["Freeze-dried leaf capsules", "Standardised root extract", "Tincture (1:5)", "Dried leaf tea", "Whole leaf powder", "Combined BPH formulas (with saw palmetto)"],
            "dosing_notes": "Leaf and root have different applications — leaf for allergy, arthritis, blood sugar; root for BPH and hormonal effects. Most BPH trials used root extract 300–600 mg/day. Freeze-drying preserves anti-histamine activity better than heat-dried preparations."
        },
        "sources": {
            "article_count": 965,
            "top_studies_urls": [
                "https://pubmed.ncbi.nlm.nih.gov/36014458/",
                "https://pubmed.ncbi.nlm.nih.gov/39000608/",
                "https://pubmed.ncbi.nlm.nih.gov/31163183/"
            ]
        },
        "consumer_view": {
            "tagline": "The humble powerhouse — from weed to medicine",
            "what_it_does": "Stinging nettle is a surprisingly versatile herb. The leaf helps with hay fever, joint inflammation, and blood sugar. The root is used for prostate health in men. It's also one of the most nutritionally rich plants — packed with iron, calcium, and vitamin K.",
            "typical_uses": ["Seasonal allergies and hay fever", "Enlarged prostate (BPH) — root extract", "Joint pain and arthritis support", "Blood sugar management (adjunct)", "Nutritional supplementation (iron, vitamin K, folate)"],
            "suggested_dose": "Leaf: 300–600 mg/day freeze-dried extract, or 3–4 cups of leaf tea daily. Root: 300–600 mg/day for prostate support. Allow 2–6 weeks depending on indication.",
            "onset": "Allergy relief can begin within a few days. Prostate and anti-inflammatory effects take 4–8 weeks.",
            "safety_snapshot": "Very safe at normal doses. Important: if you take blood thinners (warfarin) or diabetes medication, check with your doctor first — nettle can affect both. Avoid high doses in early pregnancy. Generally excellent safety profile — even used freely as a food."
        }
    }
]

def main():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

    existing_names = {e.get('scientific_name') for e in data}
    added = 0
    for plant in PLANTS:
        if plant['scientific_name'] in existing_names:
            print(f"SKIP (already exists): {plant['scientific_name']}")
            continue
        data.append(plant)
        existing_names.add(plant['scientific_name'])
        added += 1
        print(f"ADDED: {plant['scientific_name']}")

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nDone — {added} plants added. data.json now has {len(data)} entries.")

if __name__ == '__main__':
    main()
