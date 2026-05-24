# LLM Wiki Ingest Skill

Process Raw sources and compile them into focused, reusable Wiki notes.

## When to Use

- User adds a new Raw source to `Raw/Sources/`
- User asks to compile or process a source
- User wants to extract knowledge from raw material

## Workflow

1. **Search the catalog** for existing notes related to the source topic
   ```bash
   python3 scripts/wiki_tool.py search-catalog --query "related topic"
   ```

2. **Read the Raw source** and identify key claims, definitions, and connections

3. **Open relevant compiled notes** from the search results to avoid duplication

4. **Create or update Wiki notes** with focused content:
   - Create one topic note (if needed) for the domain
   - Create concept notes for key ideas
   - Create entity notes for important people/organizations
   - Create project notes for initiatives mentioned

5. **Link sources** to compiled notes:
   - Add the Raw source path to `sources` in each compiled note's frontmatter
   - Update `source_count` to match the number of sources

6. **Run maintenance checks**:
   ```bash
   python3 scripts/wiki_tool.py build
   python3 scripts/wiki_tool.py lint
   python3 scripts/wiki_tool.py source-scan --update --accept-covered
   python3 scripts/wiki_tool.py source-lint
   ```

7. **Commit** with a message like:
   ```
   Ingest: Compile [Source Title] into [list of new/updated notes]
   ```

## Guidelines

- Keep compiled notes focused and reusable (not copies of the source)
- Every claim must be traceable to a source
- Use internal wikilinks to connect related concepts
- One Raw source can contribute to multiple Wiki notes
- Multiple Raw sources can support a single Wiki note

## Output

After successful ingest:

- Updated or new files in `Wiki/Topics/`, `Wiki/Concepts/`, `Wiki/Entities/`, `Wiki/Projects/`
- Updated `Schema/source-manifest.jsonl` (source marked as processed)
- Updated `Wiki/catalog.jsonl` (new/updated notes indexed)
- All maintenance checks passing
