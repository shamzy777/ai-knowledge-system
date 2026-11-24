---
type: staged-relationship-register
run_id: RUN-002
source_id: S03
status: semantic-review-complete
publication_status: unpublished
---

# RUN-002 — Proposed Relationships

These are the original proposals. Semantic review does not edit or replace a proposal in place; rejected proposals remain here and any replacement receives a new ID.

| ID | Action | From | Relationship | To | Source support |
|---|---|---|---|---|---|
| R2-001 | add | Softmax | cause/effect | Distribution | S03 pp. 61–64, 96 |
| R2-002 | add | Distribution | prerequisite | Sampling | S03 pp. 93–96 |
| R2-003 | add-source-support | Sampling | part-of | Language Model | S03 pp. 93–96 |
| R2-004 | add | Language Model | application | Generative AI | S03 pp. 96–98 |
| R2-005 | add | Latent Vector | prerequisite | Generative Adversarial Network | S03 pp. 24–32 |
| R2-006 | add | Mode Collapse | cause/effect | Generative Adversarial Network | S03 p. 35 |
| R2-007 | add | Generative Adversarial Network | application | Generative AI | S03 pp. 19–32 |
| R2-008 | add | Generative Adversarial Network | evolution | GAN Variants | S03 pp. 36–58 |
| R2-009 | add | Information | part-of | Entropy | S03 pp. 65–75 |
| R2-010 | add | Entropy | prerequisite | Cross Entropy | S03 pp. 72–84 |
| R2-011 | add | Cross Entropy | prerequisite | KL Divergence | S03 pp. 84–87 |
| R2-012 | add | Knowledge Distillation | application | Hard and Soft Targets | S03 pp. 88–92 |
| R2-013 | add | One-Hot Encoding | part-of | Hard and Soft Targets | S03 pp. 88–92 |
| R2-014 | add | Cross Entropy | application | Loss Function | S03 pp. 68–83 |
| R2-015 | add | KL Divergence | application | Knowledge Distillation | S03 pp. 88–92 |
| R2-016 | add | Generative Adversarial Network | contrast | Language Model | S03 pp. 93–96 |
| R2-017 | add | Generative AI | contrast | Hallucination | S03 pp. 97–98 |
| R2-018 | add | Softmax | prerequisite | Cross Entropy | S03 pp. 61–81 |
| R2-019 | replacement-for-R2-006 | Generative Adversarial Network | cause/effect | Mode Collapse | S03 p. 35 |
| R2-020 | replacement-for-R2-012 | Hard and Soft Targets | application | Knowledge Distillation | S03 pp. 88–92 |

## Pre-structure rejected candidate

`Generative AI contrast Discriminative AI` was not placed in the proposal table because RUN-002 did not justify a standalone Discriminative AI endpoint. The concept distinction remains prose on `generative-ai.md` and in the conflict/scope register.
