# TEACH-HUB-001 — validation record

Timestamp: 2026-11-24T19:56:53+08:00  
Final result: PASS

## Architecture and grounding

- Root opens the Learning Hub: PASS.
- Topic 01 opens separately at `topics/next-token.html`: PASS.
- Topic 01 provides visible return-home navigation: PASS.
- Registry-driven topic rendering and restrained future placeholder: PASS.
- Eleven teaching sections and eleven visible evidence mappings: PASS.
- Six quiz items: PASS.
- Published-Wiki links: 31 checked and resolved.
- External URLs / external factual sources / S10: none.
- Published Wiki regression lint: PASS — 51 concepts, seven chapters, 72 relationships, eight deferred concepts.
- Teaching-path lint: PASS — 11 evidence rows, three approved interaction groups, six quiz items, 15 Wiki concepts.

## Language

- Traditional Chinese-first learner UI: PASS.
- Bilingual technical terminology: PASS.
- Unexpected English-only UI guard: PASS.
- Simplified-Chinese guard: PASS.
- Learner-facing nodes checked: 53 across five UI/content files.

## Interaction and technical render

- Required widths 375, 768, 1280, 1440, 1920: PASS for Hub and Topic 01.
- Horizontal page overflow / clipped content: none.
- Console errors: none.
- Keyboard navigation: PASS; ArrowDown advanced to `第 2 / 11 段`.
- Hub mechanism reveal, pipeline routing, Q/K/V selector, Sampling 1× and 10×, and Traditional Chinese quiz feedback: PASS.
- No-JavaScript Hub fallback: PASS.
- No-JavaScript Topic fallback: 11 visible/opaque sections, 31 Wiki links, six quiz items, no page overflow.
- Source/design lint: 0 failures, 0 warnings.
- Final Hub visual inspector: 0 failures, 0 warnings at 1440/768/390.
- Final Topic visual inspector: 0 failures, 0 warnings at 1440/768/390. The mobile pipeline is an intentional horizontally scrollable control with the active step brought into view; it does not create page overflow.

Preserved evidence:

- `teaching/presentation/validation/render-report.json`
- `teaching/presentation/validation/screenshots/`
- `.taste-skill/hub-review-final/report.json`
- `.taste-skill/topic-zh-final-3/report.json`

