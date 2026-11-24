---
type: staging-concept
concept_id: kl-divergence
canonical_title: "KL Divergence（KL 散度）"
run_id: RUN-002
source_ids: [S03]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/KL Divergence.md"
publication_status: staging
mastery_status: unconfirmed
---

# KL Divergence（KL 散度）

## One-sentence Definition / 一句話定義

KL Divergence（KL 散度） measures the discrepancy from target distribution `P` to comparison distribution `Q` as `H(P,Q)-H(P)`.

Source: S03, pp. 84–87.

## Why It Matters / 為什麼重要

Unlike cross entropy, it reaches zero when the compared distributions match, and S03 connects it to learning from soft targets.

Source: S03, pp. 84–92.

## Prerequisites / 先備概念

- [[distribution]]
- [[entropy]]
- [[cross-entropy]]

Source basis: S03, pp. 84–87.

## Core Idea / 核心概念

S03 visually derives `D_KL(P||Q)=H(P,Q)-H(P)` and notes that the direction from `P` to `Q` is explicit in the notation.

Source: S03, pp. 84–87.

## Concept Relationships / 概念關係

- application: [[knowledge-distillation]] for soft-target comparison (S03 pp. 88–92).

## Mastery Level / 掌握程度

Unconfirmed. RUN-002 does not infer or change mastery.

## Sources / 來源

- S03 — *Copy of 03AI為什麼每次都不一樣？.pdf*, pp. 84–92. Provenance: Course Material.

## Staging Notes / 暫存說明

- Unpublished Week 10 staging draft; no model-knowledge supplement has been added.
