---
type: staging-concept
concept_id: word2vec
canonical_title: "Word2Vec"
run_id: RUN-001
source_ids: [S04, S09]
updated_by_runs: [RUN-004]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Word2Vec.md"
publication_status: staging
mastery_status: unconfirmed
---

# Word2Vec

## One-sentence Definition / 一句話定義

Word2Vec learns word embeddings through context-prediction tasks.

Source: S04, pp. 76–85.

## Why It Matters / 為什麼重要

It demonstrates how useful representations can emerge from prediction rather than hand-authored semantic features.

Source: S04, pp. 76–85.

## Source Perspectives / 來源觀點

S09 situates Word2Vec within distributional semantics, distinguishes static word embeddings from contextual representations, and discusses intrinsic/extrinsic evaluation and social bias.

Source: S09, book pp. 127–148.

## Prerequisites / 先備概念

- [[embedding]]
- [[pretext-task]]
- Context window（上下文視窗）

Source basis: S04, pp. 76–85.

## Core Idea / 核心概念

S04 presents CBOW as predicting the center word from surrounding words and Skip-Gram as predicting surrounding words from the center word. It then relates learned weight rows to embeddings.

Source: S04, pp. 76–85.

## Concept Relationships / 概念關係

- application: [[pretext-task]] (S04 pp. 76–83).
- cause/effect: [[embedding]] (S04 pp. 77–83).
- contrast: [[transformer]] has its own end-to-end trained embedding layer (S04 p. 85).

## Mastery Level / 掌握程度

Unconfirmed. RUN-001 does not infer or change mastery.

## Sources / 來源

- S04 — *Copy of 04LLM只是在猜下一個字？.pdf*, pp. 76–85. Provenance: Course Material.
- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 127–148. Provenance: Reliable Educational Reference.
- Read-only permanent match, when listed in frontmatter, was used for identity comparison only and is not counted as an ingested source.

## Staging Notes / 暫存說明

- Unpublished Week 10 staging draft.
- No model-knowledge supplement has been added.

