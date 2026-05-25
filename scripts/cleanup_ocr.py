#!/usr/bin/env python3
"""
OCR Artifact Cleanup Script

Removes common OCR extraction errors from PDF-to-markdown conversions.
Run this on source files after pdf_to_source.py to clean up formatting issues
before manual review and ingestion.

Usage:
    python3 scripts/cleanup_ocr.py Raw/Sources/Filename.md
    python3 scripts/cleanup_ocr.py Raw/Sources/*.md
    python3 scripts/cleanup_ocr.py --fix Raw/Sources/Filename.md    (aggressive fix mode)
    python3 scripts/cleanup_ocr.py --assess Raw/Sources/Filename.md (quality assessment)
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


def fix_ocr_artifacts_aggressive(text):
    """
    Aggressively repair OCR artifacts, including fixing mangled text with missing spaces.
    Used in --fix mode to prepare extracted PDFs for manual review.
    """

    # First, apply standard cleanup
    text = cleanup_ocr_artifacts(text)

    # Fix mangled chemical/scientific notation patterns
    # pO2/pCO2 variations (missing spaces around notation)
    text = re.sub(r'\bp[O0]2', 'pO₂', text)
    text = re.sub(r'\bp[C0]O2', 'pCO₂', text)
    text = re.sub(r'\bDelta[\'′]?17[O0]', 'Δ¹⁷O', text)
    text = re.sub(r'\bDelta[\'′]?18[O0]', 'Δ¹⁸O', text)
    text = re.sub(r'\bdelta18[O0]', 'δ¹⁸O', text)
    text = re.sub(r'\bdelta34[S5]', 'δ³⁴S', text)
    text = re.sub(r'\bdelta13[C0]', 'δ¹³C', text)
    text = re.sub(r'\bGPP\s+', 'GPP ', text)

    # Fix mangled words by inserting spaces before capital letters within lowercase chains
    # Pattern: lowercase letters followed by capital letter (likely word boundary)
    # Be conservative: only fix patterns we see frequently
    mangled_patterns = {
        # Common scientific terms and phrases
        r'isotopecompositionof': 'isotope composition of',
        r'isotopeproxyis': 'isotope proxy is',
        r'presumptionthat': 'presumption that',
        r'metabolismto': 'metabolism to',
        r'locusof': 'locus of',
        r'oxidation,': 'oxidation,',
        r'availability\(': 'availability (',
        r'millionyears': 'million years',
        r'oxygenisotope': 'oxygen isotope',
        r'sulfateisotope': 'sulfate isotope',
        r'atmosphericO': 'atmospheric O',
        r'grossmetabolism': 'gross metabolism',
    }

    for pattern, replacement in mangled_patterns.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    # Fix broken subscripts in isotope notation (e.g., "O 2" → "O₂")
    text = re.sub(r'\bO\s+2\b', 'O₂', text)
    text = re.sub(r'\bC\s+O\s+2\b', 'CO₂', text)
    text = re.sub(r'\bC\s+O2\b', 'CO₂', text)
    text = re.sub(r'\bS\s+O4\b', 'SO₄', text)
    text = re.sub(r'\bBaSO\s*4\b', 'BaSO₄', text)

    # Fix spacing around percentages
    text = re.sub(r'(\d+)%\s+and\s+(\d+)%', r'\1% and \2%', text)

    # Fix fragmented references (e.g., "a n d" → "and")
    text = re.sub(r'\ba\s+n\s+d\b', 'and', text)
    text = re.sub(r'\bt\s+h\s+r\s+o\s+u\s+g\s+h\b', 'through', text)
    text = re.sub(r'\bi\s+s\b', 'is', text)

    # Fix broken words with extraneous spacing
    text = re.sub(r'\b(\w+)\s+(\w)\s+(\w)\s+(\w+)\b', lambda m: m.group(1) + m.group(2) + m.group(3) + m.group(4) if len(m.group(2)) == 1 else m.group(0), text)

    # Fix multiple spaces
    text = re.sub(r' {2,}', ' ', text)

    # Fix spacing before/after parentheses and citations
    text = re.sub(r'\s+\(', ' (', text)
    text = re.sub(r'\)\s+', ') ', text)

    return text


def process_file(filepath, aggressive_fix=False):
    """Clean OCR artifacts from a markdown source file.

    Args:
        filepath: Path to the markdown file
        aggressive_fix: If True, use aggressive fixing (--fix mode) for mangled text
    """
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

                # Clean the body with appropriate level of aggressiveness
                if aggressive_fix:
                    cleaned_body = fix_ocr_artifacts_aggressive(body)
                else:
                    cleaned_body = cleanup_ocr_artifacts(body)
                content = '---' + frontmatter + '---' + cleaned_body
            else:
                if aggressive_fix:
                    content = fix_ocr_artifacts_aggressive(content)
                else:
                    content = cleanup_ocr_artifacts(content)
        else:
            if aggressive_fix:
                content = fix_ocr_artifacts_aggressive(content)
            else:
                content = cleanup_ocr_artifacts(content)

        # Write back if changed
        if content != original_content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            if aggressive_fix:
                print(f"✓ Fixed and cleaned: {filepath}")
            else:
                print(f"✓ Cleaned: {filepath}")
            return True
        else:
            print(f"- No changes needed: {filepath}")
            return False

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def extract_section_body(text, section_name):
    """Extract body text of a markdown section (after the header, before the next header or EOF)."""
    # Find the section header
    header_pattern = f'^## {re.escape(section_name)}$'
    match = re.search(header_pattern, text, re.MULTILINE)
    if not match:
        return ""

    # Start after the header and newline
    start = match.end() + 1

    # Find the next section header or end of text
    next_header = re.search(r'^## ', text[start:], re.MULTILINE)
    if next_header:
        end = start + next_header.start()
    else:
        end = len(text)

    section_text = text[start:end].strip()
    return section_text


def assess_section_quality(section_body):
    """Assess quality of a single section body. Returns (pass: bool, reason: str, stats: dict)."""
    if not section_body or not section_body.strip():
        return False, "empty", {"words": 0, "sentences": 0}

    # Count words and sentences
    words = section_body.split()
    word_count = len(words)
    sentence_count = len(re.findall(r'[.!?]+\s+', section_body)) + (1 if section_body.strip() and not section_body.rstrip().endswith(('.', '!', '?')) else 0)

    # Check for OCR artifacts
    ocr_patterns = [
        r'/C\d+',           # Encoding artifacts
        r'ﬁ|ﬂ|ﬀ|ﬃ|ﬄ',    # Ligatures
        r'\d+\s+\.\s+\d+',  # Fragmented numbers (3. 6)
        r'\b[a-z]\s+[a-z]\s+[a-z]\b',  # Broken words
    ]
    has_artifacts = any(re.search(pattern, section_body) for pattern in ocr_patterns)

    # Determine pass/fail
    reasons = []
    if word_count < 50:
        reasons.append("too_short")
    if has_artifacts:
        reasons.append("artifacts")
    if sentence_count < 2:
        reasons.append("incoherent")

    if reasons:
        return False, "|".join(reasons), {"words": word_count, "sentences": sentence_count}

    return True, "pass", {"words": word_count, "sentences": sentence_count}


def assess_extraction_quality(filepath):
    """Assess quality of all four sections in a source file."""
    path = Path(filepath)
    if not path.exists():
        print(f"Error: File not found: {filepath}")
        return None

    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip frontmatter if present
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                body = parts[2]
            else:
                body = content
        else:
            body = content

        # Assess each section
        sections = [
            "Overall Scientific Topic",
            "Methods",
            "Results",
            "Implications"
        ]

        results = {}
        passed = 0
        for section_name in sections:
            section_body = extract_section_body(body, section_name)
            passed_check, reason, stats = assess_section_quality(section_body)
            results[section_name] = {
                "pass": passed_check,
                "reason": reason,
                "words": stats["words"],
                "sentences": stats["sentences"]
            }
            if passed_check:
                passed += 1

        # Overall verdict
        if passed == 4:
            verdict = "ACCEPTABLE"
        elif passed >= 2:
            verdict = "PARTIAL"
        else:
            verdict = "REWRITE"

        return {
            "filepath": str(path),
            "sections": results,
            "passed": passed,
            "verdict": verdict
        }

    except Exception as e:
        print(f"Error assessing {filepath}: {e}")
        return None


def print_assessment(assessment):
    """Pretty-print quality assessment results."""
    if not assessment:
        return

    print(f"\nQuality assessment: {assessment['filepath']}")
    for section_name in ["Overall Scientific Topic", "Methods", "Results", "Implications"]:
        result = assessment['sections'][section_name]
        status = "PASS" if result['pass'] else "FAIL"
        words = result['words']
        sentences = result['sentences']
        reason = result['reason']

        if result['pass']:
            print(f"  {section_name:<25} : {status} ({words} words, {sentences} sentences)")
        else:
            print(f"  {section_name:<25} : {status} ({reason}: {words} words, {sentences} sentences)")

    print()
    if assessment['verdict'] == "ACCEPTABLE":
        print(f"VERDICT: {assessment['verdict']} — proceed without rewriting")
    else:
        failed_sections = [s for s, r in assessment['sections'].items() if not r['pass']]
        print(f"VERDICT: REWRITE REQUIRED ({assessment['passed']}/4 sections passed)")
        print(f"  → Rewrite sections: {', '.join(failed_sections)}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/cleanup_ocr.py <file.md> [file2.md ...]")
        print("       python3 scripts/cleanup_ocr.py Raw/Sources/*.md")
        print("       python3 scripts/cleanup_ocr.py --fix <file.md> [file2.md ...]     (aggressive repair)")
        print("       python3 scripts/cleanup_ocr.py --assess <file.md> [file2.md ...]  (quality check)")
        sys.exit(1)

    # Check for --fix or --assess flags
    fix_mode = False
    assess_mode = False
    file_args = sys.argv[1:]

    if file_args[0] == "--fix":
        fix_mode = True
        file_args = file_args[1:]
        if not file_args:
            print("Usage: python3 scripts/cleanup_ocr.py --fix <file.md> [file2.md ...]")
            sys.exit(1)
    elif file_args[0] == "--assess":
        assess_mode = True
        file_args = file_args[1:]
        if not file_args:
            print("Usage: python3 scripts/cleanup_ocr.py --assess <file.md> [file2.md ...]")
            sys.exit(1)

    processed = 0
    changed = 0

    # Assess mode: just run quality checks
    if assess_mode:
        for filepath in file_args:
            path = Path(filepath)
            if '*' in filepath:
                for match in path.parent.glob(path.name):
                    assessment = assess_extraction_quality(str(match))
                    print_assessment(assessment)
                    processed += 1
            else:
                assessment = assess_extraction_quality(filepath)
                print_assessment(assessment)
                processed += 1
        return

    # Normal or fix mode: cleanup/fix and optionally process
    for filepath in file_args:
        # Expand glob patterns
        path = Path(filepath)
        if '*' in filepath:
            for match in path.parent.glob(path.name):
                if process_file(str(match), aggressive_fix=fix_mode):
                    changed += 1
                processed += 1
        else:
            if process_file(filepath, aggressive_fix=fix_mode):
                changed += 1
            processed += 1

    if fix_mode:
        print(f"\n✓ Fixed {processed} file(s), modified {changed} file(s)")
    else:
        print(f"\n✓ Processed {processed} file(s), cleaned {changed} file(s)")


if __name__ == '__main__':
    main()
