---
type: wiki-concept
concept_id: pretext-task
canonical_title: "Pretext Task（代理任務）"
run_id: RUN-001
source_ids: [S04]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Pretext Task.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Supporting
mastery_status: unconfirmed
---

# Pretext Task（代理任務）

## One-sentence Definition / 一句話定義

A Pretext Task（代理任務） is a proxy prediction task designed to make a model learn useful representations rather than directly solve the final application.

Source: S04, pp. 75–83.

## Why It Matters / 為什麼重要

It supplies a learning signal when the desired representation cannot be specified manually.

Source: S04, pp. 75–83.

## Prerequisites / 先備概念

- [[neural-network]]
- Prediction task（預測任務）

Source basis: S04, pp. 75–83.

## Core Idea / 核心概念

S04 explains this through hidden representations and then uses CBOW and Skip-Gram as examples of tasks whose learned weights become embeddings.

Source: S04, pp. 75–83.

## Concept Relationships / 概念關係

- cause/effect: [[embedding]] — the proxy task trains the representation (S04 pp. 75–83).
- application: [[word2vec]] — CBOW and Skip-Gram as concrete pretext tasks (S04 pp. 76–83).

## Mastery Level / 掌握程度

Unconfirmed. RUN-001 does not infer or change mastery.

## Sources / 來源

- S04 — *Copy of 04LLM只是在猜下一個字？.pdf*, pp. 75–83. Provenance: Course Material.
- Read-only permanent match, when listed in frontmatter, was used for identity comparison only and is not counted as an ingested source.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001.
- No model-knowledge supplement has been added.

