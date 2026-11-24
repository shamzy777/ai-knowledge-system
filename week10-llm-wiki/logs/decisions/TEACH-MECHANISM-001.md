# TEACH-MECHANISM-001 — Topic 01 causal teaching decisions

Date: 2026-11-24

## Local decisions

- Section 3 teaches discrete token → token identity → Embedding lookup / learned representation → abstract embedding vector. It does not invent a numeric token ID or numeric embedding dimensions.
- Positional Information remains a separate input combined with Token Embedding before the Transformer.
- Section 5 fixes `it` as the update target, separates Query/Keys comparison from Values, and progressively reveals relevance scores before information combination.
- Section 6 exposes six ordered Self-Attention stages and keeps the intuitive mechanism ahead of the optional formula.
- Section 7 uses four zoom states: Self-Attention → Transformer block → block stack → Transformer model. Positional information is shown at the input boundary, not as a repeated generic block sublayer.
- Section 11 begins without a selected token and runs Prediction → Probability → Selection → Append → Next Context. The selected token first appears at Selection.
- Three prerequisite checkpoints were added after Embedding, Q/K/V, and Self-Attention.

No mastery status or published Wiki content changed.

