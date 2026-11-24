---
artifact_id: TEACH-DECK-001-ART
status: implemented
date: 2026-11-24
---

# TEACH-DECK-001 Art Direction

## Concept

One token is the recurring visual unit. It moves from text, through vectors and contextual processing, into a probability distribution, selection, and an updated context.

## Visual system

- Direction: technical teaching deck with a tabbed-folder motif and high-contrast mechanism diagrams.
- Palette: black ground with mint, cyan, lemon, orange, blue, and pink used as stable mechanism roles.
- Typography: locally available condensed display face plus a readable system sans-serif; no network font dependency.
- Composition: causal diagrams occupy the teaching surface; provenance stays in a quieter footer layer.
- Interaction: only the three approved learning interactions are interactive.

## Deliberate media decision

The deck does not use photography or video. The topic is an invisible computational mechanism, and the approved brief requires diagrams that explain rather than decorate. Adding unrelated imagery would weaken the causal model and would create an unnecessary external-asset dependency. All visuals are code-native and factual labels are grounded in the published Week 10 Wiki.

## Accessibility and fallback

- Text and mechanism labels remain in the HTML.
- The page is navigable by headings, anchors, keyboard controls, and native `details` elements.
- With JavaScript disabled, all 11 teaching sections, all Wiki links, all six quiz items, and the static states of each mechanism remain readable.
