---
type: staged-relationship-register
run_id: RUN-004
source_ids: [S08, S09]
status: semantic-review-complete
publication_status: unpublished
---

# RUN-004 — Relationship proposals

Original historical proposals remain unchanged. `replacement-for-*` rows are new review events, not edits to history.

| ID | Action | From | Relationship | To | Source support |
|---|---|---|---|---|---|
| R4-001 | add | Tokenization | prerequisite | Embedding | S09 book pp. 42–47, 177 |
| R4-002 | add | Tokenization | prerequisite | Language Model | S09 book pp. 5, 42–47 |
| R4-003 | add | Byte-Pair Encoding | application | Tokenization | S09 book pp. 42–45 |
| R4-004 | add | Multi-Head Attention | part-of | Transformer | S08 pp. 3–5; S09 book pp. 177–184 |
| R4-005 | add | Query, Key, and Value | part-of | Multi-Head Attention | S08 pp. 4–5; S09 book pp. 183–184 |
| R4-006 | add | Positional Encoding | part-of | Transformer | S08 pp. 3, 6; S09 book pp. 191–193 |
| R4-007 | add-source-support | Embedding | part-of | Transformer | S08 pp. 3, 5; S09 book pp. 177, 193 |
| R4-008 | add-source-support | Self-Attention | part-of | Transformer | S08 pp. 3–5; S09 book pp. 177–184 |
| R4-009 | add-source-support | Transformer | application | Language Model | S09 book pp. 177–203 |
| R4-010 | add | Pretraining | application | Neural Network Training | S09 book pp. 201–203 |
| R4-011 | add | Pretraining | prerequisite | Post-Training | S09 book pp. 16–21, 209–210 |
| R4-012 | add | Post-Training | part-of | Large Language Model | S09 book pp. 16–21, 209–223 |
| R4-013 | add | Inference | contrast | Neural Network Training | S09 book pp. 16, 21–24 |
| R4-014 | add | Sampling | part-of | Inference | S09 book pp. 196–201 |
| R4-015 | add | Sampling Strategies | part-of | Inference | S09 book pp. 196–201 |
| R4-016 | add | Prompt Engineering | application | Inference | S09 book pp. 21–24 |
| R4-017 | add-source-support | Softmax | part-of | Self-Attention | S08 pp. 3–4; S09 book pp. 179–184 |
| R4-018 | add-source-support | Softmax | part-of | Language Model | S08 p. 5; S09 book pp. 5–11, 196–203 |
| R4-019 | add | Cross Entropy | application | Pretraining | S09 book pp. 201–203 |
| R4-020 | add-source-support | Recurrent Neural Network | contrast | Transformer | S08 pp. 1–2, 6–7 |
| R4-021 | add-source-support | Language Model | evolution | Large Language Model | S09 book pp. 5–24 |
| R4-022 | replacement-for-RUN-001-page-edge | Language Model | cause/effect | Hallucination | S04 pp. 38–41; S09 book pp. 29–31 |
| R4-023 | add-source-support | LLM Evaluation | application | Large Language Model | S09 book pp. 25–28 |
| R4-024 | replacement-for-R3-018 | Training, Validation, and Test Sets | part-of | Neural Network Training | S06 pp. 3–26 |
| R4-025 | replacement-for-R3-023 | Feature Scaling | prerequisite | Neural Network Training | S06 pp. 3–12, 29–38, 59–66 |
| R4-026 | replacement-for-R3-026 | Softmax | application | Classification | S02 pp. 15–20, 109–123; S05 pp. 16–20; S06 pp. 59–89 |
| R4-027 | replacement-for-R3-027 | Cross Entropy | application | Classification | S05 pp. 33–35; S06 pp. 29–89 |
| R4-028 | replacement-for-legacy-page-edge | Distribution | prerequisite | Classification | S02 pp. 15–20; S06 pp. 59–89 |
| R4-029 | replacement-for-legacy-page-edge | TensorBoard | application | Hyperparameter | S06 pp. 72–86 |
| R4-030 | replacement-for-legacy-page-edge | Optimizer | application | Multilayer Perceptron | S06 pp. 3–89 |

No relationship was silently rewritten. Superseded edges remain in earlier registers and are reviewed in the graph audit.
