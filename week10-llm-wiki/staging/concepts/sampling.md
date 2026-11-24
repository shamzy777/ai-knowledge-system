---
type: staging-concept
concept_id: sampling
canonical_title: "Sampling（取樣）"
run_id: RUN-001
source_ids: [S04, S03, S09]
updated_by_runs: [RUN-002, RUN-004]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Sampling.md"
publication_status: staging
mastery_status: unconfirmed
---

# Sampling（取樣）

## One-sentence Definition / 一句話定義

Sampling（取樣） selects an outcome according to a probability distribution rather than always choosing the highest-probability item.

Source: S04, pp. 53–64.

## Source Perspectives / 來源觀點

S03 contrasts argmax with probability sampling: the same Softmax distribution can be used for a fixed classification choice or a variable generated choice. It also distinguishes GAN randomness at latent input from language-model randomness at output selection.

Source: S03, pp. 93–96.

S09 places sampling inside decoding at inference time and contrasts random sampling with greedy selection before introducing temperature, top-k, and top-p restrictions.

Source: S09, book pp. 196–201.

## Why It Matters / 為什麼重要

It turns a language model's distribution into varied next-unit choices while preserving the possibility of lower-probability outputs.

Source: S04, pp. 53–64.

## Prerequisites / 先備概念

- [[softmax]]
- Probability distribution（機率分布）

Source basis: S04, pp. 53–64.

## Core Idea / 核心概念

S04 uses a `[0.70, 0.29, 0.01]` example and stresses that low-probability candidates remain possible unless the candidate set is restricted.

Source: S04, pp. 53–64.

## Concept Relationships / 概念關係

- part-of: [[language-model]] — selects the next unit during repeated generation (S04 pp. 53–64).
- application: [[sampling-strategies]] — modifies randomness and candidate scope (S04 pp. 53–64).
- prerequisite: [[distribution]] — sampling requires probabilities over outcomes (S03 pp. 93–96).
- contrast: [[latent-vector]] — two different locations for introducing generative variation (S03 pp. 93–96).

## Mastery Level / 掌握程度

Unconfirmed. RUN-001 does not infer or change mastery.

## Sources / 來源

- S04 — *Copy of 04LLM只是在猜下一個字？.pdf*, pp. 53–64. Provenance: Course Material.
- S03 — *Copy of 03AI為什麼每次都不一樣？.pdf*, pp. 93–96. Provenance: Course Material.
- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 196–201. Provenance: Reliable Educational Reference.
- Read-only permanent match, when listed in frontmatter, was used for identity comparison only and is not counted as an ingested source.

## Staging Notes / 暫存說明

- Unpublished Week 10 staging draft.
- No model-knowledge supplement has been added.

