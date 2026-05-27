# Naming Conventions

Consistent naming makes the vault easier to navigate and query.

## Metadata Field Conventions

### Updated Date Field

The `updated:` date field is critical for maintaining change tracking and audit trails. **It MUST be updated to the current date (YYYY-MM-DD) for every edit to a concept note.**

**Trigger updates for:**
- Creating a new concept note (set `updated:` = today)
- Adding/removing body text content
- Updating the See also section
- Adding/removing/modifying wikilinks
- Changing source metadata
- Any other structural or content modification

**Do NOT update if:** Only reading/viewing the file (no changes made)

**Example:**
```yaml
created: 2026-05-24      # NEVER changes
updated: 2026-05-27      # Changed today — reflects current edit
```

## File Naming

### Format

- Use PascalCase (CapitalizedWords) for filenames
- Avoid spaces; use capital letters to separate words
- Be concise but descriptive
- Examples:
  - `ArtificialNeuralNetwork.md`
  - `TransformerArchitecture.md`
  - `BackpropagationAlgorithm.md`
  - `ResearchPaper2024.md`

### By Type

**Topic notes**: Plural or noun phrases
- ✓ `MachineLearning.md`
- ✓ `DeepLearning.md`
- ✓ `NaturalLanguageProcessing.md`

**Concept notes**: Specific terms and techniques
- ✓ `SelfAttention.md`
- ✓ `LayerNormalization.md`
- ✓ `PositionalEncoding.md`

**Entity notes**: Proper nouns (people, organizations, products)
- ✓ `YannLeCun.md`
- ✓ `OpenAI.md`
- ✓ `BERT.md`

**Project notes**: Project or initiative names
- ✓ `GPT4Development.md`
- ✓ `TransformerOptimization.md`

**Log notes**: Date-based or chronological
- ✓ `2024-01-15_SourceIngestion.md`
- ✓ `WeeklyUpdate_2024-01-15.md`

## Folder Organization

Compiled notes live in subfolders of `Wiki/`:

- `Wiki/Topics/` — High-level domains and fields
- `Wiki/Concepts/` — Specific techniques and ideas
- `Wiki/Entities/` — People, organizations, products
- `Wiki/Projects/` — Initiatives and research efforts
- `Wiki/Logs/` — Chronological entries

Raw sources live in `Raw/Sources/` (no subfolders):

- All Raw sources in one folder to simplify tracking
- Use descriptive titles and the `Reference` field for organization

## Wikilink Naming

Internal links (wikilinks) use the exact filename without `.md`:

```markdown
[[ArtificialNeuralNetwork]]
[[SelfAttention]]
[[OpenAI]]
```

Use `[[filename|display text]]` if you want different link text:

```markdown
[[ArtificialNeuralNetwork|neural networks]]
```

## Frontmatter Fields

### Raw Sources

```yaml
Title: "Exact Source Title"
Author: "Full Author Name"
Reference: "url-or-identifier"
```

### Compiled Notes

```yaml
tags:
  - "concept"
topics:
  - "[[TopicName]]"
status: stable
created: 2024-01-15
updated: 2024-01-20
sources:
  - "Raw/Sources/SourceName.md"
source_count: 1
aliases:
  - "Alternative Name"
  - "Short Form"
```

## Aliases

Use `aliases` in compiled notes for alternative names:

```yaml
aliases:
  - "ANN"
  - "Artificial Neural Net"
```

This helps Obsidian suggest links when you type alternative names.

## Version Control

All filenames should be deterministic and meaningful. Avoid:
- Temporary names like `Draft.md` or `Temp.md`
- Numbered versions like `Note1.md`, `Note2.md`
- Timestamps in filenames (use frontmatter dates instead)
- Special characters except hyphens

## Examples

**Good naming**:
- `TransformerArchitecture.md` (clear, searchable, PascalCase)
- `GradientDescent.md` (technique, concise)
- `VladimirVapnik.md` (proper noun)
- `2024-01-15_SourceProcessing.md` (log with date prefix)

**Poor naming**:
- `transformers.md` (lowercase, unclear)
- `stuff about attention.md` (spaces, vague)
- `document_v2_final.md` (versioning in name)
- `TODO.md` (not specific)
