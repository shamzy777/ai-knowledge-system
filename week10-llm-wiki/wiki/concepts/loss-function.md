---
type: wiki-concept
concept_id: loss-function
canonical_title: "Loss Function（損失函數）"
run_id: RUN-002
source_ids: [S03, S01, S02, S05, S06, S07]
updated_by_runs: [RUN-003]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Loss Function.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Loss Function（損失函數）

## One-sentence Definition / 一句話定義

A Loss Function（損失函數） gives training a numerical objective for comparing predictions with desired behavior.

Source: S03, pp. 61–64, 68–87.

## Source Perspectives / 來源觀點

S02 uses loss as the scalar objective minimized during training; S05 maps task types to MSE, binary cross entropy, and categorical cross entropy; S06 implements those choices in regression and classification. S01/S07 list loss choices in handwritten workflow notes.

Source: S02, pp. 59–75; S05, pp. 33–35; S06, pp. 3–89; S01, pp. 6–7; S07, full image.

## Why It Matters / 為什麼重要

Choosing an objective that matches the task determines what kind of prediction error the model learns to reduce.

Source: S03, pp. 61–64, 68–87.

## Prerequisites / 先備概念

- Prediction（預測）
- Target（目標）
- [[distribution]]

Source basis: S03, pp. 61–64, 68–87.

## Core Idea / 核心概念

S03 contrasts MSE-style numeric error with cross entropy for a probability distribution and then relates cross entropy to KL divergence.

Source: S03, pp. 61–64, 68–87.

## Concept Relationships / 概念關係

- application (incoming): [[cross-entropy]] → Loss Function (S03 pp. 68–83).
- application (incoming): [[kl-divergence]] → Loss Function for distribution comparison (S03 pp. 84–92).
- part-of: [[neural-network-training]] (S02 pp. 59–75; S05 pp. 14–15).
- contrast: [[evaluation-metric]] by optimized-objective versus monitoring role (S05 pp. 33–39).

## Mastery Level / 掌握程度

Unconfirmed. RUN-002 does not infer or change mastery.

## Sources / 來源

- S03 — *Copy of 03AI為什麼每次都不一樣？.pdf*, pp. 61–92. Provenance: Course Material.
- S01 — *AI程式設計 ~9_29 筆記.pdf*, pp. 6–7. Provenance: Course Material; handwriting uncertainty.
- S02 — *02神經網路的概念.pdf*, pp. 59–75. Provenance: Course Material.
- S05 — *06 Concepts of Neural Networks.pdf*, pp. 33–39. Provenance: Course Material.
- S06 — *07 Implementation of Neural Networks.pdf*, pp. 3–89. Provenance: Course Material.
- S07 — *AI程式設計-筆記10/6.jpg*, full image. Provenance: Course Material; handwriting uncertainty.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001; no model-knowledge supplement has been added.
- PUB-GATE-001 treats Squared Error and Cross Entropy as different task/teaching contexts, not a factual contradiction.
