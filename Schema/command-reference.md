# Command Reference

All `wiki_tool.py` commands use Python standard library only.

## doctor

Non-mutating health check for folders, Python version, catalog, source manifest, and basic note counts.

```bash
python3 scripts/wiki_tool.py doctor
```

Output: vault health status and counts.

## build

Generate `Wiki/catalog.jsonl`, `Wiki/index.md`, and per-folder index files.

```bash
python3 scripts/wiki_tool.py build
```

Output:
- `Wiki/catalog.jsonl`: JSONL catalog of all compiled notes
- `Wiki/index.md`: Main index
- `Wiki/Topics/index.md`, `Wiki/Concepts/index.md`, etc.: Per-folder indexes

## lint

Validate compiled Wiki note frontmatter, allowed tags, source links, and `source_count`.

```bash
python3 scripts/wiki_tool.py lint
```

Checks:
- Every note has one allowed tag: `topic`, `concept`, `entity`, `project`, `log`
- `source_count` equals the length of `sources`
- All source paths exist under `Raw/Sources/`

Exit code: 0 if all notes valid, 1 if errors found.

## source-scan

List Raw sources and optionally update `Schema/source-manifest.jsonl`.

```bash
python3 scripts/wiki_tool.py source-scan
```

Update the manifest after sources are processed:

```bash
python3 scripts/wiki_tool.py source-scan --update --accept-covered
```

With `--accept-covered`, automatically sets `covered_by` based on current Wiki coverage.

## source-lint

Validate source frontmatter and source coverage state.

```bash
python3 scripts/wiki_tool.py source-lint
```

Checks:
- All Raw sources have required frontmatter: `Title`, `Author`, `Reference`, `Created`, `Processed`, `tags`
- If `Processed: true`, the source must be covered by at least one Wiki note

Exit code: 0 if all sources valid, 1 if errors found.

## source-delta

Show Raw sources not represented in the manifest.

```bash
python3 scripts/wiki_tool.py source-delta
```

Useful for identifying sources that haven't been added to the manifest yet.

## source-coverage

Show which Raw sources are covered by compiled Wiki notes.

```bash
python3 scripts/wiki_tool.py source-coverage
```

Output: mapping of sources to the Wiki notes that cite them.

## search-catalog

Search compiled Wiki notes through the catalog.

```bash
python3 scripts/wiki_tool.py search-catalog --query "text"
```

Searches note titles and tags. Requires `Wiki/catalog.jsonl` (run `build` first).

## log

Append a short entry to `Wiki/Logs/index.md`.

```bash
python3 scripts/wiki_tool.py log --title "title" --details "details"
```

Creates the file if it doesn't exist.

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
