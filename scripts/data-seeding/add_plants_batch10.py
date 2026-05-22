#!/usr/bin/env python3
"""Batch 10 — add cited_references for fungi indices 14-20:
Pleurotus ostreatus, Schizophyllum commune, Auricularia auricula-judae,
Coprinus comatus, Antrodia cinnamomea, Fomes fomentarius, Ophiocordyceps sinensis
"""
import json

DATA_FILE = "data.json"

PATCHES = {
    "Pleurotus ostreatus": {
        "modern_application": (
            "Among edible fungi, oyster mushrooms have the most clinical evidence for lipid-lowering "
            "effects; a review of clinical and preclinical studies confirms cardiometabolic "
            "benefits [1][2]. Consumption of P. ostreatus extract has been associated with "
            "improvements in blood parameters and cytokine profiles in clinical studies [3]. "
            "Lovastatin (mevinolin) content — a genuine statin naturally occurring in the fruiting "
            "body — is the likely cholesterol-lowering mechanism [2]. Immunomodulatory properties "
            "and anti-cancer activity are documented in preclinical and review literature [4][5]. "
            "Pleuran (beta-1,3/1,6-glucan) from P. ostreatus is commercially used as an "
            "immunomodulatory supplement [4]."
        ),
        "cited_references": [
            '[1] - Dicks L., "Effect of the Intake of Oyster Mushrooms (Pleurotus ostreatus) on Cardiometabolic Parameters-A Systematic Review.", Nutrients, 2020, PMID: 32316680',
            '[2] - Araújo PL., "Pleurotus Mushrooms in Nutrition and Health: Clinical and Preclinical Insights for Nutraceutical Applications.", Compr Rev Food Sci Food Saf, 2025, PMID: 40899490',
            '[3] - Dündar A., "Effect of Pleurotus ostreatus Water Extract Consumption on Blood Parameters and Cytokine Values in Healthy Volunteers.", J Am Nutr Assoc, 2024, PMID: 38935369',
            '[4] - Motta F., "Mushrooms and immunity.", J Autoimmun, 2021, PMID: 33276307',
            '[5] - Gariboldi MB., "Anti-Cancer Potential of Edible/Medicinal Mushrooms in Breast Cancer.", Int J Mol Sci, 2023, PMID: 37373268',
        ],
    },
    "Schizophyllum commune": {
        "modern_application": (
            "Schizophyllan (SPG / Sonifilan / sizofiran) — a beta-1,3-glucan — is approved in "
            "Japan as an adjunct to radiation therapy in cervical cancer, with clinical trials "
            "demonstrating improved survival [1]. Efficacy as an immunotherapy adjunct has also "
            "been studied in advanced gastric cancer [2]. Immunomodulatory mechanisms include "
            "enhancement of NK cell and macrophage activity [3]. Importantly, S. commune is also "
            "an opportunistic pathogen capable of causing allergic bronchopulmonary mycosis and "
            "sino-pulmonary infections in immunocompromised hosts [4][5]. Antifungal properties "
            "are noted in vitro."
        ),
        "cited_references": [
            '[1] - Okamura K., "Clinical evaluation of schizophyllan combined with irradiation in patients with cervical cancer.", Cancer, 1986, PMID: 2941141',
            '[2] - Fujimoto S., "Clinical efficacies of schizophyllan (SPG) on advanced gastric cancer.", Nihon Geka Gakkai Zasshi, 1989, PMID: 2531270',
            '[3] - Borchers AT., "Mushrooms, tumors, and immunity.", Proc Soc Exp Biol Med, 1999, PMID: 10460691',
            '[4] - Oguma T., "Clinical characteristics of allergic bronchopulmonary mycosis caused by Schizophyllum commune.", Clin Transl Allergy, 2024, PMID: 38282191',
            '[5] - Hoenigl M., "Global guideline for the diagnosis and management of rare mould infections: an initiative of the European Confederation of Medical Mycology.", Lancet Infect Dis, 2021, PMID: 33606997',
        ],
    },
    "Auricularia auricula-judae": {
        "modern_application": (
            "Clinically relevant for its significant anticoagulant and antiplatelet effects — "
            "in vitro screening has confirmed potent platelet inhibition by Auricularia extracts [1]. "
            "Antidiabetic effects via alpha-glucosidase inhibition and anti-proliferative activity "
            "against cancer cell lines are documented in preclinical research [2][4]. "
            "Polysaccharide-rich preparations have been evaluated in polyherbal combination "
            "formulas for immune support [3]. Immunomodulatory polysaccharides (AAP) exhibit "
            "multiple bioactivities in preclinical models [5]. Caution is warranted when consumed "
            "in large quantities alongside anticoagulant medication due to additive platelet "
            "inhibition [1]."
        ),
        "cited_references": [
            '[1] - Poniedziałek B., "The Effect of Mushroom Extracts on Human Platelet and Blood Coagulation: In vitro Screening of Eight Edible Species.", Nutrients, 2019, PMID: 31842490',
            '[2] - Wong JH., "Mushroom extracts and compounds with suppressive action on breast cancer: evidence from studies using cultured cancer cells, tumor-bearing animals, and clinical trials.", Appl Microbiol Biotechnol, 2020, PMID: 32274562',
            '[3] - Nakyam T., "The Polyherbal Functional Ingredient Containing Ginger, Chinese Date, and Wood Ear Mushroom (Auricularia auricula-judae) Promotes Immune System Activity.", Biomed Res Int, 2023, PMID: 37564141',
            '[4] - Panthong S., "Antioxidant activity, anti-proliferative activity, and amino acid profiles of ethanolic extracts of edible mushrooms.", Genet Mol Res, 2016, PMID: 27813595',
            '[5] - Łysakowska P., "Medicinal Mushrooms: Their Bioactive Components, Nutritional Value and Application in Functional Food Production-A Review.", Molecules, 2023, PMID: 37513265',
        ],
    },
    "Coprinus comatus": {
        "modern_application": (
            "Studied primarily for antidiabetic properties; ethanolic extracts demonstrate "
            "significant hypoglycaemic and antioxidant activity in animal models [1][3]. "
            "Mycelium polysaccharides have shown anti-diabetic nephropathic activity in "
            "preclinical studies [4]. A comprehensive review documents both the functional "
            "properties and potential safety concerns — including a disulfiram-like reaction "
            "with alcohol mediated by coprine [2]. Anti-inflammatory and antiarthritic "
            "properties are under early investigation via nanogel formulations [5]."
        ),
        "cited_references": [
            '[1] - Ratnaningtyas NI., "Ethanol extract of the mushroom Coprinus comatus exhibits antidiabetic and antioxidant activities in streptozotocin-induced diabetic rats.", Pharm Biol, 2022, PMID: 35675226',
            '[2] - Nowakowski P., "The two faces of Coprinus comatus-Functional properties and potential hazards.", Phytother Res, 2020, PMID: 32462723',
            '[3] - Husen F., "Antidiabetic Effects and Antioxidant Properties of the Saggy Ink Cap Medicinal Mushroom, Coprinus comatus.", Int J Med Mushrooms, 2021, PMID: 34595888',
            '[4] - Gao Z., "Characterization and anti-diabetic nephropathic ability of mycelium polysaccharides from Coprinus comatus.", Carbohydr Polym, 2021, PMID: 33142624',
            '[5] - Ratnaningtyas NI., "Therapeutic potential of Coprinus comatus nanogels: Antiarthritic and anti-inflammatory effects in Freund\'s adjuvant-induced arthritis.", Vet World, 2025, PMID: 40342737',
        ],
    },
    "Antrodia cinnamomea": {
        "modern_application": (
            "Hepatoprotective and anti-tumour properties are the primary research focus. "
            "Clinical evidence supports hepatoprotective activity in patients with non-alcoholic "
            "steatohepatitis (NASH) [1] and in sub-health adults [2]. Polysaccharide intervention "
            "modulates clinical symptoms likely via gut microbiome regulation [3]. "
            "Anti-proliferative activity against prostate cancer via immune modulation has been "
            "documented [4]. Hepatoprotective mechanisms are further supported by preclinical "
            "data showing reduction of hepatotoxicity in rodent models [5]. Antroquinonol, a "
            "unique ubiquinone derivative, has entered Phase II clinical trials in Taiwan."
        ),
        "cited_references": [
            '[1] - Chiou YL., "Hepatoprotective Effect of Antrodia cinnamomea Mycelium in Patients with Nonalcoholic Steatohepatitis.", J Am Coll Nutr, 2021, PMID: 32657670',
            '[2] - Ho CY., "Hepatoprotective effect of Antrodia Cinnamomea mycelia extract in subhealth Japanese adults: a double-blind, placebo-controlled clinical trial.", J Diet Suppl, 2023, PMID: 36476310',
            '[3] - Liu ZQ., "Dietary Antrodia cinnamomea Polysaccharide Intervention Modulates Clinical Symptoms by Regulating Gut Microbiota.", J Agric Food Chem, 2024, PMID: 39632724',
            '[4] - Tsai MY., "Antrodia cinnamomea Formula Suppresses Prostate Cancer Progression via Immune Modulation and Androgen Receptor Pathway Inhibition.", Int J Mol Sci, 2025, PMID: 40141325',
            '[5] - Shih YL., "Antrodia Cinnamomea Reduces Carbon Tetrachloride-induced Hepatotoxicity in Male Wistar Rats.", In Vivo, 2017, PMID: 28882954',
        ],
    },
    "Fomes fomentarius": {
        "modern_application": (
            "Contemporary research has confirmed antioxidant, anti-inflammatory, antimicrobial, "
            "and cytotoxic properties. Insoluble extracted fibres from the fruiting body "
            "demonstrate immunological activity relevant to nutraceutical applications [1]. "
            "Melanin-glucan complex shows anti-infective properties against bacterial and "
            "viral pathogens [2]. Ethanol extracts inhibit cell growth and induce apoptosis "
            "in cancer cell lines in vitro [3]. Antimicrobial activity against a range of "
            "pathogens has been confirmed in vitro [4]. Fermented extracellular polysaccharides "
            "exhibit antioxidant properties [5]. Human clinical data remain absent; "
            "biomaterial and wound-care applications are an emerging research focus."
        ),
        "cited_references": [
            '[1] - Kalitukha L., "Medicinal Potential of the Insoluble Extracted Fibers Isolated from the Fomes fomentarius Fruiting Body.", Int J Med Mushrooms, 2023, PMID: 37017659',
            '[2] - Seniuk OF., "Anti-infective properties of the melanin-glucan complex obtained from medicinal tinder bracket mushroom, Fomes fomentarius.", Int J Med Mushrooms, 2011, PMID: 22135899',
            '[3] - Lee SO., "Fomes fomentarius Ethanol Extract Exerts Inhibition of Cell Growth and Motility Induction through the Suppression of Focal Adhesion Kinase.", Int J Mol Sci, 2019, PMID: 30845749',
            '[4] - Doğan HH., "Fomes fomentarius and Tricholoma anatolicum (Agaricomycetes) Extracts Exhibit Significant Antimicrobial Activity.", Int J Med Mushrooms, 2020, PMID: 32478999',
            '[5] - Zhang Q., "Optimization of fermentation of Fomes fomentarius extracellular polysaccharide and antioxidant activity.", Cell Mol Biol (Noisy-le-grand), 2020, PMID: 33287923',
        ],
    },
    "Ophiocordyceps sinensis": {
        "modern_application": (
            "Clinically validated in Chinese RCTs for chronic kidney disease — combined use "
            "with ACE inhibitors or ARBs has demonstrated reductions in proteinuria and "
            "creatinine stabilisation in diabetic nephropathy [1][2] and general CKD [3]. "
            "Systematic review data support inclusion in integrative oncology discussions, "
            "though evidence quality varies [4]. Because wild harvesting is unsustainable "
            "and prohibitively expensive, nearly all modern research uses cultured Cs-4 "
            "mycelium (often still labelled 'Cordyceps sinensis') [5]. Anti-fatigue and "
            "VO2-max improvement in elderly subjects have been documented with cultured "
            "preparations [5]."
        ),
        "cited_references": [
            '[1] - Yan G., "The effects of Ophiocordyceps sinensis combined with ACEI/ARB on diabetic kidney disease: A systematic review and meta-analysis.", Phytomedicine, 2023, PMID: 36375237',
            '[2] - Xue X., "Ophiocordyceps sinensis preparations combined with the renin-angiotensin system inhibitor in treating diabetic nephropathy.", Front Pharmacol, 2024, PMID: 38716236',
            '[3] - Luo Y., "Use of Ophiocordyceps sinensis (syn. Cordyceps sinensis) combined with angiotensin-converting enzyme inhibitor therapy for treatment of IgA nephropathy.", Ren Fail, 2015, PMID: 25682973',
            '[4] - Narayanan S., "Medicinal Mushroom Supplements in Cancer: A Systematic Review of Clinical Studies.", Curr Oncol Rep, 2023, PMID: 36995535',
            '[5] - Łysakowska P., "Medicinal Mushrooms: Their Bioactive Components, Nutritional Value and Application in Functional Food Production-A Review.", Molecules, 2023, PMID: 37513265',
        ],
    },
}


def main():
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)

    updated = []
    for entry in data:
        name = entry["scientific_name"]
        if name not in PATCHES:
            updated.append(entry)
            continue
        patch = PATCHES[name]
        entry["narrative_summary"]["modern_application"] = patch["modern_application"]
        if "sources" not in entry:
            entry["sources"] = {}
        entry["sources"]["cited_references"] = patch["cited_references"]
        updated.append(entry)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(updated, f, ensure_ascii=False, indent=2)

    print(f"Updated {len(PATCHES)} monographs:")
    for entry in updated:
        name = entry["scientific_name"]
        if name in PATCHES:
            refs = len(entry.get("sources", {}).get("cited_references", []))
            cd = "clinical_data" in entry
            ns = "narrative_summary" in entry
            print(f"  {name:<35} | clinical_data={cd} | narrative_summary={ns} | cited_refs={refs}")


if __name__ == "__main__":
    main()
