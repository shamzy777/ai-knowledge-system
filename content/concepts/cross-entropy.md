---
concept: "Cross Entropy"
prototype_status: "presentation-layer content derived from existing knowledge"
source_canonical: "../../../Cross Entropy.md"
recorded_mastery: "🟨 可以解釋"
mastery_note: "This status exists in the current knowledge system, but no formal confirmation date or validation record is stored."
---

# Cross Entropy

## One-sentence Definition

Cross Entropy measures the cost of using a model distribution `Q` to describe a target distribution `P`, assigning a larger loss when the correct answer receives low probability.

## Why It Matters

Cross Entropy is a Loss Function that turns the mismatch between a target and a model distribution into a training loss. The existing system connects this same concept to implemented classification tasks and to next-token language-model training.

## Prerequisites

- prerequisite: Probability Distribution
- prerequisite: Information
- prerequisite: Entropy
- prerequisite: Softmax

## Core Idea

The course-derived intuition recorded in the canonical concept is:

> If the answer is correct but the model assigns it a low probability, give a large penalty.

The existing note records this relationship:

```text
Q becomes closer to P
→ Cross Entropy becomes smaller
→ KL Divergence becomes smaller
```

It also records that KL Divergence can be expressed as Cross Entropy minus the entropy of the target distribution. The full mathematical derivation remains an open question in the current knowledge system.

## Cross-course Perspectives

### 人工智慧程式設計

**Focus:** choosing and using classification loss in an implementation workflow.

**Contribution:**

- The canonical concept records `binary_crossentropy` for mushroom binary classification.
- It records categorical cross-entropy for multi-class tasks such as MNIST.
- The MLP workflow connects loss to Keras `compile()` and the repeated training cycle.
- Classification examples make Cross Entropy an implemented training objective rather than only an abstract quantity.

### TAICA 生成式 AI

**Focus:** distribution/information framing and language-model training.

**Contribution:**

- Cross Entropy is placed with Information, Entropy, KL Divergence, and Hard/Soft Targets.
- Week 4 records next-token training as prediction → correct-token comparison → cross-entropy loss → backpropagation.
- Cross Entropy compares the model's next-token distribution with the correct token during training.

### Why these belong in one concept

Both courses use Cross Entropy to penalize a model distribution that assigns insufficient probability to the target. AI Programming emphasizes implemented classification losses; TAICA places the same loss in a probability/information framework and applies it to next-token training. Their relationship is **implementation ↔ mathematical/generative framing**, not two separate Cross Entropy concepts.

## Concept Relationships

- **prerequisite:** Probability Distribution, Information, Entropy, and Softmax support the recorded explanation.
- **part-of:** Cross Entropy serves as the loss step within Neural Network Training.
- **cause/effect:** assigning low probability to the correct target produces a larger loss.
- **application:** binary and multi-class Classification.
- **application:** Language Model next-token training.
- **contrast:** the canonical note records MSE versus Cross Entropy as an unresolved task-dependent comparison rather than a settled rule.
- **theory ↔ practice:** TAICA's distribution/information framing corresponds to AI Programming's Keras classification-loss usage.

## Applications / Examples

- Mushroom binary classification uses `binary_crossentropy`.
- MNIST and other multi-class tasks use categorical cross-entropy-type loss.
- Next-token training uses Cross Entropy before backpropagation updates language-model parameters.

## My Explanation / Learning Evidence

The canonical knowledge file contains this first-person-labeled explanation:

> Cross Entropy 衡量用模型的 distribution Q 描述真實 distribution P 的代價。在分類任務中，若正確類別被模型給予很低機率，loss 會很大。

It also records first-person-labeled use of binary and categorical cross-entropy in classroom classification examples. Authorship and confirmation metadata is not stored.

## Mastery

**Recorded mastery:** 🟨 可以解釋

**Mastery note:** This status exists in the current knowledge system, but no formal confirmation date or validation record is stored. It must not be presented as verified mastery.

The canonical file still records the full mathematical derivation and the task-dependent choice between MSE and Cross Entropy as unresolved.

## Sources

### Canonical concept file

- `Cross Entropy.md`

### Course/source material

- 人工智慧程式設計 course index
- 人工智慧程式設計: `多層感知器的學習、訓練與驗證流程`
- TAICA 生成式 AI Week 3: `GAN to LLM`
- TAICA 生成式 AI Week 4: `LLM and Transformer`

## Evidence Limitations

- The recorded mastery has no formal confirmation history.
- The first-person-labeled explanation and implementation statements have no authorship or approval metadata.
- TAICA Week 3 explicitly records the full mathematical relationship among Information, Entropy, Cross Entropy, and KL Divergence as still needing clarification.
- The AI Programming MLP note names the mushroom and MNIST tasks, while the precise binary/categorical loss attribution is recorded chiefly in the canonical concept file.
- Some relationship types are formalized here from existing prose; no separately confirmed graph-edge record is stored.
