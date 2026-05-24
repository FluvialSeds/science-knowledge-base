# LLM Wiki Query Skill

Search and retrieve knowledge from the compiled Wiki to answer questions.

## When to Use

- User asks a question about a topic in the Wiki
- User wants to retrieve information from compiled notes
- User needs to cite or verify knowledge from sources

## Workflow

1. **Start with the index**
   ```bash
   cat Wiki/index.md
   ```

2. **Search the catalog** for relevant notes
   ```bash
   python3 scripts/wiki_tool.py search-catalog --query "your topic or question"
   ```

3. **Open the most relevant Wiki notes** from the search results

4. **Open Raw sources only if**:
   - The compiled note lacks sufficient detail
   - You need to verify or provide source-level evidence
   - User explicitly asks for source-level verification

5. **Answer the question** citing both:
   - The compiled Wiki note (for the answer)
   - The Raw source (for traceability)

## Example

**User question**: "What is a transformer in machine learning?"

```bash
python3 scripts/wiki_tool.py search-catalog --query "transformer"
```

Results show `Wiki/Concepts/TransformerArchitecture.md`

→ Open and read the compiled note
→ If sufficient, cite the note
→ If user needs sources, open `Raw/Sources/` files listed in the note

Answer:
> A transformer is... [from Wiki note]
>
> Source: `Wiki/Concepts/TransformerArchitecture.md` (compiled from Raw sources: `transformer-paper.md`, `attention-blog.md`)

## Guidelines

- Prefer compiled Wiki notes over broad Raw context
- Catalog search reduces token usage and speeds up retrieval
- Always cite sources when answering
- Raw sources provide evidence and additional detail

## Output

- Answer to the user's question
- Citation: Wiki note + Raw source(s)
- Relevant wikilinks to related concepts
