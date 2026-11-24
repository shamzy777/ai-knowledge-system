---
type: wiki-concept
concept_id: weight-initialization
canonical_title: "Weight Initialization（權重初始化）"
run_id: RUN-003
source_ids: [S01, S05]
decision: create-new-week10-candidate
parent_match: null
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Supporting
mastery_status: unconfirmed
---

# Weight Initialization（權重初始化）

## One-sentence Definition / 一句話定義

Weight Initialization（權重初始化）sets a network's starting parameter values before training begins. Source: S05 pp. 21–31.

## Why It Matters / 為什麼重要

Starting scale and symmetry affect how signals and gradients move through layers at the beginning of training. Source: S05 pp. 21–31.

## Prerequisites / 先備概念

- [[weight-and-bias]], [[gradient]]

## Core Idea / 核心概念

S05 introduces constant/random, Glorot/Xavier, and He families; S01 lists initialization as one training component without detailed mechanism. Source: S05 pp. 21–31; S01 p. 7.

## Concept Relationships / 概念關係

- prerequisite: [[neural-network-training]] (S05 pp. 21–31).

## Mastery Level / 掌握程度

Unconfirmed. RUN-003 does not infer or change mastery.

## Sources / 來源

- S01, p. 7; S05, pp. 21–31. Provenance: Course Material.

## Publication Notes / 發布說明

- Avoid turning source heuristics into universal guarantees. Published in the isolated Week 10 Wiki under PUB-GATE-001; no model-knowledge supplement added.
