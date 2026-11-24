---
type: canonical-decision-register
run_id: RUN-003
source_ids: [S01, S02, S05, S06, S07]
status: validated-staging
---

# RUN-003 — Canonical create/update/defer decisions

Each source retained a separate provenance identity. Matches were evaluated first against RUN-001/RUN-002 staging and then against the read-only permanent system.

## S01 decisions

| Candidate | Decision | Canonical target / reason |
|---|---|---|
| Neural Network, Loss Function, One-Hot Encoding | update | Existing staging identity; add handwritten course-workflow corroboration only. |
| Neural Network Training, MLP, Epoch and Batch, Optimizer, Data Preprocessing, Training/Validation/Test, Overfitting, Hyperparameter | create staging shadow/candidate | Independent concepts with parent-aligned identity where available. |
| NumPy operations | defer | Tool syntax, not required conceptual scope. |

## S02 decisions

| Candidate | Decision | Canonical target / reason |
|---|---|---|
| Neural Network, Softmax, Distribution, One-Hot Encoding, Loss Function | update | Same underlying concepts already staged. |
| Perceptron, MLP, Weight and Bias, Activation Function, Neural Network Training, Gradient, Backpropagation, Learning Rate, Optimizer, Tensor, Classification | create staging shadow/candidate | Independently defined mechanisms or task concepts. |
| Dense/Fully Connected Layer | merge | Covered within MLP at this evidence depth. |
| Universal Approximation | defer | Mentioned, but external verification is advisable before a beginner-facing claim. |

## S05 decisions

| Candidate | Decision | Canonical target / reason |
|---|---|---|
| Neural Network, Loss Function, Cross Entropy, Softmax, Distribution | update | Adds theory/task-selection perspective to existing pages. |
| Perceptron, MLP, Activation Function, Weight/Bias, Forward Propagation, Gradient, Backpropagation, Learning Rate, Optimizer, Epoch/Batch, Weight Initialization, Evaluation Metric, Regression, Classification | create staging shadow/candidate | Independent course-supported concepts. |
| Linear Separability, Hidden Layer | merge | Preserved within Perceptron/MLP; no extra page needed yet. |
| Individual optimizer variants | merge | Kept as families/examples within Optimizer, avoiding a variant-page explosion. |

## S06 decisions

| Candidate | Decision | Canonical target / reason |
|---|---|---|
| Neural Network, Loss Function, Cross Entropy, Softmax, Distribution, One-Hot Encoding | update | Adds implementation and evaluation perspective. |
| Training/Validation/Test, Overfitting, Data Preprocessing, Feature Scaling, Regression, Classification, TensorBoard, Hyperparameter, Evaluation Metric | create staging shadow/candidate | Reusable practice concepts independently supported. |
| “Multi-labels Classification” | reject as canonical label | Actual MNIST task is mutually exclusive multiclass classification. |
| Model architecture per exercise | merge | Examples belong under MLP/application perspectives, not canonical nodes. |

## S07 decisions

| Candidate | Decision | Canonical target / reason |
|---|---|---|
| Neural Network, Loss Function | update | Handwritten corroboration only. |
| Neural Network Training, Epoch/Batch, Training/Validation/Test, Overfitting, Classification, TensorBoard, Hyperparameter | add source support | Same concept identities created from stronger sources. |
| ANN/CNN/RNN/GNN task shorthand | defer | Overview is too compressed to update individual architecture pages. |
| “ANN/CNN → Adam; RNN → RMSprop” | defer/reject as rule | Handwritten shorthand is context-dependent and insufficient for a universal recommendation. |

## Created canonical staging concepts (22)

Activation Function; Backpropagation; Classification; Data Preprocessing; Epoch and Batch; Evaluation Metric; Feature Scaling; Forward Propagation; Gradient; Hyperparameter; Learning Rate; Multilayer Perceptron; Neural Network Training; Optimizer; Overfitting; Perceptron; Regression; Tensor; TensorBoard; Training, Validation, and Test Sets; Weight and Bias; Weight Initialization.

## Existing concepts updated (6)

Neural Network; Loss Function; Cross Entropy; Softmax; Distribution; One-Hot Encoding.

## Duplicate candidates avoided

| Duplicate candidate | Canonical resolution |
|---|---|
| Probability Distribution / class-probability vector | `distribution` |
| Dense Network / Fully Connected Network | `multilayer-perceptron` at current evidence depth |
| Mini-batch / Batch SGD / full-batch epoch vocabulary | `epoch-and-batch` plus `optimizer` |
| MSE / binary CE / categorical CE as separate loss nodes | MSE remains in `loss-function`; CE variants remain within `cross-entropy` |
| Validation split / test evaluation / holdout set | `training-validation-and-test-sets` |
| Feature normalization / standardization | `feature-scaling` |
| Multiclass versus “multi-labels” exercise heading | canonical `classification` with conflict note; no duplicate node |
| Intermediate representation → Embedding | no update; evidence does not establish the embedding mechanism |

No file in the permanent AI Knowledge System was modified.
