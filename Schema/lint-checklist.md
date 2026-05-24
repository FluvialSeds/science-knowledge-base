# Lint Checklist

Deterministic checks that must pass before commits.

## Compiled Wiki Notes

### Frontmatter Validation

- [ ] All notes have one and only one tag from: `topic`, `concept`, `entity`, `project`, `log`
- [ ] `created` and `updated` dates are in YYYY-MM-DD format
- [ ] `sources` field is a list (empty list `[]` is allowed for initial seed notes only)
- [ ] `source_count` exists and equals the length of `sources` list
- [ ] All source paths in `sources` exist and are under `Raw/Sources/`

### Content Validation

- [ ] No external links or citations without corresponding entries in `sources`
- [ ] Wikilinks (e.g., `[[Note Name]]`) point to existing files in the vault
- [ ] No unsupported claims (all factual statements traceable to sources)
- [ ] Note title matches the filename (or is listed in `aliases`)

### Structure Validation

- [ ] Every note has a title (heading or frontmatter)
- [ ] Notes are focused and reusable (not lists of unrelated facts)

## Raw Source Notes

### Frontmatter Validation

- [ ] `Title` is present and non-empty
- [ ] `Author` is present and non-empty
- [ ] `Reference` is present and non-empty
- [ ] `ContentType` is a non-empty list
- [ ] `Created` is in YYYY-MM-DD format
- [ ] `Processed` is a boolean (true or false)
- [ ] `tags` list includes `"source"`

### Source Coverage Validation

- [ ] **MANDATORY**: If a source has been compiled into Wiki notes, `Processed` MUST be set to `true`
- [ ] If `Processed: true`, at least one Wiki note includes this source in its `sources` field
- [ ] If `Processed: false`, no Wiki notes should reference it yet
- [ ] If `Processed: true` but no Wiki coverage exists, source-lint will fail (fix by creating Wiki notes or setting `Processed: false`)

## Catalog Validation

- [ ] `Wiki/catalog.jsonl` exists
- [ ] Each line is valid JSON
- [ ] Every compiled Wiki note has a corresponding catalog entry
- [ ] Catalog entries include: `path`, `title`, `tag`, `topics`, `sources`, `updated`
- [ ] All referenced sources in catalog exist

## Source Manifest Validation

- [ ] `Schema/source-manifest.jsonl` exists
- [ ] Each line is valid JSON
- [ ] Every Raw source has a corresponding manifest entry
- [ ] Manifest entries include: `path`, `title`, `processed`, `covered_by`, `updated`
- [ ] `covered_by` matches actual Wiki coverage

## Index Files

- [ ] `Wiki/index.md` exists
- [ ] Per-folder index files exist:
  - [ ] `Wiki/Topics/index.md`
  - [ ] `Wiki/Concepts/index.md`
  - [ ] `Wiki/Entities/index.md`
  - [ ] `Wiki/Projects/index.md`
  - [ ] `Wiki/Logs/index.md`
- [ ] Indexes list all notes in their folders with brief descriptions
- [ ] Index links are valid wikilinks

## Pre-Commit Checks

Run before every commit:

```bash
python3 scripts/wiki_tool.py doctor
python3 scripts/wiki_tool.py build
python3 scripts/wiki_tool.py lint
python3 scripts/wiki_tool.py source-lint
python3 scripts/audit_public.py
```

All checks must pass (exit code 0).
