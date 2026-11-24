---
type: staging-concept
concept_id: epoch-and-batch
canonical_title: "Epoch and Batch（訓練週期與批次）"
run_id: RUN-003
source_ids: [S01, S02, S05, S06, S07]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Epoch and Batch.md"
publication_status: staging
mastery_status: unconfirmed
---

# Epoch and Batch（訓練週期與批次）

## One-sentence Definition / 一句話定義

A Batch（批次）is a subset processed for an update, while an Epoch（訓練週期）is one pass through the training set. Source: S05 pp. 5–6; S06 pp. 12–21.

## Why It Matters / 為什麼重要

Batch size and epoch count shape the execution of training and the curves used to watch learning and overfitting. Source: S06 pp. 12–21, 62–70; S07 full image.

## Prerequisites / 先備概念

- [[neural-network-training]], [[training-validation-and-test-sets]]

## Core Idea / 核心概念

The sources distinguish full-batch, stochastic, and mini-batch update framings and use epochs as the x-axis for training/validation behavior. Source: S01 p. 6; S05 pp. 5–6; S06 pp. 18–21.

## Concept Relationships / 概念關係

- part-of: [[neural-network-training]] (S05 pp. 5–6; S06 pp. 12–21).
- cause/effect: [[overfitting]] when training continues beyond useful validation behavior (S06 pp. 18–21; scope: epoch component).

## Mastery Level / 掌握程度

Unconfirmed. RUN-003 does not infer or change mastery.

## Sources / 來源

- S01, p. 6; S02, pp. 116–123; S05, pp. 5–6; S06, pp. 12–21, 62–70; S07, full image. Provenance: Course Material.

## Staging Notes / 暫存說明

- Handwriting is corroboration only. Unpublished; no model-knowledge supplement added.
