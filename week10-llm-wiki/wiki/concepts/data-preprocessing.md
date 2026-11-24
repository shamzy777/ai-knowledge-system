---
type: wiki-concept
concept_id: data-preprocessing
canonical_title: "Data Preprocessing（資料前處理）"
run_id: RUN-003
source_ids: [S01, S06]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Data Preprocessing.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Supporting
mastery_status: unconfirmed
---

# Data Preprocessing（資料前處理）

## One-sentence Definition / 一句話定義

Data Preprocessing（資料前處理）transforms raw data into model-ready inputs and targets through cleaning, encoding, splitting, and scaling. Source: S01 pp. 2–4; S06 pp. 3–12, 29–38, 59–66.

## Why It Matters / 為什麼重要

The model and loss operate on numeric tensors, so data shape, missing values, label representation, and scale affect the training pipeline. Source: S01 pp. 2–4; S06 pp. 3–12.

## Prerequisites / 先備概念

- Raw features, labels, and tabular/image inputs.

## Core Idea / 核心概念

Course examples separate features and targets, impute or encode values, split datasets, scale inputs, and one-hot encode multiclass labels as appropriate. Source: S01 pp. 2–4; S06 pp. 3–12, 29–38, 59–66.

## Concept Relationships / 概念關係

- prerequisite: [[neural-network-training]] (S01 pp. 1–4; S06 pp. 3–12).
- part-of (incoming): [[feature-scaling]] and [[one-hot-encoding]] are specific preprocessing operations (S01 pp. 3–4; S06 pp. 59–66).

## Mastery Level / 掌握程度

Unconfirmed. RUN-003 does not infer or change mastery.

## Sources / 來源

- S01, pp. 1–4; S06, pp. 3–12, 29–38, 59–66. Provenance: Course Material.

## Publication Notes / 發布說明

- S01 handwriting uncertainty preserved. Published in the isolated Week 10 Wiki under PUB-GATE-001; no model-knowledge supplement added.
