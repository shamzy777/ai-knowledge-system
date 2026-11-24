# TEACH-DECK-001 — validation record

Date: 2026-11-24  
Final result: PASS

## Factual and evidence checks

- `workflow/scripts/validate_teaching_html.py`: PASS
  - 11/11 teaching sections have visible evidence footers.
  - 31 published-Wiki links resolve.
  - Six quiz items are present.
  - No external URL or S10 source marker is present.
  - The approved token/position, LM→LLM→Inference, Sampling, and factuality boundaries are present.
- `workflow/scripts/validate_teaching_path_proposal.py`: PASS
  - 11 evidence-map rows, three interactions, six quiz items, and 15 unique Wiki concept links validated.
- `workflow/scripts/validate_published_wiki.py`: PASS
  - 51 published concepts, seven chapter pages, 72 relationships, and eight deferred concepts remain valid.
  - No mastery change detected.
- Fidelity review: all 11 teaching sections remain inside the approved claim scopes recorded in `teaching/reviews/TEACH-DECK-001-fidelity-check.md`.

## Teaching checks

- Causal order: PASS.
- One primary teaching purpose per section: PASS.
- Beginner-readable terminology with bilingual canonical names: PASS.
- Diagram/mechanism match: PASS after two localized visual returns.
- Quiz-answer support: PASS; every answer names its supporting Wiki concept set.
- Content-density review: PASS after responsive inspection; no source retrieval was triggered.

## Technical and render checks

- `workflow/scripts/check_teaching_render.mjs`: PASS.
- Viewports: 375×812, 768×1024, 1280×800, 1440×900, 1920×1080.
- Horizontal overflow: none at all five widths.
- Console/page errors: none at all five widths.
- Slide/evidence presence: 11/11 at all five widths.
- Keyboard navigation: Arrow/Page/Home/End implementation present; ArrowDown advanced progress from 1 to 2 in the browser test.
- Anchors: pipeline link updated the hash to `#s9`; all 31 Wiki targets resolve locally.
- Interactions: pipeline spotlight, Q/K/V focus, and sampling tally all passed.
- No-JavaScript: 11 visible and opaque slide frames, 31 Wiki links, six quiz items, 5,073 characters of readable text, and no overflow at 375 px.
- Source lint: 0 failures, 0 warnings.
- Final visual inspector: 0 failures, 0 warnings using documented allowances for generic photography/video/font/card-count heuristics that do not fit this offline, diagram-led teaching artifact.

## Preserved evidence

- Machine report: `teaching/presentation/validation/render-report.json`
- Final screenshots: `teaching/presentation/validation/screenshots/`
- Visual inspection report: `teaching/presentation/.taste-inspect-final-r2/report.json`
- Visual critique: `teaching/reviews/TEACH-DECK-001-visual-critique.md`
