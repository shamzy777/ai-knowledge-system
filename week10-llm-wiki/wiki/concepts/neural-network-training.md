---
type: wiki-concept
concept_id: neural-network-training
canonical_title: "Neural Network Training（神經網路訓練）"
run_id: RUN-003
source_ids: [S01, S02, S05, S06, S07, S09]
updated_by_runs: [RUN-004]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Neural Network Training.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Neural Network Training（神經網路訓練）

## One-sentence Definition / 一句話定義

Neural Network Training（神經網路訓練） repeatedly computes predictions and loss, obtains gradients, and updates parameters so the model performs better on its task. Source: S02 pp. 59–104; S05 pp. 5, 14–15, 40–64.

## Why It Matters / 為什麼重要

It connects theory—functions, derivatives, loss—with practice—data splits, batches, epochs, optimizers, and evaluation. Source: S01 pp. 1–2, 6–7; S06 pp. 3–26, 29–89.

## Source Perspectives / 來源觀點

S09 shows causal LLM pretraining as the same general loop at a different scale: tokenized targets, cross-entropy, backpropagation, gradient-based updates, and held-out evaluation.

Source: S09, book pp. 201–203.

## Prerequisites / 先備概念

- [[neural-network]], [[loss-function]], [[gradient]], [[data-preprocessing]]

## Core Idea / 核心概念

The course sources converge on a loop: prepare data, choose architecture and initialization, run forward computation, measure loss, compute learning signals, update parameters, and assess validation/test behavior. Source: S01 pp. 1–2, 6–7; S02 pp. 59–104; S05 pp. 14–15; S06 pp. 3–26.

## Concept Relationships / 概念關係

- part-of: [[neural-network]] (S02 pp. 59–75; S05 pp. 14–15).
- part-of (incoming): [[training-validation-and-test-sets]] structure the workflow (S06 pp. 3–26); this is the separately reviewed replacement for R3-018.
- part-of: [[forward-propagation]], [[loss-function]], [[backpropagation]], and [[optimizer]] (S05 pp. 5, 14–15, 40–64).

## Mastery Level / 掌握程度

Unconfirmed. RUN-003 does not infer or change mastery.

## Sources / 來源

- S01, pp. 1–2, 6–7; S02, pp. 59–104; S05, pp. 5, 14–15, 40–64; S06, pp. 3–26, 29–89; S07, full image. Provenance: Course Material.
- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 201–203. Provenance: Reliable Educational Reference.

## Publication Notes / 發布說明

- S01/S07 are handwriting corroboration only. Published in the isolated Week 10 Wiki under PUB-GATE-001; no model-knowledge supplement added.
