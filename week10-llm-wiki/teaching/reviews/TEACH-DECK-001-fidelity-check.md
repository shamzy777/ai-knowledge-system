---
type: teaching-fidelity-check
deck_id: TEACH-DECK-001
check_node: evidence-mapped-section-draft
status: passed-for-html-render
---

# TEACH-DECK-001 fidelity check

## Section-by-section result

| Slide | Evidence scope | Terminology/relationship fidelity | Result |
|---|---|---|---|
| S1 | LM, LLM, Inference, Sampling | Repeated next-token loop matches Wiki framing. | Pass |
| S2 | Tokenization | Does not claim a specific tokenizer segmentation. | Pass |
| S3 | Embedding, Positional Encoding | Separates learned token vector from position information before combination. | Pass |
| S4 | Embedding, Self-Attention | Uses context-dependent representation without anthropomorphic understanding claims. | Pass |
| S5 | Q/K/V | Preserves learned-projection roles and direction. | Pass |
| S6 | Self-Attention, Softmax | Attention Softmax remains distinct from vocabulary/output Softmax. | Pass |
| S7 | MHA, Transformer, Positional Encoding | Preserves original encoder–decoder versus causal-decoder scope. | Pass |
| S8 | LM, LLM, Inference, Transformer | Uses approved `Language Modeling → LLM → Inference` teaching progression; does not assert that these are identical graph relationship types. | Pass |
| S9 | Softmax, Distribution, LM | Softmax produces a distribution and does not select a token. | Pass |
| S10 | Sampling, Softmax, Inference | Uses only the S04 `[0.70, 0.29, 0.01]` numeric example. | Pass |
| S11 | LM, Inference, Sampling, Hallucination, Evaluation | No Sampling → Hallucination causal claim. Factual grounding remains a separate limitation/evaluation issue. | Pass |

## Quiz fidelity

All six approved answers are supported by the evidence map. Q6 uses the narrower S09 Hallucination definition and does not blame Sampling.

## Provenance fidelity

- S01–S07 remain Course Material.
- S08 remains Research Paper.
- S09 remains Reliable Educational Reference.
- No external, S10, or model-knowledge claim appears in the draft.

## Result

The section draft may proceed to HTML render. A later factual failure must return only to the affected slide and this evidence check.
