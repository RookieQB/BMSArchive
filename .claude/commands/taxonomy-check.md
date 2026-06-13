---
description: Check botanical identity, accepted Latin name, synonyms, plant part, and duplicate prevention for a species in BMS Archive. Use: /project:taxonomy-check [species name or common name]
---

You are performing a taxonomy and nomenclature check for BMS Archive on: **$ARGUMENTS**

Use `taxonomy-nomenclature-agent` to conduct this check.

---

## Step 1 — Identify the species

Determine what "$ARGUMENTS" refers to:
- Is it a Latin binomial? A common name? A synonym?
- Could this common name refer to more than one species? (e.g., "ginseng", "echinacea", "licorice")
- If ambiguous, list all species the name could refer to and ask for clarification before proceeding.

---

## Step 2 — Check the accepted name

Verify the currently accepted Latin binomial using:
- **Kew Plants of the World Online (POWO)** — primary authority for plants
- **Index Fungorum / MycoBank** — primary authority for fungi
- **Species Fungorum** — supplementary for fungi

Report:
```
INPUT NAME: [what was given]
ACCEPTED BINOMIAL: [Genus species Author citation]
SYNONYMS IN USE: [list of synonyms found in literature]
BOTANICAL FAMILY: [family name]
TYPE (for data.json): "Fungi" or "Plant"
POWO/MycoBank STATUS: Accepted / Synonym / Unresolved / Not found
```

---

## Step 3 — Check for duplicates in data.json

Search `data.json` for any existing entry matching:
- The accepted Latin name
- Any known synonyms
- Common name variants

```bash
python3 -c "
import json
data = json.load(open('data.json'))
target = '$ARGUMENTS'.lower()
matches = [d for d in data if target in d.get('scientific_name','').lower() or target in d.get('common_name','').lower()]
print(f'Matching entries: {len(matches)}')
for m in matches:
    print(f'  Index {data.index(m)}: {m[\"scientific_name\"]} — {m[\"common_name\"]}')
"
```

If a duplicate is found, report it and stop. Do not create a duplicate entry.

---

## Step 4 — Verify plant part and preparation

For the identified species, document:
- What plant/fungus parts are used in clinical studies (root, leaf, fruiting body, mycelium, seed, bark, etc.)
- Common preparation types documented in the literature (aqueous extract, ethanolic extract, standardized extract, powder, etc.)
- Whether fruiting body vs. mycelium distinction matters for this fungal species (often critical)
- Whether different parts have different evidence profiles

---

## Step 5 — Flag any issues

Report any of the following if found:
- Common name refers to multiple species — ambiguity risk
- The name given is a synonym, not the accepted name
- A duplicate entry exists or is likely
- Species-level vs. genus-level evidence distinction is important for this species
- There is a species complex where cultivar or chemotype matters

---

## Output format

```
TAXONOMY CHECK: $ARGUMENTS

Accepted name:       [Genus species]
Botanical family:    [Family]
Type field value:    "Fungi" or "Plant"
Synonyms in use:     [list]
Common name check:   Unambiguous / Ambiguous — [explanation]
Duplicate in data.json: Yes [index N] / No
Used part:          [parts documented in literature]
Preparation types:  [types documented]
Issues flagged:     [list or None]

RECOMMENDATION: Proceed / Clarify ambiguity / Duplicate found — do not add
```

---

## Rules

- **Never assume a common name maps to one species** without verification
- **Never use a synonym as `scientific_name`** in `data.json` — use the accepted name
- **Always distinguish fruiting body from mycelium** for fungal species
- **If taxonomy is uncertain, flag it** — do not guess
- This check must complete before `extraction-synthesis-agent` or `add-monograph` proceeds
