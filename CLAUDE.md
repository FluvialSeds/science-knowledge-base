# LLM Wiki Agent Rules

This document tells agents how to work with this LLM Wiki.

## Core Principles

1. **Treat `Raw/Sources/` as source material, not as compiled notes.** Raw sources preserve original context, citations, and metadata. Body text must be clean and coherent (free of OCR artifacts and formatting errors). Do not edit for content bias, but DO clean OCR errors, formatting issues, and ensure factual accuracy. These are canonical sources; quality matters.

2. **Write reusable knowledge only under `Wiki/`.** Compiled notes in `Wiki/Topics/`, `Wiki/Concepts/`, `Wiki/Entities/`, `Wiki/Projects/`, and `Wiki/Logs/` are the primary knowledge base.

3. **Keep every compiled note linked to one or more Raw sources.** The `sources` field in each Wiki note's frontmatter must list the Raw source files that support it. This maintains traceability and prevents unsupported claims.

4. **Search `Wiki/catalog.jsonl` before opening broad Raw context.** Use the catalog to find relevant compiled notes. Only open Raw sources when the compiled note is insufficient or verification is needed.

5. **Run `build`, `lint`, and source checks before commits.** All maintenance gates must pass:
   ```bash
   python3 scripts/wiki_tool.py build
   python3 scripts/wiki_tool.py lint
   python3 scripts/wiki_tool.py source-lint
   ```

6. **Do not invent citations or create unsupported claims.** Every fact in a Wiki note must be traceable to a Raw source. If a claim cannot be linked to a source, do not include it.

## Ingest Workflow

When processing a new Raw source:

1. Search `Wiki/catalog.jsonl` for related topics and concepts: `python3 scripts/wiki_tool.py search-catalog --query "your keywords"`
2. **Run OCR cleanup locally** (reduces token usage): `python3 scripts/cleanup_ocr.py Raw/Sources/filename.md`
3. Open only the most relevant existing Wiki notes.
4. Create or update focused notes in `Wiki/` that compile the source material.
5. Add the Raw source path to the `sources` list in each compiled note.
6. Update `source_count` to match the number of sources.
7. **Clean source body text** (mandatory before step 8):
   - Remove OCR artifacts, formatting errors, and encoding issues
   - Ensure all sections (Overall Scientific Topic, Methods, Results, Implications) are coherent and accurate
   - Verify against the original PDF to catch extraction errors
   - See `Schema/pdf-import-guide.md` Body Text Quality Checklist for details
8. **Add wikilinks (mandatory)**:
   - Add inline wikilinks within text to related concepts using `[[ConceptName]]` syntax
   - Add a "See also" section at the end linking to:
     - Related concept notes: `[[RelatedConcept]]`
     - Source paper: `[[SourceFileName]]` (the Raw source markdown file)
   - Use `python3 scripts/wiki_tool.py suggest-links --note "Wiki/Concepts/YourNote.md"` to get suggestions
9. **Mark source as processed**: Set `Processed: true` in the Raw source frontmatter (mandatory once compiled into Wiki notes and body text is clean).
10. **Assess extraction quality** (hybrid strategy — local assessment, 0 tokens):
    ```bash
    python3 scripts/cleanup_ocr.py --assess Raw/Sources/filename.md
    ```
    - **ACCEPTABLE verdict**: all sections meet quality thresholds (≥50 words, coherent prose, no OCR artifacts) → proceed to Step 11 without rewriting
    - **REWRITE REQUIRED verdict**: one or more sections fail quality checks → rewrite only the listed failing sections before proceeding (see Body Text Quality Checklist in `Schema/pdf-import-guide.md`)
11. Run maintenance checks: `python3 scripts/wiki_tool.py build && python3 scripts/wiki_tool.py lint`
12. **Add log entry to `Wiki/log.md`** (mandatory before commit):
    - Add a new section with title: `## Ingest: [Source Title]`
    - Add timestamp line: `*Logged: YYYY-MM-DD HH:MM:SS*`
    - Describe what was created/updated and which sources were compiled
    - Use the format from existing entries as template
13. Stage all changes and commit with descriptive message including source file and concept notes.
14. Update the source manifest: `python3 scripts/wiki_tool.py source-scan --update --accept-covered`
15. Verify source integrity: `python3 scripts/wiki_tool.py source-lint`

## Query Workflow

When answering a question from the Wiki:

1. Start with `Wiki/index.md`.
2. Search the catalog: `python3 scripts/wiki_tool.py search-catalog --query "your topic"`
3. Open the most relevant Wiki notes.
4. Open Raw sources only when the compiled note is insufficient or source-level verification is needed.
5. Cite both the compiled note and Raw source when the answer depends on source material.

## Maintenance Gate

Before every meaningful commit, run:

```bash
python3 scripts/wiki_tool.py doctor
python3 scripts/wiki_tool.py build
python3 scripts/wiki_tool.py lint
python3 scripts/wiki_tool.py source-lint
python3 scripts/audit_public.py
```

After source ingestion, also run:

```bash
python3 scripts/wiki_tool.py source-scan --update --accept-covered
python3 scripts/wiki_tool.py source-lint
```

**After every ingest or maintenance step that changes the Wiki**, log the activity:

```bash
python3 scripts/wiki_tool.py log --title "Your title" --details "Description of what changed"
```

Each log entry automatically includes a timestamp (YYYY-MM-DD HH:MM:SS) for chronological tracking.

Examples:
- After ingesting sources: `log --title "Ingest: [Source]" --details "New/updated notes and key changes"`
- After schema changes: `log --title "Schema update" --details "What changed and why"`
- After tool improvements: `log --title "Tool enhancement" --details "What was improved"`

## File Structure

- **`Raw/Sources/`**: Original source material (markdown, articles, notes). Each source has title, author, reference, created date, journal/volume/pages (for journal articles), and processed flag.
- **`Raw/Files/`**: Binary source files (PDFs, images) referenced by Raw sources.
- **`Wiki/Topics/`**: High-level topic notes (e.g., "Machine Learning", "Web Development").
- **`Wiki/Concepts/`**: Detailed concept notes (e.g., "Transformer Architecture", "REST API Design").
- **`Wiki/Entities/`**: Person, organization, or product notes.
- **`Wiki/Projects/`**: Project and initiative notes.
- **`Wiki/log.md`**: Chronological log of all ingestions, schema changes, and maintenance activities.
- **`Schema/`**: Rules, templates, and metadata about the Wiki.
- **`scripts/`**: Automation and maintenance tools:
  - `wiki_tool.py`: Deterministic tool for building, querying, linting, and maintaining the Wiki
  - `pdf_to_source.py`: Converts PDF research papers into structured source markdown notes
  - `cleanup_ocr.py`: Removes common OCR artifacts from PDF-extracted markdown (local preprocessing before manual review)
  - `audit_public.py`: Validates public-facing content and metadata
