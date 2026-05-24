# Workflow Examples

Examples of how to process sources and compile them into Wiki notes.

## Example 1: Processing an Article About Neural Networks

### Raw Source

```yaml
---
Title: "An Introduction to Neural Networks"
Author: "Jane Smith"
Reference: "https://example.com/neural-networks-intro"
ContentType:
  - "markdown"
Created: 2024-01-15
Processed: false
tags:
  - "source"
---

# An Introduction to Neural Networks

Neural networks are computational models inspired by biological neurons. 
A network consists of layers of interconnected nodes...

[Full article content]
```

### Compiled Wiki Notes

**Concept Note: Artificial Neural Network**

```yaml
---
tags:
  - "concept"
topics:
  - "[[Machine Learning]]"
status: stable
created: 2024-01-20
updated: 2024-01-20
sources:
  - "Raw/Sources/neural-networks-intro.md"
source_count: 1
aliases:
  - "Neural net"
  - "ANN"
---

# Artificial Neural Network

A computational model with layers of interconnected nodes inspired by biological neurons.

## Structure

- **Input layer**: Receives data
- **Hidden layers**: Process patterns through weighted connections
- **Output layer**: Produces predictions or classifications

## Key Properties

- Learns through backpropagation (weight adjustment)
- Can approximate any continuous function (universal approximation theorem)
- Requires training data and optimization

See also: [[Backpropagation]], [[Deep Learning]]
```

**Log Entry: Source Processing**

```yaml
---
tags:
  - "log"
created: 2024-01-20
updated: 2024-01-20
sources:
  - "Raw/Sources/neural-networks-intro.md"
source_count: 1
---

## 2024-01-20: Neural Networks Article Processed

Compiled "An Introduction to Neural Networks" by Jane Smith into concept and topic notes. Covered foundational definitions of ANNs and key architectural components.
```

## Example 2: Multi-Source Topic Compilation

### Raw Sources

- `Raw/Sources/transformer-paper.md` - Original transformer architecture paper
- `Raw/Sources/attention-mechanism-blog.md` - Blog post explaining attention
- `Raw/Sources/bert-documentation.md` - BERT fine-tuning guide

### Compiled Topic Note

```yaml
---
tags:
  - "topic"
topics: []
status: stable
created: 2024-02-01
updated: 2024-02-05
sources:
  - "Raw/Sources/transformer-paper.md"
  - "Raw/Sources/attention-mechanism-blog.md"
  - "Raw/Sources/bert-documentation.md"
source_count: 3
aliases:
  - "Transformers"
---

# Attention Mechanisms and Transformers

Transformers are neural network architectures based on attention mechanisms that have become foundational to modern NLP.

## Attention Mechanism

The core innovation: instead of processing sequences sequentially, transformers compute attention weights across all positions simultaneously. This allows parallel processing and captures long-range dependencies.

## Transformer Architecture

Key components:
- Multi-head self-attention
- Position-wise feed-forward networks
- Layer normalization
- Positional encodings

## Applications

- [[BERT]] for language understanding
- [[GPT]] for text generation
- Vision transformers for computer vision

## Foundational Concepts

- Query, Key, Value projections
- Scaled dot-product attention
- Multi-head attention
```

Each source contributes different aspects:
- **transformer-paper.md**: Mathematical foundations
- **attention-mechanism-blog.md**: Intuitive explanations
- **bert-documentation.md**: Practical application details

## Example 3: Source Not Yet Processed

### Raw Source (Processed = false)

```yaml
---
Title: "Reinforcement Learning Fundamentals"
Author: "Bob Johnson"
Reference: "rl-fundamentals-2024"
ContentType:
  - "markdown"
Created: 2024-03-10
Processed: false
tags:
  - "source"
---

[Content not yet compiled into Wiki notes]
```

### Next Steps

1. Read and understand the source
2. Search catalog for existing RL-related notes
3. Create or update concept notes (e.g., "Markov Decision Process", "Policy Gradient")
4. Create or update topic note (e.g., "Reinforcement Learning")
5. Update Raw source: `Processed: true`
6. Run maintenance checks
7. Commit with message linking source to new/updated notes

## Validation Checklist

When compiling a source:

- [ ] Every claim in the compiled note has a source reference
- [ ] `sources` list includes all Raw sources that contributed
- [ ] `source_count` equals the length of `sources`
- [ ] No source is marked `Processed: true` without corresponding Wiki coverage
- [ ] All internal wikilinks resolve to existing notes
- [ ] Status field is appropriate (seed/draft/stable/archived)
