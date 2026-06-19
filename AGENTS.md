# Codex Agent Registry - BMS Archive

This repository already contains Claude-style sub-agent definitions in `.claude/agents/`.
Codex does not currently expose custom named agent registration in this workspace, but it can spawn
native `worker` and `explorer` sub-agents. When the user asks to use one of the agents below, load the
matching `.claude/agents/*.md` file and include its full instructions in the spawned Codex sub-agent prompt.

Treat `.claude/agents/` as the source of truth. Do not rewrite those files unless the user explicitly asks.

## Available Agents

| Agent | Source | Preferred Codex Role | Use for |
|---|---|---|---|
| `extraction-synthesis-agent` | `.claude/agents/extraction-synthesis-agent.md` | `worker` | Literature extraction, PubMed/Europe PMC abstracts, structured monograph evidence, dose/safety extraction |
| `scientific-qa-evidence-agent` | `.claude/agents/scientific-qa-evidence-agent.md` | `worker` | Scientific claim review, evidence hierarchy, safety text, dosage, contraindications, pharmacology |
| `security-privacy-agent` | `.claude/agents/security-privacy-agent.md` | `worker` | API routes, forms, secrets, admin exposure, deployment security, privacy risks |
| `archive-data-model-agent` | `.claude/agents/archive-data-model-agent.md` | `worker` | `data.json` schema, evidence fields, filters/facets, validation and migration planning |
| `taxonomy-nomenclature-agent` | `.claude/agents/taxonomy-nomenclature-agent.md` | `worker` | Accepted Latin names, synonyms, common-name ambiguity, duplicate species checks, plant/fungi parts |
| `project-architect-agent` | `.claude/agents/project-architect-agent.md` | `explorer` or `worker` | Feature planning, routing/project structure, architecture, admin/data pipeline design |
| `github-sync-agent` | `.claude/agents/github-sync-agent.md` | `worker` | Post-deployment git staging, commit, and push workflow |
| `qa-test-agent` | `.claude/agents/qa-test-agent.md` | `worker` | Post-change QA, data validation, browser/manual test checklist, deploy readiness |
| `ops-performance-agent` | `.claude/agents/ops-performance-agent.md` | `worker` | Docker/Nginx/Proxmox deployment, performance, SEO, production readiness |

## Invocation Pattern

When delegating to one of these agents:

1. Read the relevant `.claude/agents/<agent>.md` file.
2. Spawn a Codex sub-agent with the preferred role above.
3. Include the agent instructions and a narrow task prompt.
4. Tell the sub-agent it is not alone in the codebase and must not revert edits made by others.
5. For code-changing tasks, assign a specific ownership scope and ask it to list changed files.

Example:

```text
Spawn a worker using .claude/agents/scientific-qa-evidence-agent.md.
Task: review the updated Curcuma longa monograph claims in data.json only.
Do not edit files unless a claim is clearly unsupported; if editing, only touch data.json.
```

## Sequencing Rules

- New species: `taxonomy-nomenclature-agent` before `scientific-qa-evidence-agent`.
- Scientific content: `extraction-synthesis-agent` before `scientific-qa-evidence-agent`, then `archive-data-model-agent` if schema fit matters.
- Security-sensitive code: `security-privacy-agent` before deploy.
- Structural changes: `project-architect-agent` first, then domain-specific agents as needed.
- Deployment: `qa-test-agent`, then `ops-performance-agent`, then `github-sync-agent` only after production deployment is confirmed.

## Audit Workflows

### `weekly-bms-archive-audit`

Status: scheduled Codex automation.

Purpose: broad recurring repository audit. This should not edit files. It should report scientific,
security, architecture, code-quality, deployment, performance, SEO, and QA risks with file paths and
line numbers where possible.

### `pre-deploy-audit`

Status: on-demand workflow. Run when the user says "run pre-deploy audit", "pre deploy check",
"before deploy", or similar.

Purpose: block unsafe production deploys before files are pushed to the Proxmox/LXC/Docker stack.

Agent sequence:

1. `qa-test-agent` - inspect git status, validate JSON, run available local checks, and identify
   untested areas.
2. `security-privacy-agent` - review secrets, admin exposure, API/form handling, nginx security
   headers, and deploy file exclusions.
3. `ops-performance-agent` - review Docker/Nginx/deploy commands, cache headers, SEO assets,
   production readiness, and performance risks.
4. `project-architect-agent` - only if the pending change modifies routes, data flow, schema,
   deployment shape, or project structure.
5. `scientific-qa-evidence-agent` - only if `data.json` or user-facing scientific copy changed.

Minimum checks to run locally when relevant:

```bash
git status --short
python3 -c "import json; data=json.load(open('data.json')); print(f'Valid JSON - {len(data)} entries')"
rg -n "sk-ant-|ANTHROPIC_API_KEY=|API_KEY=|SECRET=|PRIVATE KEY|password" .
rg -n "admin.html|admin_server.py|build_plants.py|plants_progress.json" Dockerfile docker-compose.yml nginx.conf
```

Output format:

```text
PRE-DEPLOY AUDIT RESULT: PASS / BLOCKED
Critical blockers:
High-priority issues:
Checks run:
Checks not run:
Files safe to deploy:
Files that must not be deployed:
Recommended next actions:
```

Do not claim production is safe unless the relevant checks actually ran. Do not deploy unless the
user explicitly asks.

### `monograph-specific-audit`

Status: on-demand workflow. Run when the user adds, edits, imports, or reviews a specific plant or
fungus monograph.

Purpose: catch scientific, citation, taxonomy, and schema problems before a monograph becomes public.

Agent sequence:

1. `taxonomy-nomenclature-agent` - confirm accepted Latin name, common-name ambiguity, duplicate
   entries, type value, and used part/preparation specificity.
2. `extraction-synthesis-agent` - inspect supplied sources or source fields and extract what the
   studies actually support.
3. `scientific-qa-evidence-agent` - review claims, evidence hierarchy, safety, dosage, interactions,
   contraindications, and overclaiming.
4. `archive-data-model-agent` - confirm the final content fits `data.json` and renderer expectations.
5. `qa-test-agent` - validate JSON and check the entry renders in `database.html` if files changed.

Minimum checks to run locally when relevant:

```bash
python3 -c "import json; data=json.load(open('data.json')); print(f'Valid JSON - {len(data)} entries')"
python3 -c "import json; data=json.load(open('data.json')); print([d.get('scientific_name') for d in data if not d.get('sources', {}).get('top_studies_urls')])"
```

Output format:

```text
MONOGRAPH AUDIT RESULT: APPROVE / REVISE / REJECT
Entry reviewed:
Taxonomy findings:
Citation/source findings:
Scientific claim findings:
Schema/rendering findings:
Required revisions:
Optional improvements:
Checks run:
Checks not run:
```

Do not invent citations, PMIDs, DOIs, dosage ranges, safety claims, or taxonomy. If live source
verification is required and network access is unavailable, mark the relevant claim unverifiable.
