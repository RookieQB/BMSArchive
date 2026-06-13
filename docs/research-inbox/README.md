# BMS Archive — Research Inbox

The research inbox is a controlled staging area for incoming studies, papers, and literature sources before they are incorporated into published monographs.

**Nothing in the inbox is published.** Inbox items go through structured extraction, scientific QA, and explicit promotion before they appear in `data.json`.

---

## Why this exists

Raw research sources (PubMed abstracts, PDFs, DOIs) need:
1. Structured extraction against the data model
2. Scientific QA to check evidence level and language
3. Taxonomy verification
4. A deliberate decision to promote or reject

Without a staging area, sources might be added to monographs before they are properly reviewed, or lost before they are added at all.

---

## Directory structure

```
docs/research-inbox/
├── README.md                    — this file
├── SOURCE_NOTE_TEMPLATE.md      — template for new inbox items
└── items/                       — one file per source
    ├── [PMID]-[species].md
    └── [YYYY-MM-DD]-[species]-[condition].md
```

---

## Item lifecycle

```
INCOMING → EXTRACTION → QA → PROMOTE / REJECT
```

| Status | Meaning | Next action |
|---|---|---|
| `extraction_status: pending` | Study identified but not yet extracted | Run extraction-synthesis-agent |
| `extraction_status: partial` | Extraction incomplete (missing fields, full text needed) | Obtain full text, complete extraction |
| `extraction_status: complete` | All available fields extracted | Run scientific QA |
| `qa_status: pending` | Awaiting scientific-qa-evidence-agent review | Run /workflow:pre-publish check or direct QA |
| `qa_status: approved` | Scientific QA passed | Ready to promote to monograph |
| `qa_status: rejected` | Scientific QA found blocking issues | Note reason; do not promote |
| `monograph_status: not started` | Source not yet in any monograph | Promote with /workflow:new-monograph or /workflow:update-monograph |
| `monograph_status: incorporated` | Source is now in data.json | Archive the inbox item |

---

## Naming conventions

- If PMID known: `[PMID]-[species-kebab-case].md`  
  Example: `38547821-ganoderma-lucidum.md`

- If no PMID: `[YYYY-MM-DD]-[species-kebab]-[condition-slug].md`  
  Example: `2026-06-12-withania-somnifera-anxiety.md`

Use lowercase kebab-case for all filenames. Do not use spaces.

---

## What goes here

- PubMed abstracts and PMIDs
- DOIs for papers where the abstract is accessible
- Regulatory monographs (EMA/HMPC, ESCOP, WHO)
- Systematic reviews found during research
- Papers flagged for future processing from `/workflow:weekly-maintenance`

---

## What does NOT go here

- Studies that cannot be verified (no PMID, no DOI, no accessible abstract)
- Secondary sources that only cite primary literature (cite the primary)
- News articles or blog posts
- AI-generated summaries treated as sources

---

## Promotion workflow

To promote an inbox item to a monograph:

1. Confirm `extraction_status: complete` and `qa_status: approved`
2. Run `/workflow:new-monograph [species]` or `/workflow:update-monograph [species]`
3. Update the inbox item: set `monograph_status: incorporated`
4. Move or rename the file to `.archived/[original-name].md` (optional, for clean inbox)

**Do not edit `data.json` directly from an inbox item without running the monograph workflow.**

---

## Commands

| Task | Command |
|---|---|
| Add a new source | `/workflow:research-inbox [PMID or description]` |
| Check inbox status | `/workflow:weekly-maintenance` |
| Promote to monograph | `/workflow:new-monograph [species]` or `/workflow:update-monograph [species]` |
