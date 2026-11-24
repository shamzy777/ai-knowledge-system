---
type: staging-concept
concept_id: knowledge-distillation
canonical_title: "Knowledge Distillation（知識蒸餾）"
run_id: RUN-002
source_ids: [S03]
decision: create-new-week10-candidate
parent_match: null
publication_status: staging
mastery_status: unconfirmed
---

# Knowledge Distillation（知識蒸餾）

## One-sentence Definition / 一句話定義

Knowledge Distillation（知識蒸餾） trains a student model using a teacher model's output distribution as a soft target.

Source: S03, pp. 88–92.

## Why It Matters / 為什麼重要

The student can learn class relationships and uncertainty that are absent from a single one-hot answer.

Source: S03, pp. 88–92.

## Prerequisites / 先備概念

- [[hard-and-soft-targets]]
- [[kl-divergence]]

Source basis: S03, pp. 88–92.

## Core Idea / 核心概念

S03 distinguishes a teacher and student network, then uses the teacher's distribution as the student's training target; it recommends considering KL divergence for comparing soft targets.

Source: S03, pp. 88–92.

## Concept Relationships / 概念關係

- application (incoming): [[hard-and-soft-targets]] → Knowledge Distillation (S03 pp. 88–92). The rejected reverse proposal remains in semantic review.
- application (incoming): [[kl-divergence]] → Knowledge Distillation (S03 pp. 88–92).

## Mastery Level / 掌握程度

Unconfirmed. RUN-002 does not infer or change mastery.

## Sources / 來源

- S03 — *Copy of 03AI為什麼每次都不一樣？.pdf*, pp. 88–92. Provenance: Course Material.

## Staging Notes / 暫存說明

- Unpublished Week 10 staging candidate; no model-knowledge supplement has been added.
- No read-only permanent canonical file was found under this title; migration would require a fresh duplicate/meaning review.
