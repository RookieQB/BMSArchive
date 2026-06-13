---
description: Master workflow — fix all unqualified "safe" claims found by the validation script. Reviews each claim, applies precise evidence-based language, re-validates, and reports before/after counts. Run after the validation script reports "safe" warnings.
---

You are running the **BMS Archive fix-safe-claims workflow**.

The validation script found 37 warnings for unqualified "safe" claims across the existing `data.json`. This workflow systematically fixes them with precise, evidence-appropriate language.

**This is the highest-priority cleanup task. Do not skip any entry.**

---

## PHASE 0 — Baseline

Run the validation script to get the current warning list:
```bash
python3 scripts/validate_archive_data.py 2>&1 | grep -i "safe\|WARN" | sort
```

Save the count:
```bash
python3 scripts/validate_archive_data.py 2>&1 | grep -c "WARN"
```

Expected baseline: 37 warnings. Record this as the starting count.

---

## PHASE 1 — Categorise each "safe" claim

For every warning, determine which of these categories applies:

| Category | Meaning | Correct language |
|---|---|---|
| **A — Study-tolerated** | A specific study reported no serious adverse events | "Well tolerated in the cited study" / "No serious adverse events reported in [trial type, n=X]" |
| **B — No reports, limited data** | Adverse events simply were not documented (short trial, small n) | "No adverse events reported in available clinical studies, though evidence is limited to [N weeks / small trials]" |
| **C — Insufficient safety data** | No safety studies exist | "Insufficient clinical safety data. Absence of reported harm does not establish safety." |
| **D — Traditional use** | Called "safe" on the basis of traditional use only | "Long history of traditional use without documented serious harm. Modern clinical safety data are limited." |
| **E — Overclaim** | No evidence basis for the "safe" claim | Remove the word "safe" entirely; replace with a factual description of what is known |

**Do not simply delete the word "safe". Replace it with precise language.**

---

## PHASE 2 — Process entries in batches

Work through each flagged entry. For each:

1. Read the full affected field
2. Identify the category (A/B/C/D/E)
3. Use `scientific-qa-evidence-agent` to review the context and approve the replacement language
4. Apply the fix to the specific field in `data.json`

**Process 5 entries at a time. Run `python3 -c "import json; json.load(open('data.json'))"` after each batch to confirm JSON remains valid.**

### Priority order (fix first)

Pregnancy/lactation fields first — these carry the highest patient safety risk:
1. All `special_precautions.pregnancy` warnings
2. All `special_precautions.lactation` warnings
3. All `safety_and_interactions` warnings
4. All `narrative_summary.side_effects` and `narrative_summary.contraindications` warnings
5. All `special_precautions.hepatic_impairment` and `special_precautions.renal_impairment` warnings

---

## PHASE 3 — Language patterns to use

### For pregnancy fields

**Before (problematic):**
> "Safe when used in normal dietary amounts"
> "Considered safe in traditional use"

**After (correct):**
> "Safety during pregnancy has not been established in human clinical studies. If used only as a culinary spice at food-level doses, the risk profile is considered low based on long traditional use; however, medicinal doses are not recommended during pregnancy due to insufficient safety data."

> "Insufficient clinical safety data during pregnancy. Use is not recommended due to lack of established safety, particularly at therapeutic doses."

### For lactation fields

**Before (problematic):**
> "Likely safe in small amounts"
> "Safe for short-term use"

**After (correct):**
> "It is unknown whether [active compounds] or their metabolites are excreted in human breast milk. As a precautionary measure, use at medicinal doses during lactation is not recommended."

### For drug interaction / toxicity fields

**Before (problematic):**
> "Generally safe at recommended doses"
> "Safe when not combined with anticoagulants"

**After (correct):**
> "No clinically significant interactions have been formally established at standard doses. Theoretical interactions with anticoagulants exist based on [mechanism]. Caution is warranted until more data are available."

> "No serious toxicity reported in available clinical trials (duration: [N weeks], n=[N]). Long-term toxicity data in humans are not available."

### For side effects fields

**Before (problematic):**
> "Generally safe and well tolerated"

**After (correct):**
> "Well tolerated in short-term clinical trials of up to [N] weeks at [dose]. Most reported adverse effects were mild and gastrointestinal in nature. Long-term safety data are not available."

---

## PHASE 4 — Scientific QA sign-off (scientific-qa-evidence-agent)

After completing all replacements, run a targeted review:

For each changed entry, confirm:
- [ ] New language accurately reflects the actual evidence base
- [ ] No overclaiming in either direction (not weaker than evidence supports, not stronger)
- [ ] Pregnancy and lactation language follows the conservative pattern
- [ ] No "safe" remains without evidence qualification
- [ ] No claim was removed that provided genuine safety information

---

## PHASE 5 — Full validation

```bash
python3 scripts/validate_archive_data.py
```

Count warnings:
```bash
python3 scripts/validate_archive_data.py 2>&1 | grep -c "WARN"
```

**Target: 0 warnings related to unqualified "safe" claims.**

If warnings remain, process the remaining entries.

```bash
python3 scripts/validate_archive_data.py --strict
```

---

## PHASE 6 — QA

Check `database.html` in browser:
- Entries still render correctly in the grid
- Modal opens and shows updated safety text
- No console errors

---

## PHASE 7 — Final report

```
## Fix Safe Claims — Completed

### Before
Total warnings: 37
Safe-related warnings: 37

### After
Total warnings: [N]
Safe-related warnings remaining: [N]

### Changes made
| Entry | Field | Before (shortened) | After (shortened) | Category |
|---|---|---|---|---|
| [species] | [field] | "...safe..." | "...precise language..." | [A/B/C/D/E] |

### Scientific QA
[ ] All replacements reviewed by scientific-qa-evidence-agent
[ ] Pregnancy/lactation fields prioritised and verified

### Validation
JSON valid:  ✓/✗
Errors:      [N]
Warnings remaining: [N]

### Remaining work
[list any warnings that could not be resolved and why]
```

---

## Rules

- **Never simply delete "safe"** — always replace with precise language
- **Never weaken genuine safety warnings** — if "safe" appeared in a contraindication field, the field still needs a clear warning
- **Process pregnancy/lactation first** — these are highest patient-safety risk
- **Use `scientific-qa-evidence-agent` for review** — do not apply replacements without review
- **Run validation after every 5-entry batch** — detect JSON errors early
- **Do not add Instagram or social media content**
