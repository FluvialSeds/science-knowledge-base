# PDF Import Guide

Convert PDF research papers and articles into structured source markdown notes **automatically**.

## Overview

The `scripts/pdf_to_source.py` script:
1. Reads PDF files from `Raw/Files/`
2. **Automatically extracts and summarizes content** (no user input required for content)
3. Generates markdown source notes in `Raw/Sources/` with organized sections:
   - **Overall Scientific Topic** — Extracted from abstract
   - **Methods** — Extracted and summarized from Methods section
   - **Results** — Extracted and summarized from Results section
   - **Implications** — Extracted and summarized from Discussion/Conclusion

The script handles content extraction intelligently, identifying and parsing the key sections from the PDF automatically.

## File Naming Convention

Generated markdown files follow the convention: `lastname-year-journalacro.md`

**Examples:**
- `Hemingway-2016gca.md` (Geochimica et Cosmochimica Acta, 2016)
- `Smith-2020nat.md` (Nature, 2020)
- `Jones-2019sci.md` (Science, 2019)

The PDF filename should follow this same pattern so the script can preserve it.

## Installation

The script requires a PDF reading library. Install:

```bash
pip install PyPDF2
```

## Usage

```bash
python3 scripts/pdf_to_source.py --pdf "lastname-year-journalacro.pdf"
```

**Example:**

```bash
python3 scripts/pdf_to_source.py --pdf "Hemingway-2016gca.pdf"
```

The script will:
1. Extract all text from the PDF
2. Analyze the paper structure
3. Identify Methods, Results, and Discussion sections
4. Extract metadata (title, authors, year)
5. Generate summaries for each section
6. Create markdown in `Raw/Sources/` with proper frontmatter
7. Report what was generated

## Workflow

### 1. Rename PDF to Follow Convention

PDF files should be named: `lastname-year-journalacro.pdf`

**Examples:**
```bash
# Rename from original filename to convention
mv "A_paper_on_plant_biomarkers.pdf" "Hemingway-2016gca.pdf"
mv "Smith_2020_nature.pdf" "Smith-2020nat.pdf"
```

Journal acronyms (3 letters):
- GCA = Geochimica et Cosmochimica Acta
- Nat = Nature
- Sci = Science
- PNAS = Proceedings of National Academy of Sciences

### 2. Add PDF to Raw/Files/

```bash
cp /path/to/lastname-year-journalacro.pdf Raw/Files/
```

### 3. Run pdf_to_source.py

```bash
python3 scripts/pdf_to_source.py --pdf "lastname-year-journalacro.pdf"
```

The script will automatically:
- Extract text from the PDF
- Analyze paper structure
- Identify Methods, Results, Discussion sections
- Generate summaries for all four sections
- Create markdown in `Raw/Sources/lastname-year-journalacro.md`

### 4. Review Generated Source

The script creates a markdown file in `Raw/Sources/lastname-year-journalacro.md`:

```markdown
---
Title: "Paper Title"
Author: "Authors extracted from PDF"
Reference: "extracted-from-lastname-year-journalacro.pdf"
ContentType:
  - "pdf"
  - "journal-article"
Created: 2026-05-24
Processed: false
tags:
  - "source"
---

# Paper Title

## Overall Scientific Topic
[Automatically extracted from abstract and introduction]

## Methods
[Automatically extracted and summarized from Methods section]

## Results
[Automatically extracted and summarized from Results section]

## Implications
[Automatically extracted and summarized from Discussion/Conclusion]
```

**If sections need refinement:** Edit the file to improve accuracy. The automated extraction is a good starting point but may need tweaks for complex papers.

### 5. Compile Into Wiki Notes

Follow the standard ingest workflow:

1. Search catalog for related topics: `python3 scripts/wiki_tool.py search-catalog --query "topic"`
2. Create or update Wiki notes in `Wiki/` with focused knowledge
3. Link Wiki notes back to this source in their `sources` field
4. **Add wikilinks** (mandatory):
   - Add inline `[[ConceptName]]` wikilinks within note text to related concepts
   - Add a "See also" section at the end with related concepts and source paper links
   - Use `python3 scripts/wiki_tool.py suggest-links --note "Wiki/Concepts/YourNote.md"` for suggestions
5. **Mark source as `Processed: true`** in the Raw source file
6. Run maintenance checks: `python3 scripts/wiki_tool.py build && python3 scripts/wiki_tool.py lint`
7. Log the ingest: `python3 scripts/wiki_tool.py log --title "Ingest: [Paper Title]" --details "Compiled into [Wiki notes]"`

## Quality Notes

### Automated Section Extraction

The script identifies sections by looking for headers ("Methods", "Results", "Discussion") and extracts text between them. Quality depends on:

- **Structured PDFs** (from journals): Usually excellent extraction
- **Scanned PDFs**: May have OCR errors; content may be unclear  
- **Non-standard layouts**: May miss or misidentify sections

### If Extraction is Poor

1. Check that the PDF is a standard research paper with clear sections
2. Try a different PDF to test the tool
3. Edit `Raw/Sources/filename.md` manually to improve content
4. For heavily formatted papers, consider manual summarization

## Troubleshooting

### PDF Text Extraction Fails

- Ensure PyPDF2 is installed: `pip install PyPDF2`
- Check that PDF is not encrypted or corrupted
- Try opening the PDF in a standard viewer to confirm it works

### Section Extraction Missed Content

- The script looks for standard headers ("Methods", "Results", "Discussion")
- If your paper uses different headers, edit the generated file
- Complex multi-section papers may need manual refinement

## Related Commands

```bash
# Update source manifest after importing
python3 scripts/wiki_tool.py source-scan --update --accept-covered

# Search catalog for related topics
python3 scripts/wiki_tool.py search-catalog --query "your topic"

# Check source coverage
python3 scripts/wiki_tool.py source-coverage

# Validate all sources
python3 scripts/wiki_tool.py source-lint
```
