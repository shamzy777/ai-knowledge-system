---
type: relationship-semantic-review
run_id: RUN-003
source_ids: [S01, S02, S05, S06, S07]
review_independent_of_structural_lint: true
status: complete
---

# RUN-003 — Independent page-grounded semantic review

| ID | Outcome | Evidence/type/direction rationale |
|---|---|---|
| R3-001 | accepted | Both sources place training as the process that changes a neural network's parameters; part-of direction is supported. |
| R3-002 | accepted | Weighted sum plus bias is inside the perceptron computation. |
| R3-003 | accepted | Activation follows the weighted sum inside the perceptron. |
| R3-004 | accepted | S05 explicitly contrasts single-perceptron linear limits with MLP nonlinear capacity. |
| R3-005 | accepted | MLP is taught as a neural-network architecture. |
| R3-006 | accepted | S05 places forward computation inside the training loop. |
| R3-007 | accepted | Loss is calculated inside training and supplies the objective. |
| R3-008 | accepted | S05 places backward propagation inside training after the loss. |
| R3-009 | accepted | Optimizer/update behavior is a training component. |
| R3-010 | accepted | S05 supports backward computation producing/propagating gradients; direction retained. |
| R3-011 | accepted | Optimizer descriptions require gradients as input to update rules. |
| R3-012 | accepted | Learning rate scales optimizer updates in both sources. |
| R3-013 | accepted | Batches and epochs structure execution of training. |
| R3-014 | accepted | S01/S06 perform preprocessing before fitting the model; prerequisite direction is supported for the shown workflows. |
| R3-015 | accepted | Initial values are selected before training begins. |
| R3-016 | accepted | Metrics are configured/observed within the training-evaluation workflow. |
| R3-017 | accepted | Batch/epoch/architecture settings are external training configuration. |
| R3-018 | accepted | S06 links the conceptual data roles to actual fit/validate/test execution; symmetric theory-practice edge is appropriate. |
| R3-019 | accepted | Distinct training and validation observations are needed for the overfitting pattern shown. |
| R3-020 | accepted | S06 applies TensorBoard to log and inspect training runs. |
| R3-021 | accepted | S06's metric curves make TensorBoard applicable to overfitting inspection; not claimed as a cure. |
| R3-022 | accepted | Scaling is one named preprocessing operation in both sources. |
| R3-023 | accepted | S06 repeatedly translates scaling rationale into executable model preparation. |
| R3-024 | accepted | S06 uses an MLP for a regression task; method-to-use direction is supported. |
| R3-025 | accepted | S06 uses MLPs for binary and multiclass classification. |
| R3-026 | accepted | S02/S05 explain Softmax; S06 implements it for multiclass classification. |
| R3-027 | accepted | S05 explains task-specific CE; S06 implements binary/categorical CE. |
| R3-028 | accepted | One-hot targets are part of the taught multiclass classification representation. |
| R3-029 | accepted | Adds page-grounded S02/S05/S06 support to existing R2-001; no new edge. |
| R3-030 | accepted | Adds task/application support to existing R2-014; no new edge. |
| R3-031 | accepted | S02 explicitly frames inputs/intermediate layer values/outputs as tensors within network computation. |
| R3-032 | accepted | S02 shows weights and biases as neural-unit/layer parameters. |
| R3-033 | accepted | S02/S05 show activations inside neural units/layers. |
| R3-034 | accepted-with-scope | S06 supports excessive epochs contributing to the observed overfitting route; the edge must retain “epoch component,” not imply batch size necessarily causes overfitting. |
| R3-035 | rejected-returned-to-staging | S02 p. 75 conflates terms, but stronger page-grounded evidence distinguishes backprop gradient computation from optimizer update. The causal edge is unsupported and remains rejected. |
| R3-036 | rejected-returned-to-staging | S02 discusses intermediate representations but does not establish learned embedding identity/mechanism. No Embedding update or edge is allowed. |
| R3-037 | rejected-returned-to-staging | S05 contrasts task/output/loss choices; it does not claim either task evolved from the other. |

## Result

- Accepted: 34 proposals, including 2 additional-source-support records and 1 scoped acceptance.
- Rejected and returned to staging: R3-035, R3-036, R3-037.
- Original proposals remain unchanged; no silent fix was made.
