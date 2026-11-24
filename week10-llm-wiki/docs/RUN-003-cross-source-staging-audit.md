# RUN-003 Cross-source Staging Audit

Date: 2026-11-23 (Asia/Taipei)

Scope: S01, S02, S05, S06, and S07 against RUN-001/RUN-002 staging and the read-only permanent system. Nothing was published to `wiki/` or `teaching/`.

## Inventory result

- Five separate manifests and claim registers are present; together with S03/S04, the course-first set now contains seven real ingests.
- 22 new staging concepts were created and 6 existing concepts were updated.
- Total staging concepts after RUN-003: 52.
- S01 and S07 handwriting is labelled low-to-medium confidence and never supplies the only strong support for a high-impact claim.
- Embedding received no RUN-003 update because the batch did not independently establish embedding identity or mechanism.

## Canonical duplicate audit

No normalized-title duplicate was accepted. Avoided duplicate candidates include Probability Distribution, Dense/Fully Connected Network, mini-batch variants, separate loss-variant pages, validation/test aliases, and intermediate-representation-as-Embedding. Variant depth is retained inside the canonical page until evidence justifies a separate concept.

## Definition and scope conflicts

Two publication-gated conflicts remain:

1. S02 p. 75 conflates gradient descent with backpropagation; S05 and the parent system distinguish gradient computation from optimizer updating.
2. S06 labels the MNIST section “Multi-labels Classification,” while the task is mutually exclusive multiclass classification.

Squared error in S02 versus categorical cross entropy in S05/S06 is treated as an example-versus-task-specific scope difference, not forced into a contradiction. Optimizer and initializer heuristics remain contextual.

## Provenance completeness

- Every RUN-003 concept page has Course Material provenance and source locators.
- Every source has a checksum-bound local copy and Drive identity.
- The two handwriting sources explicitly carry uncertainty notes.
- No Model Knowledge was added or counted.
- The permanent-system paths are identity comparisons only and are not counted as ingests.

## Unsupported synthesis audit

Rejected or deferred synthesis:

- Backpropagation → Optimizer causal edge: unsupported conflation.
- Embedding as part of generic Neural Network from S02 intermediate-representation slides: insufficient evidence.
- Classification evolving from Regression: unsupported relationship type.
- Universal architecture-to-optimizer prescriptions from S07: insufficient/context-dependent.
- Universal Approximation and time-sensitive tool guidance: deferred pending stronger/primary support.

No rejected synthesis was written into an accepted graph edge.

## Relationship consistency

- 37 stable proposals were structurally reviewed.
- 34 were semantically accepted, including 2 records that add provenance to existing edges rather than create new edges.
- 3 were rejected and explicitly returned to staging.
- R3-034 is accepted only with the scope that excessive epoch count can contribute to overfitting; it does not claim batch size necessarily causes overfitting.
- Page-level relationship wording was aligned with the accepted type/direction, including incoming-edge labels where the page is the target.

## Missing prerequisite links

The batch added a coherent beginner path:

`Tensor / Data Preprocessing → Neural Network → Perceptron / MLP → Forward Propagation → Loss Function → Gradient / Backpropagation → Optimizer → Training/Validation/Test → Overfitting / Evaluation`

Remaining prerequisite gaps for the broader LLM route:

- Tokenization and vocabulary construction need a stronger bridge into embedding and language modeling.
- Positional encoding, multi-head attention, and Transformer block composition rely mainly on S04 and lack independent primary support.
- Pretraining objectives, instruction tuning/post-training, alignment, and practical inference/deployment are not adequately covered.
- LLM evaluation, retrieval/tool use, safety, data governance, and compute/scaling tradeoffs are outside this course-first batch.

## Weak or single-source concepts

- Forward Propagation is clear but supported only by S05 in this batch.
- Embedding, Transformer, Self-Attention, and several LLM-specific concepts remain primarily S04-supported.
- S01/S07-only shorthand is not promoted; their accepted claims are corroborated by stronger sources.
- TensorBoard is strongly supported by S06 and secondarily corroborated by S07.

## Cross-course theory ↔ practice convergence

The clearest convergences are:

- S02/S05 theory of Softmax plus S06 MNIST implementation.
- S03/S05 cross-entropy theory plus S06 binary/multiclass implementations.
- S02/S05 loss/gradient/optimizer framing plus S06 fit/validation/test workflow.
- S01/S05 component checklist plus S06 compile/train/evaluate practice.
- S06 visual curves plus S07 handwritten validation/overfitting notes.

## External-source recommendation before publication

The seven course sources already satisfy the assignment's 5+ requirement. No S08–S10 source is required merely to validate or publish a tightly bounded neural-network-training learning path.

For publication of the broader “從零開始認識 LLM” Wiki or a bounded path that reaches Transformer/LLM mechanisms, external gap filling is recommended:

- **S08 is needed** when the path makes technical claims about scaled dot-product attention, multi-head attention, positional encoding, or the original Transformer architecture.
- **S09 is recommended** to provide a coherent beginner bridge across tokenization, embeddings, language modeling, pretraining/post-training, and modern LLM terminology.
- **S10 is optional** unless the selected teaching path includes practical model use, tokenizers, fine-tuning, or datasets.

These are recommendations only; S08–S10 remain un-ingested and require a later authorized run.

## Audit conclusion

RUN-003 reached validated staging. Structural relationship lint passed with 37 proposals and 0 errors; semantic-record lint passed with 34 accepted and 3 returned; overall staging lint passed with 52 concepts, 0 errors, and 0 warnings. Publication remains prohibited and conflict treatment remains a human confirmation point.
