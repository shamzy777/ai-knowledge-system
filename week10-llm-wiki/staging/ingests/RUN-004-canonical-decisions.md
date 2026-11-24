---
type: canonical-decision-register
run_id: RUN-004
source_ids: [S08, S09]
status: complete
publication_status: unpublished
---

# RUN-004 — Canonical decisions

## New independently justified concepts

| Concept | Decision | Parent comparison | Evidence basis |
|---|---|---|---|
| Tokenization | create staging shadow | Permanent `Tokenization.md` matched read-only | S09 book pp. 33–47 |
| Byte-Pair Encoding | create new Week 10 candidate | No same-meaning staging or parent page found | S09 book pp. 42–46 |
| Multi-Head Attention | create new Week 10 candidate | Distinct mechanism from generic Self-Attention | S08 pp. 4–5; S09 pp. 183–184 |
| Positional Encoding | create new Week 10 candidate | Distinct order-representation mechanism | S08 p. 6; S09 pp. 191–193 |
| Pretraining | create new Week 10 candidate | Distinct training lifecycle stage | S09 pp. 16–18, 201–203 |
| Post-Training | create new Week 10 candidate | Distinct objectives and datasets after pretraining | S09 pp. 16–21, 209–223 |
| Inference | create new Week 10 candidate | Distinct non-parameter-updating model-use stage | S09 pp. 21–24, 196–201 |

## Existing concepts updated

S08 strengthened Transformer, Self-Attention, Query/Key/Value, Embedding, Softmax, and Recurrent Neural Network. S09 strengthened Transformer, Self-Attention, Query/Key/Value, Embedding, Language Model, Large Language Model, Sampling, Sampling Strategies, Softmax, Cross Entropy, Word2Vec, Prompt Engineering, LLM Evaluation, Hallucination, and Neural Network Training.

## Duplicate candidates avoided

- Scaled Dot-Product Attention was retained inside Self-Attention; it did not receive a duplicate page at the approved beginner granularity.
- Transformer Block was retained inside Transformer.
- Causal/Autoregressive Language Model was retained as a source perspective on Language Model.
- Decoding was represented through Inference plus Sampling and Sampling Strategies.
- Instruction Tuning, preference alignment, parameter-efficient adaptation, and RL with verifiable rewards remain scoped sections within Post-Training until deeper independent coverage justifies pages.
- Token/Subword were retained inside Tokenization; BPE received a page because S09 supplies an independent algorithmic mechanism.
- Language-model output head remains within Language Model/Transformer rather than becoming a thin page.

## Isolation decision

All changes are Week 10 staging-only. The permanent Knowledge System was searched for identity comparison and not modified. No page was written to `wiki/` or `teaching/`, and no mastery value was inferred.
