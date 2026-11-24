---
type: wiki-concept
concept_id: byte-pair-encoding
canonical_title: "Byte-Pair Encoding（位元組對編碼）"
run_id: RUN-004
source_ids: [S09]
decision: create-new-week10-candidate
parent_match: null
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Supporting
mastery_status: unconfirmed
---

# Byte-Pair Encoding（位元組對編碼）

## One-sentence Definition / 一句話定義

Byte-Pair Encoding（BPE）is a subword-tokenization method whose training phase repeatedly merges frequent adjacent units and whose encoder applies the learned merges to new text. Source: S09, book pp. 42-45. Provenance: Reliable Educational Reference.

## Why It Matters / 為什麼重要

BPE induces a finite vocabulary that can represent frequent longer units while retaining smaller units for unfamiliar strings. Source: S09, book pp. 42-46. Provenance: Reliable Educational Reference.

## Prerequisites / 先備概念

- [[tokenization]]; frequency counts and a training corpus.

## Core Idea / 核心概念

Training begins from small units and adds merged tokens according to corpus frequency; encoding then greedily applies the learned merge order. Source: S09, book pp. 43-45. Provenance: Reliable Educational Reference.

## Concept Relationships / 概念關係

- application: [[tokenization]] (S09 book pp. 42-45).

## Mastery Level / 掌握程度

Unconfirmed. RUN-004 does not infer or change mastery.

## Sources / 來源

- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 42-46. Provenance: Reliable Educational Reference.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001; not Course Material; no model-knowledge supplement added.
