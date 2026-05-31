# Frontmatter Schema

This document defines the required and optional frontmatter fields for Raw sources and compiled Wiki notes.

## Raw Source Notes

Raw source notes preserve original source metadata and processing state.

```yaml
---
Title: "Source Title"
Author: "Author Name"
Reference: "url-or-identifier"
ContentType:
  - "markdown"
Created: YYYY-MM-DD
Processed: false
tags:
  - "source"
---
```

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `Title` | string | Yes | Original source title |
| `Author` | string | Yes | Original source author(s) — use format: "FirstName MiddleInitial. LastName, FirstName MiddleInitial. LastName, ..." |
| `Reference` | string | Yes | URL, DOI, ISBN, or other permanent identifier |
| `ContentType` | list | Yes | Content types: `markdown`, `pdf`, `video`, `article`, etc. |
| `Created` | date | Yes | Original publication or creation date (YYYY-MM-DD) |
| `Processed` | boolean | Yes | Whether this source has been compiled into Wiki notes |
| `tags` | list | Yes | Must include `source` tag |

## Compiled Wiki Notes

Compiled notes are curated, focused knowledge extracted from Raw sources.

```yaml
---
tags:
  - "concept"
topics: []
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - "Raw/Sources/example.md"
source_count: 1
aliases: []
---
```

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `tags` | list | Yes | One of: `topic`, `concept`, `entity`, `project`, `log` |
| `topics` | list | No | Related topic links (wikilinks to topic notes) |
| `status` | string | No | Status: `seed`, `draft`, `stable`, `archived` |
| `created` | date | Yes | Date the note was created (YYYY-MM-DD) |
| `updated` | date | Yes | **CRITICAL: Date the note was last updated (YYYY-MM-DD). MUST be updated for ANY edit—new content, See also changes, wikilink additions, or any other modification.** This field maintains accurate change tracking and audit trails. |
| `sources` | list | Yes | List of Raw source paths that support this note |
| `source_count` | integer | Yes | Must equal the length of `sources` (for lint validation) |
| `aliases` | list | No | Alternative names for this note (used by Obsidian link suggestions) |

### Tag Values

- `topic`: High-level topic or domain (e.g., "Machine Learning")
- `concept`: Detailed concept or technique (e.g., "Backpropagation")
- `entity`: Person, organization, product, or place
- `project`: Project, initiative, or research effort
- `log`: Chronological entry or event

### Status Values

- `seed`: Minimal note, only definition or key facts
- `draft`: In progress, may have incomplete sections
- `stable`: Complete and validated against sources
- `archived`: No longer actively maintained; kept for historical reference

## See Also Section Format

**MANDATORY REQUIREMENTS:**

1. **Only ONE "See also" section per concept note** — Do not create multiple See also sections or duplicate them
2. **No repeated wikilinks** — Each concept should appear in the See also section exactly once
3. **Source papers in single bullet point** — All sources listed in ONE bullet point only, separated by COMMAS (not semicolons):
   ```markdown
   - Source papers: [[Paper1]] — Description, [[Paper2]] — Description, [[Paper3]] — Description
   ```
4. **Proper format for concept wikilinks:**
   ```markdown
   ## See also

   - [[RelatedConcept1]] — Description of relationship
   - [[RelatedConcept2]] — Description of relationship
   - [[RelatedConcept3]] — Description of relationship
   - Source papers: [[Source1]] — Citation info, [[Source2]] — Citation info, [[Source3]] — Citation info
   ```

**Example (CORRECT):**
```markdown
## See also

- [[AquaticCO2EvasionFlux]] — CO₂ production from DOM respiration
- [[DissolvedOrganicMatter]] — DOM bioavailability and composition
- [[RadiocarbonOrganicMatter]] — Radiocarbon age determination
- Source papers: [[Smith-2020nat]] — Young carbon effects, [[Jones-2021bgc]] — DOM cycling, [[Brown-2019jgr]] — Evasion mechanisms
```

**Example (INCORRECT - Do NOT use these patterns):**
```markdown
## See also
- [[AquaticCO2EvasionFlux]] — CO₂ production
- [[RadiocarbonOrganicMatter]] — Radiocarbon (DUPLICATE)
- Source papers: [[Smith-2020nat]] — Young carbon effects; [[Jones-2021bgc]] — DOM cycling (SEMICOLON)
- Source papers: [[Other-2018jgr]] — Other effects (DUPLICATE BULLET)
```
