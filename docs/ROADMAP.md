# BMS Archive — Roadmap

> Priority: fix scientific credibility issues before adding new content.
> Deployment-blocking issues are marked **[BLOCKING]**.

---

## Now — active priorities

| Priority | Task | Command | Status |
|---|---|---|---|
| 1 | Fix 37 unqualified "safe" warnings in data.json | `/workflow:fix-safe-claims` | ✅ Done |
| 2 | Add medical disclaimer to database.html modal view | manual | ✅ Done |
| 3 | Review thin safety fields (pregnancy/lactation across all 50 entries) | `/workflow:weekly-maintenance` | ✅ Done (6 fields improved) |

---

## Next — in progress

| Task | Command | Status | Notes |
|---|---|---|---|
| Add rate limiting to `/api/waitlist` | manual (nginx) | ✅ Done | 5 req/min per IP, burst=3, 429 on exceed |
| Add favicon | manual | ✅ Done | SVG favicon, forest green, "B" |
| Update README | manual | ✅ Done | Reflects 50 entries, full current stack |
| Add `.env.example` | manual | ✅ Done | Documents `ANTHROPIC_API_KEY` |

---

## Later — medium-term

| Task | Notes |
|---|---|
| Phase 2 — user search and filter improvements | Full-text search across monograph content |
| Evidence-level filter on database.html | Filter by A/B/C/D/E/T evidence level |
| Printable monograph PDF export | Static HTML → PDF, no server required |
| Dark mode toggle | Tailwind already supports dark: prefix |
| ESCOP monograph cross-reference links | Link from entries to official ESCOP PDFs |
| EMA/HMPC cross-reference links | Link from entries to official EMA assessment reports |
| Glossary page | Define: SR-MA, RCT, CCT, ADME, bioavailability, standardisation |
| Mushroom fruiting body vs mycelium distinction callout | Visual indicator per entry |

---

## Backlog — aspirational

| Task | Notes |
|---|---|
| Phase 3 — user accounts / bookmarking | Requires backend rework |
| API endpoint for programmatic data access | Public read-only JSON API |
| Citation manager integration (Zotero) | Export monograph references as BibTeX/RIS |
| Email newsletter content from archive data | Monthly evidence summary |
| Multilingual support | Danish or Turkish priority |
| Peer review workflow | External scientific reviewer process |
| DOI registration for data.json | Make the dataset citable |

---

## Done — completed milestones

| Milestone | Date |
|---|---|
| Phase 1 static site launched | — |
| TLS / HTTPS live on bmsarchive.com | Done |
| Email waitlist backend live | Done |
| 25 fungi monographs with PubMed-verified sources | Done |
| 25 plant monographs with cited references | Done |
| Claude Code subagent setup (8 agents) | Done |
| 12 project-level slash commands | Done |
| Python validation script (0 errors on initial run) | Done |
| Evidence scoring rubric (A–U) | Done |
| Monograph template + study extraction template | Done |
| Master workflow commands (8 workflows) | Done |
| Research inbox system | Done |
| GitHub Actions CI (JSON + validation) | Done |
| Fix 37 unqualified "safe" claims in data.json | Done |
| Fix nginx add_header inheritance (security headers now reach HTML pages) | Done |
| Content-Security-Policy header added | Done |
| og:image (1200×630) — index.html + database.html | Done |
| robots.txt + sitemap.xml | Done |
| database.html entry count: "25 profiles" → "50 profiles" | Done |
| Modal disclaimer banner in database.html | Done |
| Thin safety fields audit — 6 fields improved | Done |

---

## Known issues (not yet roadmapped)

- No rate limiting on `/api/waitlist` — low priority
