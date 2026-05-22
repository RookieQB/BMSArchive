#!/usr/bin/env python3
"""Batch 9 — add cited_references for fungi indices 7-13:
Grifola frondosa, Agaricus blazei, Tremella fuciformis,
Phellinus linteus, Poria cocos, Polyporus umbellatus, Flammulina velutipes
"""
import json

DATA_FILE = "data.json"

PATCHES = {
    "Grifola frondosa": {
        "modern_application": (
            "D-fraction and MD-fraction (beta-1,6/1,3-glucan protein complexes) have shown "
            "immunomodulatory and anti-tumour effects in preclinical studies and small human "
            "trials; a meta-analysis confirmed polysaccharide anti-tumour activity [1]. "
            "Neurotrophic properties, including support of nerve growth factor (NGF) signalling, "
            "are under investigation [2]. Anti-proliferative activity in keratinocyte-related "
            "pathways via MAPK inhibition has been documented [3]. Maitake is included in "
            "reviews of edible mushroom anti-cancer potential across multiple cancer types [4]. "
            "Neuroprotective bioactivities are an emerging research focus [5]."
        ),
        "cited_references": [
            '[1] - Zhao F., "Antitumor activities of Grifola frondosa (Maitake) polysaccharide: A meta-analysis based on preclinical evidence.", J Ethnopharmacol, 2021, PMID: 34271115',
            '[2] - Naguib AM., "Maitake Medicinal Mushroom, Grifola frondosa (Agaricomycetes), and Its Neurotrophic Properties.", Int J Med Mushrooms, 2023, PMID: 36749053',
            '[3] - Choi EJ., "Extracts of Grifola frondosa inhibit the MAPK signaling pathways involved in keratinocyte hyperproliferation.", Nutr Res Pract, 2023, PMID: 38053833',
            '[4] - Gariboldi MB., "Anti-Cancer Potential of Edible/Medicinal Mushrooms in Breast Cancer.", Int J Mol Sci, 2023, PMID: 37373268',
            '[5] - Abdelmoaty MM., "Neuroprotective Mushrooms.", NeuroImmune Pharm Ther, 2024, PMID: 40370689',
        ],
    },
    "Agaricus blazei": {
        "modern_application": (
            "Studied primarily for immunomodulation and anti-tumour activity [1][4]. A Norwegian "
            "randomised clinical trial with AndoSan preparation demonstrated reduced inflammatory "
            "cytokine markers (TNF-α, IL-6) in blood donors [2]. Reduced inflammatory mediators "
            "were also observed in elderly women in a separate randomised trial [3]. Chemical "
            "composition analysis confirms beta-glucans and ergosterol as the primary bioactives "
            "driving immunomodulatory effects [4][5]."
        ),
        "cited_references": [
            '[1] - Hetland G., "Antitumor, Anti-Inflammatory and Antiallergic Effects of Agaricus blazei Mushroom Extract.", Nutrients, 2020, PMID: 32397163',
            '[2] - Mahmood F., "Agaricus blazei-Based Mushroom Extract Supplementation to Birch Allergic Blood Donors: A Randomized and Double-Blinded Crossover Trial.", Nutrients, 2019, PMID: 31581605',
            '[3] - Lima CU., "Agaricus blazei Murrill and inflammatory mediators in elderly women: a randomized clinical study.", Scand J Immunol, 2012, PMID: 22010847',
            '[4] - Huang K., "Critical review on chemical compositions and health-promoting effects of mushroom Agaricus.", Curr Res Food Sci, 2022, PMID: 36387602',
            '[5] - da Silva de Souza AC., "Agaricus blazei Bioactive Compounds and their Effects on Human Health: Benefits and Controversies.", Curr Pharm Des, 2017, PMID: 28103773',
        ],
    },
    "Tremella fuciformis": {
        "modern_application": (
            "Tremella polysaccharide (TP) is studied for neuroprotective effects (NGF-like "
            "activity), skin hydration, and immunomodulation via multiple molecular mechanisms [1]. "
            "The high water-retention capacity of TP — comparable to hyaluronic acid — underpins "
            "its extensive use in cosmetic dermatology [2]. A clinical trial demonstrated "
            "improvements in glycated haemoglobin (HbA1c) and waist circumference in overweight "
            "subjects following T. fuciformis supplementation [3]. Anti-proliferative activity "
            "against EBV-associated gastric cancer has been documented via ferroptosis induction [4]. "
            "Anti-inflammatory properties relevant to atopic dermatitis are under preclinical "
            "investigation [5]."
        ),
        "cited_references": [
            '[1] - Yang D., "Tremella polysaccharide: The molecular mechanisms of its drug action.", Prog Mol Biol Transl Sci, 2019, PMID: 31030755',
            '[2] - Mineroff J., "The potential cutaneous benefits of Tremella fuciformis.", Arch Dermatol Res, 2023, PMID: 36757441',
            '[3] - Gitsomboon S., "Tremella fuciformis beverage improves glycated hemoglobin A1c and waist circumference in overweight Thai adults: a double-blind, randomized, placebo-controlled study.", BMC Nutr, 2024, PMID: 38439104',
            '[4] - Kong W., "Tremella fuciformis polysaccharides induce ferroptosis in Epstein-Barr virus-associated gastric cancer.", Aging (Albany NY), 2024, PMID: 38244583',
            '[5] - Xie L., "Tremella fuciformis polysaccharides alleviate induced atopic dermatitis in mice by regulating the Th1/Th2 balance.", Front Pharmacol, 2022, PMID: 36091780',
        ],
    },
    "Phellinus linteus": {
        "modern_application": (
            "Strongly investigated for anti-tumour and immunomodulatory properties [5]. Preclinical "
            "studies show consistent anti-proliferative effects across multiple cancer cell lines "
            "(breast, prostate, colon, leukaemia) [5]. Three CONSORT-compliant randomised "
            "controlled trials have documented immune enhancement effects of oral Phellinus linteus "
            "extract in healthy subjects [1][2][3]. Perioperative use as a nutraceutical adjunct "
            "in pancreatic cancer management has been clinically evaluated [4]. Anti-inflammatory "
            "properties relevant to IBD and arthritis are documented in preclinical models [5]."
        ),
        "cited_references": [
            '[1] - Ku YH., "Efficacy of Phellinus linteus extract on immunity enhancement: A CONSORT-randomized, double-blind, parallel-group study.", Medicine (Baltimore), 2022, PMID: 36221338',
            '[2] - Ku YH., "Effects of Phellinus linteus extract on immunity improvement: A CONSORT-randomized, double-blind, parallel-group study.", Medicine (Baltimore), 2022, PMID: 36042633',
            '[3] - Ku YH., "Clinical trial to analyze the effects of oral intake of Phellinus linteus (sanghuang) extract on immune function.", Trials, 2021, PMID: 34838112',
            '[4] - Kim J., "Perioperative Clinical Usage of Phellinus Linteus as a Nutraceutical for Non-FOLFIRINOX-Based Pancreatic Cancer Patients.", Integr Cancer Ther, 2025, PMID: 40590265',
            '[5] - Chen H., "Traditional uses, fermentation, phytochemistry and pharmacology of Phellinus linteus: A review.", Fitoterapia, 2016, PMID: 27343366',
        ],
    },
    "Poria cocos": {
        "modern_application": (
            "Beta-pachymaran and pachymic acids are the primary studied bioactives; renoprotective "
            "pharmacology of triterpenoids has been comprehensively characterised [2]. A clinical "
            "study demonstrated improved sleep quality with Poria cocos extract, aligning with "
            "its traditional use for insomnia [1]. Polysaccharides show gut microbiome-modulating "
            "properties in antibiotic-associated diarrhoea models [3]. Anti-tumour activity of "
            "Poria cocos polysaccharide (PCP) is supported by preclinical mechanistic data [4]. "
            "Effects on metabolic dysfunction-associated fatty liver disease have been "
            "investigated [5]."
        ),
        "cited_references": [
            '[1] - Kim H., "Efficacy of Poria Cocos Extract on Sleep Quality Enhancement: A Clinical Perspective with Potential Neurological Implications.", Nutrients, 2023, PMID: 37836526',
            '[2] - Guo ZY., "Poria cocos: traditional uses, triterpenoid components and their renoprotective pharmacology.", Acta Pharmacol Sin, 2025, PMID: 39482471',
            '[3] - Xu H., "Poria cocos Polysaccharide Ameliorated Antibiotic-Associated Diarrhea in Mice via Regulating Gut Microbiota.", Int J Mol Sci, 2023, PMID: 36674937',
            '[4] - Li X., "Molecular basis for Poria cocos mushroom polysaccharide used as an antitumour drug in China.", J Cell Mol Med, 2019, PMID: 30444050',
            '[5] - He J., "Effects of Poria cocos extract on metabolic dysfunction-associated fatty liver disease via regulating lipid metabolism.", Front Pharmacol, 2022, PMID: 36278226',
        ],
    },
    "Polyporus umbellatus": {
        "modern_application": (
            "Ergone and polysaccharides (PU-PS) are the primary bioactives; phytochemistry, "
            "pharmacology, and pharmacokinetics have been comprehensively reviewed [3][2]. "
            "Zhu Ling polysaccharide injection (ZPS) is used in China as an adjunct in cancer "
            "management, with evidence of efficacy demonstrated for hepatitis B [1]. Diuretic "
            "effects are well-documented in the pharmacological literature. Renoprotective "
            "polysaccharide activity has been demonstrated in preclinical models [4]. "
            "Immunomodulatory nanocomposites derived from PU polysaccharides are under "
            "investigation for enhanced anti-tumour activity [5]."
        ),
        "cited_references": [
            '[1] - Guo Z., "The efficacy of Polyporus Umbellatus polysaccharide in treating hepatitis B in China.", Prog Mol Biol Transl Sci, 2019, PMID: 31030753',
            '[2] - He D., "Phytochemistry and bioactivities of the main constituents of Polyporus umbellatus (Pers.) Fr.", Phytomedicine, 2022, PMID: 35667259',
            '[3] - Zhao YY., "Traditional uses, phytochemistry, pharmacology, pharmacokinetics and quality control of Polyporus umbellatus.", J Ethnopharmacol, 2013, PMID: 23811047',
            '[4] - Li H., "Renoprotective effect and mechanism of polysaccharide from Polyporus umbellatus sclerotia.", Carbohydr Polym, 2019, PMID: 30832835',
            '[5] - Liu T., "Polyporus umbellatus polysaccharide iron-based nanocomposite for synergistic M1 polarization and tumor cell death.", Int J Biol Macromol, 2023, PMID: 37586629',
        ],
    },
    "Flammulina velutipes": {
        "modern_application": (
            "Polysaccharides from F. velutipes demonstrate immunomodulatory, antioxidant, and "
            "anti-tumour activities with diverse structural and functional properties [1][5]. "
            "Renoprotective effects have been documented in chronic kidney disease models [2]. "
            "Protective activity against cisplatin-induced acute kidney injury has been observed "
            "in preclinical settings [3]. Flammutoxin, a cardiotoxic protein present in the raw "
            "mushroom, is inactivated by cooking — an important safety consideration [4]. "
            "Ergothioneine content is among the highest of edible mushrooms, contributing to "
            "its antioxidant profile [1]."
        ),
        "cited_references": [
            '[1] - Ye S., "Research progress and future development potential of Flammulina velutipes polysaccharides.", Int J Biol Macromol, 2024, PMID: 38599436',
            '[2] - Lee MM., "Renoprotective Effects of Brown-Strain Flammulina velutipes Singer in Chronic Kidney Disease.", Int J Mol Sci, 2024, PMID: 39596166',
            '[3] - Tu Y., "Flammulina Velutipes polysaccharides ameliorate cisplatin-induced acute kidney injury in mice.", Int J Biol Macromol, 2025, PMID: 39706410',
            '[4] - Mustonen AM., "Myo- and cardiotoxic effects of the wild winter mushroom (Flammulina velutipes) on mice.", Exp Biol Med (Maywood), 2018, PMID: 29495884',
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
