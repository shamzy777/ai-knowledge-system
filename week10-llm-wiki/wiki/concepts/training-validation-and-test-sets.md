---
type: wiki-concept
concept_id: training-validation-and-test-sets
canonical_title: "Training, Validation, and Test Sets（訓練、驗證與測試集）"
run_id: RUN-003
source_ids: [S01, S06, S07]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Training, Validation, and Test Sets.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Training, Validation, and Test Sets（訓練、驗證與測試集）

## One-sentence Definition / 一句話定義

Training data fits parameters, validation data guides model/training choices, and test data estimates final performance after those choices. Source: S06 pp. 3–26, 29–58; S07 full image.

## Why It Matters / 為什麼重要

Separating these roles reduces the risk of mistaking adaptation to seen data for general performance. Source: S06 pp. 18–26; S07 full image.

## Prerequisites / 先備概念

- [[data-preprocessing]], [[neural-network-training]]

## Core Idea / 核心概念

S06 plots training and validation loss and then evaluates a held-out test set; S01/S07 supply handwritten course workflow corroboration. Source: S01 pp. 2–4; S06 pp. 18–26; S07 full image.

## Concept Relationships / 概念關係

- prerequisite: [[overfitting]] detection/interpretation (S06 pp. 18–21).
- part-of: [[neural-network-training]] (S06 pp. 3–26); this is the separately reviewed replacement for R3-018.

## Mastery Level / 掌握程度

Unconfirmed. RUN-003 does not infer or change mastery.

## Sources / 來源

- S01, pp. 2–4; S06, pp. 3–26, 29–58; S07, full image. Provenance: Course Material.

## Publication Notes / 發布說明

- S01/S07 are handwriting corroboration only. Published in the isolated Week 10 Wiki under PUB-GATE-001; no model-knowledge supplement added.
