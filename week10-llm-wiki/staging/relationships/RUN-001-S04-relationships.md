---
type: staged-relationship-register
run_id: RUN-001
source_id: S04
status: validated-staging
publication_status: unpublished
---

# RUN-001 — Proposed Relationships

Only the approved relationship vocabulary is used.

| From | Relationship | To | Source support |
|---|---|---|---|
| Neural Network | prerequisite | Language Model | S04 pp. 5, 12–14 |
| Language Model | evolution | Large Language Model | S04 pp. 39–47 |
| Recurrent Neural Network | contrast | Transformer | S04 pp. 24–31 |
| Recurrent Neural Network | application | Language Model | S04 pp. 12, 24–27 |
| Transformer | application | Language Model | S04 pp. 27–31, 85 |
| Query, Key, and Value | part-of | Self-Attention | S04 pp. 29–31 |
| Self-Attention | part-of | Transformer | S04 pp. 28–31 |
| Softmax | part-of | Self-Attention | S04 pp. 30–31 |
| Softmax | part-of | Language Model | S04 pp. 17–19, 50–52 |
| Sampling | part-of | Language Model | S04 pp. 53–64 |
| Sampling Strategies | application | Sampling | S04 pp. 53–64 |
| One-Hot Encoding | contrast | Embedding | S04 pp. 67–75 |
| Pretext Task | cause/effect | Embedding | S04 pp. 75–83 |
| Word2Vec | application | Pretext Task | S04 pp. 76–83 |
| Word2Vec | cause/effect | Embedding | S04 pp. 77–83 |
| Embedding | part-of | Transformer | S04 p. 85 |
| Hallucination | cause/effect | Language Model | S04 pp. 38–41; relationship is course-framed and must retain its caveat |
| Prompt Engineering | application | Large Language Model | S04 pp. 100–115 |
| LLM Evaluation | application | Large Language Model | S04 pp. 88–90 |

## Relationship caveats

- `Hallucination cause/effect Language Model` does not mean every generated statement is factually false. S04 explicitly distinguishes creative, true, false, and truth-neutral outputs.
- The S04 RNN/Transformer contrast concerns sequential recurrence versus matrix-based attention processing; it is not a complete architecture comparison.
- No cross-course relationship is claimed because RUN-001 contains only S04.
