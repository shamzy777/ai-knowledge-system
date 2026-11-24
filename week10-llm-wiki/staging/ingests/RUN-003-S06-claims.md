---
type: source-claim-register
run_id: RUN-003
source_id: S06
status: validated-staging
---

# S06 source-supported claims

| Claim ID | Locator | Supported claim |
|---|---|---|
| S06-C01 | pp. 3–26 | A regression workflow preprocesses/splits/scales data, defines and compiles a network, trains with validation, plots curves, and evaluates on held-out test data. |
| S06-C02 | pp. 18–21 | Diverging training and validation loss can reveal overfitting and support epoch/model-selection decisions. |
| S06-C03 | pp. 29–58 | Binary classification uses digitized labels, scaling, a sigmoid output, binary cross entropy, metrics, and train/validation/test evaluation. |
| S06-C04 | pp. 59–89 | The MNIST practice is mutually exclusive ten-class classification using flattening/scaling, one-hot labels, Softmax, categorical cross entropy, accuracy, and argmax. |
| S06-C05 | pp. 45–56, 72–86 | TensorBoard logs/visualizes training, while HParams supports comparison of hyperparameter runs. |

Terminology note: the p. 59 section label says “Multi-labels Classification,” but the actual task and implementation are multiclass, single-label classification.
