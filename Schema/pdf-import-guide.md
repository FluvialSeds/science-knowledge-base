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
Journal: "[Journal name]"
Volume: "[Volume number]"
Pages: "[Page range]"
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

**Text Quality Requirements:** Before marking a source as `Processed: true`, the body text must meet the following quality standards (see Body Text Quality Checklist below).

**If sections need refinement:** Edit the file to improve accuracy and quality. The automated extraction is a starting point but requires review and cleanup before the source can be considered complete.

**Important metadata cleanup:**
- **Title format**: Use sentence case (capitalize only the first word and proper nouns), NOT title case
  - ✓ Correct: `"Assessing the blank carbon contribution of the ramped pyrolysis instrument"`
  - ✗ Incorrect: `"Assessing the Blank Carbon Contribution of the Ramped Pyrolysis Instrument"`
  - Exception: Proper nouns remain capitalized (e.g., "Congo River", "NOSAMS", "Nature")
- **Author format**: Must be comma-separated full names: `"FirstName MiddleInitial. LastName, FirstName MiddleInitial. LastName, ..."`
  - Example: `"Jordon D. Hemingway, Robert G. Hilton, Niels Hovius"`
  - NOT: `"Hemingway, J.D.; Hilton, R.G.; Hovius, N."`
- **Reference field**: Replace `"extracted-from-..."` with actual DOI or URL
  - Example: `"https://doi.org/10.1126/science.aao6463"` or full URL to the paper
- **Journal, Volume, Pages** (mandatory for journal articles):
  - **Journal**: Name of the journal (e.g., "Chemical Geology", "Science", "Nature")
  - **Volume**: Volume number (e.g., "466") or leave empty `""` if not applicable
  - **Pages**: Page range (e.g., "454–465") or article number (e.g., "e12345"), leave empty `""` if not available

### 4b. Body Text Quality Cleanup (Mandatory Before Processing)

Before proceeding to Wiki compilation, the source body text must be reviewed and cleaned for quality. This is a **mandatory** step to ensure Raw sources preserve clean, coherent material.

**Body Text Quality Checklist:**

- [ ] **Title is accurate, complete, and in sentence case** — Not truncated, malformed, or a DOI/URL
  - Compare against the actual PDF title page
  - Fix incomplete titles like "Glacier meltwater and monsoon precipitation drive Upper" → "Glacier meltwater and monsoon precipitation drive Upper Ganges Basin dissolved organic matter composition"
  - Use sentence case (capitalize only first word and proper nouns), NOT title case
  - ✓ "Glacier meltwater and monsoon precipitation drive Upper Ganges Basin dissolved organic matter composition"
  - ✗ "Glacier Meltwater And Monsoon Precipitation Drive Upper Ganges Basin Dissolved Organic Matter Composition"

- [ ] **No OCR artifacts or encoding errors** — Common issues to fix:
  - Random spaces within words: "ﬁelds" → "fields", "orderto" → "order to"
  - Garbled characters: "/C255", "/C176C", "/C01", "ﬂections" → "deflections"
  - Broken formatting: "t ob e( 3. 6 )" → "3.6", "min–1)t ob e" → "at 5°C/min"
  - Degree symbols: "450/C176C, 4 h" → "450°C, 4 h"

- [ ] **Overall Scientific Topic is coherent** — Should be 3–4 sentences summarizing:
  - What problem/question the paper addresses
  - Why it matters (scientific significance)
  - Brief overview of the approach
  - Should read naturally without OCR artifacts

- [ ] **Methods section is clear and coherent** — Should describe:
  - Study sites/samples (where, what, how many)
  - Analytical techniques and instruments
  - Experimental design and procedures
  - Should flow logically without OCR errors or truncation

- [ ] **Results section accurately reflects key findings** — Should present:
  - Main quantitative results (measurements, values, ranges)
  - Key patterns or relationships observed
  - Statistical or analytical outcomes
  - Should be factually accurate based on the PDF content

- [ ] **Implications section addresses significance** — Should explain:
  - What the results mean for the field
  - How findings advance understanding
  - Applications or follow-up questions
  - Should avoid speculation beyond the paper's scope

- [ ] **No author affiliations or footer text** — Remove department addresses, author notes, and publication metadata that belongs in frontmatter, not body text

- [ ] **Spelling and grammar are correct** — Fix obvious errors introduced by OCR, but preserve the tone and voice of the original paper

**Cleanup Strategy:**
1. Read the PDF version of each section directly
2. Compare PDF text to the extracted markdown
3. Rewrite sections with significant OCR errors rather than trying to patch individual characters
4. Ensure sentences are complete and coherent
5. Verify factual accuracy against the PDF source

**When OCR is Poor:**
If a PDF has extensive OCR errors (scanned document, poor image quality), consider:
- Rewriting sections based on manual reading of the PDF
- Focusing on the most critical information (Overall Topic, key Methods, main Results)
- Using the PDF's abstract as a reference for the Overall Scientific Topic section
- Noting in a comment if OCR quality was particularly challenging

### 5. Compile Into Wiki Notes

Follow the standard ingest workflow:

1. Search catalog for related topics: `python3 scripts/wiki_tool.py search-catalog --query "topic"`
2. Create or update Wiki notes in `Wiki/` with focused knowledge
3. Link Wiki notes back to this source in their `sources` field
4. **Add wikilinks** (mandatory):
   - Add inline `[[ConceptName]]` wikilinks within note text to related concepts
   - Add ONLY a "See also" section at the end with related concepts and source paper links (do NOT create separate "Complementary Concepts" or similar sections)
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
