---
concept: "Softmax"
prototype_status: "presentation-layer content derived from existing knowledge"
source_canonical: "../../../Softmax.md"
recorded_mastery: "🟨 可以解釋"
mastery_note: "This status exists in the current knowledge system, but no formal confirmation date or validation record is stored."
---

# Softmax

## One-sentence Definition

Softmax is an output-layer activation that converts multiple scores into a relative distribution whose values sum to one.

## Why It Matters

The same mechanism supports two applications recorded in different courses. In classification, argmax can select the highest-scoring mutually exclusive class; in probabilistic generation, sampling can select from a next-token distribution while preserving variation.

## Prerequisites

- prerequisite: Activation Function
- prerequisite: Classification

## Core Idea

Softmax considers all candidate scores together and converts them into a relative distribution. Raising one candidate's share reduces the shares available to the others.

The existing system distinguishes Softmax from sigmoid:

- Softmax: outputs compete and sum to one; used for mutually exclusive choices.
- Sigmoid: outputs are independent; used for binary classification or labels that may be simultaneously true.

The downstream decision is separate from Softmax itself:

```text
scores
→ Softmax
→ probability distribution
├── argmax → classification / stable choice
└── sampling → generation / varied choice
```

## Cross-course Perspectives

### 人工智慧程式設計

**Focus:** classification output behavior and implementation choices.

**Contribution:**

- Softmax is used at the output layer for mutually exclusive multi-class classification.
- The course materials contrast Softmax with sigmoid.
- Taken together, the canonical Softmax and Activation Function material, the AI Programming classification material, and the MLP note's MNIST example support the integrated Softmax-in-MNIST interpretation; no single source note states the complete claim.
- The AI Programming course index records the activation-function and classification context.

### TAICA 生成式 AI

**Focus:** distributions, selection, and probabilistic generation.

**Contribution:**

- Neural-network scores are converted into a probability distribution.
- Argmax and sampling produce different uses of the same distribution.
- A language model uses Softmax to obtain a next-token distribution.
- Week 2 includes Taiwan myna classification before Weeks 3–4 extend the distribution to generation.
- Week 4 places Softmax after Transformer representations and vocabulary scores, before sampling the next token.

### Why these belong in one concept

Both courses use the same score-to-distribution mechanism. What changes is the downstream application: classification selects among classes, while generation samples among possible next tokens. Splitting these into course-specific Softmax pages would duplicate the mechanism and hide the **classification ↔ probabilistic generation** connection.

## Concept Relationships

- **application:** mutually exclusive multi-class Classification.
- **application:** Language Model next-token probability and generation.
- **contrast:** Softmax outputs compete and sum to one; sigmoid outputs are independent.
- **theory ↔ practice:** TAICA's probability-distribution framing corresponds to AI Programming's classification output examples.

## Applications / Examples

- Taiwan myna classification: three class scores are converted into a distribution.
- MNIST: ten output classes use Softmax.
- Language generation: vocabulary scores become a next-token distribution before sampling.

## My Explanation / Learning Evidence

The canonical knowledge file contains this first-person-labeled explanation:

> Softmax 是一種用在 output layer 的 Activation Function，會把多個輸出分數轉換成總和為 1 的相對分布。

It also records first-person-labeled use in the Taiwan myna and MNIST classroom examples. Authorship and confirmation metadata is not stored.

## Mastery

**Recorded mastery:** 🟨 可以解釋

**Mastery note:** This status exists in the current knowledge system, but no formal confirmation date or validation record is stored. It must not be presented as verified mastery.

The canonical file says further validation through multi-class classification practice is still expected.

## Sources

### Canonical concept file

- `Softmax.md`

### Course/source material

- 人工智慧程式設計: `2026-09-29 手寫筆記整理`, section “Perceptron 與 Neural Network”
- 人工智慧程式設計: `多層感知器的學習、訓練與驗證流程`
- TAICA 生成式 AI Week 2: `神經網路`
- TAICA 生成式 AI Week 3: `GAN to LLM`
- TAICA 生成式 AI Week 4: `LLM and Transformer`

## Evidence Limitations

- The recorded mastery has no formal confirmation history.
- The first-person-labeled explanation and classroom-use statement have no authorship or approval metadata.
- The handwritten AI Programming source warns that OCR errors remain and that source organization does not itself prove understanding.
- The source metadata identifies course lessons, but the project stores no formal record confirming when the Softmax mastery status was assigned.
- The relationship labels in this presentation summarize mechanisms already expressed in prose; no separately confirmed graph-edge record is stored.
