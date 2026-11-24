---
type: staging-concept
concept_id: recurrent-neural-network
canonical_title: "Recurrent Neural Network（循環神經網路）"
run_id: RUN-001
source_ids: [S04, S08]
updated_by_runs: [RUN-004]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Recurrent Neural Network.md"
publication_status: staging
mastery_status: unconfirmed
---

# Recurrent Neural Network（循環神經網路）

## One-sentence Definition / 一句話定義

A Recurrent Neural Network（循環神經網路, RNN） passes a previous hidden state into the current computation so earlier sequence information can affect later outputs.

Source: S04, pp. 12, 24–27.

## Why It Matters / 為什麼重要

It provides one way to represent context when the current text unit alone cannot determine the next continuation.

Source: S04, pp. 12, 24–27.

## Source Perspectives / 來源觀點

S08 uses recurrence as the principal architectural contrast for motivating the Transformer's constant sequential-operation path and shorter dependency paths.

Source: S08, pp. 1–2, 6–7.

## Prerequisites / 先備概念

- [[neural-network]]
- Sequence context（序列上下文）

Source basis: S04, pp. 12, 24–27.

## Core Idea / 核心概念

S04 shows the recurrence `(x_t, h_{t-1}) → h_t` and emphasizes that each step depends on the previous step, limiting parallel execution.

Source: S04, pp. 12, 24–27.

## Concept Relationships / 概念關係

- contrast: [[transformer]] — sequential recurrence versus attention-based matrix processing (S04 pp. 24–31).
- application: [[language-model]] — carries preceding context for next-unit prediction (S04 pp. 12, 24–27).

## Mastery Level / 掌握程度

Unconfirmed. RUN-001 does not infer or change mastery.

## Sources / 來源

- S04 — *Copy of 04LLM只是在猜下一個字？.pdf*, pp. 12, 24–27. Provenance: Course Material.
- S08 — Vaswani et al., *Attention Is All You Need*, pp. 1–2, 6–7. Provenance: Research Paper.
- Read-only permanent match, when listed in frontmatter, was used for identity comparison only and is not counted as an ingested source.

## Staging Notes / 暫存說明

- Unpublished Week 10 staging draft.
- No model-knowledge supplement has been added.

