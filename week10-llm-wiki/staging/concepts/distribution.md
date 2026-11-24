---
type: staging-concept
concept_id: distribution
canonical_title: "Distribution（機率分布）"
run_id: RUN-002
source_ids: [S03, S02, S05, S06]
updated_by_runs: [RUN-003]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Distribution.md"
publication_status: staging
mastery_status: unconfirmed
---

# Distribution（機率分布）

## One-sentence Definition / 一句話定義

A Probability Distribution（機率分布） assigns relative probability mass or density across possible outcomes.

Source: S03, pp. 24–32, 61–64, 93–96.

## Source Perspectives / 來源觀點

S02 illustrates a normalized class distribution from Softmax; S05 connects predicted probabilities to cross-entropy formulas; S06 uses the resulting distribution in multiclass implementation and argmax decoding.

Source: S02, pp. 15–20; S05, pp. 16–20, 33–35; S06, pp. 59–89.

## Why It Matters / 為什麼重要

Distributions connect model scores, uncertainty, sampling, GAN training, and measures such as entropy and KL divergence.

Source: S03, pp. 24–32, 61–87, 93–96.

## Prerequisites / 先備概念

- Probability（機率）
- Possible outcomes（可能結果）

Source basis: S03, pp. 24–32, 61–64.

## Core Idea / 核心概念

S03 uses `p_z`, `p_data`, and `p_g` for GANs and `P`/`Q` for target and predicted distributions. Softmax provides a discrete distribution from scores, after which a system may take argmax or sample.

Source: S03, pp. 24–32, 61–64, 76–87, 93–96.

## Concept Relationships / 概念關係

- prerequisite: [[sampling]], [[entropy]], [[cross-entropy]], and [[kl-divergence]] (S03 pp. 61–87, 93–96).
- cause/effect (incoming): [[softmax]] → Distribution (S03 pp. 61–64, 96).
- prerequisite: [[classification]] — predicted class probabilities are interpreted as a distribution (S02 pp. 15–20; S06 pp. 59–89); separately reviewed replacement for the legacy page-only edge.

## Mastery Level / 掌握程度

Unconfirmed. RUN-002 does not infer or change mastery.

## Sources / 來源

- S03 — *Copy of 03AI為什麼每次都不一樣？.pdf*, pp. 24–32, 61–87, 93–96. Provenance: Course Material.
- S02 — *02神經網路的概念.pdf*, pp. 15–20. Provenance: Course Material.
- S05 — *06 Concepts of Neural Networks.pdf*, pp. 16–20, 33–35. Provenance: Course Material.
- S06 — *07 Implementation of Neural Networks.pdf*, pp. 59–89. Provenance: Course Material.

## Staging Notes / 暫存說明

- Unpublished Week 10 staging draft; no model-knowledge supplement has been added.
