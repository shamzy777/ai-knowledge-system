---
type: staging-concept
concept_id: pretraining
canonical_title: "Pretraining（預訓練）"
run_id: RUN-004
source_ids: [S09]
decision: create-new-week10-candidate
parent_match: null
publication_status: staging
mastery_status: unconfirmed
---

# Pretraining（預訓練）

## One-sentence Definition / 一句話定義

Pretraining（預訓練）learns general model parameters from a large corpus before task- or preference-oriented post-training; for a causal LLM, S09 teaches self-supervised next-token prediction. Source: S09, book pp. 16-18, 201-203. Provenance: Reliable Educational Reference.

## Why It Matters / 為什麼重要

It connects tokenized corpora, next-token targets, cross-entropy, backpropagation, and Transformer weights into one scalable learning stage. Source: S09, book pp. 201-203. Provenance: Reliable Educational Reference.

## Prerequisites / 先備概念

- [[tokenization]], [[language-model]], [[transformer]], [[cross-entropy]], [[neural-network-training]]

## Core Idea / 核心概念

The natural next token supplies the target, so no separate human gold labels are required; the loss updates embeddings, attention, feed-forward, and other weights. Source: S09, book pp. 201-202. Provenance: Reliable Educational Reference.

## Concept Relationships / 概念關係

- application: [[neural-network-training]] for causal [[language-model]] learning (S09 book pp. 201-203).
- prerequisite: [[post-training]] (S09 book pp. 16-21, 209-210).

## Mastery Level / 掌握程度

Unconfirmed. RUN-004 does not infer or change mastery.

## Sources / 來源

- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 16-18, 201-203. Provenance: Reliable Educational Reference.

## Staging Notes / 暫存說明

- Unpublished; this page describes the S09 causal-LLM route and does not claim every pretraining objective is next-token prediction.
