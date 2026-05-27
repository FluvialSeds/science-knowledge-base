# Lint Protocol: Source Metadata-to-Wikilink Verification

## Purpose
Ensure that all sources listed in a concept note's YAML frontmatter `sources` field are referenced as wikilinks in the "See also" section.

## Requirement
**Every source file listed in the `sources:` metadata must appear as a wikilink in the "See also" section** using the format:
- `- Source paper: [[SourceFileName]] — Brief description` (if single source)
- OR as part of consolidated source list: `- Source papers: [[Source1]] — desc; [[Source2]] — desc; [[Source3]] — desc`

## Format Standard
Consolidated source papers bullet should list ALL sources in metadata as a single bullet point with wikilinks separated by semicolons.

**Good:**
```yaml
- Source papers: [[Eglinton-2021pnas]] — Climate controls on fluvial biomarker ages; [[Bolandini-2025rad]] — Online ORO-AMS; [[Hemingway-2025tog]] — MIF processes
```

**Bad:**
```yaml
- Source paper: [[Eglinton-2021pnas]] — Climate controls
- Source paper: [[Bolandini-2025rad]] — Online ORO-AMS
```
(Multiple separate source paper bullets are confusing and violate DRY principle)

## Verification Steps

1. **Extract metadata sources:** Get the list from `sources:` in YAML frontmatter
2. **Find "See also" section:** Locate the ## See also section at end of note
3. **Check wikilinks:** Verify each source file appears as `[[FileName]]` somewhere in See also
4. **Verify uniqueness:** No duplicate concept links (except different descriptions permitted)
5. **Consolidation rule:** If multiple sources exist, use SINGLE "Source papers:" bullet (not multiple bullets)

## Automated Check Command

```bash
python3 scripts/lint-sources.py Wiki/Concepts/*.md
```

(To be implemented: Python script that validates source metadata against See also wikilinks)

## Example Validation

**Metadata:**
```yaml
sources:
  - "Raw/Sources/Hemingway-2017cg.md"
  - "Raw/Sources/Hemingway-2017rad.md"
  - "Raw/Sources/Hemingway-2019nat.md"
  - "Raw/Sources/Hemingway-2021og.md"
  - "Raw/Sources/Drake-2026natgeo.md"
  - "Raw/Sources/Eglinton-2021pnas.md"
  - "Raw/Sources/Bolandini-2025rad.md"
source_count: 7
```

**Valid See also:**
```markdown
- Source papers: [[Hemingway-2017cg]] — Radiocarbon in Congo POM; [[Hemingway-2017rad]] — Analytical methods; [[Hemingway-2019nat]] — Mineral protection; [[Hemingway-2021og]] — Biosynthetic fractionation; [[Drake-2026natgeo]] — Millennially-aged carbon; [[Eglinton-2021pnas]] — Climate controls; [[Bolandini-2025rad]] — Online ORO-AMS
```

**Invalid (duplicates):**
```markdown
- Source papers: [[Hemingway-2017cg]] — ...
- [[Hemingway-2017rad]] — ...  (separate bullet—improper formatting)
```

## Enforcement
Run lint before every commit:
```bash
python3 scripts/wiki_tool.py lint
python3 scripts/lint-sources.py Wiki/Concepts/*.md  # (when implemented)
```
