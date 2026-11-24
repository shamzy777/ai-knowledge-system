---
type: wiki-concept
concept_id: classification
canonical_title: "Classification（分類）"
run_id: RUN-003
source_ids: [S01, S02, S05, S06, S07]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Classification.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Supporting
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
- contrast: Regression（Deferred; unpublished endpoint）(S05 pp. 16–20, 33–39); retained as a provenance note, not an active published edge.

## Mastery Level / 掌握程度

Unconfirmed. RUN-003 does not infer or change mastery.

## Sources / 來源

- S01, pp. 1, 3–4; S02, pp. 7–20, 109–123; S05, pp. 16–20, 33–39; S06, pp. 29–89; S07, full image. Provenance: Course Material.

## Publication Notes / 發布說明

- Conflict treatment resolved at PUB-GATE-001: the demonstrated MNIST task is mutually exclusive multiclass classification; S06's “Multi-labels” slide title remains an attributed source mismatch. No model-knowledge supplement added.
