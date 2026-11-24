---
type: staging-concept
concept_id: self-attention
canonical_title: "Self-Attention（自注意力）"
run_id: RUN-001
source_ids: [S04, S08, S09]
updated_by_runs: [RUN-004]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Self-Attention.md"
publication_status: staging
mastery_status: unconfirmed
---

# Self-Attention（自注意力）

## One-sentence Definition / 一句話定義

Self-Attention（自注意力） compares queries with keys, normalizes the scores, and uses the resulting weights to combine values.

Source: S04, pp. 29–31.

## Why It Matters / 為什麼重要

It lets each sequence position form a context-dependent representation through relationships with other positions.

Source: S04, pp. 29–31.

## Source Perspectives / 來源觀點

S08 defines scaled dot-product attention and its roles in the original Transformer; S09 re-explains the same mechanism inside a causal masked language-model block.

Source: S08, pp. 3–5; S09, book pp. 179–184.

## Prerequisites / 先備概念

- [[query-key-and-value]]
- [[softmax]]
- [[embedding]]

Source basis: S04, pp. 29–31.

## Core Idea / 核心概念

The visually verified formula on S04 p. 31 is `Attention(Q,K,V)=softmax(QK^T/√d_K)V`. Connector text extraction initially lost the radical, so the original page rendering is the authoritative RUN-001 evidence.

Source: S04, pp. 29–31.

## Concept Relationships / 概念關係

- part-of: [[transformer]] (S04 pp. 28–31).
- part-of (incoming): [[softmax]] normalizes attention scores (S04 pp. 30–31; S08 pp. 3–4).
- application: [[multi-head-attention]] runs multiple projected attention heads in parallel (S08 pp. 4–5; S09 book pp. 183–184).

## Mastery Level / 掌握程度

Unconfirmed. RUN-001 does not infer or change mastery.

## Sources / 來源

- S04 — *Copy of 04LLM只是在猜下一個字？.pdf*, pp. 29–31. Provenance: Course Material.
- S08 — Vaswani et al., *Attention Is All You Need*, pp. 3–5. Provenance: Research Paper.
- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 179–184. Provenance: Reliable Educational Reference.
- Read-only permanent match, when listed in frontmatter, was used for identity comparison only and is not counted as an ingested source.

## Staging Notes / 暫存說明

- Unpublished Week 10 staging draft.
- No model-knowledge supplement has been added.

