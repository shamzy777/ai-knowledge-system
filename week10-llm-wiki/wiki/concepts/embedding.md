---
type: wiki-concept
concept_id: embedding
canonical_title: "Embedding（嵌入）"
run_id: RUN-001
source_ids: [S04, S08, S09]
updated_by_runs: [RUN-004]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Embedding.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Embedding（嵌入）

## One-sentence Definition / 一句話定義

An Embedding（嵌入） is a learned dense feature vector used to represent an input item.

Source: S04, pp. 67–85.

## Why It Matters / 為什麼重要

Unlike a pure identity code, a learned representation can support relationships that help a prediction task.

Source: S04, pp. 67–85.

## Source Perspectives / 來源觀點

S09 distinguishes distributional word embeddings from contextual token representations. S08 shows learned token embeddings inside the original Transformer and ties the input and pre-Softmax weights.

Source: S08, p. 5; S09, book pp. 11, 127–148, 177–195.

## Prerequisites / 先備概念

- [[one-hot-encoding]]
- [[neural-network]]

Source basis: S04, pp. 67–85.

## Core Idea / 核心概念

S04 first motivates intermediate neural representations, then shows Word2Vec tasks and a Transformer embedding layer. The slide metaphor that a layer is the computer's “understanding” is treated as pedagogical, not literal.

Source: S04, pp. 67–85.

## Concept Relationships / 概念關係

- contrast: [[one-hot-encoding]] (S04 pp. 67–75).
- cause/effect: [[pretext-task]] can produce useful embeddings (S04 pp. 75–83).
- part-of: [[transformer]] — trainable embedding layer (S04 p. 85).

## Mastery Level / 掌握程度

Unconfirmed. RUN-001 does not infer or change mastery.

## Sources / 來源

- S04 — *Copy of 04LLM只是在猜下一個字？.pdf*, pp. 67–85. Provenance: Course Material.
- S08 — Vaswani et al., *Attention Is All You Need*, p. 5. Provenance: Research Paper.
- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 11, 127–148, 177–195. Provenance: Reliable Educational Reference.
- Read-only permanent match, when listed in frontmatter, was used for identity comparison only and is not counted as an ingested source.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001.
- No model-knowledge supplement has been added.

