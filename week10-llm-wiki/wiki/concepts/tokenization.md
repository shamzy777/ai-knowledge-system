---
type: wiki-concept
concept_id: tokenization
canonical_title: "Tokenization（詞元化）"
run_id: RUN-004
source_ids: [S09]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Tokenization.md"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
publication_class: Core
mastery_status: unconfirmed
---

# Tokenization（詞元化）

## One-sentence Definition / 一句話定義

Tokenization（詞元化）segments running text into a deterministic sequence of tokens used by downstream language-processing models. Source: S09, book pp. 33-47. Provenance: Reliable Educational Reference.

## Why It Matters / 為什麼重要

The token inventory determines sequence length, unknown-unit handling, vocabulary identity, and what a language model predicts. Different tokenization can also make perplexity comparisons misleading. Source: S09, book pp. 42-47, 203. Provenance: Reliable Educational Reference.

## Prerequisites / 先備概念

- Unicode/text representation and vocabulary identity.

## Core Idea / 核心概念

Words, morphemes, and characters each have boundary or granularity problems. Modern systems commonly use data-driven subword units, but excessive fragmentation can lengthen contexts and weaken representation quality, especially across languages. Source: S09, book pp. 33-47. Provenance: Reliable Educational Reference.

## Concept Relationships / 概念關係

- prerequisite: [[embedding]] and [[language-model]] (S09 book pp. 11, 42-47, 177).
- part-of (incoming): [[byte-pair-encoding]] is one Tokenization method (S09 book pp. 42-45).

## Mastery Level / 掌握程度

Unconfirmed. RUN-004 does not infer or change mastery.

## Sources / 來源

- S09 — *Speech and Language Processing*, 3rd ed. draft, book pp. 33-47, 203. Provenance: Reliable Educational Reference.

## Publication Notes / 發布說明

- Published in the isolated Week 10 Wiki under PUB-GATE-001; not Course Material; no model-knowledge supplement added.
- Week 10 canonical Chinese term: `詞元化`. Other translations such as `分詞` or `斷詞` may appear in other contexts, but they are not the primary label in this Wiki.
