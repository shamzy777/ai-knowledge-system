---
type: staging-concept
concept_id: hyperparameter
canonical_title: "Hyperparameter（超參數）"
run_id: RUN-003
source_ids: [S01, S06, S07]
decision: create-new-week10-candidate
parent_match: null
publication_status: staging
mastery_status: unconfirmed
---

# Hyperparameter（超參數）

## One-sentence Definition / 一句話定義

A Hyperparameter（超參數）is a training/model setting selected outside the learned weights, such as batch size, epoch count, or architecture choices. Source: S01 pp. 1–2; S07 full image.

## Why It Matters / 為什麼重要

Hyperparameter choices change training behavior and can be compared through validation results and logged runs. Source: S06 pp. 72–86; S07 full image.

## Prerequisites / 先備概念

- [[neural-network-training]], [[training-validation-and-test-sets]]

## Core Idea / 核心概念

The sources distinguish learned parameters from externally chosen settings and show HParams/TensorBoard as one comparison workflow. Source: S01 pp. 1–2; S06 pp. 72–86; S07 full image.

## Concept Relationships / 概念關係

- part-of: [[neural-network-training]] configuration (S01 pp. 1–2; S06 pp. 72–86).
- application (incoming): [[tensorboard]] records and compares hyperparameter runs (S06 pp. 72–86).

## Mastery Level / 掌握程度

Unconfirmed. RUN-003 does not infer or change mastery.

## Sources / 來源

- S01, pp. 1–2; S06, pp. 72–86; S07, full image. Provenance: Course Material.

## Staging Notes / 暫存說明

- S01/S07 are handwriting corroboration only. Unpublished; no model-knowledge supplement added.
