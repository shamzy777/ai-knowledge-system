---
type: wiki-concept
concept_id: query-key-and-value
canonical_title: "Query, Key, and Value（查詢、鍵、值）"
run_id: RUN-001
source_ids: [S04, S08, S09]
updated_by_runs: [RUN-004]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Query, Key, and Value.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Query, Key, and Value（查詢、鍵、值）

## One-sentence Definition / 一句話定義

Query, Key, and Value（Q/K/V） are learned linear projections of sequence representations used in self-attention.

Source: S04, pp. 29–31.

## Why It Matters / 為什麼重要

They separate the representation used for comparison from the representation whose information is combined.

Source: S04, pp. 29–31.

## Source Perspectives / 來源觀點

S08 gives the original scaled dot-product and multi-head formulations; S09 supplies a pedagogical causal-attention explanation with the same Q/K/V roles.

Source: S08, pp. 3–5; S09, book pp. 179–184.

## Prerequisites / 先備概念

- [[embedding]]
- Linear transformation（線性轉換）

Source basis: S04, pp. 29–31.

## Core Idea / 核心概念

S04 explicitly shows `q_i = x_i W_Q`, analogous K/V projections, query-key dot products, Softmax weights, and a weighted sum of values.

Source: S04, pp. 29–31.

## Concept Relationships / 概念關係

- part-of: [[self-attention]] — Q/K create scores and V carries combined information (S04 pp. 29–31).
- part-of: [[multi-head-attention]] — every head has learned Q/K/V projections (S08 pp. 4–5; S09 book pp. 183–184).

## Mastery Level / 掌握程度

Unconfirmed. RUN-001 does not infer or change mastery.

## Sources / 來源

- S04 — *Copy of 04LLM只是在猜下一個字？.pdf*, pp. 29–31. Provenance: Course Material.
- S08 — Vaswani et al., *Attention Is All You Need*, pp. 3–5. Provenance: Research Paper.
- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 179–184. Provenance: Reliable Educational Reference.
- Read-only permanent match, when listed in frontmatter, was used for identity comparison only and is not counted as an ingested source.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001.
- No model-knowledge supplement has been added.

