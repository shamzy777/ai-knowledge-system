---
type: relationship-semantic-review
run_id: RUN-001
source_id: S04
review_independent_of_structural_lint: true
status: complete-after-workflow-refinement
---

# RUN-001 — Retrospective Independent Relationship Semantic Review

RUN-001 originally passed combined structural lint. After the RUN-002 workflow refinement, its nineteen original rows were assigned stable review IDs in their existing order and checked independently against S04. The original register remains unchanged.

| ID | Original edge | Outcome | Evidence review and direction rationale |
|---|---|---|---|
| R1-001 | Neural Network prerequisite Language Model | accepted | S04 pp. 5, 12–14 implements the taught LM with a neural network. |
| R1-002 | Language Model evolution Large Language Model | accepted | S04 pp. 39–47 frames LLMs as scaled language models. |
| R1-003 | Recurrent Neural Network contrast Transformer | accepted | S04 pp. 24–31 explicitly contrasts sequential recurrence with attention/matrix processing. |
| R1-004 | Recurrent Neural Network application Language Model | accepted | S04 pp. 12, 24–27 applies RNNs to contextual sequence modeling. |
| R1-005 | Transformer application Language Model | accepted | S04 pp. 27–31, 85 applies Transformer mechanisms to language modeling. |
| R1-006 | Query, Key, and Value part-of Self-Attention | accepted | S04 pp. 29–31 places Q/K/V inside self-attention. |
| R1-007 | Self-Attention part-of Transformer | accepted | S04 pp. 28–31 places self-attention inside the taught Transformer. |
| R1-008 | Softmax part-of Self-Attention | accepted | S04 pp. 30–31 uses Softmax on attention scores. |
| R1-009 | Softmax part-of Language Model | accepted | S04 pp. 17–19, 50–52 uses Softmax in the next-unit route. |
| R1-010 | Sampling part-of Language Model | accepted | S04 pp. 53–64 uses sampling in repeated generation. |
| R1-011 | Sampling Strategies application Sampling | rejected | S04 pp. 53–64 supports applying strategies in the language-model decoding route, but the proposed target `Sampling` makes the application direction ambiguous. R1-020 is the separate replacement. |
| R1-012 | One-Hot Encoding contrast Embedding | accepted | S04 pp. 67–75 explicitly contrasts identity coding with learned feature representation. |
| R1-013 | Pretext Task cause/effect Embedding | accepted | S04 pp. 75–83 teaches proxy tasks as the cause of learned representations. |
| R1-014 | Word2Vec application Pretext Task | accepted | S04 pp. 76–83 uses CBOW/Skip-Gram proxy tasks in Word2Vec. |
| R1-015 | Word2Vec cause/effect Embedding | accepted | S04 pp. 77–83 uses Word2Vec training to produce embeddings. |
| R1-016 | Embedding part-of Transformer | accepted | S04 p. 85 places a trainable embedding layer in the Transformer route. |
| R1-017 | Hallucination cause/effect Language Model | rejected | S04 pp. 38–41 supports the reverse direction: generation by the language model can produce unsupported continuation. R1-021 is the separate replacement. |
| R1-018 | Prompt Engineering application Large Language Model | accepted | S04 pp. 100–115 applies prompting to LLM use. |
| R1-019 | LLM Evaluation application Large Language Model | accepted | S04 pp. 88–90 evaluates model/task fit. |
| R1-020 | Sampling Strategies application Language Model | accepted | Replacement for R1-011; S04 pp. 53–64 applies temperature/top-k/top-p in LM decoding. |
| R1-021 | Language Model cause/effect Hallucination | accepted | Replacement for R1-017; S04 pp. 38–41 supports generation as the causal route, with the existing scope caveat retained. |

## Semantic result

- Original proposals accepted: 17.
- Original proposals rejected and returned to staging: R1-011 and R1-017.
- Separately identified replacements accepted: R1-020 and R1-021.
- The original proposal table was not silently rewritten.
