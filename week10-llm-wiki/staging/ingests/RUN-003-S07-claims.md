---
type: source-claim-register
run_id: RUN-003
source_id: S07
status: validated-staging
extraction_confidence: low-to-medium-handwriting
---

# S07 source-supported claims

| Claim ID | Locator | Supported claim | Confidence / handling |
|---|---|---|---|
| S07-C01 | full image, upper half | Training uses `fit`; validation data is observed for overfitting; the test set is used after training decisions. | Medium. |
| S07-C02 | full image, middle | Batch size and epochs are hyperparameters. | Medium. |
| S07-C03 | full image, lower half | Binary classification uses sigmoid with binary cross entropy. | Medium; corroborates S05/S06. |
| S07-C04 | full image, bottom | TensorBoard visualizes execution/training logs. | Medium; corroborates S06. |
| S07-C05 | full image | ANN/CNN/RNN/GNN labels are associated with different data/task patterns. | Low; overview only. |

Deferred: “ANN/CNN → Adam; RNN → RMSprop” is handwritten shorthand, not a universal optimizer rule.
