---
type: wiki-concept
concept_id: cross-entropy
canonical_title: "Cross Entropy（交叉熵）"
run_id: RUN-002
source_ids: [S03, S05, S06, S07, S09]
updated_by_runs: [RUN-003, RUN-004]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Cross Entropy.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Cross Entropy（交叉熵）

## One-sentence Definition / 一句話定義

Cross Entropy（交叉熵） measures the expected negative log probability assigned by predicted distribution `Q` to outcomes distributed according to target `P`.

Source: S03, pp. 68–84.

## Source Perspectives / 來源觀點

S05 separates binary cross entropy for binary classification from categorical cross entropy for multiclass classification. S06 implements both routes; S07 handwritten notes corroborate the binary route.

Source: S05, pp. 33–35; S06, pp. 29–89; S07, full image.

S09 connects token-level cross entropy to causal language-model pretraining: the observed next token supplies the target and gradients update Transformer parameters.

Source: S09, book pp. 201–203.

## Why It Matters / 為什麼重要

It is a practical classification loss that penalizes low predicted probability on the target outcome.

Source: S03, pp. 68–83.

## Prerequisites / 先備概念

- [[distribution]]
- [[information]]
- [[entropy]]
- [[softmax]]

Source basis: S03, pp. 61–84.

## Core Idea / 核心概念

For a one-hot target, only the correct-class term remains. When `Q=P`, cross entropy reaches `H(P)`, which need not be zero.

Source: S03, pp. 76–84.

## Concept Relationships / 概念關係

- application: [[loss-function]] (S03 pp. 68–83).
- prerequisite: [[kl-divergence]] through `D_KL(P||Q)=H(P,Q)-H(P)` (S03 pp. 84–87).
- application: [[classification]] — formulas/task selection in S05 and implementations in S06 (S05 pp. 33–35; S06 pp. 29–89); this is the separately reviewed replacement for R3-027.
- application: [[pretraining]] — next-token loss for causal language-model training (S09 book pp. 201–203).

## Mastery Level / 掌握程度

Unconfirmed. RUN-002 does not infer or change mastery.

## Sources / 來源

- S03 — *Copy of 03AI為什麼每次都不一樣？.pdf*, pp. 61–87. Provenance: Course Material.
- S05 — *06 Concepts of Neural Networks.pdf*, pp. 33–35. Provenance: Course Material.
- S06 — *07 Implementation of Neural Networks.pdf*, pp. 29–89. Provenance: Course Material.
- S07 — *AI程式設計-筆記10/6.jpg*, full image. Provenance: Course Material; handwriting uncertainty.
- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 201–203. Provenance: Reliable Educational Reference.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001; no model-knowledge supplement has been added.
