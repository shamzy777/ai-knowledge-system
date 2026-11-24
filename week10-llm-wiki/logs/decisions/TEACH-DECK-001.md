# TEACH-DECK-001 — implementation decisions

Date: 2026-11-24  
Status: implemented; awaiting human final review

## Authorization applied

- TEACH-PATH-001 is recorded as `approved-for-html-implementation` with `html_authorized: true`.
- The three human clarifications are binding:
  1. token embedding and positional information are separate mechanisms;
  2. the later teaching progression is `Language Modeling → Large Language Model → Inference` while Wiki relationship scopes remain unchanged;
  3. Sampling controls token selection and is not taught as the cause of Hallucination.

## Implementation scope

- Built 11 teaching sections plus a separate six-item formative quiz.
- Used only published Week 10 Wiki concept pages and their carried source labels.
- Added no S10, model knowledge, web knowledge, or new Wiki claim.
- Left the published Wiki, mastery status, and permanent AI Knowledge System unchanged.
- Chose code-native mechanism diagrams instead of photographs/video because the approved learning objective concerns an invisible causal process and requires explanatory visuals.
- Stopped before public deployment.

## Validation-script state transition

The existing proposal and Wiki validators originally encoded the earlier pre-approval state. After the human gate was recorded in proposal metadata, their authorization checks were changed to accept teaching implementation only when both `status: approved-for-html-implementation` and `html_authorized: true` are present. Wiki content checks were not weakened.
