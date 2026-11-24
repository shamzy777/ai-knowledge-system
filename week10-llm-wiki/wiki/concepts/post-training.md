---
type: wiki-concept
concept_id: post-training
canonical_title: "Post-Training（後訓練）"
run_id: RUN-004
source_ids: [S09]
decision: create-new-week10-candidate
parent_match: null
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Post-Training（後訓練）

## One-sentence Definition / 一句話定義

Post-Training（後訓練）adapts a pretrained base model toward instruction following, preferences/alignment, or verifiable task performance. Source: S09, book pp. 16-21, 209-223. Provenance: Reliable Educational Reference.

## Why It Matters / 為什麼重要

Next-token pretraining alone does not specify desired instruction-following or safety behavior; later stages use different datasets and objectives to shape model behavior. Source: S09, book pp. 209-210. Provenance: Reliable Educational Reference.

## Prerequisites / 先備概念

- [[pretraining]], [[large-language-model]], [[cross-entropy]]

## Core Idea / 核心概念

S09 groups instruction tuning/SFT, preference alignment, and reinforcement learning with verifiable rewards as distinct post-training stages; parameter-efficient methods can adapt only a subset of parameters. Source: S09, book pp. 210-223. Provenance: Reliable Educational Reference.

## Concept Relationships / 概念關係

- prerequisite (incoming): [[pretraining]] precedes later behavioral adaptation stages (S09 book pp. 16-21, 209-223).
- part-of: [[large-language-model]] development lifecycle (S09 book pp. 16-21).

## Mastery Level / 掌握程度

Unconfirmed. RUN-004 does not infer or change mastery.

## Sources / 來源

- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 16-21, 209-223. Provenance: Reliable Educational Reference.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001; current method names are attributed to the dated S09 manuscript.
