#!/usr/bin/env python3
"""
BMS Archive — data.json updater
Queries NCBI PubMed eSearch API for real PMIDs + article counts,
updates sources.top_studies_urls and article_count for all 25 items,
adds missing 'distribution' field to pharmacokinetics (items 8–24),
and wraps key pharmacological targets in <strong> tags (items 8–24).
"""

import json
import time
import urllib.request
import urllib.parse

DATA_FILE = "data.json"
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
SLEEP_SECONDS = 0.5  # stay well below 3 req/s anonymous limit

# ── Pre-prepared distribution text for items 8–24 ──────────────────────────
DISTRIBUTION = {
    "Agaricus blazei": (
        "Beta-glucan fractions concentrate at gut-associated lymphoid tissue (GALT), "
        "spleen, and mesenteric lymph nodes; limited systemic distribution. Blazein "
        "(steroid compound) distributes broadly due to lipophilicity; plasma protein "
        "binding not established in humans. No quantitative human tissue distribution studies available."
    ),
    "Tremella fuciformis": (
        "High-molecular-weight polysaccharides remain largely confined to the GI tract "
        "and GALT; smaller oligosaccharide fragments may enter systemic circulation via "
        "lymphatic uptake. Skin distribution is suggested by clinical hydration data, "
        "consistent with promotion of dermal hyaluronic acid synthesis. No formal human PK distribution studies."
    ),
    "Phellinus linteus": (
        "Hispidin and styrylpyrone compounds are lipophilic and distribute widely to "
        "liver, adipose tissue, and inflammatory foci. Polysaccharide fractions "
        "preferentially target GALT, spleen, and bone marrow. No formal human tissue "
        "distribution data available; preclinical rodent data only."
    ),
    "Poria cocos": (
        "Pachymaran (polysaccharide) preferentially targets GALT and spleen; limited "
        "systemic absorption. Pachymic acid (triterpenoid) is lipophilic; distributes "
        "to liver and adipose tissue. Plasma protein binding of triterpenoids estimated "
        ">80% by analogy with structurally related compounds. No human clinical PK distribution studies."
    ),
    "Polyporus umbellatus": (
        "Polysaccharide fractions (PU-PS) concentrate in kidneys, spleen, and lymph "
        "nodes, consistent with diuretic and immunomodulatory effects. Ergosterol "
        "derivatives distribute systemically. No formal human pharmacokinetic "
        "distribution studies available."
    ),
    "Flammulina velutipes": (
        "FVE (Flammulina velutipes lectin) and high-MW polysaccharides primarily act "
        "at mucosal surfaces and GALT. Flammulin distributes preferentially to actively "
        "dividing cells. Ergothioneine accumulates in erythrocytes via the OCTN1 "
        "transporter. No formal human PK distribution data."
    ),
    "Pleurotus ostreatus": (
        "Lovastatin undergoes extensive hepatic first-pass metabolism; the active "
        "β-hydroxy acid metabolite distributes systemically with high hepatic uptake "
        "(target organ) and ~95% plasma protein binding. Ergothioneine concentrates in "
        "erythrocytes via OCTN1 transporter. Polysaccharide fractions confined to GI/GALT. "
        "Volume of distribution of lovastatin ~0.5 L/kg."
    ),
    "Schizophyllum commune": (
        "Schizophyllan (SPG) is a high-molecular-weight β-glucan; following clinical "
        "(IV/IM) administration in Japan, it distributes to spleen, lymph nodes, and "
        "tumour-associated lymphatics. Oral bioavailability is poor; clinically relevant "
        "distribution data applies to parenteral routes only. No meaningful systemic oral distribution."
    ),
    "Auricularia auricula-judae": (
        "Adenosine distributes rapidly to red blood cells and vascular endothelium via "
        "active transport; plasma half-life ~10 seconds. High-MW anticoagulant "
        "polysaccharides distribute to vascular endothelium. Ergosterol distributes "
        "to lipid-rich membranes. No formal human PK studies for the fungal extract as a whole."
    ),
    "Coprinus comatus": (
        "Polysaccharide fractions concentrate at GALT, pancreatic tissue, and spleen, "
        "consistent with antidiabetic and immunomodulatory activity. Vanadium-containing "
        "compounds (if present) distribute to bone and kidney. No formal human "
        "pharmacokinetic distribution data available for this species."
    ),
    "Antrodia cinnamomea": (
        "Antroquinonol and ubiquinone derivatives are highly lipophilic; distribute to "
        "tumour vasculature, liver, and adipose tissue. Significant hepatic first-pass "
        "metabolism expected. Half-life of antroquinonol estimated at ~4–6 hours in "
        "preclinical models. No formal human PK distribution data available."
    ),
    "Fomes fomentarius": (
        "Fomentariol and hispidin are phenolic compounds with moderate lipophilicity; "
        "distribute systemically after intestinal absorption. Polysaccharide fractions "
        "concentrate in GALT and spleen. No formal human pharmacokinetic distribution "
        "data; all available data from in vitro and rodent studies."
    ),
    "Ophiocordyceps sinensis": (
        "Cordycepin distributes rapidly to lung, kidney, liver, and immune tissues. "
        "CSE-PS (polysaccharide) concentrates in spleen and thymus. Adenosine has a "
        "very short plasma half-life (~10 seconds) due to active cellular uptake. "
        "Plasma protein binding of nucleoside compounds is generally low (<30%). "
        "Pharmacokinetics closely parallel those of Cordyceps sinensis (Cs-4)."
    ),
    "Xylaria nigripes": (
        "Active alkaloids and sesquiterpenes are lipophilic; cross the blood-brain "
        "barrier in animal studies and distribute broadly to CNS, with preference for "
        "limbic structures (amygdala, hippocampus). No formal human PK distribution "
        "data; all data from rodent sleep and anxiety models."
    ),
    "Ustilago maydis": (
        "Ustilagic acid and lipid compounds are highly lipophilic; distribute to "
        "lipid-rich membranes and adipose tissue. Ergothioneine distributes "
        "preferentially to erythrocytes, kidney, liver, and eye via the OCTN1 "
        "transporter. Polysaccharides confined to GI/GALT. No formal PK "
        "distribution data."
    ),
    "Psilocybe cubensis": (
        "Psilocybin is rapidly converted to psilocin in the gut and liver by alkaline "
        "phosphatase. Psilocin (active form) is lipophilic; crosses the blood-brain "
        "barrier readily and distributes broadly to cortex, thalamus, and limbic "
        "structures (high 5-HT2A receptor density). Plasma protein binding ~64%. "
        "Volume of distribution estimated ~0.8 L/kg. Half-life of psilocin ~3 hours."
    ),
    "Amanita muscaria": (
        "Muscimol is water-soluble with moderate CNS penetration via passive diffusion; "
        "distributes to GABAergic neurons in cortex, cerebellum, and limbic system. "
        "Ibotenic acid is rapidly decarboxylated to muscimol in vivo. Muscimol is "
        "excreted largely unchanged in urine (~80%). Plasma half-life of muscimol "
        "approximately 3–5 hours."
    ),
}

# ── Pre-prepared mechanism_of_action with <strong> tags for items 8–24 ─────
MOA_STRONG = {
    "Agaricus blazei": (
        "Beta-glucans activate macrophages and NK cells via <strong>Dectin-1</strong>; "
        "upregulate Th1 cytokines (<strong>IL-12</strong>, <strong>IFN-γ</strong>, "
        "<strong>TNF-α</strong>). Anti-tumour mechanisms include direct cytotoxicity "
        "via induction of apoptosis (<strong>caspase-3</strong> pathway) and "
        "anti-angiogenic effects. Antidiabetic mechanism involves <strong>PPAR-γ</strong> "
        "activation and improved insulin receptor signalling. Agaritine is a potentially "
        "carcinogenic hydrazine compound degraded by cooking."
    ),
    "Tremella fuciformis": (
        "Tremella polysaccharides stimulate <strong>NGF</strong> secretion in astrocytes "
        "(similar mechanism to Lion's Mane), promoting neuronal differentiation and "
        "survival. Anti-inflammatory effects via inhibition of <strong>NF-κB</strong> "
        "and <strong>COX-2</strong>. Skin-hydrating effects attributed to polysaccharide "
        "hygroscopic properties and upregulation of hyaluronic acid synthase "
        "(<strong>HAS2</strong>). Immunomodulation via <strong>TLR-4</strong> activation."
    ),
    "Phellinus linteus": (
        "Hispidin and related styrylpyrones inhibit <strong>PKC</strong> (protein kinase C) "
        "and scavenge free radicals. Polysaccharides activate macrophages and NK cells via "
        "<strong>Dectin-1</strong>/<strong>TLR-4</strong>; upregulate <strong>IL-12</strong> "
        "and <strong>IFN-γ</strong>. Anti-tumour activity involves <strong>TRAIL</strong>-mediated "
        "apoptosis and <strong>VEGF</strong> inhibition (anti-angiogenic). Antidiabetic effect "
        "via α-glucosidase inhibition and improved insulin sensitivity through <strong>PPAR-γ</strong>."
    ),
    "Poria cocos": (
        "Pachymaran activates macrophages and NK cells via <strong>Dectin-1</strong>/<strong>TLR-4</strong>. "
        "Pachymic acid inhibits <strong>NF-κB</strong> pathway, reducing pro-inflammatory "
        "cytokines (<strong>IL-6</strong>, <strong>TNF-α</strong>, <strong>COX-2</strong>). "
        "Diuretic action attributed to direct renal tubular effects. Sedative effects involve "
        "positive modulation of <strong>GABA-A</strong> receptor (animal data only)."
    ),
    "Polyporus umbellatus": (
        "PU-PS activates macrophages and T-cells via <strong>TLR-2</strong>/<strong>Dectin-1</strong>; "
        "stimulates <strong>IL-2</strong>, <strong>IFN-γ</strong>. Anti-tumour effects via "
        "<strong>NK cell</strong> activation and induction of tumour cell apoptosis "
        "(<strong>Bcl-2</strong> suppression). Diuretic mechanism: inhibition of renal "
        "<strong>Na⁺/K⁺-ATPase</strong> and modulation of aquaporin expression. "
        "Ergosterol is a precursor to vitamin D2."
    ),
    "Flammulina velutipes": (
        "FVE activates macrophages and NK cells; stimulates Th1 cytokines "
        "(<strong>IFN-γ</strong>, <strong>IL-2</strong>). Flammulin inhibits protein "
        "synthesis in cancer cells via ribosome inactivating protein (RIP)-like activity. "
        "Lectins act as <strong>TLR-4</strong> ligands, activating innate immunity. "
        "Proflamin targets <strong>CD4+</strong> T-cells as an immunomodulatory lectin."
    ),
    "Pleurotus ostreatus": (
        "Lovastatin competitively inhibits <strong>HMG-CoA reductase</strong>, reducing "
        "hepatic cholesterol synthesis and upregulating <strong>LDL receptor</strong> "
        "expression. Beta-glucans activate <strong>Dectin-1</strong>, promoting Th1 immune "
        "response. <strong>ACE</strong>-inhibitory peptides reduce angiotensin II formation, "
        "producing antihypertensive effects. Ergothioneine acts as antioxidant via "
        "<strong>Nrf2</strong>/<strong>HO-1</strong> upregulation."
    ),
    "Schizophyllum commune": (
        "Schizophyllan activates macrophages and NK cells via <strong>Dectin-1</strong> "
        "receptor; upregulates <strong>IL-2</strong>, <strong>IFN-γ</strong>, "
        "<strong>TNF-α</strong>. Augments T-lymphocyte and dendritic cell function. "
        "Anti-tumour mechanism involves host-mediated immunostimulation rather than direct "
        "cytotoxicity. <strong>TLR-2</strong>/<strong>Dectin-1</strong> co-activation "
        "amplifies innate immune signalling cascades."
    ),
    "Auricularia auricula-judae": (
        "Adenosine and AAP inhibit platelet aggregation via <strong>adenosine A2A receptor</strong> "
        "activation, increasing platelet <strong>cAMP</strong> and reducing thromboxane A2. "
        "Anticoagulant polysaccharides inhibit <strong>thrombin</strong> and "
        "<strong>factor Xa</strong> (heparin-like mechanism). Hypoglycaemic activity via "
        "α-glucosidase inhibition and <strong>GLUT4</strong> upregulation in skeletal muscle. "
        "Immunomodulation via <strong>TLR-4</strong>/<strong>Dectin-1</strong>."
    ),
    "Coprinus comatus": (
        "Polysaccharides stimulate insulin secretion from pancreatic beta-cells and improve "
        "insulin sensitivity via <strong>PPAR-γ</strong> activation; inhibit α-glucosidase "
        "and <strong>aldose reductase</strong>. Lectins act as <strong>TLR-4</strong> agonists, "
        "promoting macrophage activation. Ink-cap polysaccharides upregulate "
        "<strong>Nrf2</strong>/<strong>HO-1</strong>, providing antioxidant protection "
        "in hyperglycaemic conditions. Coprinol exhibits antimicrobial activity against MRSA."
    ),
    "Antrodia cinnamomea": (
        "Antroquinonol inhibits <strong>Ras/Akt/mTOR</strong> signalling, inducing tumour "
        "cell autophagy and apoptosis; also inhibits <strong>HIF-1α</strong>, reducing "
        "hypoxia-driven <strong>VEGF</strong> expression (anti-angiogenic). Triterpenoids "
        "inhibit <strong>NF-κB</strong> pathway, reducing <strong>IL-6</strong>, "
        "<strong>TNF-α</strong>, and <strong>COX-2</strong>. Hepatoprotective via "
        "<strong>Nrf2</strong>/<strong>HO-1</strong> upregulation and suppression of "
        "<strong>CYP2E1</strong>-mediated oxidative stress."
    ),
    "Fomes fomentarius": (
        "Hispidin and fomentariol act as potent antioxidants (radical scavenging via "
        "phenolic hydroxyl groups). Fomentariol inhibits <strong>topoisomerase II</strong>, "
        "inducing cancer cell cycle arrest (G2/M phase). Polysaccharide fractions activate "
        "<strong>Dectin-1</strong>/<strong>TLR-4</strong>, promoting <strong>IL-12</strong> "
        "and <strong>TNF-α</strong> secretion. Anticoagulant activity through inhibition "
        "of <strong>thrombin</strong> and platelet aggregation."
    ),
    "Ophiocordyceps sinensis": (
        "Cordycepin inhibits <strong>mRNA polyadenylation</strong>, blocking cancer cell "
        "proliferation. <strong>Adenosine receptor</strong> modulation regulates cardiac "
        "output and vascular tone. <strong>HIF-1α</strong> stabilisation improves tissue "
        "oxygenation under hypoxic conditions. Cordycepin activates <strong>AMPK</strong>, "
        "enhancing glucose uptake in muscle. <strong>Th1/Th2</strong> balance regulation "
        "via <strong>IL-12</strong>/<strong>IL-10</strong> axis modulation."
    ),
    "Xylaria nigripes": (
        "Positive allosteric modulation of <strong>GABA-A receptor</strong> (benzodiazepine-like "
        "effect), prolonging inhibitory chloride channel opening. <strong>5-HT</strong> "
        "reuptake inhibition proposed in animal models. Anti-inflammatory effects via "
        "<strong>NF-κB</strong> inhibition and reduction of <strong>IL-6</strong>, "
        "<strong>TNF-α</strong>. Adenosine receptor modulation may contribute to "
        "anxiolytic and sleep-promoting effects."
    ),
    "Ustilago maydis": (
        "Ustilagic acid disrupts bacterial and fungal cell membranes (detergent-like "
        "mechanism) and inhibits <strong>NF-κB</strong>-mediated pro-inflammatory "
        "signalling. Ergothioneine accumulates via <strong>OCTN1</strong> transporter; "
        "protects mitochondria and DNA from oxidative damage. Polysaccharides activate "
        "<strong>Dectin-1</strong>/<strong>TLR-4</strong>, promoting macrophage "
        "differentiation. Rich in melanin precursors with UV-protective properties."
    ),
    "Psilocybe cubensis": (
        "Psilocybin is rapidly dephosphorylated to psilocin by <strong>alkaline phosphatase</strong>. "
        "Psilocin is a full agonist at serotonin <strong>5-HT2A receptor</strong> in cortical "
        "pyramidal neurons, disrupting default mode network (DMN) activity. Also agonist at "
        "<strong>5-HT2C</strong> and <strong>5-HT1A</strong>. Promotes neuroplasticity via "
        "<strong>BDNF</strong> upregulation and synaptogenesis. <strong>AMPA/NMDA</strong> "
        "receptor modulation contributes to sustained antidepressant effect."
    ),
    "Amanita muscaria": (
        "Muscimol is a highly potent, selective <strong>GABA-A receptor</strong> agonist "
        "(structural analogue of GABA), producing sedation, anxiolysis, and psychedelic effects. "
        "Ibotenic acid is an <strong>NMDA receptor</strong> and <strong>mGluR</strong> agonist "
        "(excitotoxic at high doses); rapidly decarboxylated in vivo to muscimol. Muscimol also "
        "acts at cerebellar <strong>GABA-B</strong> receptors. Muscarine (minor component) "
        "activates <strong>mAChR</strong> (muscarinic acetylcholine receptors), contributing "
        "to cholinergic toxidrome symptoms."
    ),
}


def pubmed_search(scientific_name):
    """Query PubMed eSearch and return (count, [pmid, ...])."""
    params = urllib.parse.urlencode({
        "db": "pubmed",
        "term": scientific_name,
        "retmode": "json",
        "retmax": 3,
    })
    url = f"{ESEARCH_URL}?{params}"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            result = json.loads(resp.read().decode())["esearchresult"]
            count = int(result.get("count", 0))
            ids = result.get("idlist", [])
            return count, ids
    except Exception as exc:
        print(f"  WARNING: API error for '{scientific_name}': {exc}")
        return None, []


def main():
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)

    for i, item in enumerate(data):
        name = item.get("scientific_name", "")
        print(f"[{i+1}/25] {name}")

        # ── 1. PubMed API ────────────────────────────────────────────────────
        count, pmids = pubmed_search(name)
        time.sleep(SLEEP_SECONDS)

        if count is not None:
            item["article_count"] = count
            print(f"       article_count → {count}")

        if pmids:
            urls = [f"https://pubmed.ncbi.nlm.nih.gov/{pid}/" for pid in pmids]
            item["sources"] = {"top_studies_urls": urls}
            print(f"       sources → {urls}")
        else:
            item["sources"] = {"top_studies_urls": ["N/A"]}
            print(f"       sources → N/A (no results)")

        # ── 2. Distribution field (items 8–24 only) ──────────────────────────
        pk = item.get("clinical_data", {}).get("pharmacokinetics", {})
        if "distribution" not in pk and name in DISTRIBUTION:
            # Insert 'distribution' between 'absorption' and 'metabolism'
            new_pk = {}
            for key, val in pk.items():
                new_pk[key] = val
                if key == "absorption":
                    new_pk["distribution"] = DISTRIBUTION[name]
            if "absorption" not in pk:
                new_pk["distribution"] = DISTRIBUTION[name]
            item["clinical_data"]["pharmacokinetics"] = new_pk
            print(f"       distribution → added")

        # ── 3. <strong> tags in mechanism_of_action (items 8–24 only) ────────
        moa = item.get("clinical_data", {}).get("mechanism_of_action", "")
        if "<strong>" not in moa and name in MOA_STRONG:
            item["clinical_data"]["mechanism_of_action"] = MOA_STRONG[name]
            print(f"       mechanism_of_action → <strong> tags added")

    # ── Save ─────────────────────────────────────────────────────────────────
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\ndata.json updated and saved.")


if __name__ == "__main__":
    main()
