# BMS Archive — Evidence Scoring Rubric

Version 1.0 | For use with `scientific-qa-evidence-agent`, `extraction-synthesis-agent`, and all monograph workflows.

---

## Evidence Levels

Each clinical use claim in BMS Archive must be assigned an evidence level. The level reflects the **strongest evidence available for that specific claim**, not the strongest evidence for the plant or fungus in general.

### Level A — Strong Human Evidence

**Definition:** Consistent findings from multiple well-designed randomized controlled trials in humans, ideally synthesized in a systematic review or meta-analysis.

**Study types that qualify:**
- Systematic reviews with meta-analysis of ≥2 RCTs with consistent direction of effect
- Multiple independent RCTs with consistent results

**Language that fits Level A:**
> "Systematic reviews support...", "Clinical trial evidence demonstrates...", "Meta-analyses confirm..."

**Examples:**
- Ginkgo biloba for symptomatic dementia — multiple RCTs, meta-analyses available
- Silybum marianum (milk thistle) for supportive liver function — systematic review level evidence

**Does not qualify if:**
- RCTs are industry-funded with high bias
- Results are inconsistent across trials
- Studies used very different preparations or doses with no standardization

---

### Level B — Moderate Human Evidence

**Definition:** At least one relevant, adequately powered human RCT, or several smaller controlled clinical trials (CCTs) with consistent results.

**Study types that qualify:**
- Single RCT of adequate quality
- Multiple CCTs (non-randomized controlled trials) with consistent results
- Phase II clinical trials with pre-specified endpoints

**Language that fits Level B:**
> "Clinical evidence suggests...", "A randomized trial demonstrated...", "Controlled studies indicate..."

**Does not qualify if:**
- The single RCT has major methodological flaws
- No blinding or inadequate allocation concealment
- Very small sample size (n < 20 per group)

---

### Level C — Limited Human Evidence

**Definition:** Human evidence exists, but from observational studies, small pilot trials, or uncontrolled studies. Suggestive but not conclusive.

**Study types that qualify:**
- Cohort studies
- Case-control studies
- Cross-sectional studies
- Uncontrolled pilot trials
- Open-label trials without control group

**Language that fits Level C:**
> "Preliminary human data suggests...", "Observational studies indicate...", "Pilot studies have shown...", "Exploratory findings suggest..."

**Does not qualify if:**
- Confounding is severe and uncorrected
- No objective outcome measure used

---

### Level D — Preclinical Evidence Only

**Definition:** Evidence comes entirely from animal models (in vivo preclinical studies). No human clinical data exists for this specific indication.

**Study types that qualify:**
- Rodent models
- Non-human primate studies
- Other animal models

**Language that fits Level D:**
> "Animal studies suggest...", "Preclinical evidence indicates...", "In rodent models...", "Results in animal models have not been confirmed in human trials."

**Critical rule:** Never use Level D findings to make human efficacy claims. Animal pharmacology does not equal clinical efficacy.

---

### Level E — Mechanistic / In Vitro Evidence Only

**Definition:** Evidence comes from cell culture, isolated enzyme systems, or molecular mechanism studies. No in vivo or human data for this specific indication.

**Study types that qualify:**
- Cell line studies
- Receptor binding assays
- Enzyme inhibition studies
- Isolated compound mechanistic studies

**Language that fits Level E:**
> "In vitro studies demonstrate...", "Cell studies show that...", "Mechanistically, the compound...", "In vitro findings have not been confirmed in animal or human studies."

**Critical rule:** Mechanism of action ≠ clinical efficacy. Many compounds with compelling in vitro data fail in human trials.

---

### Level T — Traditional Use Only

**Definition:** Historical or ethnobotanical use documented in the literature. Modern scientific evidence for the specific claimed use is absent or minimal.

**Source types that qualify:**
- Documented ethnobotanical records
- Historical pharmacopoeias
- Traditional medical system texts (Ayurveda, TCM, European folk medicine)
- EMA Traditional Herbal Registration (if applicable)

**Language that fits Level T:**
> "Traditionally used for...", "Historical use includes...", "In [culture/region], [plant] has been used for...", "Traditional use is not supported by modern clinical evidence at this time."

**Critical rule:** Traditional use is not the same as proven clinical benefit. Label it as traditional use, not efficacy.

---

### Level U — Unknown / Insufficient Evidence

**Definition:** No reliable evidence exists for the specific claimed use, or the available evidence is too heterogeneous, low-quality, or contradictory to draw any conclusion.

**When to use Level U:**
- Claimed use has been studied but results are contradictory
- Only case reports or expert opinion exist
- Evidence is present but preparation used in studies differs too much from what is available

**Language that fits Level U:**
> "Evidence is insufficient to draw conclusions.", "Available data is conflicting and no recommendation can be made.", "This use has not been adequately studied."

---

## Assignment Rules

### One plant, multiple levels

A single plant or fungus will typically have different evidence levels for different uses:

> **Withania somnifera (Ashwagandha):**
> - Stress / cortisol reduction: Level B (multiple RCTs)
> - Thyroid modulation: Level C (small studies, mixed results)
> - Anticancer properties: Level E (in vitro only)
> - Traditional tonic use: Level T

Always assign evidence level **per indication**, never as a blanket rating for the whole plant.

### Never upgrade based on mechanism

A compound mechanism (Level E) does not justify a Level D or C classification:

> ❌ WRONG: "In vitro NF-κB inhibition suggests this compound may treat inflammation in humans." → Do not write this as if it is clinical evidence.
> 
> ✓ CORRECT: "In vitro studies demonstrate NF-κB pathway inhibition [Level E]. Human anti-inflammatory efficacy has not been established."

### Never upgrade based on tradition

Traditional use (Level T) does not imply modern clinical efficacy:

> ❌ WRONG: "Used for centuries in Ayurveda to treat digestive disorders, confirming its efficacy for this indication."
> 
> ✓ CORRECT: "Traditionally used in Ayurvedic medicine for digestive complaints [Level T]. Modern clinical evidence for this indication is currently insufficient [Level U]."

### Never present animal findings as human evidence

> ❌ WRONG: "Studies show this compound reduces tumour size by 40%." (if the study was in mice)
> 
> ✓ CORRECT: "In a murine tumour model, [compound] reduced tumour size by 40% [Level D — animal study]. Clinical evidence in humans is not available."

---

## Dosage Evidence Rule

Human dosage recommendations require one of the following:
- Human clinical data specifying dose, extract type, duration, and population
- An official regulatory monograph (EMA/HMPC, ESCOP, WHO) with defined dosing
- Clearly labeled traditional dosing from a recognized pharmacopoeia

**Animal or in vitro doses must never be presented as human doses.**

If dosage has not been established in humans: "No evidence-based human dosage has been established. Traditional or pharmacopoeial dosing guidance: [source]."

---

## Safety Evidence Rule

Safety concerns can exist even when efficacy evidence is weak.

> A Level U or Level T compound can still have documented safety concerns at Level B or Level C. Evidence level for safety is assessed independently from evidence level for efficacy.

**Absence of reported adverse effects ≠ safety.** When no safety data exists, write: "Insufficient clinical safety data. Absence of reported adverse events may reflect limited study exposure, not established safety."

---

## Applying This Rubric

All content added to `data.json` must be consistent with the evidence level assigned. Use these prompts when reviewing content:

1. "Does the language strength match the evidence level?"
2. "Is human evidence being claimed from animal or in vitro data?"
3. "Is traditional use being presented as clinical efficacy?"
4. "Is the dosage claim grounded in human or regulatory data?"
5. "Is a safety concern being downplayed because efficacy evidence is weak?"

---

## Examples in Practice

**Example 1: Correct Level A statement**
> "A 2024 Cochrane systematic review of 8 RCTs (n=1,240) found that Ginkgo biloba extract EGb 761® (240 mg/day) produced statistically significant improvements in cognitive function scores compared to placebo in patients with mild-to-moderate Alzheimer's disease [1]. Evidence level: A."

**Example 2: Correct Level E statement**
> "In vitro studies in human hepatocellular carcinoma cell lines demonstrated concentration-dependent cytotoxicity of [compound], mediated through caspase-3 activation [2]. Clinical evidence for anticancer efficacy in humans is not available. Evidence level: E."

**Example 3: Correct Level T statement**
> "Valerian root (Valeriana officinalis) has been used in European folk medicine as a sleep aid since at least the 16th century [3]. Evidence level: T for this traditional use."

**Example 4: Correct mixed evidence statement**
> "Strong evidence (Level A) supports Ashwagandha for perceived stress reduction in healthy adults. Evidence for anxiolytic efficacy equivalent to prescription medications is currently Level C. Evidence for cognitive enhancement is Level C. Evidence for thyroid hormone modulation is Level C (small studies, conflicting results). Evidence for anticancer activity in humans is Level E (in vitro only)."
