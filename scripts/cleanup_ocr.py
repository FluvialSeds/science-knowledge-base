#!/usr/bin/env python3
"""
OCR Artifact Cleanup Script

Removes common OCR extraction errors from PDF-to-markdown conversions.
Run this on source files after pdf_to_source.py to clean up formatting issues
before manual review and ingestion.

Usage:
    python3 scripts/cleanup_ocr.py Raw/Sources/Filename.md
    python3 scripts/cleanup_ocr.py Raw/Sources/*.md
"""

import sys
import re
from pathlib import Path


def cleanup_ocr_artifacts(text):
    """Remove common OCR artifacts from extracted text."""

    # Fix garbled special characters
    replacements = {
        # Ligatures and formatting characters
        'ﬁ': 'fi',
        'ﬂ': 'fl',
        'ﬀ': 'ff',
        'ﬃ': 'ffi',
        'ﬄ': 'ffl',

        # Encoding artifacts (common from PDFs)
        '/C255': '',
        '/C176': '°',
        '/C01': '',
        '/C2': '',

        # Degree symbols
        '◦': '°',
        '∘': '°',

        # Quotes and dashes
        '"': '"',
        '"': '"',
        ''': "'",
        ''': "'",

        # Math operators
        '−': '-',
        '–': '–',
        '—': '—',
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Fix random spaces within words (e.g., "orderto" → "order to", but preserve "POM" etc.)
    # Look for patterns like lowercase-lowercase with space issues
    text = re.sub(r'orderto', 'order to', text)
    text = re.sub(r'meanigful', 'meaningful', text)
    text = re.sub(r'ob\s+e\s*\(', 'be (', text)  # "t ob e( 3. 6 )" → "be (3.6)"

    # Fix fragmented numbers (e.g., "3. 6" → "3.6", "1 . 5" → "1.5")
    text = re.sub(r'(\d+)\s*\.\s*(\d+)', r'\1.\2', text)

    # Fix spacing around degree symbols and units
    text = re.sub(r'(\d+)\s*°\s*C', r'\1°C', text)
    text = re.sub(r'(\d+)\s*μg\s+C', r'\1 μg C', text)

    # Remove extra spaces before punctuation
    text = re.sub(r'\s+([.,;:!?])', r'\1', text)

    # Fix multiple spaces
    text = re.sub(r' {2,}', ' ', text)

    # Fix line breaks with hanging text (e.g., "pyrite\noxidation" → "pyrite oxidation")
    # Only for lines that end with lowercase and next line starts lowercase
    lines = text.split('\n')
    cleaned_lines = []
    skip_next = False

    for i, line in enumerate(lines):
        if skip_next:
            skip_next = False
            continue

        if i < len(lines) - 1:
            current_ends_lower = line and line[-1].islower()
            next_starts_lower = lines[i+1] and lines[i+1][0].islower()

            # If current line is mid-word and next line continues, join them
            # But only if it looks like actual text continuation, not section structure
            if (current_ends_lower and next_starts_lower and
                line.strip() and lines[i+1].strip() and
                not line.strip().startswith('##') and
                not lines[i+1].strip().startswith('##') and
                len(line.strip()) > 10):
                cleaned_lines.append(line + ' ' + lines[i+1].strip())
                skip_next = True
                continue

        cleaned_lines.append(line)

    text = '\n'.join(cleaned_lines)

    # Fix common OCR word errors (conservative - only obvious ones)
    word_fixes = {
        r'\bde ﬂ': 'defl',
        r'\bde\s+ﬂ': 'defl',
        r'\bde\s+fl': 'defl',
        r'\breﬂ': 'refl',
        r'\bre\s+ﬂ': 'refl',
        r'\bre\s+fl': 'refl',
    }

    for pattern, replacement in word_fixes.items():
        text = re.sub(pattern, replacement, text)

    # Remove page numbers and headers that may have been extracted
    # (lines that are just numbers or contain "page" at start of line)
    lines = text.split('\n')
    filtered_lines = []
    for line in lines:
        # Skip lines that are just page numbers
        if re.match(r'^\d+\s*$', line.strip()):
            continue
        # Skip common PDF headers
        if re.match(r'^(Downloaded from|Available at|Published|Received|©)', line.strip()):
            continue
        filtered_lines.append(line)

    text = '\n'.join(filtered_lines)

    return text


def process_file(filepath):
    """Clean OCR artifacts from a markdown source file."""
    path = Path(filepath)

    if not path.exists():
        print(f"Error: File not found: {filepath}")
        return False

    if not path.suffix == '.md':
        print(f"Error: File must be markdown (.md): {filepath}")
        return False

    try:
        # Read the file
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Split frontmatter from body
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                body = parts[2]

                # Clean only the body, preserve frontmatter
                cleaned_body = cleanup_ocr_artifacts(body)
                content = '---' + frontmatter + '---' + cleaned_body
            else:
                content = cleanup_ocr_artifacts(content)
        else:
            content = cleanup_ocr_artifacts(content)

        # Write back if changed
        if content != original_content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Cleaned: {filepath}")
            return True
        else:
            print(f"- No changes needed: {filepath}")
            return False

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/cleanup_ocr.py <file.md> [file2.md ...]")
        print("       python3 scripts/cleanup_ocr.py Raw/Sources/*.md")
        sys.exit(1)

    files = sys.argv[1:]
    processed = 0
    changed = 0

    for filepath in files:
        # Expand glob patterns
        path = Path(filepath)
        if '*' in filepath:
            for match in path.parent.glob(path.name):
                if process_file(str(match)):
                    changed += 1
                processed += 1
        else:
            if process_file(filepath):
                changed += 1
            processed += 1

    print(f"\n✓ Processed {processed} file(s), cleaned {changed} file(s)")


if __name__ == '__main__':
    main()
