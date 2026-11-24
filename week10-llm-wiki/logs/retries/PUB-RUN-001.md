# PUB-RUN-001 Retry Events

## publication-write-permission
- timestamp: `2026-11-23T17:03:00+08:00`; publication_run: `PUB-RUN-001`; gate_id: `PUB-GATE-001`; event_type: `retry`
- action: Initial publication script stopped before writing the first concept because the Week 10 project path required renewed turn-scoped write permission; request exact-path permission and rerun from an empty `wiki/concepts/` directory.
- status: `succeeded-on-retry`
- reason: Workspace permission boundary, not a content or validation failure.
- input_paths: `staging/concepts/`
- output_paths: `wiki/concepts/`, `wiki/relationship-registry.md`
- next_route: `chapter-creation-and-lint`

## publication-deferred-link-return
- timestamp: `2026-11-23T17:14:00+08:00`; publication_run: `PUB-RUN-001`; gate_id: `PUB-GATE-001`; event_type: `retry`
- action: Post-copy link scan found ten wikilinks from published pages to Deferred concepts; return those page mirrors for correction, retain the source-supported relationship as plain-text provenance context, and exclude the edges from the published graph.
- status: `resolved`
- reason: Publishing the link target would violate the approved Deferred boundary; leaving the link would create a broken Wiki link.
- input_paths: `wiki/concepts/`
- output_paths: `wiki/concepts/`, `wiki/relationship-registry.md`
- next_route: `full-post-publication-lint`

## publication-lint-false-positive
- timestamp: `2026-11-23T17:18:00+08:00`; publication_run: `PUB-RUN-001`; gate_id: `PUB-GATE-001`; event_type: `retry`
- action: Initial full lint reported a superseded `theory ↔ practice` edge because the validator searched explanatory prose in the registry; restrict the check to the relationship column and rerun.
- status: `resolved-validator-false-positive`
- reason: The phrase appeared only in a scope note explaining its exclusion; none of the 72 registry rows used that relationship.
- input_paths: `wiki/relationship-registry.md`, `workflow/scripts/validate_published_wiki.py`
- output_paths: `workflow/scripts/validate_published_wiki.py`
- next_route: `rerun-full-post-publication-lint`
