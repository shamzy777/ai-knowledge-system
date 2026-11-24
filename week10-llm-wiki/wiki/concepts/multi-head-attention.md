---
type: wiki-concept
concept_id: multi-head-attention
canonical_title: "Multi-Head Attention（多頭注意力）"
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

# Multi-Head Attention（多頭注意力）

## One-sentence Definition / 一句話定義

Multi-Head Attention（多頭注意力）runs multiple learned Q/K/V attention projections in parallel, concatenates their outputs, and applies an output projection. Source: S08, pp. 4-5; S09, book pp. 183-184. Provenance: Research Paper; Reliable Educational Reference.

## Why It Matters / 為什麼重要

Separate heads allow the model to combine information from different representation subspaces and positions while keeping the overall block shape stackable. Source: S08, p. 5; S09, book pp. 178, 183-184. Provenance: Research Paper; Reliable Educational Reference.

## Prerequisites / 先備概念

- [[self-attention]], [[query-key-and-value]]

## Core Idea / 核心概念

Each head has its own learned projections, performs scaled dot-product attention, and yields a value vector; head outputs are concatenated and projected back to the model dimension. Source: S08, pp. 4-5, Fig. 2; S09, book pp. 183-184. Provenance: Research Paper; Reliable Educational Reference.

## Concept Relationships / 概念關係

- part-of: [[transformer]] (S08 pp. 3-5; S09 book pp. 177-184).
- application: [[self-attention]] — the causal block applies self-attention through multiple parallel heads (S09 book pp. 178-184).

## Mastery Level / 掌握程度

Unconfirmed. RUN-004 does not infer or change mastery.

## Sources / 來源

- S08 — Vaswani et al., *Attention Is All You Need*, pp. 4-5. Provenance: Research Paper.
- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 178, 183-184. Provenance: Reliable Educational Reference.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001; provenance categories remain separate; no model-knowledge supplement added.
