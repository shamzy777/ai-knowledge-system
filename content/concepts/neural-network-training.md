---
concept: "Neural Network Training"
prototype_status: "presentation-layer content derived from existing knowledge"
source_canonical: "../../../Neural Network Training.md"
recorded_mastery: "🟨 可以解釋"
mastery_note: "This status exists in the current knowledge system, but no formal confirmation date or validation record is stored."
---

# Neural Network Training

## One-sentence Definition

Neural Network Training is the repeated process of adjusting learnable parameters so that a neural network's output moves closer to its training target.

## Why It Matters

Training allows a model to change from its initialized behavior by using data, predictions, loss, gradients, and parameter updates. The existing notes also distinguish training from validation and testing: training data updates parameters, validation data is used to observe the training process, and test data is reserved for final evaluation.

## Prerequisites

- prerequisite: Neural Network
- prerequisite: Weight and Bias
- prerequisite: Loss Function
- prerequisite: differentiation, partial derivatives, and the chain rule

## Core Idea

The existing system records this training cycle:

```text
data / batch
→ forward computation
→ prediction
→ loss
→ backpropagation computes gradients
→ optimizer updates weights and biases
→ repeat
```

All training samples being used once completes one epoch. The AI Programming source also records that a validation set can be evaluated after an epoch without backpropagation or parameter updates.

TAICA Week 4 applies the same training logic to a language model: prediction is compared with the correct token through cross-entropy loss, then backpropagation updates embeddings, Q/K/V, and other parameters.

## Cross-course Perspectives

### 人工智慧程式設計

**Focus:** implementation and model-evaluation workflow.

**Contribution:**

- `compile()` configures loss, optimizer, and metrics.
- `fit()` carries out forward computation, loss calculation, backpropagation, and parameter updates.
- `predict()` produces predictions; `evaluate()` performs final evaluation.
- `batch_size` and `epochs` connect the conceptual loop to Keras controls.
- Training, validation, and test data have different roles.
- Course examples include California Housing regression, mushroom binary classification, and MNIST multi-class classification.

### TAICA 生成式 AI

**Focus:** the conceptual mechanism by which a parameterized function learns.

**Contribution:**

- A model produces a prediction and compares it with a correct target through loss.
- Backpropagation computes gradients; gradient descent uses them to update parameters.
- The causal sequence is recorded as prediction → loss → gradient calculation → parameter update → new model behavior.
- Week 4 shows the mechanism applied to embeddings, Q/K/V, and other language-model parameters.

### Why these belong in one concept

Both courses describe the same parameter-learning process. TAICA supplies the conceptual causal loop, while AI Programming maps that loop to Keras operations, dataset roles, and implementation examples. Their relationship is **theory ↔ practice**, not two course-specific versions of Neural Network Training.

## Concept Relationships

- **prerequisite:** Neural Network supplies the parameterized architecture being trained.
- **prerequisite:** Weight and Bias are parameters updated during training.
- **part-of:** Forward Propagation, Loss Function, Gradient, Backpropagation, Optimizer, Learning Rate, and Epoch and Batch form parts of the recorded training workflow.
- **cause/effect:** prediction error produces loss; backpropagation computes gradients from that loss; the optimizer uses gradients to update parameters.
- **application:** TAICA Week 4 applies the training loop to embeddings and Transformer parameters during next-token training.
- **theory ↔ practice:** TAICA's conceptual loop corresponds to AI Programming's `compile()` and `fit()` workflow.

## Applications / Examples

- California Housing regression: compare `loss` and `val_loss`.
- Mushroom binary classification: sigmoid with `binary_crossentropy`.
- MNIST multi-class classification: Softmax with TensorBoard hyperparameter comparison.

## My Explanation / Learning Evidence

The canonical knowledge file contains this first-person-labeled explanation:

> Neural Network Training 是透過反覆調整參數，讓神經網路的輸出逐漸接近正確結果的過程。

It also records first-person-labeled use of Keras `compile()`, `fit()`, `predict()`, and `evaluate()`. Authorship and confirmation metadata for these statements is not stored.

## Mastery

**Recorded mastery:** 🟨 可以解釋

**Mastery note:** This status exists in the current knowledge system, but no formal confirmation date or validation record is stored. It must not be presented as verified mastery.

The canonical note still records open questions about full multilayer backpropagation, optimizer differences, stopping conditions, and interactions among batch size and epochs.

## Sources

### Canonical concept file

- `Neural Network Training.md`

### Course/source material

- 人工智慧程式設計 course index
- 人工智慧程式設計: `2026-09-29 手寫筆記整理`, section “Model Training”
- 人工智慧程式設計: `多層感知器的學習、訓練與驗證流程`
- TAICA 生成式 AI Week 2: `神經網路`
- TAICA 生成式 AI Week 4: `LLM and Transformer`

### Additional index reference

- 人工智慧方法與工具 lists Neural Network Training, but the current project contains no detailed course note showing a distinct contribution from that course.

## Evidence Limitations

- The recorded mastery has no formal confirmation history.
- The first-person-labeled explanation and usage statements have no authorship or approval metadata.
- The handwritten AI Programming note is marked `source-organized`, explicitly says it does not prove understanding, and warns that some OCR remains uncertain.
- 人工智慧方法與工具 is an index reference only and is not presented here as a substantive third perspective.
- Some relationship types are made explicit in this presentation layer from the causal workflow stored as prose; no separately validated graph-edge record exists.
