# LLM Wiki Agent Rules

This document tells agents how to work with this LLM Wiki.

## Core Principles

1. **Treat `Raw/Sources/` as source material, not as compiled notes.** Raw sources preserve original context, citations, and metadata. Body text must be clean and coherent (free of OCR artifacts and formatting errors). Do not edit for content bias, but DO clean OCR errors, formatting issues, and ensure factual accuracy. These are canonical sources; quality matters.

2. **Write reusable knowledge only under `Wiki/`.** Compiled notes in `Wiki/Topics/`, `Wiki/Concepts/`, `Wiki/Entities/`, and `Wiki/Projects/` are the primary knowledge base. Activity logs are stored in `Wiki/log.md` (not in `Wiki/Logs/`).

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

1. **PDF extraction and auto-cleanup** (automated):
   - Run `python3 scripts/pdf_to_source.py --pdf "filename.pdf"` to extract and convert PDF to markdown
   - The script automatically runs aggressive OCR cleanup (`--fix` mode) to repair:
     - Missing spaces in mangled text
     - Broken chemical notation (pO₂, δ¹⁸O, etc.)
     - Fragmented references and citations
   - Output markdown is pre-cleaned but still requires metadata verification and body text review

2. **Verify source metadata** (before any other work):
   - Author names: Verify full author list against the paper's DOI, PubMed, or journal website
   - Journal/volume/pages: Confirm exact publication details match the PDF
   - Publication year: Add `Year: "YYYY"` to frontmatter after Pages property
   - Do NOT rely on web search summaries for metadata—always verify against authoritative sources
   - Frontmatter order for journal articles: Title, Author, Reference, ContentType, Created, Journal, Volume, Pages, Year, Processed

3. **Assess and fix remaining OCR artifacts**:
   - Run `python3 scripts/cleanup_ocr.py --assess Raw/Sources/filename.md` to check quality
   - ACCEPTABLE verdict (all sections ≥50 words, coherent, no artifacts) → proceed to step 4
   - REWRITE REQUIRED verdict → manually fix only the listed failing sections

4. Search `Wiki/catalog.jsonl` for related topics and concepts: `python3 scripts/wiki_tool.py search-catalog --query "your keywords"`

5. Open only the most relevant existing Wiki notes to understand naming conventions and structure.

6. Create focused concept notes in `Wiki/Concepts/` that compile the source material.

7. **Use correct naming for concept files**:
   - Use **PascalCase** (no hyphens): `MethylhopanoidBiosynthesis.md` not `Methylhopanoid-Biosynthesis.md`
   - Pattern: ConcatWords capitalized, no spaces or hyphens
   - Check existing files for precedent: `PlantWaxBiomarkers.md`, `DissolvedOrganicMatter.md`, etc.

8. Add the Raw source path to the `sources` list in each compiled note. Update `source_count` to match.

9. **Add wikilinks and auto-generate descriptions (mandatory)**:
   - For first mentions of related concepts in body text, use pipe syntax: `[[ConceptName|display text]]` so text reads naturally
   - Run the tool to auto-generate the "See also" section:
     ```bash
     python3 scripts/wiki_tool.py suggest-links --note "Wiki/Concepts/YourNote.md"
     ```
   - This generates:
     - Wikilinks to related concepts (extracted from body text)
     - Wikilinks to source papers
     - **Auto-generated descriptions** for both concept relationships and source coverage
   - The tool will only suggest concepts that exist in the catalog (no broken links)
   - Review the suggestions and accept them into your "See also" section
   - You may manually edit descriptions if the auto-generated versions don't capture nuance, but auto-generation is acceptable
   - Format: `- [[ConceptName]] — Description` with source papers as final entry

10. **Mark source as processed**: Set `Processed: true` in the Raw source frontmatter (mandatory once compiled into Wiki notes and body text is clean).

11. Run maintenance checks: `python3 scripts/wiki_tool.py build && python3 scripts/wiki_tool.py lint`

12. **Add log entry to `Wiki/log.md`** (mandatory before commit):
    - Use `python3 scripts/wiki_tool.py log --title "Ingest: [Source]" --details "..."`
    - Describe what was created/updated and which sources were compiled
    - Use the format from existing entries as template

13. Stage all changes and commit with descriptive message including source file and concept notes.

14. Update the source manifest: `python3 scripts/wiki_tool.py source-scan --update --accept-covered`

15. Verify source integrity: `python3 scripts/wiki_tool.py source-lint`

## Ingest Quality Checklist (Before Commit)

Before committing any ingestion, verify:

- ✓ **Source metadata**: Author names verified against DOI/journal, Year property included (after Pages)
- ✓ **Body text**: All sections (Overall Scientific Topic, Methods, Results, Implications) pass quality assessment (ACCEPTABLE verdict)
- ✓ **Results section quality**: Coherent narrative with proper evidence, NOT fragmented OCR artifacts
- ✓ **Concept filenames**: Use PascalCase (e.g., `DissolvedOrganicMatter.md`)—check existing files for naming pattern
- ✓ **"See also" format**: Matches standard format with descriptions after " — " separator, includes source paper link
- ✓ **Wikilinks**: Use PascalCase without hyphens (e.g., `[[NitrogenCycle]]` not `[[Nitrogen-Cycle]]`)
- ✓ **Maintenance checks pass**: `build`, `lint`, and `source-lint` all succeed
- ✓ **Log entry**: Added to `Wiki/log.md` (not `Wiki/Logs/`)
- ✓ **Source marked processed**: `Processed: true` in Raw source frontmatter

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

**After every ingest or maintenance step that changes the Wiki**, log the activity to `Wiki/log.md`:

```bash
python3 scripts/wiki_tool.py log --title "Your title" --details "Description of what changed"
```

**IMPORTANT:** All log entries must be written to `Wiki/log.md` (the canonical activity log file). The `Wiki/Logs/` directory is not used for logging. The `wiki_tool.py log` command automatically appends to the correct location.

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
