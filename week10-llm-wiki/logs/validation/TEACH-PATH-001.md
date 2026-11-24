# TEACH-PATH-001 Validation Events

## proposal-lint-preparation
- timestamp: `2026-11-24T10:20:00+08:00`; teaching_path_id: `TEACH-PATH-001`; event_type: `validation`
- action: Validate proposal metadata, published-Wiki links, eight-concept coverage, eleven-section/evidence-map alignment, interactions, quizzes, provenance categories, validation gates, graph-return routes, mastery, and absence of HTML.
- status: `pending-script-run`
- input_paths: `teaching/paths/TEACH-PATH-001-proposal.md`, `wiki/concepts/`
- output_paths: `workflow/scripts/validate_teaching_path_proposal.py`
- next_route: `pass-or-return-to-proposal`

## proposal-lint-result
- timestamp: `2026-11-24T10:22:00+08:00`; teaching_path_id: `TEACH-PATH-001`; event_type: `validation`
- action: Run the teaching-path proposal lint.
- status: `passed`
- reason: 0 errors and 0 warnings; 11 teaching sections match 11 evidence rows; 3 interactions and 6 quiz items are mapped; all 15 unique concept links resolve to published Wiki pages; required provenance, validation, and return routes are present; no HTML exists.
- input_paths: `teaching/paths/TEACH-PATH-001-proposal.md`, `wiki/concepts/`
- output_paths: `workflow/scripts/validate_teaching_path_proposal.py`, `logs/validation/TEACH-PATH-001.md`
- next_route: `human-approval`

## wiki-regression-check
- timestamp: `2026-11-24T10:23:00+08:00`; teaching_path_id: `TEACH-PATH-001`; event_type: `validation`
- action: Re-run the published Wiki lint after proposal creation; update the historical validator to permit authorized Markdown teaching proposals while still rejecting HTML/CSS/JavaScript implementation.
- status: `pending-rerun`
- reason: The first regression check correctly found the new proposal but used the earlier phase's blanket teaching-directory prohibition; no Wiki content error was reported.
- input_paths: `wiki/`, `teaching/paths/TEACH-PATH-001-proposal.md`
- output_paths: `workflow/scripts/validate_published_wiki.py`
- next_route: `rerun-wiki-lint`

## final-validation-result
- timestamp: `2026-11-24T10:25:00+08:00`; teaching_path_id: `TEACH-PATH-001`; event_type: `validation`
- action: Re-run the teaching-path lint and published-Wiki regression lint after aligning the phase boundary; verify absence of HTML/CSS/JavaScript files.
- status: `passed`
- reason: Teaching-path lint 0 errors/0 warnings; Wiki lint 0 errors/0 warnings; only the Markdown proposal exists under teaching; published Wiki remains 51 concepts, 7 chapters, and 72 relationships.
- input_paths: `teaching/paths/TEACH-PATH-001-proposal.md`, `wiki/`, `workflow/scripts/`
- output_paths: `logs/validation/TEACH-PATH-001.md`
- next_route: `stop-and-request-human-approval-no-html`
