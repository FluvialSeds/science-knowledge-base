---
Title: LLM Wiki Starter Demo Source
Author: LLM Wiki Starter
Reference: owned-demo
ContentType:
  - markdown
Created: 2026-05-24
Processed: false
tags:
  - source
---

# LLM Wiki Starter Demo Source

An LLM Wiki separates captured source material from compiled knowledge notes. Raw sources preserve original context, while Wiki notes turn useful claims into short, linked, reusable knowledge. The most useful workflow is to search the compiled Wiki first, then open Raw sources only when more evidence or detail is needed.

## Key Principles

The core workflow divides work into two layers:

1. **Raw/Sources/**: Original material with full context and citations. This layer is never edited except for formatting cleanup.
2. **Wiki/**: Compiled knowledge extracted from sources. Notes are focused, reusable, and always traceable back to sources.

This separation allows:
- **Source preservation**: Original context never lost
- **Knowledge reuse**: Compiled notes are concise and linkable
- **Traceability**: Every claim in Wiki notes points back to Raw sources
- **Scalability**: One source can feed multiple Wiki notes; multiple sources can support a single note

## Workflow Example

When you find a new article or paper:

1. Add cleaned Markdown to `Raw/Sources/`
2. Search `Wiki/catalog.jsonl` for related compiled notes
3. Create or update focused notes in `Wiki/Topics/`, `Wiki/Concepts/`, etc.
4. Link each Wiki note back to the Raw source in its `sources` field
5. Run maintenance checks: `build`, `lint`, `source-lint`
6. Commit with a message describing what changed

Compiled notes reference sources—not the other way around. This preserves the raw source as read-only reference material.

## Why This Matters

Without this separation, source material gets mixed with processed knowledge, making it hard to:
- Trust claims (no clear source trail)
- Reuse knowledge (everything is in context of the original source)
- Update information (can't distinguish original from interpretation)

With separation:
- Trust is explicit: every claim links to a source
- Knowledge is modular: notes are focused and reusable
- Updates are clear: change compiled notes or sources independently
