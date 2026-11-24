---
type: staging-concept
concept_id: classification
canonical_title: "Classification（分類）"
run_id: RUN-003
source_ids: [S01, S02, S05, S06, S07]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Classification.md"
publication_status: staging
mastery_status: unconfirmed
---

# Classification（分類）

## One-sentence Definition / 一句話定義

Classification（分類）maps an input to one or more categorical labels; the batch evidence directly covers binary and mutually exclusive multiclass cases. Source: S02 pp. 7–20, 109–123; S06 pp. 29–89.

## Why It Matters / 為什麼重要

Task structure determines label encoding, output activation, loss, metric, and decoding. Source: S05 pp. 16–20, 33–39; S06 pp. 29–89.

## Prerequisites / 先備概念

- [[data-preprocessing]], [[activation-function]], [[loss-function]]

## Core Idea / 核心概念

Binary practice uses sigmoid and binary cross entropy; the ten-class MNIST practice uses one-hot labels, Softmax, categorical cross entropy, and argmax. S06's “Multi-labels” heading is not promoted because the task is single-label multiclass. Source: S06 pp. 29–89.

## Concept Relationships / 概念關係

- application (incoming): [[multilayer-perceptron]] is used for Classification (S06 pp. 29–89).
- application (incoming): [[softmax]] and [[cross-entropy]] are applied to multiclass outputs and loss (S05 pp. 16–20, 33–35; S06 pp. 59–89); separately reviewed replacements for R3-026/R3-027.
- contrast: [[regression]] (S05 pp. 16–20, 33–39).

## Mastery Level / 掌握程度

Unconfirmed. RUN-003 does not infer or change mastery.

## Sources / 來源

- S01, pp. 1, 3–4; S02, pp. 7–20, 109–123; S05, pp. 16–20, 33–39; S06, pp. 29–89; S07, full image. Provenance: Course Material.

## Staging Notes / 暫存說明

- S06 terminology conflict requires user confirmation before publication treatment. No model-knowledge supplement added.
