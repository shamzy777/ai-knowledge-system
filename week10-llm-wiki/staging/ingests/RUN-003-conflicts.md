---
type: conflict-and-scope-register
run_id: RUN-003
status: open-publication-gates-recorded
requires_user_confirmation_before_publication: true
---

# RUN-003 — Conflicts and scope differences

## CONFLICT-003-001 — Gradient descent versus backpropagation

- S02 p. 75 says gradient descent is, because of neural-network characteristics, also called backpropagation.
- S05 pp. 5, 14–15, 40–64 separates backward gradient computation from optimizer/update methods.
- The read-only parent canonical concepts also keep Backpropagation and Optimizer distinct.
- Staging treatment: preserve S02 as a pedagogical simplification; canonical draft distinguishes gradient computation from parameter update.
- Publication gate: user confirmation required for how explicitly to correct/qualify the slide wording.

## CONFLICT-003-002 — “Multi-labels” heading versus actual MNIST task

- S06 p. 59 labels the section “Multi-labels Classification.”
- S06 pp. 59–89 uses one-hot targets, one Softmax distribution, categorical cross entropy, and argmax over ten mutually exclusive digits.
- Staging treatment: classify the implemented task as single-label multiclass; preserve the source heading as a terminology conflict.
- Publication gate: user confirmation required for whether to call it a slide wording error or only explain the distinction.

## SCOPE-003-003 — Squared-error teaching example versus task-specific loss choices

- S02 pp. 68–72 uses squared error to illustrate loss minimization with one-hot-like outputs.
- S05 pp. 33–35 and S06 pp. 59–89 use categorical cross entropy for practical multiclass classification.
- Treatment: not a direct contradiction. Preserve S02 as a generic optimization example and S05/S06 as task-specific practice.

## SCOPE-003-004 — Optimizer shorthand

- S07 associates ANN/CNN with Adam and RNN with RMSprop in handwritten notes.
- S05 pp. 40–64 presents optimizer families and tradeoffs rather than a universal architecture-to-optimizer mapping.
- Treatment: S07 shorthand is deferred and excluded from canonical recommendations.

## SCOPE-003-005 — Weight-initialization and activation heuristics

- S05 supplies practical heuristics for initializers and activations.
- Treatment: retain the course perspective but do not convert “often used” guidance into guarantees.

The unresolved RUN-001 Hallucination conflict remains an independent publication gate.
