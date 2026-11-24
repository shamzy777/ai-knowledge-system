---
type: wiki-concept
concept_id: transformer
canonical_title: "Transformer（變換器）"
run_id: RUN-001
source_ids: [S04, S08, S09]
updated_by_runs: [RUN-004]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Transformer.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Transformer（變換器）

## One-sentence Definition / 一句話定義

A Transformer is an attention-based sequence architecture built from attention, position-wise feed-forward layers, residual connections, normalization, and explicit position information.

Source: S08, pp. 1–6; S09, book pp. 177–195.

## Source Perspectives / 來源觀點

S08 is primary evidence for the original encoder–decoder Transformer. S09 teaches the causal decoder block used in modern language-model pretraining. These are architecture scope and evolution differences, not conflicting definitions.

Source: S08, pp. 1–6; S09, book pp. 177–195.

## Why It Matters / 為什麼重要

S04 contrasts it with sequential RNN recurrence and uses it as the modern architecture for language-model context processing.

Source: S04, pp. 24–31, 85.

## Prerequisites / 先備概念

- [[neural-network]]
- [[embedding]]
- [[query-key-and-value]]
- [[self-attention]]

Source basis: S04, pp. 24–31, 85.

## Core Idea / 核心概念

S04 introduces the attention core. S08 supplies the original stacked encoder–decoder design, while S09 supplies a beginner-oriented causal block with masked self-attention, feed-forward layers, residual paths, normalization, and positional information.

Source: S04, pp. 24–31, 85; S08, pp. 3–6; S09, book pp. 177–195.

## Concept Relationships / 概念關係

- contrast: [[recurrent-neural-network]] — parallelizable matrix operations versus recurrence (S04 pp. 24–31).
- part-of (incoming): [[self-attention]], [[multi-head-attention]], [[embedding]], and [[positional-encoding]] are components of the architecture (S08 pp. 3–6; S09 book pp. 177–195).
- application: [[language-model]] (S04 pp. 27–31).

## Mastery Level / 掌握程度

Unconfirmed. RUN-001 does not infer or change mastery.

## Sources / 來源

- S04 — *Copy of 04LLM只是在猜下一個字？.pdf*, pp. 24–31, 85. Provenance: Course Material.
- S08 — Vaswani et al., *Attention Is All You Need*, pp. 1–6. Provenance: Research Paper.
- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 177–195. Provenance: Reliable Educational Reference.
- Read-only permanent match, when listed in frontmatter, was used for identity comparison only and is not counted as an ingested source.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001.
- No model-knowledge supplement has been added.

