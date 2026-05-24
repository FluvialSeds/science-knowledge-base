# PDF Import Guide

Convert PDF research papers and articles into structured source markdown notes.

## Overview

The `scripts/pdf_to_source.py` script reads PDF files from `Raw/Files/` and generates markdown source notes in `Raw/Sources/` with the frontmatter template and organized sections for:

1. **Overall Scientific Topic** — The main research question or subject
2. **Methods** — How the study was conducted
3. **Results** — Key findings and data
4. **Implications** — Significance and applications

## Installation

The script requires a PDF reading library. Install one:

```bash
pip install PyPDF2
```

or

```bash
pip install pdfplumber
```

## Usage

### Interactive Mode

```bash
python3 scripts/pdf_to_source.py
```

The script will:
1. List available PDFs in `Raw/Files/`
2. Prompt you to select a PDF
3. Ask for paper metadata (title, author, reference)
4. Guide you through describing each section
5. Generate the markdown source note

### Command Line Mode

```bash
python3 scripts/pdf_to_source.py \
  --pdf "paper.pdf" \
  --title "Machine Learning in Healthcare" \
  --author "Jane Smith, John Doe" \
  --reference "https://doi.org/10.1234/example"
```

## Workflow

### 1. Add PDF to Raw/Files/

Place your PDF in the `Raw/Files/` folder:

```bash
cp /path/to/paper.pdf Raw/Files/
```

### 2. Run pdf_to_source.py

```bash
python3 scripts/pdf_to_source.py
```

### 3. Review Generated Source

The script creates a markdown file in `Raw/Sources/` with:

```markdown
---
Title: "Paper Title"
Author: "Authors"
Reference: "doi-or-url"
ContentType:
  - "pdf"
  - "markdown"
Created: 2026-05-24
Processed: false
tags:
  - "source"
---

# Paper Title

## Overall Scientific Topic
[Your description of the main topic and research question]

## Methods
[How the research was conducted]

## Results
[Key findings from the study]

## Implications
[What the results mean and their applications]
```

### 4. Compile Into Wiki Notes

Follow the standard ingest workflow:

1. Search catalog for related topics
2. Create or update Wiki notes in `Wiki/` with focused knowledge
3. Link Wiki notes back to this source in the `sources` field
4. Mark source as `Processed: true` in the Raw source file
5. Run maintenance checks
6. Log the ingest

Example:

```bash
python3 scripts/wiki_tool.py source-scan --update --accept-covered
python3 scripts/wiki_tool.py log --title "Ingest: [Paper Title]" --details "Compiled into [Wiki notes]"
```

## Tips for Good Source Notes

### Overall Scientific Topic

Describe in 2-3 sentences:
- What is the main research question?
- What field or domain is this in?
- Why does this matter?

**Example**: "This study investigates how machine learning models can improve early detection of diabetic complications in primary care. Understanding biomarker patterns is important because early intervention can prevent serious health outcomes."

### Methods

Summarize:
- Study design (observational, experimental, etc.)
- Sample size and population
- Key variables measured
- Analysis techniques used

**Example**: "The researchers conducted a prospective cohort study of 5,000 patients from 20 primary care clinics. They measured 15 biomarkers quarterly and used gradient boosting to predict complications within 2 years."

### Results

Include:
- Primary findings with numbers/percentages
- Performance metrics (accuracy, p-values, effect sizes)
- Key comparisons or patterns
- Notable limitations or caveats

**Example**: "The model achieved 94% sensitivity and 87% specificity for prediction (AUC = 0.91). Performance was consistent across all age groups (p = 0.34), but slightly lower in underrepresented populations (AUC = 0.85)."

### Implications

Discuss:
- Clinical or practical significance
- Limitations of the study
- Recommended next steps or applications
- Broader impact on the field

**Example**: "The model shows promise for deployment in primary care to identify high-risk patients. Further validation in diverse populations is needed. If validated, this could reduce preventable complications by 15-20%."

## Troubleshooting

### PDF Extraction Fails

- Ensure PyPDF2 or pdfplumber is installed
- Check that the PDF is not corrupted or encrypted
- Some scanned PDFs may have poor text extraction quality

### Generated File Has Placeholder Text

You provided minimal information. The script fills in templates to guide you. Edit `Raw/Sources/[filename].md` to add real content.

### Large PDFs Are Slow

Text extraction from large PDFs (100+ pages) can take time. This is normal. Consider splitting very large documents into parts.

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
