# TEACH-HUB-001 — reusable Learning Hub decision

Timestamp: 2026-11-24T19:56:53+08:00  
Status: implemented; awaiting human review

Decision: keep the validated static HTML/CSS/JavaScript implementation and introduce a two-level site structure:

`Learning Hub / Homepage → Topic 01 → eleven-section interactive teaching experience`

Architecture:

- `teaching/presentation/index.html` is navigation and presentation only; it is not a knowledge source.
- `teaching/presentation/topics.js` is the topic metadata registry.
- `teaching/presentation/hub.js` renders available topic cards from the registry.
- `teaching/presentation/topics/next-token.html` is the Topic 01 entry.
- `topic.css` and `topic.js` retain the existing mechanism visuals and interactions.

The registry stores `id`, `slug`, `label`, `title`, `description`, `status`, `difficulty`, `duration`, `format`, section count, concept tags, entry path, and optional progress. Only Topic 01 is registered. The future area says that more topics may be added, but contains no fabricated lesson.

Visual direction retained: modern editorial interactive science explainer, education/playful direction seed `1788920606`, warm light ground, bold condensed display type, semantic accent fields, code-native mechanism diagrams, and no decorative stock imagery. No art-direction redraw was needed because the established direction matched the human review.

