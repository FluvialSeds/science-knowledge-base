#!/usr/bin/env python3
"""
Convert PDF files to source markdown notes.

Reads a PDF from Raw/Files/, extracts information, and generates a structured
markdown source note in Raw/Sources/ with sections for: topic, methods, results,
and implications.

Usage:
    python3 scripts/pdf_to_source.py --pdf filename.pdf --title "Paper Title" --author "Author Name" --reference "doi-or-url"

Or run interactively:
    python3 scripts/pdf_to_source.py
"""

import sys
import os
import re
from pathlib import Path
from datetime import datetime


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from PDF file. Requires PyPDF2 or pdfplumber."""
    try:
        import PyPDF2
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
            return text
    except ImportError:
        try:
            import pdfplumber
            with pdfplumber.open(pdf_path) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
                return text
        except ImportError:
            print("✗ PyPDF2 or pdfplumber required. Install with:")
            print("  pip install PyPDF2")
            print("  or: pip install pdfplumber")
            return None


def identify_sections(text: str) -> dict:
    """Try to identify Methods, Results, Discussion sections in PDF text."""
    sections = {
        "methods": None,
        "results": None,
        "discussion": None,
    }

    # Look for common section headers
    text_lower = text.lower()

    # Find Methods section
    methods_idx = text_lower.find("methods")
    results_idx = text_lower.find("results")
    discussion_idx = text_lower.find("discussion")

    # Extract text between sections (rough approximation)
    if methods_idx >= 0 and results_idx > methods_idx:
        sections["methods"] = text[methods_idx:results_idx][:1500]

    if results_idx >= 0 and discussion_idx > results_idx:
        sections["results"] = text[results_idx:discussion_idx][:1500]

    if discussion_idx >= 0:
        sections["discussion"] = text[discussion_idx:][:1500]

    return sections


def prompt_for_section(section_name: str, extracted: str = None) -> str:
    """Prompt user to provide or edit a section."""
    print(f"\n{'='*60}")
    print(f"Enter {section_name.upper()}")
    print(f"{'='*60}")

    if extracted:
        print(f"\nExtracted text (edit or replace):\n{extracted}\n")
        print("(Press Enter twice when done, or paste your version)")
    else:
        print(f"(Press Enter twice when done)")

    lines = []
    empty_lines = 0
    while empty_lines < 2:
        try:
            line = input()
            if line == "":
                empty_lines += 1
            else:
                empty_lines = 0
                lines.append(line)
        except EOFError:
            break

    return "\n".join(lines).strip()


def generate_markdown(title: str, author: str, reference: str,
                     topic: str, methods: str, results: str,
                     implications: str) -> str:
    """Generate markdown source note from extracted information."""

    today = datetime.now().strftime("%Y-%m-%d")

    markdown = f"""---
Title: "{title}"
Author: "{author}"
Reference: "{reference}"
ContentType:
  - "pdf"
  - "markdown"
Created: {today}
Processed: false
tags:
  - "source"
---

# {title}

## Overall Scientific Topic

{topic}

## Methods

{methods}

## Results

{results}

## Implications

{implications}
"""

    return markdown


def sanitize_filename(title: str) -> str:
    """Convert title to valid filename."""
    # Remove special characters and replace spaces with capitals
    name = re.sub(r'[^\w\s-]', '', title)
    name = re.sub(r'[-\s]+', '', name)
    return name + ".md"


def main():
    vault_root = Path.cwd()
    raw_files = vault_root / "Raw" / "Files"
    raw_sources = vault_root / "Raw" / "Sources"

    # Ensure directories exist
    raw_files.mkdir(parents=True, exist_ok=True)
    raw_sources.mkdir(parents=True, exist_ok=True)

    # Get parameters
    pdf_filename = None
    title = None
    author = None
    reference = None

    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description="Convert PDF to source markdown")
    parser.add_argument("--pdf", help="PDF filename in Raw/Files/")
    parser.add_argument("--title", help="Paper title")
    parser.add_argument("--author", help="Author name(s)")
    parser.add_argument("--reference", help="DOI, URL, or reference identifier")

    args = parser.parse_args()

    pdf_filename = args.pdf
    title = args.title
    author = args.author
    reference = args.reference

    # Interactive mode if not all args provided
    if not pdf_filename:
        print("Available PDF files:")
        pdf_files = list(raw_files.glob("*.pdf"))
        if not pdf_files:
            print("  (No PDF files in Raw/Files/)")
            print(f"\nAdd a PDF file to: {raw_files}")
            return 1

        for i, f in enumerate(pdf_files, 1):
            print(f"  {i}. {f.name}")

        choice = input("\nSelect PDF (number): ").strip()
        try:
            pdf_filename = pdf_files[int(choice) - 1].name
        except (ValueError, IndexError):
            print("✗ Invalid selection")
            return 1

    pdf_path = raw_files / pdf_filename
    if not pdf_path.exists():
        print(f"✗ PDF not found: {pdf_path}")
        return 1

    print(f"\n✓ Reading: {pdf_filename}")

    # Extract text from PDF
    pdf_text = extract_text_from_pdf(str(pdf_path))
    if not pdf_text:
        return 1

    print(f"✓ Extracted {len(pdf_text)} characters from PDF")

    # Try to identify sections
    identified = identify_sections(pdf_text)

    # Prompt for metadata
    if not title:
        title = input("\nPaper title: ").strip()
    if not author:
        author = input("Author(s): ").strip()
    if not reference:
        reference = input("Reference (DOI/URL/identifier): ").strip()

    # Prompt for sections
    topic = prompt_for_section("overall scientific topic")
    methods = prompt_for_section("methods", identified.get("methods"))
    results = prompt_for_section("results", identified.get("results"))
    implications = prompt_for_section("implications of the study", identified.get("discussion"))

    # Generate markdown
    markdown = generate_markdown(title, author, reference, topic, methods, results, implications)

    # Save to file
    filename = sanitize_filename(title)
    output_path = raw_sources / filename

    with open(output_path, "w") as f:
        f.write(markdown)

    print(f"\n✓ Created source note: {output_path.relative_to(vault_root)}")
    print(f"\nNext steps:")
    print(f"  1. Compile this source into Wiki notes using the ingest workflow")
    print(f"  2. Run: python3 scripts/wiki_tool.py source-scan --update")
    print(f"  3. Set Processed: true after compilation")

    return 0


if __name__ == "__main__":
    sys.exit(main())
