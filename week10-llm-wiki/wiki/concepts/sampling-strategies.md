---
type: wiki-concept
concept_id: sampling-strategies
canonical_title: "Sampling Strategies（取樣策略）"
run_id: RUN-001
source_ids: [S04, S09]
updated_by_runs: [RUN-004]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Sampling Strategies.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Sampling Strategies（取樣策略）

## One-sentence Definition / 一句話定義

Sampling Strategies（取樣策略） adjust a language model's next-unit distribution or candidate set before sampling.

Source: S04, pp. 53–64.

## Why It Matters / 為什麼重要

They balance output diversity against the risk of choosing weak candidates.

Source: S04, pp. 53–64.

## Source Perspectives / 來源觀點

S09 independently presents greedy, random, temperature, top-k, and top-p decoding and makes their inference-time role explicit.

Source: S09, book pp. 196–201.

## Prerequisites / 先備概念

- [[sampling]]
- [[softmax]]
- Probability distribution（機率分布）

Source basis: S04, pp. 53–64.

## Core Idea / 核心概念

S04 covers Temperature, Top-k, and Top-p（Nucleus Sampling）. Temperature rescales scores; Top-k keeps a fixed candidate count; Top-p keeps a dynamic set whose cumulative probability crosses a threshold, then renormalizes.

Source: S04, pp. 53–64.

## Concept Relationships / 概念關係

- application: [[sampling]] (S04 pp. 53–64).
- contrast: Top-k uses a fixed count while Top-p uses a dynamic cumulative-probability set (S04 pp. 60–64).

## Mastery Level / 掌握程度

Unconfirmed. RUN-001 does not infer or change mastery.

## Sources / 來源

- S04 — *Copy of 04LLM只是在猜下一個字？.pdf*, pp. 53–64. Provenance: Course Material.
- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 196–201. Provenance: Reliable Educational Reference.
- Read-only permanent match, when listed in frontmatter, was used for identity comparison only and is not counted as an ingested source.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001.
- No model-knowledge supplement has been added.

