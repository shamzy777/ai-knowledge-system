# TEACH-PATH-001 Retry Events

## historical-wiki-validator-phase-boundary
- timestamp: `2026-11-24T10:23:00+08:00`; teaching_path_id: `TEACH-PATH-001`; event_type: `retry`
- action: Published-Wiki regression lint treated the newly authorized Markdown proposal as a premature teaching artifact; narrow the historical check to forbid implementation files while allowing the current proposal phase.
- status: `validator-adjusted-awaiting-rerun`
- reason: Phase authorization changed from “no teaching artifacts” to “proposal allowed, HTML forbidden”; Wiki content itself remained valid.
- input_paths: `workflow/scripts/validate_published_wiki.py`, `teaching/paths/TEACH-PATH-001-proposal.md`
- output_paths: `workflow/scripts/validate_published_wiki.py`
- next_route: `rerun-wiki-regression-lint`

## historical-wiki-validator-phase-boundary-result
- timestamp: `2026-11-24T10:25:00+08:00`; teaching_path_id: `TEACH-PATH-001`; event_type: `retry-result`
- action: Re-run both validators after narrowing the historical Wiki check to implementation files.
- status: `resolved`
- reason: Both validators passed with 0 errors and 0 warnings; no HTML/CSS/JavaScript file exists.
- input_paths: `workflow/scripts/validate_published_wiki.py`, `workflow/scripts/validate_teaching_path_proposal.py`
- output_paths: `logs/validation/TEACH-PATH-001.md`
- next_route: `human-approval`
