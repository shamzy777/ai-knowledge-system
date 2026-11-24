---
artifact_id: TEACH-DECK-001-VISUAL-CRITIQUE
date: 2026-11-24
final_status: pass
---

# TEACH-DECK-001 Visual Critique

## Round 1 — first rendered inspection

### Top three issues

1. The hero wrapped to three lines at 1440 px, weakening the opening question.
2. Provenance labels on light slides had insufficient contrast, and two source lines approached viewport edges.
3. Reveal behavior plus full-height sections created apparent blank stretches on mobile.

### Action

Returned to the CSS/layout node only. Widened and resized the hero measure, raised small-text size and contrast, made provenance disclosure flow in layout, removed unnecessary full-height constraints, and guaranteed mobile reveal visibility.

### Score

7.2/10 — clear concept and visual language, but not yet robust enough across viewports.

## Round 2 — hierarchy and responsive review

### Top three issues

1. Evidence footers on reverse-layout slides could precede the heading.
2. A fixed mobile navigation bar could cover large text during scrolling.
3. The Softmax heading wrapped to three lines at 1280 px.

### Action

Returned only to the affected layout selectors and Slide 9 heading. Ordered copy → visual → evidence consistently, changed the mobile navigation to a non-overlapping sticky bar, and composed the Softmax heading as two intentional lines.

### Score

8.7/10 — mechanism diagrams and causal rhythm were strong; the remaining issues were local hierarchy problems.

## Round 3 — final review

### Result

- Headings stay within two lines at all inspected widths.
- No covered or clipped teaching text was detected.
- The token/position distinction, Q/K/V flow, Softmax/Sampling distinction, and factuality boundary are visually explicit.
- Mobile, tablet, and desktop compositions retain the same causal order.
- The diagram-only approach is intentional: photographs and footage are not meaningful evidence for this mechanism and were not added.

### Score

9.3/10 — ready for human final review.
