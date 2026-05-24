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
| `Author` | string | Yes | Original source author(s) |
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
| `updated` | date | Yes | Date the note was last updated (YYYY-MM-DD) |
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
