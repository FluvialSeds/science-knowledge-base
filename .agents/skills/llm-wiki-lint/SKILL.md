# LLM Wiki Lint Skill

Validate and fix Wiki structure, links, and metadata.

## When to Use

- Before committing changes
- After ingesting a new source
- When checking vault health
- User asks to verify or audit the Wiki

## Workflow

1. **Run the doctor** (non-mutating health check)
   ```bash
   python3 scripts/wiki_tool.py doctor
   ```

2. **Build indexes and catalog**
   ```bash
   python3 scripts/wiki_tool.py build
   ```

3. **Lint compiled notes** (check frontmatter, tags, sources)
   ```bash
   python3 scripts/wiki_tool.py lint
   ```

4. **Lint Raw sources** (check coverage and metadata)
   ```bash
   python3 scripts/wiki_tool.py source-lint
   ```

5. **Fix any errors**:
   - Update frontmatter fields
   - Fix broken wikilinks
   - Add missing source citations
   - Update source_count if sources list changed

6. **Re-run lint** until all checks pass

## Common Issues and Fixes

| Issue | Fix |
|-------|-----|
| `source_count != len(sources)` | Update `source_count` to match the length of `sources` |
| Wikilink `[[Note]]` doesn't resolve | Create the note or fix the filename |
| `sources` list is empty but `source_count > 0` | Remove sources or add them to the list |
| Source marked `Processed: true` but no Wiki coverage | Create Wiki notes or mark `Processed: false` |
| Missing required frontmatter field | Add the field with appropriate value |

## Guidelines

- Run lint after every source ingest
- Run lint before every commit
- Lint catches broken links and unsupported claims
- Address all lint errors before committing

## Output

- All maintenance checks passing (exit code 0)
- Optionally: a report of fixes made
