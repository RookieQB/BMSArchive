#!/usr/bin/env python3
"""Batch 8 — add cited_references for fungi indices 0-6:
Ganoderma lucidum, Hericium erinaceus, Inonotus obliquus,
Cordyceps sinensis, Cordyceps militaris, Trametes versicolor, Lentinula edodes
"""
import json, sys

DATA_FILE = "data.json"

PATCHES = {
    "Ganoderma lucidum": {
        "modern_application": (
            "Clinically studied as an adjunct in oncology for immunomodulation — trials show "
            "increased NK cell and T-lymphocyte activity [1]. Hepatoprotective and anti-fatigue "
            "properties documented in preclinical and clinical contexts [1]. Beta-glucan "
            "polysaccharides demonstrate anti-proliferative activity against multiple cancer cell "
            "lines in vitro [2]. Gut microbiome modulation has been documented in murine models [3]. "
            "Anti-cancer potential in breast and colorectal cancer is supported by in vitro and "
            "network pharmacology studies [4][5]."
        ),
        "cited_references": [
            '[1] - Ahmad R., "Ganoderma lucidum (Reishi) an edible mushroom; a comprehensive and critical review of its nutritional, cosmeceutical, mycochemical, pharmacological, clinical, and toxicological properties.", Phytother Res, 2021, PMID: 34411377',
            '[2] - Sohretoglu D., "Ganoderma lucidum Polysaccharides as An Anti-cancer Agent.", Anticancer Agents Med Chem, 2018, PMID: 29141563',
            '[3] - Chang CJ., "Ganoderma lucidum reduces obesity in mice by modulating the composition of the gut microbiota.", Nat Commun, 2015, PMID: 26102296',
            '[4] - Gariboldi MB., "Anti-Cancer Potential of Edible/Medicinal Mushrooms in Breast Cancer.", Int J Mol Sci, 2023, PMID: 37373268',
            '[5] - Zhao X., "Network Pharmacology and Bioinformatics Study of Six Medicinal Food Homologous Plants Against Colorectal Cancer.", Int J Mol Sci, 2025, PMID: 39940699',
        ],
    },
    "Hericium erinaceus": {
        "modern_application": (
            "Clinically studied for its nerve growth factor (NGF)-stimulating properties. "
            "A 2009 double-blind RCT demonstrated significant improvement in mild cognitive "
            "impairment after 16 weeks of supplementation [1]. A 4-week pilot study documented "
            "reduction in depression and anxiety scores [4]. Neuroprotective mechanisms include "
            "antioxidant and anti-inflammatory activity mediated by hericenones and erinacines [2][3]. "
            "Evidence supports investigation as a neuroprotective agent in Alzheimer's and "
            "Parkinson's disease models [2][3]."
        ),
        "cited_references": [
            '[1] - Mori K., "Improving effects of the mushroom Yamabushitake (Hericium erinaceus) on mild cognitive impairment: a double-blind placebo-controlled clinical trial.", Phytother Res, 2009, PMID: 18844328',
            '[2] - Contato AG., "Lion\'s Mane Mushroom (Hericium erinaceus): A Neuroprotective Fungus with Antioxidant, Anti-Inflammatory, and Antimicrobial Potential-A Narrative Review.", Nutrients, 2025, PMID: 40284172',
            '[3] - Chong PS., "Therapeutic Potential of Hericium erinaceus for Depressive Disorder.", Int J Mol Sci, 2019, PMID: 31881712',
            '[4] - Nagano M., "Reduction of depression and anxiety by 4 weeks Hericium erinaceus intake.", Biomed Res, 2010, PMID: 20834180',
            '[5] - Łysakowska P., "Medicinal Mushrooms: Their Bioactive Components, Nutritional Value and Application in Functional Food Production-A Review.", Molecules, 2023, PMID: 37513265',
        ],
    },
    "Inonotus obliquus": {
        "modern_application": (
            "Studied primarily for antioxidant and anti-tumour activity [1][2]. Betulinic acid "
            "and polysaccharides show anti-proliferative effects in vitro and in animal models [2]. "
            "Anti-inflammatory and anti-hyperglycaemic effects have been observed in preclinical "
            "studies, including inhibition of intestinal inflammation and insulin metabolism "
            "impairment in Drosophila models [3]. Application in diabetic kidney disease is under "
            "investigation [4]. Human RCT data remains limited [1][5]."
        ),
        "cited_references": [
            '[1] - Szychowski KA., "Inonotus obliquus - from folk medicine to clinical use.", J Tradit Complement Med, 2021, PMID: 34195023',
            '[2] - Tee PYE., "A review on the cultivation, bioactive compounds, health-promoting factors and clinical trials of medicinal mushrooms Taiwanofungus camphoratus, Inonotus obliquus and Tropicoporus linteus.", Fungal Biol Biotechnol, 2024, PMID: 38987829',
            '[3] - Yu S., "Inonotus obliquus aqueous extract inhibits intestinal inflammation and insulin metabolism defects in Drosophila.", Toxicol Mech Methods, 2024, PMID: 38872277',
            '[4] - Wang S., "Research Progress on Application of Inonotus obliquus in Diabetic Kidney Disease.", J Inflamm Res, 2023, PMID: 38161352',
            '[5] - Łysakowska P., "Medicinal Mushrooms: Their Bioactive Components, Nutritional Value and Application in Functional Food Production-A Review.", Molecules, 2023, PMID: 37513265',
        ],
    },
    "Cordyceps sinensis": {
        "modern_application": (
            "Studied for anti-fatigue, athletic performance enhancement, and immunomodulation [1][5]. "
            "A systematic review of RCTs demonstrated that Cordyceps sinensis mycelium used as "
            "adjuvant in lung cancer treatment was associated with improved clinical outcomes [3]. "
            "Bidirectional cardiac-regulatory effects have been described in clinical evaluations "
            "using network pharmacology [2]. A randomised controlled trial demonstrated efficacy "
            "for primary insomnia [4]. The expensive wild-harvested form is largely replaced by "
            "cultured mycelium (CS-4 strain) in research contexts [5]."
        ),
        "cited_references": [
            '[1] - Das G., "Cordyceps spp.: A Review on Its Immune-Stimulatory and Other Biological Potentials.", Front Pharmacol, 2020, PMID: 33628175',
            '[2] - Wang L., "Bidirectional regulatory effects of Cordyceps on arrhythmia: Clinical evaluations and network pharmacology.", Front Pharmacol, 2022, PMID: 36059969',
            '[3] - Wang C., "Adjuvant treatment with Cordyceps sinensis for lung cancer: A systematic review and meta-analysis of randomized controlled trials.", J Ethnopharmacol, 2024, PMID: 38484953',
            '[4] - Zhao S., "Effectiveness of fermentation broth of Cordyceps sinensis for primary insomnia: a randomized clinical trial with digital health tool.", Front Neurol, 2025, PMID: 40726627',
            '[5] - Łysakowska P., "Medicinal Mushrooms: Their Bioactive Components, Nutritional Value and Application in Functional Food Production-A Review.", Molecules, 2023, PMID: 37513265',
        ],
    },
    "Cordyceps militaris": {
        "modern_application": (
            "Contains higher concentrations of cordycepin than wild C. sinensis and is more "
            "accessible for research [3]. A randomised controlled trial demonstrated significant "
            "improvements in immune response markers in healthy adults following supplementation [1]. "
            "Safety has been assessed in randomised clinical trials with cultured Cordyceps "
            "preparations [2]. Immunomodulatory, anti-inflammatory, and anti-tumour activities "
            "are supported by both in vitro and in vivo evidence [3][4]. Properties including "
            "antidiabetic and renoprotective effects remain under active investigation [5]."
        ),
        "cited_references": [
            '[1] - Ontawong A., "A randomized controlled clinical trial examining the effects of Cordyceps militaris beverage on the immune response in healthy adults.", Sci Rep, 2024, PMID: 38580687',
            '[2] - Tsai YS., "Safety Assessment of HEA-Enriched Cordyceps cicadae Mycelium: A Randomized Clinical Trial.", J Am Coll Nutr, 2021, PMID: 32702252',
            '[3] - Yang EJ., "An Immunomodulatory Mushroom, Cordyceps militaris, and Its Constituents: A Review of In Vitro/In Vivo Studies and Clinical Trials.", Phytother Res, 2026, PMID: 41432716',
            '[4] - Das G., "Cordyceps spp.: A Review on Its Immune-Stimulatory and Other Biological Potentials.", Front Pharmacol, 2020, PMID: 33628175',
            '[5] - Łysakowska P., "Medicinal Mushrooms: Their Bioactive Components, Nutritional Value and Application in Functional Food Production-A Review.", Molecules, 2023, PMID: 37513265',
        ],
    },
    "Trametes versicolor": {
        "modern_application": (
            "PSK (polysaccharide-K) and PSP (polysaccharide-peptide) are the most clinically "
            "studied compounds [2]. A Phase 1 clinical trial in women with breast cancer "
            "demonstrated safety and immune enhancement following oral administration [1]. "
            "PSP shows anti-proliferative activity against colorectal cancer cells via multiple "
            "molecular targets [3]. Immunomodulatory potential in the context of cancer and "
            "infectious disease is under continued investigation [4]. Clinical data supports its "
            "role as an adjunct in oncology when used alongside conventional chemotherapy [2][5]."
        ),
        "cited_references": [
            '[1] - Torkelson CJ., "Phase 1 Clinical Trial of Trametes versicolor in Women with Breast Cancer.", ISRN Oncol, 2012, PMID: 22701186',
            '[2] - Habtemariam S., "Trametes versicolor (Synn. Coriolus versicolor) Polysaccharides in Cancer Therapy: Targets and Efficacy.", Biomedicines, 2020, PMID: 32466253',
            '[3] - He Z., "Polysaccharide-Peptide from Trametes versicolor: The Potential Medicine for Colorectal Cancer Treatment.", Biomedicines, 2022, PMID: 36359361',
            '[4] - Jędrzejewski T., "COVID-19 and Cancer Diseases-The Potential of Coriolus versicolor Mushroom to Combat Global Health Challenges.", Int J Mol Sci, 2023, PMID: 36902290',
            '[5] - Łysakowska P., "Medicinal Mushrooms: Their Bioactive Components, Nutritional Value and Application in Functional Food Production-A Review.", Molecules, 2023, PMID: 37513265',
        ],
    },
    "Lentinula edodes": {
        "modern_application": (
            "Lentinan, the primary beta-glucan, is approved in Japan as an adjunct in gastric "
            "cancer treatment (IV formulation) [5]. AHCC (Active Hexose Correlated Compound), "
            "derived from shiitake mycelium, is studied for NK and T-cell enhancement [2] and "
            "has demonstrated tumour growth inhibitory activity in patient-derived xenograft "
            "models [3]. A randomised controlled trial evaluated AHCC supplementation for "
            "clearance of persistent HPV infections [1]. Adjuvant use following hepatic resection "
            "for hepatocellular carcinoma has been investigated [4]. Immunomodulatory "
            "polysaccharides engage innate immune pathways via pattern recognition receptors [5]."
        ),
        "cited_references": [
            '[1] - Smith JA., "AHCC® Supplementation to Support Immune Function to Clear Persistent Human Papillomavirus Infections.", Front Oncol, 2022, PMID: 35814366',
            '[2] - Shin MS., "The Effects of AHCC®, a Standardized Extract of Cultured Lentinura edodes Mycelia, on Natural Killer and T Cells in Health and Disease: Reviews on Human and Animal Studies.", J Immunol Res, 2019, PMID: 31930148',
            '[3] - Yoshii R., "The Tumor Growth Inhibitory Effect of a Standardized Extract of Cultured Lentinula edodes Mycelia Using Patient Derived Xenograft Model.", Biol Pharm Bull, 2024, PMID: 38417905',
            '[4] - Kamiyama T., "Preventing Recurrence of Hepatocellular Carcinoma After Curative Hepatectomy With Active Hexose-correlated Compound Derived From Lentinula edodes Mycelia.", Integr Cancer Ther, 2022, PMID: 35075934',
            '[5] - Roszczyk A., "Immunomodulatory Properties of Polysaccharides from Lentinula edodes.", Int J Mol Sci, 2022, PMID: 36012249',
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
