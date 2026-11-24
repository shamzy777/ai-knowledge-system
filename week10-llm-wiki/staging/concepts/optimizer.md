---
type: staging-concept
concept_id: optimizer
canonical_title: "Optimizer（最佳化器）"
run_id: RUN-003
source_ids: [S01, S02, S05, S06, S07]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Optimizer.md"
publication_status: staging
mastery_status: unconfirmed
---

# Optimizer（最佳化器）

## One-sentence Definition / 一句話定義

An Optimizer（最佳化器）uses gradient information and an update rule to change trainable parameters toward lower loss. Source: S02 pp. 77–104; S05 pp. 40–64.

## Why It Matters / 為什麼重要

Different optimizers alter update history, scaling, and practical training behavior while serving the same parameter-update role. Source: S05 pp. 40–64.

## Prerequisites / 先備概念

- [[gradient]], [[learning-rate]], [[loss-function]]

## Core Idea / 核心概念

S05 compares SGD, momentum, adaptive methods, RMSprop, and Adam; S06 shows optimizer configuration in working models. S07's family-to-optimizer shorthand is not treated as a universal rule. Source: S05 pp. 40–64; S06 pp. 3–89; S07 full image.

## Concept Relationships / 概念關係

- part-of: [[neural-network-training]] (S05 pp. 14–15, 40–64).
- application: [[multilayer-perceptron]] training (S06 pp. 3–89).

## Mastery Level / 掌握程度

Unconfirmed. RUN-003 does not infer or change mastery.

## Sources / 來源

- S01, pp. 6–7; S02, pp. 77–123; S05, pp. 40–64; S06, pp. 3–89; S07, full image. Provenance: Course Material.

## Staging Notes / 暫存說明

- S01/S07 are handwriting corroboration only. Unpublished; no model-knowledge supplement added.
