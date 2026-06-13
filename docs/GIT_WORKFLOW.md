# BMS Archive — Git Workflow Guide

Simple, practical git conventions for BMS Archive development.

---

## Principles

1. **Inspect before you change** — always run `git status` and review what is staged
2. **Small commits** — one logical change per commit
3. **Run checks before committing** — validate data.json, check for regressions
4. **Never commit secrets** — the `ANTHROPIC_API_KEY` stays in the shell only
5. **Review the diff** — run `git diff` before staging to confirm what changes

---

## Standard Workflow

```bash
# 1. Check current state before starting work
git status
git log --oneline -10

# 2. Create a branch for significant changes
git checkout -b [type]/[short-description]
# Examples:
#   git checkout -b feature/add-category-filters
#   git checkout -b monograph/hypericum-perforatum
#   git checkout -b fix/json-validation-error
#   git checkout -b ops/update-nginx-config

# 3. Make your changes (use Claude Code commands for scientific workflows)

# 4. Run validation before staging
python3 scripts/validate_archive_data.py       # always for data.json changes
# Open index.html and database.html in browser for UI changes
# Run API smoke test for server.js changes

# 5. Review what changed
git diff
git diff --staged

# 6. Stage specific files (not git add -A to avoid staging accidental files)
git add data.json                              # for data changes
git add index.html database.html               # for UI changes
git add nginx.conf docker-compose.yml          # for config changes

# 7. Commit
git commit -m "[type]: [short description]"

# 8. Push and create PR if working on a branch
git push origin [branch-name]
```

---

## Branch Naming Conventions

| Prefix | Use for | Example |
|---|---|---|
| `feature/` | New website features | `feature/search-by-compound` |
| `monograph/` | Adding or updating monographs | `monograph/hypericum-perforatum` |
| `fix/` | Bug fixes or corrections | `fix/json-validation-error` |
| `ops/` | Deployment, Docker, Nginx changes | `ops/add-certbot-renewal` |
| `docs/` | Documentation changes | `docs/update-readme` |
| `data/` | data.json updates (bulk, scripts) | `data/refresh-pubmed-sources` |

---

## Commit Message Conventions

```
[type]: [short imperative description]
```

| Type | Use for |
|---|---|
| `feat` | New website feature |
| `monograph` | Add or update a monograph entry |
| `fix` | Bug fix or data correction |
| `ops` | Deployment or infrastructure change |
| `docs` | Documentation only |
| `data` | data.json update (not a new monograph) |
| `style` | Visual/CSS change, no logic change |
| `refactor` | Code reorganization, no behavior change |

**Good examples:**
```
monograph: Add Hypericum perforatum (St. John's Wort) profile
feat: Add primary category filter chips to database page
fix: Correct Ganoderma lucidum drug_interactions field — was empty
ops: Add HTTP/2 to nginx.conf
data: Refresh PubMed article counts for all 50 entries
docs: Add evidence scoring rubric
```

**Avoid:**
```
update stuff
fix
changed things
wip
```

---

## Pre-Commit Checklist

Run through this before every commit:

- [ ] `git status` — only the intended files are staged
- [ ] `git diff --staged` — reviewed all changes; nothing unexpected
- [ ] No `.env` file staged
- [ ] `ANTHROPIC_API_KEY` not in any staged file
- [ ] `admin.html` and `admin_server.py` staging is intentional (they are committed but not deployed)
- [ ] data.json changes: `python3 scripts/validate_archive_data.py` passed
- [ ] UI changes: browser check passed (grid renders, modal opens, form works)
- [ ] No unrelated files accidentally staged

---

## Pre-Deploy Checklist

Before deploying to production, additionally verify:

- [ ] `git log --oneline -5` — recent commits match what is being deployed
- [ ] `admin.html` and `admin_server.py` are NOT in the deploy file list (see `CLAUDE.md` deploy workflow)
- [ ] `/project:security-review` passed
- [ ] `/project:validate-data` passed
- [ ] `/project:prepare-deploy` ran — deploy commands reviewed

---

## Files That Must Never Be Committed With Secrets

| File / pattern | Risk | Prevention |
|---|---|---|
| `.env` | API keys, DB credentials | Add to `.gitignore` |
| `plants_progress.json` | May contain API responses | Add to `.gitignore` or delete after use |
| Any file with `sk-ant-` | Anthropic API key | Never write to a file |
| `waitlist.txt` | User emails | Lives in Docker volume, never in repo |

**Recommended `.gitignore` additions:**
```gitignore
.env
.env.*
plants_progress.json
*.pyc
__pycache__/
.DS_Store
```

---

## Undoing Mistakes (Safe Operations Only)

```bash
# Unstage a file before commit (safe)
git restore --staged [filename]

# Discard local changes to a file (safe — only if not yet committed)
git restore [filename]

# View what a commit changed (safe, read-only)
git show [commit-hash]

# Compare current state with a previous commit (safe)
git diff [commit-hash] HEAD
```

**Do not run without understanding the impact:**
- `git reset --hard` — discards local changes permanently
- `git push --force` — overwrites remote history
- `git checkout .` — discards all local changes

When in doubt, ask before running destructive git commands.

---

## Working with data.json

`data.json` is the entire database. It deserves extra care.

```bash
# Always validate before committing
python3 scripts/validate_archive_data.py

# If you're making many changes, commit after each logical group
# Don't batch 50 entry changes into one commit if avoidable

# If something goes wrong, check git history
git log --oneline data.json
git show [commit-hash]:data.json > data_backup.json

# Compare current with a previous version
git diff [commit-hash] data.json
```

---

## Deployment Is Separate From Git

The deploy process (SSH → scp → pct push → docker compose up) is documented in `CLAUDE.md`.

Git push to `main` does **not** automatically deploy. Deployment is always a manual step using `/project:prepare-deploy`.
