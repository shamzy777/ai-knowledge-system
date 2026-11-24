---
type: staging-concept
concept_id: hard-and-soft-targets
canonical_title: "Hard and Soft Targets（硬目標與軟目標）"
run_id: RUN-002
source_ids: [S03]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Hard and Soft Targets.md"
publication_status: staging
mastery_status: unconfirmed
---

# Hard and Soft Targets（硬目標與軟目標）

## One-sentence Definition / 一句話定義

A hard target assigns all mass to one class, while a soft target preserves a distribution across classes.

Source: S03, pp. 88–92.

## Why It Matters / 為什麼重要

Soft targets can preserve similarity and uncertainty information that a one-hot label discards.

Source: S03, pp. 88–92.

## Prerequisites / 先備概念

- [[one-hot-encoding]]
- [[distribution]]

Source basis: S03, pp. 88–92.

## Core Idea / 核心概念

S03 uses one-hot labels as hard targets and a teacher model's output distribution as the soft target used to train a student.

Source: S03, pp. 88–92.

## Concept Relationships / 概念關係

- contrast: [[one-hot-encoding]] with a distributed target (S03 pp. 88–92).
- application: [[knowledge-distillation]] (S03 pp. 88–92).

## Mastery Level / 掌握程度

Unconfirmed. RUN-002 does not infer or change mastery.

## Sources / 來源

- S03 — *Copy of 03AI為什麼每次都不一樣？.pdf*, pp. 88–92. Provenance: Course Material.

## Staging Notes / 暫存說明

- Unpublished Week 10 staging draft; no model-knowledge supplement has been added.
