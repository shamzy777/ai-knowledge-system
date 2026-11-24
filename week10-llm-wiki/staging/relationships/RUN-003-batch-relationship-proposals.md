---
type: staged-relationship-register
run_id: RUN-003
source_ids: [S01, S02, S05, S06, S07]
status: semantic-review-complete
publication_status: unpublished
---

# RUN-003 — Batch relationship proposals

`add` means a new edge. `add-source-support` means the same typed/directed edge already existed and this batch only adds provenance. Rejected proposals remain in history.

| ID | Action | From | Relationship | To | Source support |
|---|---|---|---|---|---|
| R3-001 | add | Neural Network Training | part-of | Neural Network | S02 pp. 59–75; S05 pp. 14–15 |
| R3-002 | add | Weight and Bias | part-of | Perceptron | S02 pp. 33–39; S05 pp. 3–5 |
| R3-003 | add | Activation Function | part-of | Perceptron | S02 pp. 33–39; S05 pp. 3–5 |
| R3-004 | add | Perceptron | contrast | Multilayer Perceptron | S05 pp. 6–8 |
| R3-005 | add | Multilayer Perceptron | part-of | Neural Network | S02 pp. 41–50; S05 pp. 10–15 |
| R3-006 | add | Forward Propagation | part-of | Neural Network Training | S05 pp. 5, 14–15 |
| R3-007 | add | Loss Function | part-of | Neural Network Training | S02 pp. 59–75; S05 pp. 14–15 |
| R3-008 | add | Backpropagation | part-of | Neural Network Training | S05 pp. 5, 14–15 |
| R3-009 | add | Optimizer | part-of | Neural Network Training | S05 pp. 14–15, 40–64 |
| R3-010 | add | Backpropagation | cause/effect | Gradient | S05 p. 5 |
| R3-011 | add | Gradient | prerequisite | Optimizer | S05 pp. 40–64 |
| R3-012 | add | Learning Rate | part-of | Optimizer | S02 pp. 77–104; S05 pp. 40–64 |
| R3-013 | add | Epoch and Batch | part-of | Neural Network Training | S05 pp. 5–6; S06 pp. 12–21 |
| R3-014 | add | Data Preprocessing | prerequisite | Neural Network Training | S01 pp. 1–4; S06 pp. 3–12 |
| R3-015 | add | Weight Initialization | prerequisite | Neural Network Training | S05 pp. 21–31 |
| R3-016 | add | Evaluation Metric | part-of | Neural Network Training | S05 pp. 14–15, 36–39; S06 pp. 3–89 |
| R3-017 | add | Hyperparameter | part-of | Neural Network Training | S01 pp. 1–2; S06 pp. 72–86 |
| R3-018 | add | Training, Validation, and Test Sets | theory ↔ practice | Neural Network Training | S06 pp. 3–26 |
| R3-019 | add | Training, Validation, and Test Sets | prerequisite | Overfitting | S06 pp. 18–21 |
| R3-020 | add | TensorBoard | application | Neural Network Training | S06 pp. 45–56, 72–86 |
| R3-021 | add | TensorBoard | application | Overfitting | S06 pp. 18–21, 45–56 |
| R3-022 | add | Feature Scaling | part-of | Data Preprocessing | S01 pp. 2, 4; S06 pp. 8–12 |
| R3-023 | add | Feature Scaling | theory ↔ practice | Neural Network Training | S06 pp. 3–12, 29–38, 59–66 |
| R3-024 | add | Multilayer Perceptron | application | Regression | S06 pp. 3–26 |
| R3-025 | add | Multilayer Perceptron | application | Classification | S06 pp. 29–89 |
| R3-026 | add | Softmax | theory ↔ practice | Classification | S02 pp. 15–20, 109–123; S06 pp. 59–89 |
| R3-027 | add | Cross Entropy | theory ↔ practice | Classification | S05 pp. 33–35; S06 pp. 29–89 |
| R3-028 | add | One-Hot Encoding | part-of | Classification | S02 pp. 7–13, 109–123; S06 pp. 59–89 |
| R3-029 | add-source-support | Softmax | cause/effect | Distribution | S02 pp. 15–20; S05 pp. 16–20; S06 pp. 59–89 |
| R3-030 | add-source-support | Cross Entropy | application | Loss Function | S05 pp. 33–35; S06 pp. 29–89 |
| R3-031 | add | Tensor | part-of | Neural Network | S02 pp. 3–13, 41–50 |
| R3-032 | add | Weight and Bias | part-of | Neural Network | S02 pp. 33–50 |
| R3-033 | add | Activation Function | part-of | Neural Network | S02 pp. 33–50; S05 pp. 10–20 |
| R3-034 | add | Epoch and Batch | cause/effect | Overfitting | S06 pp. 18–21; scope: epoch count |
| R3-035 | add | Backpropagation | cause/effect | Optimizer | S02 p. 75 |
| R3-036 | add | Embedding | part-of | Neural Network | S02 pp. 41–50 |
| R3-037 | add | Classification | evolution | Regression | S05 pp. 16–20, 33–39 |

No proposal was silently relabelled, reversed, or deleted.
