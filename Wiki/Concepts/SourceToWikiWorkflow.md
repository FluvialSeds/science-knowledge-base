---
tags:
  - "concept"
topics:
  - "[[LLMWiki]]"
status: stable
created: 2026-05-24
updated: 2026-05-24
sources:
  - "Raw/Sources/LLMWikiStarterDemo.md"
source_count: 1
aliases:
  - "Ingest workflow"
  - "Source processing"
---

# Source to Wiki Workflow

The process of converting raw source material into compiled Wiki notes while maintaining traceability.

## Steps

1. **Add source**: Place cleaned Markdown in `Raw/Sources/` with required frontmatter (Title, Author, Reference, Created, Processed)
2. **Search catalog**: Look for existing Wiki notes on related topics using `search-catalog --query "topic"`
3. **Create or update notes**: Write focused notes in `Wiki/Topics/`, `Wiki/Concepts/`, `Wiki/Entities/`, `Wiki/Projects/`
4. **Link sources**: Add the Raw source path to each compiled note's `sources` field
5. **Validate**: Run `build`, `lint`, `source-lint` before committing
6. **Commit**: Push changes with a message describing what was added or updated

## Key Principle

One Raw source can feed multiple Wiki notes (different aspects of the same material). Multiple Raw sources can support a single Wiki note (many sources contributing to one compiled piece).

The `sources` field in each compiled note records exactly which Raw sources contributed to it. This maintains a clear audit trail.
