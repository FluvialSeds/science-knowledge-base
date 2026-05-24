---
tags:
  - "project"
topics:
  - "[[LLMWiki]]"
status: stable
created: 2026-05-24
updated: 2026-05-24
sources:
  - "Raw/Sources/LLMWikiStarterDemo.md"
source_count: 1
aliases:
  - "Wiki initialization"
---

# LLM Wiki Setup

Establishing a functional [[LLMWiki]] system with documented rules, templates, tools, and initial content.

## Objectives

- Create clean folder structure separating Raw sources and Wiki knowledge
- Define schema for note types and frontmatter
- Build deterministic tools for building, querying, and validating the Wiki
- Establish ingest workflow for processing new sources
- Document naming conventions and maintenance procedures

## Architecture

### Folders

- `Raw/Sources/`: Raw source material (read-only except for format cleanup)
- `Wiki/Topics/`, `Wiki/Concepts/`, `Wiki/Entities/`, `Wiki/Projects/`, `Wiki/Logs/`: Compiled knowledge organized by type
- `Schema/`: Rules and metadata about the Wiki
- `_templates/`: Note templates for consistency
- `.claude/skills/`: Reusable agent workflows

### Tools

- `scripts/wiki_tool.py`: Core tool for building catalog, validating notes, searching knowledge
- `scripts/audit_public.py`: Security audit for secrets and local paths
- `.githooks/pre-commit`: Automatic validation before commits

## Key Principles

1. **Separation of concerns**: Raw sources and Wiki knowledge are distinct
2. **Traceability**: Every Wiki claim links to a Raw source
3. **Determinism**: Tools produce consistent, idempotent results
4. **Validation**: All changes checked by automated gates before commits

## Status

Core system initialized with demo source and initial compiled notes. Ready for user sources.
