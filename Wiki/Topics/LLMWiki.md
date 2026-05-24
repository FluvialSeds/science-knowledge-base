---
tags:
  - "topic"
topics: []
status: stable
created: 2026-05-24
updated: 2026-05-24
sources:
  - "Raw/Sources/LLMWikiStarterDemo.md"
source_count: 1
aliases:
  - "Knowledge Base"
  - "Wiki System"
---

# LLM Wiki

A knowledge base system that separates raw source material from compiled, reusable knowledge notes.

## Core Structure

- **Raw/Sources/**: Original source material (articles, papers, notes) preserved with full context
- **Wiki/**: Compiled knowledge organized by type (Topics, Concepts, Entities, Projects, Logs)

## Key Principle

Maintain traceability: every fact in a Wiki note links back to the Raw source that supports it. This ensures trust, enables verification, and prevents unsupported claims.

## Workflow

1. Add sources to `Raw/Sources/`
2. Search catalog for related compiled notes
3. Create or update Wiki notes with focused knowledge
4. Link Wiki notes back to Raw sources via `sources` field
5. Run maintenance checks before commits

## Benefits

- **Source preservation**: Original context never lost
- **Knowledge reuse**: Compiled notes are concise and linkable
- **Traceability**: Every claim points to a source
- **Modularity**: One source feeds multiple notes; multiple sources support one note
