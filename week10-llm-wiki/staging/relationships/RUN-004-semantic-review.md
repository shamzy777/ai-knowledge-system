---
type: relationship-semantic-review
run_id: RUN-004
source_ids: [S08, S09]
review_independent_of_structural_lint: true
status: complete
---

# RUN-004 — Independent page-grounded semantic review

| ID | Outcome | Evidence/type/direction rationale |
|---|---|---|
| R4-001 | accepted | S09 shows token IDs feeding lookup embeddings; prerequisite direction is supported. |
| R4-002 | accepted | The model predicts units defined by the tokenizer; direction is supported. |
| R4-003 | accepted | BPE is explicitly an algorithm used for tokenization. |
| R4-004 | accepted | Both sources place multi-head attention inside Transformer blocks. |
| R4-005 | accepted | Every head has learned Q/K/V projections. |
| R4-006 | accepted | Both sources place position information in Transformer input representations. |
| R4-007 | accepted-additional-support | Same typed edge as RUN-001; no new edge. |
| R4-008 | accepted-additional-support | Same typed edge as RUN-001; no new edge. |
| R4-009 | accepted-additional-support | S09 grounds the causal Transformer as a language-model architecture. |
| R4-010 | accepted-with-scope | Causal LLM pretraining is an application of the general neural training loop; no claim is made that all training is pretraining. |
| R4-011 | accepted | S09 orders pretraining before post-training. |
| R4-012 | accepted-with-scope | Post-training is part of the LLM development lifecycle taught by S09, not a component of every historical language model. |
| R4-013 | accepted | S09 explicitly distinguishes parameter-updating training from model-use inference. |
| R4-014 | accepted | Sampling is one decoding operation during generative inference. |
| R4-015 | accepted | The named strategies modify decoding during inference. |
| R4-016 | accepted | Prompting supplies inference context without updating weights. |
| R4-017 | accepted-additional-support | Softmax normalizes attention scores; same edge as RUN-001. |
| R4-018 | accepted-additional-support | Softmax converts output logits to a next-token distribution; same edge as RUN-001. |
| R4-019 | accepted | S09 uses next-token cross entropy as the causal pretraining loss. |
| R4-020 | accepted-additional-support | S08 explicitly contrasts recurrence and self-attention architectures. |
| R4-021 | accepted-additional-support | S09 traces language modeling into large neural/Transformer models; same scoped evolution edge. |
| R4-022 | accepted-replacement | Evidence supports language-model generation leading to possible hallucination; the historical reverse direction is not supported. |
| R4-023 | accepted-additional-support | S09 supplies multiple methods for evaluating LLMs. |
| R4-024 | accepted-replacement | Data-split roles are components of the training/evaluation workflow; `part-of` is more precise than the broad symmetric category. |
| R4-025 | accepted-replacement-with-scope | In the cited workflows scaling is performed before fitting; `prerequisite` is supported only for those workflows. |
| R4-026 | accepted-replacement | Softmax is applied as the multiclass output; `application` is more precise than `theory ↔ practice`. |
| R4-027 | accepted-replacement | Cross entropy is applied as classification loss; `application` is more precise than `theory ↔ practice`. |
| R4-028 | accepted-replacement | Probability-distribution interpretation is prerequisite knowledge for the cited classification output. |
| R4-029 | accepted-replacement | TensorBoard is the tool applied to compare hyperparameter runs; direction is tool-to-use. |
| R4-030 | accepted-replacement | S06 applies optimizers while training MLPs; the application direction is supported. |

## Semantic result

- Accepted: 30/30 proposals.
- Additional-source support only: R4-007, R4-008, R4-009, R4-017, R4-018, R4-020, R4-021, R4-023.
- New replacement events: R4-022 and R4-024–R4-030.
- No proposal was silently reversed or relabelled.
