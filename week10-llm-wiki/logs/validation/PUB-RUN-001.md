# PUB-RUN-001 Validation Events

## publication-lint-preparation
- timestamp: `2026-11-23T17:16:00+08:00`; publication_run: `PUB-RUN-001`; gate_id: `PUB-GATE-001`; event_type: `validation`
- action: Validate concept count/classification, provenance preservation, mastery, internal links, chapter navigation schema/membership, relationship registry, conflict treatments, Deferred exclusion, isolation, and absence of teaching/S10 artifacts.
- status: `pending-script-run`
- input_paths: `wiki/`, `staging/concepts/`, `staging/relationships/`, `docs/PUB-GATE-001-publication-review.md`
- output_paths: `workflow/scripts/validate_published_wiki.py`
- next_route: `pass-or-return-to-publication-layer`

## publication-lint-result
- timestamp: `2026-11-23T17:19:00+08:00`; publication_run: `PUB-RUN-001`; gate_id: `PUB-GATE-001`; event_type: `validation`
- action: Re-run full post-publication lint after Deferred-link corrections and validator scope correction; independently verify Wiki tree, Deferred absence, staging retention, and empty teaching layer.
- status: `passed`
- reason: 0 errors and 0 warnings; 51 concepts (33 Core, 18 Supporting), 7 chapters, 72 active published relationships, 8 Deferred retained; provenance, conflict treatments, terminology, mastery, links, and isolation checks passed.
- input_paths: `wiki/`, `staging/concepts/`, `staging/relationships/`, `sources/`, `teaching/`
- output_paths: `workflow/scripts/validate_published_wiki.py`, `logs/validation/PUB-RUN-001.md`
- next_route: `stop-publication-complete-ready-for-teaching-path-selection`
