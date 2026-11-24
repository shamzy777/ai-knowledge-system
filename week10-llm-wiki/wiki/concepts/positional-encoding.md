---
type: wiki-concept
concept_id: positional-encoding
canonical_title: "Positional Encoding（位置編碼）"
run_id: RUN-004
source_ids: [S08, S09]
decision: create-new-week10-candidate
parent_match: null
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Positional Encoding（位置編碼）

## One-sentence Definition / 一句話定義

Positional Encoding（位置編碼）adds sequence-position information to token representations so an attention-based model can distinguish order. Source: S08, p. 6; S09, book pp. 191-193. Provenance: Research Paper; Reliable Educational Reference.

## Why It Matters / 為什麼重要

Without recurrence or convolution, token embeddings alone do not encode where each token occurs in the sequence. Source: S08, p. 6. Provenance: Research Paper.

## Prerequisites / 先備概念

- [[tokenization]], [[embedding]], [[transformer]]

## Core Idea / 核心概念

The original Transformer sums sinusoidal position vectors with token embeddings. S09 distinguishes this original choice from learned absolute embeddings and later relative-position approaches. Source: S08, p. 6; S09, book pp. 191-193. Provenance: Research Paper; Reliable Educational Reference.

## Concept Relationships / 概念關係

- part-of: [[transformer]] input representation (S08 pp. 3, 6; S09 book pp. 177, 191-193).
- application: [[embedding]] — position information is combined with token representations (S08 p. 6; S09 book pp. 191-193).

## Mastery Level / 掌握程度

Unconfirmed. RUN-004 does not infer or change mastery.

## Sources / 來源

- S08 — Vaswani et al., *Attention Is All You Need*, p. 6. Provenance: Research Paper.
- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 191-193. Provenance: Reliable Educational Reference.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001; later positional methods are S09 perspective, not attributed to S08.
