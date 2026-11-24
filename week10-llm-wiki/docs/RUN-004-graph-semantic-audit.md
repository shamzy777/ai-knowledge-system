# RUN-004 graph-level semantic audit

## Method

Reviewed all accepted RUN-001–RUN-003 relationship registers at category-family level, then inspected every accepted or page-mirrored `theory ↔ practice` edge individually. The audit asks whether the category and direction are supported, not merely whether the endpoints are related.

## Required relabel/return events

| Historical edge | Review result | New event |
|---|---|---|
| R3-018 Training/Validation/Test `theory ↔ practice` Training | returned; relationship is workflow composition | R4-024 `part-of` |
| R3-023 Feature Scaling `theory ↔ practice` Training | returned; cited workflows support ordered dependency | R4-025 `prerequisite` with scope |
| R3-026 Softmax `theory ↔ practice` Classification | returned; use relation is directional | R4-026 `application` |
| R3-027 Cross Entropy `theory ↔ practice` Classification | returned; use relation is directional | R4-027 `application` |
| Distribution page mirror `theory ↔ practice` Classification | returned; probability interpretation is prerequisite knowledge | R4-028 `prerequisite` |
| Hyperparameter page mirror `theory ↔ practice` TensorBoard | returned; tool-to-use direction was reversed/underspecified | R4-029 TensorBoard `application` Hyperparameter |
| Optimizer page mirror `theory ↔ practice` MLP | returned; cited use is directional | R4-030 `application` |
| Prompt Engineering page narrative `theory ↔ practice` without endpoint | structurally invalid legacy prose; returned | existing Prompt Engineering `application` LLM retained; R4-016 adds `application` Inference |

The broad `theory ↔ practice` label was therefore removed from current concept-page mirrors. Earlier proposal files remain unchanged as historical evidence.

## Other direction findings

- RUN-001's prose table had `Hallucination cause/effect Language Model`; evidence supports the opposite direction. R4-022 records the replacement `Language Model cause/effect Hallucination`.
- Some concept pages had prose mirrors written from the page's perspective even when the actual graph edge pointed inward (Transformer/Self-Attention/Softmax and Inference/Sampling). These mirrors were clarified as incoming without changing accepted proposal history.
- R3-035, R3-036, and R3-037 remain rejected; this audit did not revive them.

## Stable categories

The remaining accepted prerequisite, part-of, application, contrast, evolution, and scoped cause/effect families were consistent with their cited sources at the reviewed granularity. No cross-domain analogy edge exists in staging, and no new `theory ↔ practice` edge is proposed by RUN-004.
