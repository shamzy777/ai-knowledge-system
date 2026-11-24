---
type: staged-source-conflict-review
run_id: RUN-002
source_id: S03
status: validated-staging-with-existing-publication-gate
requires_user_confirmation_before_publication: true
---

# RUN-002 Source Perspectives, Conflicts, and Scope Differences

## No new direct contradiction

S03 and S04 do not directly disagree about Softmax, sampling, or language-model distributions. S03 supplies a broader classification-versus-generation comparison; S04 supplies the detailed language-model sampling strategies. They are complementary, so no consensus was forced and neither source's scope was overwritten.

Source basis: S03 pp. 61–64, 93–98; S04 pp. 50–64.

## SCOPE-002 — Where randomness enters

- S03 pp. 93–96 distinguishes random latent input for GANs, argmax for a typical classification example, and output sampling for a language model.
- S04 pp. 53–64 focuses on output sampling and its temperature/top-k/top-p controls.
- Treatment: preserve both as model/task-specific routes. Do not generalize that all generative systems use the same source of randomness.

## SCOPE-003 — Generative versus discriminative framing

- S03 pp. 97–98 uses “generative” and “discriminative” as useful task/output labels but emphasizes shared probabilistic principles.
- Treatment: add this as a source perspective on `Generative AI`; do not create a standalone `Discriminative AI` node from S03 alone.

## Existing CONFLICT-001 remains open — Hallucination

S03 p. 98 repeats the common claim that generative AI hallucinates and discriminative AI should be used, then immediately cautions that their principles are similar. This does not resolve RUN-001's broad-versus-narrow use of “Hallucination”; it adds a reason not to treat the generative/discriminative label as a reliability guarantee.

Publication treatment still requires user confirmation. No publication occurs in RUN-002.
