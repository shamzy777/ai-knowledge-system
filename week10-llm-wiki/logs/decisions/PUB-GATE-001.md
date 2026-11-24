# PUB-GATE-001 Decision Events

## publication-review-classification
- timestamp: `2026-11-23T16:35:00+08:00`; gate_id: `PUB-GATE-001`; source_ids: `S01-S09`; event_type: `decision`
- action: Review all 59 validated staging concepts and propose Core, Supporting, or Deferred publication status under the seven-chapter beginner architecture.
- status: `proposal-complete-awaiting-user-approval`
- reason: Source ingestion is sufficient; publication requires an explicit human gate.
- input_paths: `staging/concepts/`, `staging/ingests/RUN-001-S04-conflicts.md`, `staging/ingests/RUN-003-conflicts.md`, `staging/ingests/RUN-004-conflicts.md`
- output_paths: `docs/PUB-GATE-001-publication-review.md`
- next_route: `explicit-user-approval-or-revision`

## publication-review-conflict-treatment
- timestamp: `2026-11-23T16:38:00+08:00`; gate_id: `PUB-GATE-001`; source_ids: `S02,S04,S06,S08,S09`; event_type: `human-confirmation`
- action: Apply the user's six conflict/scope decisions to the publication proposal without rewriting source history.
- status: `applied-to-proposal`
- reason: Backpropagation/optimizer, MNIST terminology, Hallucination scope, loss contexts, Transformer scope, and positional variants now have explicit canonical publication treatments.
- input_paths: user-approved gate instructions and existing conflict registers
- output_paths: `docs/PUB-GATE-001-publication-review.md`
- next_route: `publication-review-validation`

## publication-review-boundary
- timestamp: `2026-11-23T16:40:00+08:00`; gate_id: `PUB-GATE-001`; source_ids: `none`; event_type: `decision`
- action: Keep all Deferred concepts in staging, leave mastery unconfirmed, ingest no new sources, and create no files under wiki/ or teaching/.
- status: `enforced`
- reason: The user authorized review only, not publication.
- output_paths: `docs/PUB-GATE-001-publication-review.md`
- next_route: `stop-at-human-publication-gate`
