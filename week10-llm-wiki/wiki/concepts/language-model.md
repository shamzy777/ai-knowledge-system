---
type: wiki-concept
concept_id: language-model
canonical_title: "Language Model（語言模型）"
run_id: RUN-001
source_ids: [S04, S03, S09]
updated_by_runs: [RUN-002, RUN-004]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Language Model.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Language Model（語言模型）

## One-sentence Definition / 一句話定義

A Language Model（語言模型） uses preceding text to score possible next units, converts the scores to a distribution, and repeatedly selects the next unit.

Source: S04, pp. 9–21, 50–64.

## Source Perspectives / 來源觀點

S03 independently frames a language model as reading preceding text, producing a Softmax distribution over the next unit, and sampling from that distribution. Unlike S04, S03 does not add temperature, top-k, or top-p details.

Source: S03, pp. 93–96.

S09 formalizes language modeling as a probability distribution over the next token, connects n-gram and neural approaches, and then places causal Transformer pretraining and decoding on the same path.

Source: S09, book pp. 5–11, 68–88, 177–203.

## Why It Matters / 為什麼重要

This reframes text generation as a repeatable prediction task whose training examples can be derived from existing text.

Source: S04, pp. 9–21, 50–64.

## Prerequisites / 先備概念

- [[neural-network]]
- Numeric text representation（文字的數值表示）
- [[softmax]]
- [[sampling]]

Source basis: S04, pp. 9–21, 50–64.

## Core Idea / 核心概念

S04 illustrates next-item prediction, context-dependent continuation, score generation, Softmax, and repeated sampling. The slides mostly say 字 rather than formally defining tokenization, so this draft does not claim a tokenizer algorithm.

Source: S04, pp. 9–21, 50–64.

## Concept Relationships / 概念關係

- evolution: [[large-language-model]] — scaling the language-model framing (S04 pp. 39–47).
- application: [[recurrent-neural-network]] and [[transformer]] — sequence architectures used to represent context (S04 pp. 12, 24–31).
- part-of: [[softmax]] and [[sampling]] — output-to-next-unit generation pipeline (S04 pp. 17–19, 50–64).
- application: [[generative-ai]] — language generation is one generative use of probability distributions (S03 pp. 96–98).

## Mastery Level / 掌握程度

Unconfirmed. RUN-001 does not infer or change mastery.

## Sources / 來源

- S04 — *Copy of 04LLM只是在猜下一個字？.pdf*, pp. 9–21, 50–64. Provenance: Course Material.
- S03 — *Copy of 03AI為什麼每次都不一樣？.pdf*, pp. 93–98. Provenance: Course Material.
- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 5–11, 68–88, 177–203. Provenance: Reliable Educational Reference.
- Read-only permanent match, when listed in frontmatter, was used for identity comparison only and is not counted as an ingested source.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001.
- No model-knowledge supplement has been added.

