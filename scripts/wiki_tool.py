#!/usr/bin/env python3
"""
LLM Wiki deterministic tool for building, querying, and maintaining the Wiki.
Uses only Python standard library.
"""

import sys
import json
import os
import re
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Any


@dataclass
class CatalogEntry:
    path: str
    title: str
    tag: str
    topics: List[str]
    sources: List[str]
    updated: str


@dataclass
class ManifestEntry:
    path: str
    title: str
    processed: bool
    covered_by: List[str]
    updated: str


class WikiTool:
    def __init__(self):
        self.vault_root = Path.cwd()
        self.raw_sources = self.vault_root / "Raw" / "Sources"
        self.wiki_root = self.vault_root / "Wiki"
        self.schema_root = self.vault_root / "Schema"

    def doctor(self) -> int:
        """Non-mutating health check."""
        errors = []

        # Check folder structure
        required_folders = [
            "Raw/Sources", "Raw/Files", "Wiki/Topics", "Wiki/Concepts",
            "Wiki/Entities", "Wiki/Projects", "Wiki/Logs", "Schema",
            "_templates", ".claude/skills", "scripts"
        ]
        for folder in required_folders:
            if not (self.vault_root / folder).exists():
                errors.append(f"Missing folder: {folder}")

        # Check Python version
        if sys.version_info < (3, 6):
            errors.append(f"Python 3.6+ required, found {sys.version_info.major}.{sys.version_info.minor}")

        # Check for CLAUDE.md
        if not (self.vault_root / "CLAUDE.md").exists():
            errors.append("Missing CLAUDE.md")

        # Count notes
        wiki_notes = list(self.vault_root.glob("Wiki/*/*.md"))
        wiki_notes = [n for n in wiki_notes if not n.name.startswith("index")]
        raw_sources = list(self.raw_sources.glob("*.md"))

        print(f"✓ Vault health check")
        print(f"  Raw sources: {len(raw_sources)}")
        print(f"  Wiki notes: {len(wiki_notes)}")
        print(f"  Folders: {len(required_folders)}/{len(required_folders)}")

        if errors:
            for error in errors:
                print(f"  ✗ {error}")
            return 1

        print(f"  ✓ All checks passed")
        return 0

    def build(self) -> int:
        """Generate catalog.jsonl, index.md, and per-folder indexes."""
        catalog_entries = []

        # Collect all compiled notes
        for note_path in self.wiki_root.glob("*/*.md"):
            if note_path.name == "index.md":
                continue

            try:
                entry = self._read_note_metadata(note_path)
                if entry:
                    catalog_entries.append(entry)
            except Exception as e:
                print(f"✗ Error reading {note_path}: {e}", file=sys.stderr)
                return 1

        # Write catalog
        catalog_path = self.wiki_root / "catalog.jsonl"
        with open(catalog_path, "w") as f:
            for entry in catalog_entries:
                f.write(json.dumps(asdict(entry)) + "\n")

        print(f"✓ Built catalog: {len(catalog_entries)} entries")

        # Build per-folder indexes
        for folder in self.wiki_root.iterdir():
            if not folder.is_dir() or folder.name == "Logs":
                continue

            notes = sorted([n for n in folder.glob("*.md") if n.name != "index.md"])
            if not notes:
                continue

            index_content = f"# {folder.name}\n\n"
            for note_path in notes:
                title = self._extract_title(note_path)
                index_content += f"- [[{note_path.stem}]] — {title}\n"

            index_path = folder / "index.md"
            with open(index_path, "w") as f:
                f.write(index_content)

        # Build main Wiki index
        wiki_index = "# LLM Wiki\n\n"
        for folder in sorted(self.wiki_root.iterdir()):
            if not folder.is_dir() or folder.name == "Logs":
                continue
            notes = [n for n in folder.glob("*.md") if n.name != "index.md"]
            if notes:
                wiki_index += f"## {folder.name}\n\n"
                wiki_index += f"[[{folder.name}/index|View all]]\n\n"

        with open(self.wiki_root / "index.md", "w") as f:
            f.write(wiki_index)

        print(f"✓ Built indexes")
        return 0

    def lint(self) -> int:
        """Validate compiled Wiki note frontmatter and source links."""
        errors = []

        for note_path in self.wiki_root.glob("*/*.md"):
            if note_path.name == "index.md":
                continue

            frontmatter = self._read_frontmatter(note_path)
            if not frontmatter:
                errors.append(f"{note_path}: Missing frontmatter")
                continue

            # Check for valid tag
            tags = frontmatter.get("tags", [])
            valid_tags = {"topic", "concept", "entity", "project", "log"}
            if not tags or not any(t in valid_tags for t in tags):
                errors.append(f"{note_path}: Invalid or missing tag (must be one of {valid_tags})")

            # Check created and updated dates
            created = frontmatter.get("created")
            updated = frontmatter.get("updated")
            date_pattern = r"^\d{4}-\d{2}-\d{2}$"
            
            if not created:
                errors.append(f"{note_path}: Missing 'created' date")
            elif not re.match(date_pattern, str(created)):
                errors.append(f"{note_path}: 'created' date not in YYYY-MM-DD format: {created}")
            
            if not updated:
                errors.append(f"{note_path}: Missing 'updated' date")
            elif not re.match(date_pattern, str(updated)):
                errors.append(f"{note_path}: 'updated' date not in YYYY-MM-DD format: {updated}")
            elif created and updated < created:
                errors.append(f"{note_path}: 'updated' date ({updated}) is before 'created' date ({created})")

            # Check source_count
            sources = frontmatter.get("sources", [])
            source_count = frontmatter.get("source_count", 0)
            # Convert to int if string
            if isinstance(source_count, str):
                source_count = int(source_count) if source_count.isdigit() else 0
            if source_count != len(sources):
                errors.append(f"{note_path}: source_count ({source_count}) != len(sources) ({len(sources)})")

            # Check sources exist
            for source in sources:
                source_path = self.vault_root / source
                if not source_path.exists():
                    errors.append(f"{note_path}: Source not found: {source}")

            # Check "See also" section has descriptions for all entries
            try:
                with open(note_path) as f:
                    content = f.read()
                see_also_match = re.search(r'## See also\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
                if see_also_match:
                    see_also_text = see_also_match.group(1)
                    # Look for wikilinks without descriptions (missing " — ")
                    wikilink_lines = re.findall(r'^\s*-\s*\[\[([^\]]+)\]\](?:\s|$)', see_also_text, re.MULTILINE)
                    for wikilink in wikilink_lines:
                        # Check if this wikilink line has a description (contains " — ")
                        line_with_link = re.search(r'^\s*-\s*\[\[' + re.escape(wikilink) + r'\]\](.*?)$', see_also_text, re.MULTILINE)
                        if line_with_link and " — " not in line_with_link.group(1):
                            errors.append(f"{note_path}: 'See also' entry [[{wikilink}]] missing description after ' — '")
            except Exception:
                pass

        if errors:
            for error in errors:
                print(f"✗ {error}")
            return 1

        print(f"✓ Lint passed: all compiled notes valid")
        return 0

    def source_scan(self, update: bool = False, accept_covered: bool = False) -> int:
        """List Raw sources and optionally update source-manifest.jsonl."""
        manifest_entries = []

        for source_path in sorted(self.raw_sources.glob("*.md")):
            frontmatter = self._read_frontmatter(source_path)
            if not frontmatter:
                continue

            title = frontmatter.get("Title", source_path.stem)
            processed = frontmatter.get("Processed", False)

            # Find which Wiki notes cover this source
            covered_by = []
            if accept_covered:
                for wiki_note in self.wiki_root.glob("*/*.md"):
                    if wiki_note.name == "index.md":
                        continue
                    wiki_fm = self._read_frontmatter(wiki_note)
                    if wiki_fm and str(source_path) in wiki_fm.get("sources", []):
                        covered_by.append(str(wiki_note.relative_to(self.vault_root)))

            entry = ManifestEntry(
                path=str(source_path.relative_to(self.vault_root)),
                title=title,
                processed=processed,
                covered_by=covered_by,
                updated=datetime.now().strftime("%Y-%m-%d")
            )
            manifest_entries.append(entry)
            print(f"  {source_path.name}: {title} ({'processed' if processed else 'pending'})")

        if update:
            manifest_path = self.schema_root / "source-manifest.jsonl"
            with open(manifest_path, "w") as f:
                for entry in manifest_entries:
                    f.write(json.dumps(asdict(entry)) + "\n")
            print(f"✓ Updated manifest: {len(manifest_entries)} sources")
        else:
            print(f"✓ Found {len(manifest_entries)} sources")

        return 0

    def source_lint(self) -> int:
        """Validate source frontmatter and coverage."""
        errors = []

        for source_path in self.raw_sources.glob("*.md"):
            frontmatter = self._read_frontmatter(source_path)
            if not frontmatter:
                errors.append(f"{source_path.name}: Missing frontmatter")
                continue

            # Check required fields
            required = ["Title", "Author", "Reference", "Created", "Processed", "tags"]
            for field in required:
                if field not in frontmatter:
                    errors.append(f"{source_path.name}: Missing {field}")
                # For Processed, allow boolean False; for others, check they're non-empty
                elif field != "Processed" and not frontmatter[field]:
                    errors.append(f"{source_path.name}: Empty {field}")

            # Check coverage if processed
            if frontmatter.get("Processed"):
                covered = False
                source_relative = str(source_path.relative_to(self.vault_root))
                for wiki_note in self.wiki_root.glob("*/*.md"):
                    if wiki_note.name == "index.md":
                        continue
                    wiki_fm = self._read_frontmatter(wiki_note)
                    if wiki_fm:
                        # Check both relative and absolute path formats
                        sources = wiki_fm.get("sources", [])
                        if source_relative in sources or str(source_path) in sources:
                            covered = True
                            break

                if not covered:
                    errors.append(f"{source_path.name}: Marked processed but has no Wiki coverage")

        if errors:
            for error in errors:
                print(f"✗ {error}")
            return 1

        print(f"✓ Source lint passed")
        return 0

    def source_delta(self) -> int:
        """Show Raw sources not in the manifest."""
        manifest_entries = set()
        manifest_path = self.schema_root / "source-manifest.jsonl"

        if manifest_path.exists():
            with open(manifest_path) as f:
                for line in f:
                    entry = json.loads(line)
                    manifest_entries.add(entry["path"])

        all_sources = {str(p.relative_to(self.vault_root)) for p in self.raw_sources.glob("*.md")}
        delta = all_sources - manifest_entries

        if delta:
            print(f"✓ Sources not in manifest:")
            for source in sorted(delta):
                print(f"  {source}")
        else:
            print(f"✓ All sources in manifest")

        return 0

    def source_coverage(self) -> int:
        """Show which Raw sources are covered by compiled Wiki notes."""
        coverage = {}

        for source_path in sorted(self.raw_sources.glob("*.md")):
            coverage[source_path.name] = []

            for wiki_note in self.wiki_root.glob("*/*.md"):
                if wiki_note.name == "index.md":
                    continue
                wiki_fm = self._read_frontmatter(wiki_note)
                if wiki_fm and str(source_path) in wiki_fm.get("sources", []):
                    coverage[source_path.name].append(wiki_note.relative_to(self.vault_root))

        print(f"✓ Source coverage:")
        for source, covered_by in coverage.items():
            if covered_by:
                print(f"  {source}:")
                for note in covered_by:
                    print(f"    - {note}")
            else:
                print(f"  {source}: (not covered)")

        return 0

    def search_catalog(self, query: str) -> int:
        """Search compiled Wiki notes through the catalog."""
        catalog_path = self.wiki_root / "catalog.jsonl"
        if not catalog_path.exists():
            print(f"✗ Catalog not found. Run 'build' first.")
            return 1

        query_lower = query.lower()
        results = []

        with open(catalog_path) as f:
            for line in f:
                entry = json.loads(line)
                if query_lower in entry["title"].lower() or query_lower in entry["tag"].lower():
                    results.append(entry)

        if results:
            print(f"✓ Found {len(results)} result(s):")
            for entry in results:
                print(f"  {entry['path']}: {entry['title']} ({entry['tag']})")
        else:
            print(f"✓ No results for: {query}")

        return 0

    def log(self, title: str, details: str) -> int:
        """Append a short entry to Wiki/log.md or create if missing."""
        log_path = self.wiki_root / "log.md"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"\n## {title}\n*Logged: {timestamp}*\n\n{details}\n"

        if log_path.exists():
            with open(log_path, "a") as f:
                f.write(entry)
        else:
            with open(log_path, "w") as f:
                f.write(f"# Logs\n{entry}")

        print(f"✓ Logged: {title} ({timestamp})")
        return 0

    def suggest_links(self, note_path: str) -> int:
        """Suggest wikilinks for a note by matching keywords to catalog, with auto-generated descriptions."""
        note_file = self.vault_root / note_path

        if not note_file.exists():
            print(f"✗ Note not found: {note_path}")
            return 1

        catalog_path = self.wiki_root / "catalog.jsonl"
        if not catalog_path.exists():
            print(f"✗ Catalog not found. Run 'build' first.")
            return 1

        # Read the note
        try:
            with open(note_file) as f:
                content = f.read()
        except Exception as e:
            print(f"✗ Error reading note: {e}")
            return 1

        # Extract frontmatter and body
        fm = self._read_frontmatter(note_file)
        note_title = fm.get("title", "") if fm else note_file.stem
        note_sources = fm.get("sources", []) if fm else []

        # Extract keywords from title and topics
        keywords = set()
        keywords.update(note_title.lower().split())
        if fm and fm.get("topics"):
            for topic in fm.get("topics", []):
                keywords.update(topic.lower().split())

        # Extract content keywords (first 1000 chars of body)
        body_start = content.find("---", 3)
        if body_start > 0:
            body_start = content.find("\n", body_start) + 1
            body_text = content[body_start:body_start+1000].lower()
            # Simple word extraction
            words = re.findall(r'\b[a-z]+\b', body_text)
            keywords.update(words[:20])  # Limit to first 20 words

        # Search catalog for matches and generate descriptions
        matches = {}
        try:
            with open(catalog_path) as f:
                for line in f:
                    entry = json.loads(line)
                    entry_path = entry["path"]

                    # Skip self-reference
                    if entry_path == str(note_file.relative_to(self.vault_root)):
                        continue

                    entry_title = entry["title"].lower()
                    entry_name = entry_path.split("/")[-1].replace(".md", "")
                    is_source = entry_path.startswith("Raw/Sources/")

                    # Score based on matches
                    score = 0
                    matched_keywords = []

                    for kw in keywords:
                        if kw in entry_title or kw in entry_name.lower():
                            score += 1
                            matched_keywords.append(kw)

                    if score > 0:
                        # Auto-generate description
                        description = self._extract_description(
                            self.vault_root / entry_path,
                            entry["title"],
                            is_source
                        )
                        matches[entry_path] = {
                            "title": entry["title"],
                            "tag": entry["tag"],
                            "score": score,
                            "keywords": list(set(matched_keywords)),
                            "description": description,
                            "is_source": is_source
                        }
        except Exception as e:
            print(f"✗ Error reading catalog: {e}")
            return 1

        # Sort by score
        sorted_matches = sorted(matches.items(), key=lambda x: x[1]["score"], reverse=True)

        if sorted_matches:
            print(f"✓ Suggested wikilinks for: {note_title}")
            print(f"\nAdd these to your 'See also' section:")

            # Separate sources from concept notes
            concept_matches = [m for m in sorted_matches if not m[1]["is_source"]]
            source_matches = [m for m in sorted_matches if m[1]["is_source"]]

            # Show top 5 concept matches
            for path, info in concept_matches[:5]:
                note_name = path.split("/")[-1].replace(".md", "")
                print(f"  - [[{note_name}]] — {info['description']}")

            # Show source papers if they were in sources
            for path, info in source_matches:
                if path in note_sources:
                    note_name = path.split("/")[-1].replace(".md", "")
                    print(f"  - Source paper: [[{note_name}]] — {info['description']}")

            if len(concept_matches) > 5:
                print(f"\n  (and {len(concept_matches) - 5} more concept matches)")
        else:
            print(f"✓ No related notes found in catalog")

        return 0

    def _extract_description(self, note_path: Path, title: str, is_source: bool = False) -> str:
        """Extract auto-generated description from note's Core Concept or first paragraph."""
        try:
            with open(note_path, encoding='utf-8') as f:
                content = f.read()

            # For sources, use title or first sentence of body
            if is_source:
                # Try to extract first sentence from body
                body_start = content.find("---", 3)
                if body_start > 0:
                    body_start = content.find("\n", body_start) + 1
                    body_text = content[body_start:].strip()
                    # Get first sentence (up to first period/newline)
                    match = re.match(r'^([^.!?\n]+[.!?]?)', body_text)
                    if match:
                        desc = match.group(1).strip()
                        if len(desc) > 100:
                            desc = desc[:97] + "..."
                        return desc
                return title

            # For wiki concepts, extract from Core Concept section
            core_concept_match = re.search(r'## Core Concept\s*\n\n(.+?)(?=\n## |\Z)', content, re.DOTALL)
            if core_concept_match:
                core_text = core_concept_match.group(1).strip()
                # Remove wikilinks but keep the text
                core_text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', core_text)
                core_text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', core_text)

                # Extract first 1-2 sentences
                sentences = re.split(r'(?<=[.!?])\s+', core_text)
                if sentences:
                    desc = sentences[0]
                    if len(sentences) > 1 and len(desc) < 80:
                        desc = desc + " " + sentences[1]
                    # Limit to ~100 chars
                    if len(desc) > 100:
                        desc = desc[:97] + "..."
                    return desc.strip()

            return title
        except Exception:
            return title

    def _read_frontmatter(self, path: Path) -> Optional[Dict[str, Any]]:
        """Extract YAML frontmatter from a note."""
        try:
            with open(path) as f:
                content = f.read()

            if not content.startswith("---"):
                return None

            end_idx = content.find("---", 3)
            if end_idx == -1:
                return None

            fm_str = content[3:end_idx].strip()
            return self._parse_yaml(fm_str)
        except:
            return None

    def _parse_yaml(self, yaml_str: str) -> Dict[str, Any]:
        """Simple YAML parser for frontmatter."""
        data = {}
        lines = yaml_str.split("\n")
        i = 0

        while i < len(lines):
            line = lines[i]
            stripped = line.strip()

            if not stripped or stripped.startswith("#"):
                i += 1
                continue

            # Only process lines that start without indentation (top-level keys)
            if line and not line[0].isspace() and ":" in line:
                key, value = stripped.split(":", 1)
                key = key.strip()
                value = value.strip()

                # Handle lists starting with []
                if value.startswith("[") and value.endswith("]"):
                    data[key] = json.loads(value)
                    i += 1
                # Handle lists with - syntax (empty value followed by list items)
                elif value == "" or value == "[]":
                    list_items = []
                    i += 1
                    while i < len(lines):
                        next_line = lines[i]
                        if next_line.startswith("  - "):
                            item = next_line[4:].strip().strip('"\'')
                            list_items.append(item)
                            i += 1
                        elif next_line and next_line[0].isspace():
                            i += 1
                        else:
                            break
                    data[key] = list_items
                else:
                    # Handle scalar values (boolean, string, number)
                    if value.lower() == "true":
                        data[key] = True
                    elif value.lower() == "false":
                        data[key] = False
                    else:
                        # Try to parse as number
                        try:
                            if "." in value:
                                data[key] = float(value)
                            else:
                                data[key] = int(value)
                        except (ValueError, AttributeError):
                            data[key] = value.strip('"\'')
                    i += 1
            else:
                i += 1

        return data

    def _read_note_metadata(self, note_path: Path) -> Optional[CatalogEntry]:
        """Extract metadata for catalog entry."""
        frontmatter = self._read_frontmatter(note_path)
        if not frontmatter:
            return None

        title = self._extract_title(note_path)
        tag = frontmatter.get("tags", [""])[0] if frontmatter.get("tags") else ""
        topics = frontmatter.get("topics", [])
        sources = frontmatter.get("sources", [])
        updated = frontmatter.get("updated", datetime.now().strftime("%Y-%m-%d"))

        return CatalogEntry(
            path=str(note_path.relative_to(self.vault_root)),
            title=title,
            tag=tag,
            topics=topics,
            sources=sources,
            updated=updated
        )

    def _extract_title(self, note_path: Path) -> str:
        """Extract title from note."""
        try:
            with open(note_path) as f:
                for line in f:
                    if line.startswith("# "):
                        return line[2:].strip()
            return note_path.stem
        except:
            return note_path.stem


def main():
    tool = WikiTool()

    if len(sys.argv) < 2:
        print("Usage: wiki_tool.py <command> [args]")
        print("Commands: doctor, build, lint, source-scan, source-lint, source-delta, source-coverage, search-catalog, suggest-links, log")
        return 1

    command = sys.argv[1]

    if command == "doctor":
        return tool.doctor()
    elif command == "build":
        return tool.build()
    elif command == "lint":
        return tool.lint()
    elif command == "source-scan":
        update = "--update" in sys.argv
        accept_covered = "--accept-covered" in sys.argv
        return tool.source_scan(update=update, accept_covered=accept_covered)
    elif command == "source-lint":
        return tool.source_lint()
    elif command == "source-delta":
        return tool.source_delta()
    elif command == "source-coverage":
        return tool.source_coverage()
    elif command == "search-catalog":
        query_idx = sys.argv.index("--query") + 1 if "--query" in sys.argv else -1
        if query_idx > 0 and query_idx < len(sys.argv):
            return tool.search_catalog(sys.argv[query_idx])
        else:
            print("Usage: wiki_tool.py search-catalog --query 'search term'")
            return 1
    elif command == "suggest-links":
        note_idx = sys.argv.index("--note") + 1 if "--note" in sys.argv else -1
        if note_idx > 0 and note_idx < len(sys.argv):
            return tool.suggest_links(sys.argv[note_idx])
        else:
            print("Usage: wiki_tool.py suggest-links --note 'path/to/note.md'")
            return 1
    elif command == "log":
        title_idx = sys.argv.index("--title") + 1 if "--title" in sys.argv else -1
        details_idx = sys.argv.index("--details") + 1 if "--details" in sys.argv else -1
        if title_idx > 0 and details_idx > 0:
            return tool.log(sys.argv[title_idx], sys.argv[details_idx])
        else:
            print("Usage: wiki_tool.py log --title 'title' --details 'details'")
            return 1
    else:
        print(f"Unknown command: {command}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
