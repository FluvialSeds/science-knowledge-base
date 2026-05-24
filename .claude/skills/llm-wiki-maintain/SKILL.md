# LLM Wiki Maintain Skill

Perform periodic maintenance and health checks on the Wiki.

## When to Use

- Before significant commits
- Weekly or after multiple source ingestions
- When checking overall Wiki state
- User asks for a maintenance report

## Maintenance Gate

Run this before every meaningful commit:

```bash
python3 scripts/wiki_tool.py doctor
python3 scripts/wiki_tool.py build
python3 scripts/wiki_tool.py lint
python3 scripts/wiki_tool.py source-lint
python3 scripts/audit_public.py
```

After source ingestion, also run:

```bash
python3 scripts/wiki_tool.py source-scan --update --accept-covered
python3 scripts/wiki_tool.py source-lint
```

All checks must pass (exit code 0).

## What Each Check Does

| Command | Purpose |
|---------|---------|
| `doctor` | Non-mutating health check: folders, Python version, basic counts |
| `build` | Generate catalog and index files |
| `lint` | Validate compiled note frontmatter, tags, and source links |
| `source-lint` | Validate Raw source metadata and coverage |
| `source-scan` | List Raw sources and update manifest |
| `audit_public.py` | Check for secrets, local paths, private keys |

## Status Report

After running maintenance, you can check:

- Number of Raw sources: `ls -1 Raw/Sources/ | wc -l`
- Number of compiled notes: `find Wiki -name "*.md" -type f | grep -v index | wc -l`
- Catalog entries: `wc -l < Wiki/catalog.jsonl`
- Source manifest entries: `wc -l < Schema/source-manifest.jsonl`

## Guidelines

- Maintenance is deterministic and idempotent
- Running checks multiple times produces the same results
- All checks must pass before commits
- Fixes are made by hand; tools only validate

## Output

- Pass/fail status for each check
- Optionally: a maintenance report with counts and status
