#!/usr/bin/env python3
"""
build_plants.py — BMS Archive plant profile builder (v2)

Generates evidence-based plant monographs with master's thesis-level citations.

Per plant:
  1. PubMed esearch  → article count + top PMIDs
  2. PubMed efetch   → metadata + abstracts for top articles
  3. Europe PMC      → 15 additional results (0.5 s sleep, no key required)
  4. Build numbered reference list, deduplicate by title
  5. Claude opus-4-7 → JSON profile with strict [N] inline citations

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    python3 build_plants.py

Resume after interruption: re-run — completed plants are skipped.
Fresh start: delete plants_progress.json, then run.
"""

import json
import os
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

import anthropic

# ── Config ─────────────────────────────────────────────────────────────────────
PROGRESS_FILE    = "plants_progress.json"
DATA_FILE        = "data.json"
SLEEP_PUBMED     = 0.5
SLEEP_EPMC       = 0.5        # Europe PMC allows up to 10 req/s; 0.5 s is safe
SLEEP_S2         = 1.1        # Semantic Scholar: 1 req/s cumulative; add small buffer
PUBMED_MAX       = 5          # top PubMed articles per plant
EPMC_PAGE_SIZE   = 15         # Europe PMC results per plant
S2_MAX           = 10         # Semantic Scholar results per plant
ABSTRACT_CHARS   = 700        # truncate each abstract to keep context manageable

PLANTS = [
    ("Ginkgo biloba",         "Ginkgo / Maidenhair tree"),
    ("Panax ginseng",         "Asian ginseng / Korean red ginseng"),
    ("Bacopa monnieri",       "Brahmi / Water hyssop"),
    ("Rhodiola rosea",        "Golden root / Arctic root"),
    ("Withania somnifera",    "Ashwagandha / Indian winter cherry"),
    ("Valeriana officinalis", "Valerian"),
    ("Matricaria chamomilla", "German chamomile"),
    ("Passiflora incarnata",  "Passionflower / Maypop"),
    ("Nigella sativa",        "Black seed / Black cumin"),
    ("Echinacea purpurea",    "Purple coneflower"),
    ("Sambucus nigra",        "Elderberry"),
    ("Astragalus propinquus", "Astragalus / Huang Qi"),
    ("Curcuma longa",         "Turmeric"),
    ("Zingiber officinale",   "Ginger"),
    ("Boswellia serrata",     "Indian frankincense / Shallaki"),
    ("Salix alba",            "White willow / Willow bark"),
    ("Berberis vulgaris",     "Barberry"),
    ("Silybum marianum",      "Milk thistle"),
    ("Allium sativum",        "Garlic"),
    ("Cinnamomum verum",      "Ceylon cinnamon / True cinnamon"),
    ("Crataegus monogyna",    "Hawthorn"),
    ("Vitex agnus-castus",    "Chaste tree / Chasteberry"),
    ("Serenoa repens",        "Saw palmetto"),
    ("Tribulus terrestris",   "Tribulus / Puncture vine"),
    ("Urtica dioica",         "Stinging nettle"),
]


SCHEMA_EXAMPLE = """{
  "scientific_name": "...",
  "common_name": "...",
  "type": "Plant",
  "article_count": 0,
  "primary_categories": ["Category1", "Category2"],
  "sources": {
    "top_studies_urls": [],
    "cited_references": ["[1] - Author(s), Title, Journal, Year, PMID/DOI"]
  },
  "narrative_summary": {
    "historical_use": "...",
    "modern_application": "...",
    "side_effects": "...",
    "contraindications": "..."
  },
  "clinical_data": {
    "used_part": "...",
    "primary_active_compounds": ["Compound1", "Compound2"],
    "mechanism_of_action": "... <strong>TARGET</strong> ...",
    "pharmacokinetics": {
      "absorption": "...",
      "distribution": "...",
      "metabolism": "...",
      "excretion": "..."
    },
    "safety_and_interactions": {
      "drug_interactions": "...",
      "toxicity": "..."
    },
    "special_precautions": {
      "pregnancy": "...",
      "lactation": "...",
      "hepatic_impairment": "...",
      "renal_impairment": "..."
    }
  }
}"""

CLAUDE_PROMPT = """\
You are an expert clinical pharmacognosist. Write a complete evidence-based monograph for the \
medicinal plant below at the standard of a master's thesis in clinical pharmacology.

Plant: {scientific_name} (common name: {common_name})

════════════════════════════════════════
NUMBERED REFERENCE LIST
These are the only sources available to you. Cite them by bracket number [N].
════════════════════════════════════════
{numbered_source_list}

════════════════════════════════════════
RETRIEVED ABSTRACTS
Read these before writing. Use them to populate every field.
════════════════════════════════════════
{context_block}

════════════════════════════════════════
OUTPUT RULES — read carefully
════════════════════════════════════════
Return ONLY valid JSON matching the schema exactly. No markdown, no code fences, no commentary.

CITATION RULES:
• Every pharmacokinetic value, interaction claim, or clinical fact must end with [N] or [N, M].
  Examples: "Oral bioavailability is ~29% [1]."  /  "Inhibits CYP3A4 and CYP2C9 [2, 3]."
• sources.cited_references must list every source you actually cite, each formatted as:
  "[N] - Author(s), Title, Journal, Year, PMID/DOI"
  Only include sources whose number appears in the text above.
• Do NOT invent citations. Do NOT reference a source number that is not in the list above.
• If insufficient peer-reviewed human data exist for a PK subfield, begin that field with:
  "No human pharmacokinetic data are available for this species. The following is derived \
from preclinical animal studies and in vitro data only, and may not reflect human pharmacology. — "
  then continue with the best available evidence [N].
• For drug_interactions: if no peer-reviewed clinical study from the list above directly \
documents an interaction for this species, write EXACTLY this and nothing else:
  "Lack of clinical studies prevents interaction grading. Unknown safety profile with concomitant drug use."

FIELD RULES:
• type: must be "Plant"
• article_count: set to 0 (the script overwrites this with the real PubMed count)
• sources.top_studies_urls: set to [] (the script overwrites this)
• primary_categories: 2–4 concise clinical categories (e.g. "Adaptogen", "Anti-inflammatory")
• narrative_summary: each subfield 2–4 sentences with citations where possible
• used_part: plant part(s) used medicinally (e.g. "Root and rhizome", "Leaf extract")
• primary_active_compounds: 4–7 specific named phytochemicals
• mechanism_of_action: 3–5 sentences; wrap every receptor, enzyme, cytokine, or pathway \
in <strong> tags (e.g. <strong>NF-κB</strong>, <strong>CYP3A4</strong>); cite each claim
• pharmacokinetics.absorption: oral bioavailability %, Cmax timing, formulation effects — cited
• pharmacokinetics.distribution: tissue distribution, protein binding %, BBB penetration — cited
• pharmacokinetics.metabolism: hepatic enzymes, key metabolites, prodrug conversion — cited
• pharmacokinetics.excretion: route (renal/biliary), approximate half-life — cited
• safety_and_interactions.drug_interactions: cite every interaction with [N], or write the exact disclaimer
• safety_and_interactions.toxicity: LD50 if known, dose-dependent effects, hepatotoxicity concerns — cited
• special_precautions: pregnancy, lactation, hepatic_impairment, renal_impairment — 1–2 sentences each

Schema:
{schema}
"""


# ── PubMed ─────────────────────────────────────────────────────────────────────
def pubmed_search_ids(scientific_name):
    params = urllib.parse.urlencode({
        "db": "pubmed", "term": scientific_name,
        "retmode": "json", "retmax": PUBMED_MAX, "sort": "relevance",
    })
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?{params}"
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            data = json.loads(r.read().decode())["esearchresult"]
        return int(data.get("count", 0)), data.get("idlist", [])
    except Exception as e:
        print(f"  PubMed esearch error: {e}")
        return 0, []


def pubmed_fetch_articles(pmids):
    if not pmids:
        return []
    params = urllib.parse.urlencode({
        "db": "pubmed", "id": ",".join(pmids),
        "rettype": "abstract", "retmode": "xml",
    })
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?{params}"
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            root = ET.fromstring(r.read())
    except Exception as e:
        print(f"  PubMed efetch error: {e}")
        return []

    articles = []
    for art in root.findall(".//PubmedArticle"):
        pmid = art.findtext(".//PMID", "")

        title_el = art.find(".//ArticleTitle")
        title = "".join(title_el.itertext()) if title_el is not None else ""

        author_els = art.findall(".//Author")
        parts = []
        for a in author_els[:3]:
            last = a.findtext("LastName", "")
            init = a.findtext("Initials", "")
            if last:
                parts.append(f"{last} {init}".strip())
        authors = ", ".join(parts) + (" et al." if len(author_els) > 3 else "")

        journal = (art.findtext(".//Journal/Title")
                   or art.findtext(".//ISOAbbreviation", ""))
        year = (art.findtext(".//PubDate/Year")
                or (art.findtext(".//PubDate/MedlineDate") or "")[:4])

        abstract_els = art.findall(".//AbstractText")
        abstract = " ".join((el.text or "") for el in abstract_els).strip()

        articles.append({
            "pmid":     pmid,
            "title":    title,
            "authors":  authors or "Unknown",
            "journal":  journal,
            "year":     year,
            "abstract": abstract,
            "url":      f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        })
    return articles


# ── Semantic Scholar ───────────────────────────────────────────────────────────
def semantic_scholar_search(scientific_name):
    """Query Semantic Scholar for papers on a species, sorted by citation count."""
    api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
    params = urllib.parse.urlencode({
        "query":  scientific_name,
        "fields": "paperId,title,abstract,year,authors,citationCount,externalIds,journal",
        "limit":  S2_MAX,
    })
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?{params}"
    req = urllib.request.Request(url)
    if api_key:
        req.add_header("x-api-key", api_key)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read().decode())
        return data.get("data", [])
    except Exception as e:
        print(f"  Semantic Scholar error: {e}")
        return []


# ── Europe PMC ─────────────────────────────────────────────────────────────────
def europepmc_search(scientific_name):
    params = urllib.parse.urlencode({
        "query":      (f'{scientific_name} AND (pharmacokinetics OR CYP450 OR '
                       '"drug interactions" OR "clinical trial")'),
        "format":     "json",
        "resultType": "core",
        "pageSize":   EPMC_PAGE_SIZE,
    })
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?{params}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "BMS-Archive-Research/2.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read().decode())
    except Exception as e:
        print(f"  Europe PMC error: {e}")
        return []

    papers = []
    for item in data.get("resultList", {}).get("result", []):
        pmid    = item.get("pmid", "")
        doi     = item.get("doi", "")
        title   = (item.get("title", "") or "").rstrip(".")
        year    = str(item.get("pubYear", "") or "")
        authors = item.get("authorString", "") or "Unknown"
        journal = ((item.get("journalInfo") or {})
                   .get("journal", {}).get("title", ""))
        abstract = item.get("abstractText", "") or ""
        url_str  = (f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid
                    else f"https://doi.org/{doi}" if doi else "")
        papers.append({
            "title":    title,
            "authors":  authors,
            "journal":  journal,
            "year":     year,
            "pmid":     pmid,
            "doi":      doi,
            "abstract": abstract,
            "url":      url_str,
        })
    return papers


# ── Reference builder ───────────────────────────────────────────────────────────
def build_reference_list(pubmed_articles, epmc_papers, s2_papers=None):
    seen = set()
    refs = []

    def try_add(title, authors, journal, year, id_str, abstract, url):
        key = title[:60].lower().strip()
        if not key or key in seen:
            return
        seen.add(key)
        n = len(refs) + 1
        journal_part = f", {journal}" if journal else ""
        label = f"[{n}] - {authors}, \"{title}\"{journal_part}, {year}, {id_str}"
        refs.append({"n": n, "label": label, "abstract": abstract, "url": url})

    for art in pubmed_articles:
        id_str = f"PMID: {art['pmid']}" if art["pmid"] else "no ID"
        try_add(art["title"], art["authors"], art["journal"],
                art["year"], id_str, art["abstract"], art["url"])

    for paper in epmc_papers:
        id_str = (f"PMID: {paper['pmid']}" if paper["pmid"]
                  else f"DOI: {paper['doi']}" if paper["doi"] else "no ID")
        try_add(paper["title"], paper["authors"], paper["journal"],
                paper["year"], id_str, paper["abstract"], paper["url"])

    # Semantic Scholar: add papers ranked by citation count; skip if no verifiable ID
    for p in sorted(s2_papers or [], key=lambda x: x.get("citationCount", 0), reverse=True):
        ext      = p.get("externalIds") or {}
        pmid     = ext.get("PubMed", "")
        doi      = ext.get("DOI", "")
        if not pmid and not doi:
            continue
        id_str   = f"PMID: {pmid}" if pmid else f"DOI: {doi}"
        url_str  = (f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid
                    else f"https://doi.org/{doi}")
        al       = p.get("authors") or []
        a_parts  = [a.get("name", "") for a in al[:3] if a.get("name")]
        authors_str = (", ".join(a_parts) + (" et al." if len(al) > 3 else "")) or "Unknown"
        journal  = ((p.get("journal") or {}).get("name", ""))
        try_add(p.get("title", ""), authors_str, journal,
                str(p.get("year", "") or ""), id_str,
                (p.get("abstract") or ""), url_str)

    numbered_source_list = "\n".join(r["label"] for r in refs) or "(no sources retrieved)"

    context_parts = []
    for r in refs:
        ab = (r["abstract"] or "").strip()
        if ab:
            context_parts.append(f"Abstract [{r['n']}]:\n{ab[:ABSTRACT_CHARS]}")
    context_block = "\n\n".join(context_parts) or "(no abstracts available)"

    urls = [r["url"] for r in refs if r["url"]]
    return numbered_source_list, context_block, urls


# ── JSON extraction (robust) ───────────────────────────────────────────────────
def extract_json(raw):
    raw = raw.strip()
    start = raw.find("{")
    end   = raw.rfind("}") + 1
    if start == -1 or end <= start:
        raise ValueError("No JSON object found in response")
    return json.loads(raw[start:end])


# ── Claude ─────────────────────────────────────────────────────────────────────
def generate_profile(client, scientific_name, common_name, numbered_source_list, context_block):
    prompt = CLAUDE_PROMPT.format(
        scientific_name=scientific_name,
        common_name=common_name,
        numbered_source_list=numbered_source_list,
        context_block=context_block,
        schema=SCHEMA_EXAMPLE,
    )
    msg = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return extract_json(msg.content[0].text)


# ── Progress ────────────────────────────────────────────────────────────────────
def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {}

def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


# ── Main ────────────────────────────────────────────────────────────────────────
def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("ERROR: set ANTHROPIC_API_KEY before running.")

    client   = anthropic.Anthropic(api_key=api_key)
    progress = load_progress()

    for i, (sci_name, com_name) in enumerate(PLANTS):
        if sci_name in progress:
            print(f"[{i+1}/25] {sci_name} — already done, skipping")
            continue

        print(f"\n[{i+1}/25] {sci_name}")

        # 1 — PubMed IDs + count
        print("  → PubMed esearch...")
        count, pmids = pubmed_search_ids(sci_name)
        time.sleep(SLEEP_PUBMED)

        # 2 — PubMed abstracts
        pubmed_articles = []
        if pmids:
            print(f"  → PubMed efetch ({len(pmids)} articles)...")
            pubmed_articles = pubmed_fetch_articles(pmids)
            time.sleep(SLEEP_PUBMED)

        # 3 — Europe PMC
        print("  → Europe PMC...")
        epmc_papers = europepmc_search(sci_name)
        time.sleep(SLEEP_EPMC)

        # 4 — Semantic Scholar (supplementary, ranked by citation count)
        s2_papers = []
        if os.environ.get("SEMANTIC_SCHOLAR_API_KEY"):
            print("  → Semantic Scholar...")
            s2_papers = semantic_scholar_search(sci_name)
            time.sleep(SLEEP_S2)
        else:
            print("  → Semantic Scholar: skipped (SEMANTIC_SCHOLAR_API_KEY not set)")

        # 5 — Build numbered reference list
        numbered_source_list, context_block, urls = build_reference_list(
            pubmed_articles, epmc_papers, s2_papers)
        unique_refs = len(numbered_source_list.splitlines())
        print(f"  → {len(pubmed_articles)} PubMed + {len(epmc_papers)} EPMC "
              f"+ {len(s2_papers)} S2 hits → {unique_refs} unique refs")

        # 6 — Claude
        print("  → Claude (generating cited profile)...")
        try:
            profile = generate_profile(client, sci_name, com_name,
                                       numbered_source_list, context_block)
        except (ValueError, json.JSONDecodeError) as e:
            print(f"  ERROR: JSON parse failed — {e}. Skipping {sci_name}.")
            continue
        time.sleep(1.0)

        # 7 — Inject real PubMed metadata (override Claude placeholders)
        profile["scientific_name"]  = sci_name
        profile["common_name"]      = com_name
        profile["type"]             = "Plant"
        profile["article_count"]    = count
        profile.setdefault("sources", {})["top_studies_urls"] = urls or ["N/A"]

        progress[sci_name] = profile
        save_progress(progress)
        print(f"  ✓ saved — {count} PubMed articles, {unique_refs} refs")

    # ── Merge into data.json ────────────────────────────────────────────────────
    print("\nAll 25 plants generated. Merging into data.json...")
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)

    name_to_idx = {d["scientific_name"]: idx for idx, d in enumerate(data)}
    added = updated = 0
    for sci_name, _ in PLANTS:
        if sci_name not in progress:
            print(f"  MISSING (skipped during generation): {sci_name}")
            continue
        if sci_name in name_to_idx:
            data[name_to_idx[sci_name]] = progress[sci_name]
            updated += 1
        else:
            data.append(progress[sci_name])
            added += 1

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Done — {added} added, {updated} updated. data.json now has {len(data)} entries.")
    print()
    print("Deploy:")
    print('  scp "data.json" root@192.168.0.100:/tmp/data.json')
    print("  ssh root@192.168.0.100 \"pct push 102 /tmp/data.json /opt/bms-archive/data.json && "
          "pct exec 102 -- bash -c 'cd /opt/bms-archive && docker compose up -d --build'\"")

if __name__ == "__main__":
    main()
