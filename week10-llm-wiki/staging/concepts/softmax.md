---
type: staging-concept
concept_id: softmax
canonical_title: "Softmax"
run_id: RUN-001
source_ids: [S04, S03, S02, S05, S06, S08, S09]
updated_by_runs: [RUN-002, RUN-003, RUN-004]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Softmax.md"
publication_status: staging
mastery_status: unconfirmed
---

# Softmax

## One-sentence Definition / 一句話定義

Softmax converts a set of scores into non-negative relative values that sum to one.

Source: S04, pp. 17–19, 30–31, 50–58.

## Source Perspectives / 來源觀點

S03 uses the same score-to-distribution mechanism for classification, then distinguishes choosing the maximum-probability class from sampling according to the distribution. It also connects Softmax output to cross-entropy training.

Source: S03, pp. 61–64, 68–71, 93–96.

S02 independently teaches positive normalization for class scores; S05 positions Softmax as a multiclass output activation; S06 implements it with categorical cross entropy and argmax in MNIST.

Source: S02, pp. 15–20, 109–123; S05, pp. 16–20; S06, pp. 59–89.

S08 uses Softmax inside scaled dot-product attention and at the Transformer output. S09 uses it both for attention weights and next-token distributions.

Source: S08, pp. 3–5; S09, book pp. 5–11, 179–184, 196–203.

## Why It Matters / 為什麼重要

Language models use it to turn next-unit scores into a distribution from which generation can select.

Source: S04, pp. 17–19, 30–31, 50–58.

## Prerequisites / 先備概念

- Scores / logits（分數）
- Exponential transformation（指數轉換）

Source basis: S04, pp. 17–19, 30–31, 50–58.

## Core Idea / 核心概念

S04 demonstrates exponentiating scores and dividing by their total. The course's “winner-takes-all” wording is preserved as teaching shorthand, not a universal technical definition.

Source: S04, pp. 17–19, 30–31, 50–58.

## Concept Relationships / 概念關係

- part-of: [[language-model]] — next-unit distribution (S04 pp. 17–19, 50–52).
- part-of: [[self-attention]] — attention-score normalization (S04 pp. 30–31).
- prerequisite: [[sampling]] and [[sampling-strategies]] (S04 pp. 52–64).
- cause/effect: [[distribution]] — normalized discrete output distribution (S03 pp. 61–64, 96).
- prerequisite: [[cross-entropy]] — predicted class distribution used by the loss (S03 pp. 68–81).
- application: [[classification]] — normalized multiclass output in theory and implementation (S02 pp. 15–20, 109–123; S05 pp. 16–20; S06 pp. 59–89); this is the separately reviewed replacement for R3-026.

## Mastery Level / 掌握程度

Unconfirmed. RUN-001 does not infer or change mastery.

## Sources / 來源

- S04 — *Copy of 04LLM只是在猜下一個字？.pdf*, pp. 17–19, 30–31, 50–58. Provenance: Course Material.
- S03 — *Copy of 03AI為什麼每次都不一樣？.pdf*, pp. 61–71, 93–96. Provenance: Course Material.
- S02 — *02神經網路的概念.pdf*, pp. 15–20, 109–123. Provenance: Course Material.
- S05 — *06 Concepts of Neural Networks.pdf*, pp. 16–20. Provenance: Course Material.
- S06 — *07 Implementation of Neural Networks.pdf*, pp. 59–89. Provenance: Course Material.
- S08 — Vaswani et al., *Attention Is All You Need*, pp. 3–5. Provenance: Research Paper.
- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 5–11, 179–184, 196–203. Provenance: Reliable Educational Reference.
- Read-only permanent match, when listed in frontmatter, was used for identity comparison only and is not counted as an ingested source.

## Staging Notes / 暫存說明

- Unpublished Week 10 staging draft.
- No model-knowledge supplement has been added.

