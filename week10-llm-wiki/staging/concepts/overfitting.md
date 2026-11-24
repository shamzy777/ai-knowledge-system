---
type: staging-concept
concept_id: overfitting
canonical_title: "Overfitting（過度擬合）"
run_id: RUN-003
source_ids: [S01, S06, S07]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Overfitting.md"
publication_status: staging
mastery_status: unconfirmed
---

# Overfitting（過度擬合）

## One-sentence Definition / 一句話定義

Overfitting（過度擬合）occurs when training performance continues to improve while performance on unseen/validation data stops improving or worsens. Source: S06 pp. 18–21.

## Why It Matters / 為什麼重要

It motivates validation monitoring, epoch/model selection, and final held-out testing. Source: S06 pp. 18–26; S07 full image.

## Prerequisites / 先備概念

- [[training-validation-and-test-sets]], [[loss-function]]

## Core Idea / 核心概念

S06 makes the pattern visible through diverging training and validation curves. S01/S07 mention the same workflow with lower-confidence handwriting. Source: S01 pp. 2, 4; S06 pp. 18–21; S07 full image.

## Concept Relationships / 概念關係

- cause/effect (incoming): [[epoch-and-batch]] has a scoped link through excessive epochs (S06 pp. 18–21).
- application: [[tensorboard]] can visualize relevant curves (S06 pp. 45–56, 72–86).

## Mastery Level / 掌握程度

Unconfirmed. RUN-003 does not infer or change mastery.

## Sources / 來源

- S01, pp. 2, 4; S06, pp. 18–26; S07, full image. Provenance: Course Material.

## Staging Notes / 暫存說明

- Unpublished; no model-knowledge supplement added.
