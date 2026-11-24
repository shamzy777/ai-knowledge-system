---
type: wiki-concept
concept_id: backpropagation
canonical_title: "Backpropagation（反向傳播）"
run_id: RUN-003
source_ids: [S01, S02, S05]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Backpropagation.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Backpropagation（反向傳播）

## One-sentence Definition / 一句話定義

Backpropagation（反向傳播）propagates loss derivatives backward through a network to obtain parameter gradients. Source: S05 pp. 5, 14–15.

## Why It Matters / 為什麼重要

It supplies gradients to an optimizer but is not itself the optimizer update rule. Source: S05 pp. 5, 40–64; read-only parent identity check.

## Prerequisites / 先備概念

- [[forward-propagation]], [[loss-function]], [[gradient]]

## Core Idea / 核心概念

S02 p. 75 informally merges gradient descent and backpropagation; S05 separates forward/loss/backward computation from optimizer updating. The canonical draft preserves the separated mechanism and flags the course difference. Source: S02 p. 75; S05 pp. 5, 14–15, 40–64.

## Concept Relationships / 概念關係

- part-of: [[neural-network-training]] (S05 pp. 5, 14–15).
- cause/effect: [[gradient]] (S05 p. 5).

## Mastery Level / 掌握程度

Unconfirmed. RUN-003 does not infer or change mastery.

## Sources / 來源

- S01, p. 6 (handwritten vocabulary); S02, p. 75; S05, pp. 5, 14–15, 40–64. Provenance: Course Material.

## Publication Notes / 發布說明

- Conflict treatment resolved at PUB-GATE-001: Backpropagation computes gradients; Optimizer uses them for parameter updates. S02's conflated wording remains attributed. No model-knowledge supplement added.
