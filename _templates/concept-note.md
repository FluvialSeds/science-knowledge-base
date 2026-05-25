---
tags:
  - "concept"
topics: []
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
source_count: 0
aliases: []
---

# Concept Name

## Core Concept

2-3 sentence summary of the core concept. Include first mentions of related concepts using pipe syntax for natural reading: `[[RelatedConcept|related concept text]]`. The tool will auto-generate wikilinks for first mentions when you run `suggest-links`.

## Additional body sections

Relevant sections, each containing text and/or bullet points. Use pipe syntax for related concept mentions: `[[ConceptName|display text]]` so the text reads naturally.

## See also

Bullet points with wikilinks to related concepts and source papers, each followed by " — " and a brief (<1 sentence) auto-generated description. Format:
- `[[ConceptName]] — Auto-generated description of relationship`
- `[[AnotherConcept]] — How this concept connects`
- `Source paper: [[SourceName]] — Auto-generated summary of what the source covers`

Use `python3 scripts/wiki_tool.py suggest-links --note "Wiki/Concepts/YourNote.md"` to auto-generate descriptions and wikilink suggestions based on your body text.

