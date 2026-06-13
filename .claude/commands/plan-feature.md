---
description: Plan a new BMS Archive feature before writing any code. Produces an implementation plan, identifies affected files, defines acceptance criteria, and assigns the correct agents.
---

You are planning a new feature for BMS Archive: **$ARGUMENTS**

BMS Archive is a plain HTML5 + Tailwind CSS + vanilla JS scientific phytomedicine archive. There is no framework, no build step, and no npm. Data lives in `data.json`. Deployment is Docker Compose on Proxmox/LXC. Do not introduce a framework or build tooling unless explicitly requested.

## Step 1 — Read before planning

Read these files before proposing anything:
- `CLAUDE.md` — project conventions and rules
- `README.md` — current architecture overview
- Any files directly relevant to the requested feature (pages, API routes, data schema, config)

## Step 2 — Use project-architect-agent

Delegate architecture planning to the `project-architect-agent`. Ask it to:
- Describe the current state of the relevant code
- Propose the minimal implementation that achieves the goal
- Identify all files that will be created or modified
- Identify risks and trade-offs
- Confirm whether the change fits the current project stage (Phase 1 static site) or requires Phase 2 infrastructure

## Step 3 — Identify required agents

Based on what the feature touches, determine which additional agents are needed:

| Feature area | Agent |
|---|---|
| New plant/fungus data or health claims | `scientific-qa-evidence-agent` |
| Species names, plant parts, taxonomy | `taxonomy-nomenclature-agent` |
| `data.json` schema or new fields | `archive-data-model-agent` |
| New API route, form, user input, auth | `security-privacy-agent` |
| Deployment, SEO, performance, Nginx | `ops-performance-agent` |
| Final quality gate | `qa-test-agent` |

## Step 4 — Produce the plan

Output a structured plan with exactly these sections:

```
## Feature Plan: [feature name]

### Current state
[What exists today — based on files read, not assumptions]

### Proposed change
[What will be built — minimal viable implementation]

### Files to create
- [path] — [what it is]

### Files to modify
- [path] — [what changes]

### Acceptance criteria
- [ ] [specific, testable criterion]
- [ ] [specific, testable criterion]

### Agents required
- [agent name] — [why]

### Risks
- [risk] — [mitigation]

### Out of scope
- [what this change deliberately does not include]
```

## Rules

- Do not start coding until the plan is reviewed and approved
- Do not introduce npm, React, Vue, TypeScript, or a bundler without explicit approval
- Do not add Instagram, social media, or content creation logic
- If the feature touches scientific claims, mark `scientific-qa-evidence-agent` as required
- If the feature touches API routes or forms, mark `security-privacy-agent` as required
- Prefer the simplest solution that works at the current project stage
