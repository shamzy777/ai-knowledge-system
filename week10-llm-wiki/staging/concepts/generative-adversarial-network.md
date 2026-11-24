---
type: staging-concept
concept_id: generative-adversarial-network
canonical_title: "Generative Adversarial Network（生成對抗網路）"
run_id: RUN-002
source_ids: [S03]
decision: create-staging-shadow
parent_match: "/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/Generative Adversarial Network.md"
publication_status: staging
mastery_status: unconfirmed
---

# Generative Adversarial Network（生成對抗網路）

## One-sentence Definition / 一句話定義

A Generative Adversarial Network（GAN，生成對抗網路） trains a Generator and Discriminator in competition so generated samples become harder to distinguish from real data.

Source: S03, pp. 19–32.

## Why It Matters / 為什麼重要

GANs turn distribution matching into a learnable adversarial game and offer a concrete model of generative variability.

Source: S03, pp. 19–32.

## Prerequisites / 先備概念

- [[neural-network]]
- [[latent-vector]]
- [[distribution]]

Source basis: S03, pp. 19–32.

## Core Idea / 核心概念

The Generator maps `z` to samples, while the Discriminator learns to separate real data from generated data. Alternating updates aim to bring `p_g` closer to `p_data`; S03's diagrams are pedagogical approximations of that training process.

Source: S03, pp. 19–32.

## Concept Relationships / 概念關係

- application: [[generative-ai]] (S03 pp. 19–32).
- cause/effect: [[mode-collapse]] as a possible failure mode (S03 p. 35).
- evolution: [[gan-variants]] (S03 pp. 36–58).

## Mastery Level / 掌握程度

Unconfirmed. RUN-002 does not infer or change mastery.

## Sources / 來源

- S03 — *Copy of 03AI為什麼每次都不一樣？.pdf*, pp. 19–35. Provenance: Course Material.

## Staging Notes / 暫存說明

- Unpublished Week 10 staging draft; no model-knowledge supplement has been added.
