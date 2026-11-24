# PUB-RUN-001 Publication Decision Events

## publication-confirmation
- timestamp: `2026-11-23T17:05:00+08:00`; publication_run: `PUB-RUN-001`; gate_id: `PUB-GATE-001`; event_type: `human-confirmation`
- action: Record explicit approval to publish all 33 Core and 18 Supporting concepts plus seven chapter/navigation pages; retain eight Deferred concepts in staging.
- status: `approved-and-executed`
- reason: User approved PUB-GATE-001 classifications, Feature Scaling status, Tokenization terminology, conflict treatments, and publication scope.
- input_paths: `docs/PUB-GATE-001-publication-review.md`, `staging/concepts/`
- output_paths: `wiki/concepts/`, `wiki/chapters/`, `wiki/README.md`, `wiki/relationship-registry.md`
- next_route: `post-publication-validation`

## publication-terminology
- timestamp: `2026-11-23T17:07:00+08:00`; publication_run: `PUB-RUN-001`; gate_id: `PUB-GATE-001`; event_type: `decision`
- action: Publish `Tokenization（詞元化）` as the canonical bilingual label and retain `分詞`／`斷詞` only as contextual alternatives.
- status: `applied`
- output_paths: `staging/concepts/tokenization.md`, `wiki/concepts/tokenization.md`, `wiki/chapters/04-representing-language.md`
- next_route: `lint-terminology`

## publication-conflict-treatments
- timestamp: `2026-11-23T17:10:00+08:00`; publication_run: `PUB-RUN-001`; gate_id: `PUB-GATE-001`; event_type: `decision`
- action: Carry forward all approved conflict/scope treatments into relevant concept and chapter pages without rewriting source provenance.
- status: `applied`
- reason: Canonical definitions and attributed source perspectives must remain visibly distinct.
- output_paths: `wiki/concepts/backpropagation.md`, `wiki/concepts/classification.md`, `wiki/concepts/hallucination.md`, `wiki/concepts/loss-function.md`, `wiki/concepts/transformer.md`, `wiki/concepts/positional-encoding.md`, `wiki/chapters/`
- next_route: `post-publication-validation`

## publication-boundaries
- timestamp: `2026-11-23T17:12:00+08:00`; publication_run: `PUB-RUN-001`; gate_id: `PUB-GATE-001`; event_type: `decision`
- action: Exclude all Deferred pages and all graph edges with a Deferred endpoint; retain plain-text provenance context where a published page discusses a Deferred concept.
- status: `applied`
- reason: Deferred knowledge remains valid staging knowledge but is not part of this publication.
- output_paths: `wiki/concepts/`, `wiki/relationship-registry.md`
- next_route: `post-publication-validation`
