---
type: staging-concept
concept_id: inference
canonical_title: "Inference（推論）"
run_id: RUN-004
source_ids: [S09]
decision: create-new-week10-candidate
parent_match: null
publication_status: staging
mastery_status: unconfirmed
---

# Inference（推論）

## One-sentence Definition / 一句話定義

Inference（推論）runs a trained model on input context to produce outputs without updating its learned weights. Source: S09, book pp. 16, 21-24. Provenance: Reliable Educational Reference.

## Why It Matters / 為什麼重要

It separates model use from training and connects prompting, probability distributions, decoding, and repeated generation. Source: S09, book pp. 21-24, 196-201. Provenance: Reliable Educational Reference.

## Prerequisites / 先備概念

- [[large-language-model]], [[language-model]], [[softmax]]

## Core Idea / 核心概念

For a causal language model, inference repeatedly conditions on prior context and selects a next token through greedy or sampling-based decoding. Source: S09, book pp. 196-201. Provenance: Reliable Educational Reference.

## Concept Relationships / 概念關係

- contrast: [[neural-network-training]] (S09 book pp. 16, 21).
- part-of (incoming): [[sampling]] and [[sampling-strategies]] are decoding operations within generative inference (S09 book pp. 196-201).
- application: [[prompt-engineering]] supplies inference-time context and instructions (S09 book pp. 21-24).

## Mastery Level / 掌握程度

Unconfirmed. RUN-004 does not infer or change mastery.

## Sources / 來源

- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 16, 21-24, 196-201. Provenance: Reliable Educational Reference.

## Staging Notes / 暫存說明

- Unpublished; not Course Material; no model-knowledge supplement added.
