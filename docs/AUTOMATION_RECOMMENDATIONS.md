# BMS Archive — Automation Recommendations

This document describes what is safe to automate, what requires human review, and what must never be automated.

---

## Level 1 — Automate now (safe, low risk, already partially done)

These are either already automated or trivially safe to add.

| What | How | Status |
|---|---|---|
| JSON syntax check on every commit/PR | GitHub Actions CI (`.github/workflows/ci.yml`) | Done |
| Validation script on every commit/PR | GitHub Actions CI | Done |
| Secret detection in committed files | GitHub Actions CI (grep for `sk-ant-`) | Done |
| Admin tools exclusion check in CI | GitHub Actions CI | Done |

---

## Level 2 — Automate with care (medium risk, requires review)

These are safe if the output is reviewed before action is taken. Automate the detection, not the fix.

| What | Recommended approach | Caution |
|---|---|---|
| Weekly health report | Schedule `/workflow:weekly-maintenance` and review output | Read-only — do not automate fixes from this output |
| Research inbox status | Add to weekly maintenance output | The inbox is a staging area; auto-promotion would bypass QA |
| Citation URL reachability check | Script to test each URL in `top_studies_urls` returns HTTP 200 | PMIDs are stable; this detects link rot, not citation errors |
| `og:image` and SEO field presence check | Add to CI alongside JSON check | Non-blocking; report but do not fail CI |
| Thin field detection | Add Python check (fields < 50 chars) to CI as a warning | Non-blocking warning only |

---

## Level 3 — Automate with explicit approval step (high risk)

These should produce a plan/report that a human reviews before executing.

| What | Recommended approach | Why approval is needed |
|---|---|---|
| Deploy to production | `/workflow:pre-deploy` produces commands; human runs them | A failed deploy can take the site offline |
| Batch monograph updates | Run workflow per entry, review before committing | Automated changes to scientific content require scientific review |
| Safe-claim replacement | `/workflow:fix-safe-claims` proposes replacements; human reviews | Medical language changes have scientific credibility implications |
| New monograph creation from inbox | `/workflow:research-inbox` stages; `/workflow:new-monograph` creates; human reviews and promotes | New content requires full scientific QA before publishing |

---

## Never automate — hard limits

These must always involve human review and decision-making. Automating them would undermine the scientific credibility and safety of the archive.

| What | Why |
|---|---|
| Evidence level assignment | Requires scientific judgement about study quality; cannot be reliably inferred from text |
| Safety claim approval | Medical safety language has direct patient safety implications |
| Citation creation | Fabricated citations are fraud; only a human can confirm a PMID exists and matches the claim |
| Taxonomy change | An incorrect accepted binomial poisons all evidence claims for that entry |
| Publishing new monographs without scientific QA | Would circumvent the evidence-gating that gives the archive its credibility |
| Running `docker compose up --build` automatically | A misconfigured deploy can take the production site offline |
| Committing data.json changes from an automated agent | All data changes must be git-committed by a human who has reviewed the diff |
| Sending emails to the waitlist | Requires editorial review of content |

---

## CI pipeline philosophy

The current CI is intentionally minimal:
- JSON syntax — fast, blocks broken data from reaching main
- Validation script — catches scientific quality issues automatically
- Secret detection — blocks accidental key exposure
- Admin tools check — blocks a specific class of security mistake

**Do not add npm, lint, or build steps** unless the tech stack changes to require them (it currently does not). Adding commands that don't exist produces CI failures that mislead reviewers.

**Do not add browser/E2E tests** to CI unless a headless browser service is added to the workflow. Currently, browser QA is manual.

---

## Automation maturity model for BMS Archive

```
Current state (Phase 1):
  CI ──── validates data.json and validation script
  Humans ─ run all workflows, review all output, commit all changes

Phase 2 goal:
  CI ──── + citation reachability check, SEO field presence
  Humans ─ review weekly maintenance report, approve all changes

Phase 3 potential:
  Scheduled CI ── weekly maintenance report (read-only)
  Humans ──────── still approve all content and deploy changes
```

---

## The non-negotiable rule

> **Scientific content must never be modified by an automated process without human review of the diff.**

The archive's value is its scientific credibility. Any automated process that modifies monograph content — even to fix a formatting issue — must show the human what changed before it is committed.
