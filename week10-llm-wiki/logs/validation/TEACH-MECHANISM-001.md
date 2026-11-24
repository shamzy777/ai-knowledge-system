# TEACH-MECHANISM-001 — validation record

Date: 2026-11-24  
Final result: PASS

## Factual and teaching gates

- `validate_teaching_html.py`: PASS — 11 sections, 31 resolving published-Wiki links, six supported quiz items, no external URLs.
- `validate_teaching_language.py`: PASS — 60 learner-facing nodes and five files checked for Traditional Chinese-first language.
- `validate_teaching_mechanisms.py`: PASS — 9/9 mechanism questions; progressive stages Embedding=4, Q/K/V=5, Self-Attention=6, Transformer zoom=4, repeat loop=5; checkpoints=3.
- `validate_teaching_path_proposal.py`: PASS — approved 11-section evidence map remains valid.
- `validate_published_wiki.py`: PASS — 51 published concepts, seven chapters, 72 relationships, eight deferred concepts; no Wiki mutation.
- JavaScript and Python syntax: PASS. Python source was parsed with `ast.parse` after bytecode-cache writing was unavailable.

## Browser and render gates

- `check_teaching_render.mjs`: PASS at 375, 768, 1280, 1440, and 1920 px.
- Horizontal overflow and console errors: none at all five widths.
- Keyboard navigation: PASS; ArrowDown advanced progress to 2/11.
- Anchors and provenance: PASS; pipeline target and all 31 Wiki links resolve.
- Interaction state: PASS for Embedding, Q/K/V, Self-Attention, Transformer zoom, Sampling, checkpoints, and repeat loop.
- Repeat-loop initial state: no token selected; five causal stages complete in order after activation; selected token appears only at Selection.
- No JavaScript: 11 visible sections, 31 Wiki links, six quiz items, 6,533 readable characters, no overflow at 375 px.
- Taste source lint: 0 failures, 0 warnings.
- Final visual inspector: 0 findings at 1440, 768, and 390 px; no overflow, broken media, or low-contrast findings.

Evidence:

- `teaching/presentation/validation/render-report.json`
- `teaching/presentation/validation/screenshots/topic-mechanisms-expanded-1280.png`
- `.taste-skill/mechanism-review-final-r2/report.json`
- `teaching/reviews/TEACH-DECK-001-mechanism-review.md`

