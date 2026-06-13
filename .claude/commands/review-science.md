---
description: Scientific fact-check and evidence review for any BMS Archive content. Validates claims against sources, flags overclaiming, checks study types, safety, and dose data. Use: /project:review-science [monograph name, field, or text to review]
---

You are performing a scientific evidence review for BMS Archive on: **$ARGUMENTS**

Use `scientific-qa-evidence-agent` to conduct this review.

---

## Review scope

If "$ARGUMENTS" is a species name, locate and review the full entry in `data.json`.
If "$ARGUMENTS" is a specific field or passage, review only that text.
If "$ARGUMENTS" is a file path, read and review that file.

---

## Step 1 — Read the content

Read the target content in full before starting the review. Do not begin commenting until you have read the complete text.

---

## Step 2 — Apply the evidence review checklist

For each claim in the content, evaluate:

**Evidence quality:**
- What study type supports this claim? (SR-MA / RCT / CCT / OBS / ANIMAL / IN-VITRO / TRAD)
- Is the language strength appropriate for the evidence level?
  - SR-MA/RCT language: "clinical evidence supports...", "studies have demonstrated..."
  - Animal/in vitro language: "preclinical data suggests...", "in vitro studies indicate..."
  - Traditional use: "traditionally used for...", "historical use includes..."
- Is human evidence being extrapolated from animal or in vitro data?

**Source validity:**
- Is the PMID or URL cited for this claim real?
- Does the cited source actually support the exact claim being made?
- Is the citation relevant to the population, dose, extract type, and condition claimed?

**Dosage accuracy:**
- Does the dosage claim specify: extract type, plant part, dose amount, frequency, duration, population?
- Is the dosage sourced from human data, official monographs, or traditional/regulatory guidance?
- Is the dose claim appropriate given the study design?

**Safety completeness:**
- Is the adverse effects section non-empty?
- Are contraindications documented?
- Are drug interactions flagged even when evidence is limited?
- Are pregnancy and lactation sections present?
- Are hepatic and renal precautions documented?
- Does any text write "safe" without supporting data?

**Overclaiming check:**
- Does any text imply the compound treats, cures, prevents, or diagnoses a disease?
- Does any text present in vitro or animal findings as proven human benefit?
- Does any text present mechanistic plausibility as clinical evidence?

---

## Step 3 — Produce a structured review report

For each issue found:

```
LOCATION: [field name or line]
CLAIM: [exact text]
ISSUE TYPE: Overclaiming / Unsupported / Wrong evidence level / Missing source / Safety gap / Citation mismatch
SEVERITY: Critical / Major / Minor
CURRENT TEXT: [what it says]
REQUIRED FIX: [what it should say]
```

At the end, produce a summary:
```
REVIEW SUMMARY
Total claims checked: [N]
Issues found: [N]
  Critical: [N]
  Major: [N]  
  Minor: [N]
Overall assessment: Approved / Requires revision / Rejected
```

---

## Rules

- **Never fabricate corrections** — if you cannot verify what the correct answer is, say so
- **Never invent citations** as replacements for unsupported claims
- **Flag every instance of "safe" without supporting data**
- **Flag every instance where in vitro/animal evidence is used to support human efficacy claims**
- **Do not soften safety warnings** — report them as found or flag them as insufficient
- Critical issues must be fixed before content is published or committed to `data.json`
