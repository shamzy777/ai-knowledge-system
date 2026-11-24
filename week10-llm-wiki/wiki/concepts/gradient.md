---
type: wiki-concept
concept_id: gradient
canonical_title: "Gradient（梯度）"
run_id: RUN-003
source_ids: [S02, S05]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Gradient.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Gradient（梯度）

## One-sentence Definition / 一句話定義

A Gradient（梯度）collects the loss's partial derivatives with respect to model parameters and points toward local increase. Source: S02 pp. 77–104.

## Why It Matters / 為什麼重要

Optimizers use gradient information, usually stepping in the opposite direction to reduce loss. Source: S02 pp. 77–104; S05 pp. 40–64.

## Prerequisites / 先備概念

- [[loss-function]]; derivatives and partial derivatives.

## Core Idea / 核心概念

The learning rate scales an update derived from gradient information; computing the gradient and applying the optimizer update remain separate roles. Source: S02 pp. 77–104; S05 pp. 40–64.

## Concept Relationships / 概念關係

- prerequisite: [[optimizer]] (S05 pp. 40–64).
- cause/effect (incoming): [[backpropagation]] computes/propagates parameter gradients (S05 p. 5).

## Mastery Level / 掌握程度

Unconfirmed. RUN-003 does not infer or change mastery.

## Sources / 來源

- S02, pp. 77–104; S05, pp. 40–64. Provenance: Course Material.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001; no model-knowledge supplement added.
