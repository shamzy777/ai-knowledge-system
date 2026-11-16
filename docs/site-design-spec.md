# Week 9 Prototype Site Design Specification

## 1. Scope and evidence boundary

This document specifies the presentation design for the Week 9 prototype. It does not authorize website implementation, changes to the approved concept content, or changes to the parent AI Knowledge System.

The site must present the prototype content layer as a view onto existing canonical knowledge, not as a second knowledge base. The parent system remains the source of truth. Course names identify provenance; they must not become the site's primary information architecture.

The implementation must preserve these rules:

- one concept has one canonical node;
- courses are knowledge sources, not final knowledge categories;
- AI-generated or source-organized material is not automatically permanent knowledge;
- mastery is shown only as a recorded state, never as independently verified mastery;
- first-person learning evidence keeps its authorship and confirmation limitations;
- relationships use only supported, typed links;
- evidence limitations remain visible;
- supporting nodes without prototype pages must not be presented as complete pages or broken links.

The approved presentation content is:

- `content/concepts/neural-network-training.md`
- `content/concepts/softmax.md`
- `content/concepts/cross-entropy.md`
- `content/concepts/index.md`

The supporting canonical concepts are Neural Network, Backpropagation, Tokenization, Embedding, Self-Attention, Transformer, and Large Language Model. They may appear as graph or index nodes, but this phase does not give them full prototype pages.

## 2. Design goals

### Primary communication goal

An instructor who knows AI but has not seen this system should understand, within the first screen, that the project combines overlapping course material into a concept-oriented knowledge network.

The page argument is:

1. Separate courses contribute partial perspectives.
2. Those perspectives converge on one canonical concept.
3. Understanding and confirmation gate what becomes permanent knowledge.
4. Typed relationships connect concepts into a reusable mental model.

### Intended first-screen belief

“This is not a collection of course notebooks. It is a governed system for integrating course knowledge by concept.”

### Proof shown by the site

- Softmax, Cross Entropy, and Neural Network Training each receive meaningful contributions from both 人工智慧程式設計 and TAICA 生成式 AI.
- The intake workflow distinguishes source material, AI-assisted learning, understanding checks, confirmation, and permanent knowledge.
- A separate technical chain demonstrates supported relationships among Tokenization, Embedding, Self-Attention, Transformer, and Large Language Model.
- Provenance, recorded mastery, and evidence limitations remain attached to what is displayed.

### Primary action

The main action is **Explore concepts**. It leads to the concept index, not to course pages.

### Non-goals

- Do not make the prototype look like a course marketplace, dashboard, or general AI textbook.
- Do not add generic explanations, proof, metrics, testimonials, or unrecorded learning claims.
- Do not imply that the technical chain is cross-course; its current provenance is mainly TAICA.
- Do not make the knowledge graph an exhaustive map of the parent vault.
- Do not present recorded 🟨 states as confirmed mastery.

## 3. Visual direction

### Direction: one merge motif

Use one subject-derived motif throughout the site: multiple source streams converging through a solid junction into one canonical concept node.

The motif is functional, not decorative. At different scales it becomes:

- the hero's course-to-concept diagram;
- the branch shape in the cross-course comparison;
- the confirmation gate in the knowledge workflow;
- the relationship junction in the knowledge map;
- a compact site mark in navigation and the footer.

Do not add unrelated neural-network imagery, circuit patterns, floating particles, brains, robots, decorative graphs, or stock photography. The project's actual outputs—concept text, provenance, evidence states, and relationship diagrams—are its visual material.

### Character

The site should feel editorial, academically credible, and intentionally built, while remaining easy to explain in a classroom. Strong typography and filled colour fields should carry the design. Avoid the appearance of a SaaS landing page.

### Composition

- Desktop grid: 12 columns with equal left and right page margins.
- Tablet grid: 8 columns.
- Mobile: one compositional column, not a squeezed desktop grid.
- Alternate between text-led, diagram-led, and split-field sections so the page does not become a repeated card stack.
- Use off-centre compositions only when the merge motif balances the visual weight.
- Keep headings to two lines or fewer at every breakpoint.
- Use generous vertical spacing, but do not create blank “cinematic” gaps without content.

### Colour system

Use a restrained blush-and-aubergine palette:

```css
--background: #edccbe;
--surface: #e8c2b2;
--ink: #351a2b;
--muted-ink: #6c4857;
--inverse-background: #351a2b;
--inverse-ink: #edccbe;
```

Usage rules:

- The blush background is the primary reading field.
- Aubergine is the primary ink and the solid field for emphasis, full-page concept nodes, the understanding gate, and the closing section.
- Use the slightly darker blush surface to separate regions by tone.
- Keep any additional accent below five percent of the page; the base palette should work without it.
- Use flat colour only: no gradients, glows, glass effects, or decorative shadows.
- Separate surfaces by colour, spacing, and alignment rather than hairline borders.
- Verify normal text and interactive states against WCAG AA contrast during implementation.

### Typography

Use **General Sans** for display and body text, with a system sans-serif fallback. One family keeps the small site coherent; hierarchy comes from scale, weight, width, and placement rather than extra font styles.

Suggested scale:

| Role | Desktop | Mobile | Weight / treatment |
|---|---:|---:|---|
| Hero title | 72–88 px | 42–52 px | 700, tight tracking |
| Section title | 44–56 px | 32–38 px | 700, tight tracking |
| Concept title | 56–72 px | 38–46 px | 700 |
| Lead text | 24–30 px | 20–24 px | 400–500 |
| Body | 18 px | 17 px | 400, comfortable line height |
| Metadata | 14–15 px | 14–15 px | 500–700, sentence case |

Do not use monospaced type for ordinary labels. Reserve it for literal code names such as `compile()` and `fit()`.

### Shape and surface rules

- Prefer square corners and strong filled regions.
- A single clipped or stepped corner may identify a merge junction when it has structural meaning.
- Source badges and relationship labels are compact rectangular text blocks, not pill chips.
- Do not place every item inside a bordered card.
- Do not use icon grids. Text and diagrams already provide the required meaning.
- Navigation is a plain aligned row, not a floating rounded capsule.

### Accessibility

- All interactive controls must have visible keyboard focus.
- Minimum target size is 44 by 44 px on touch screens.
- Diagrams must have equivalent adjacent text or list representations.
- Do not communicate mastery, provenance, node availability, or relationship type by colour alone.
- Motion is unnecessary. If a small transition is used for the comparison switcher, respect `prefers-reduced-motion`.

## 4. Sitemap and routes

```text
/
├── index.html                         Home
└── concepts/
    ├── index.html                     Concept index
    ├── neural-network-training.html   Full concept page
    ├── softmax.html                   Full concept page
    └── cross-entropy.html             Full concept page
```

There are no course landing pages in this prototype. Course labels appear only as provenance.

Supporting concepts appear in the index and knowledge map as unlinked nodes. They must be visibly identified as “supporting node” or equivalent plain text, not styled like an unavailable button.

### Global navigation

```text
[merge mark] AI Knowledge System     Overview     Concepts
```

- **Overview** returns to the home page.
- **Concepts** opens the concept index.
- The current page is indicated with text and weight, not colour alone.
- Concept-detail pages may add a compact “All concepts” return link below the navigation.

## 5. Homepage specification

### Homepage narrative

The home page moves from the problem of isolated course notes to the system's concept-oriented answer. It then proves cross-course integration with actual concept evidence, explains the understanding gate, and shows how typed relationships form a connected mental model. The final sections invite concept exploration and disclose the project rules that keep the demonstration honest.

### Section sequence

#### 1. Hero: one network across courses

Purpose: make the project's central idea legible in the first screen.

Required content:

- eyebrow: `Week 9 prototype`
- H1: `AI Knowledge System`
- lead: `Building one connected mental model across multiple AI courses.`
- principle: `Courses are knowledge sources, not the final knowledge structure.`
- primary action: `Explore concepts`

The right or lower half contains a compact functional diagram:

```text
人工智慧程式設計 ─┐
                  ├━━ Softmax
TAICA 生成式 AI ─┘
```

The diagram establishes the merge motif immediately. Do not place an abstract illustration behind the copy.

#### 2. Problem: from course folders to concepts

Heading: `From course folders to concepts`

Use a split composition:

- left: separated course/source strips with fragments that cannot connect across folders;
- right: the same sources converge into shared canonical nodes;
- short explanation: organizing only by course preserves provenance but hides overlap, prerequisites, and application links.

The right side must not imply that source notes are deleted or collapsed into indistinguishable content. Source labels remain attached to their contributions.

#### 3. Cross-course proof: one concept, many perspectives

Heading: `One concept, many perspectives`

This is the homepage's main evidence section. Use a small progressive-enhancement switcher with these choices:

1. Softmax — default
2. Cross Entropy
3. Neural Network Training

The Softmax state shows:

```text
人工智慧程式設計                 TAICA 生成式 AI
classification output             probability distribution
mutually exclusive classes        argmax or sampling
          └──────────────┬──────────────┘
                       Softmax
                one canonical concept
```

The other two states use only the approved summaries in the content files:

- Cross Entropy: implemented classification loss ↔ probability/information framing and next-token training.
- Neural Network Training: Keras workflow and dataset roles ↔ prediction/loss/gradient/update mechanism and later parameter-learning application.

Each state must show both course contributions at the same time. The control switches concepts; it must not hide one course perspective behind a tab. Without JavaScript, the Softmax state remains complete and readable.

Include the plain statement: `Different contributions. One canonical concept.`

#### 4. Understanding-first workflow

Heading: `Understanding before storage`

Show the complete governed flow:

```text
Source Material
      ↓
AI-assisted Learning
      ↓
Understanding Check
      ↓
Knowledge Intake
      ↓
USER CONFIRMATION
      ↓
Permanent Knowledge
```

The User Confirmation step is a solid aubergine gate across the flow. Steps before it are staging or review states; the final step is the permanent knowledge destination.

Required supporting copy:

- `AI output is not permanent knowledge.`
- Recorded mastery and first-person learning evidence retain their limitations until the system contains confirmation evidence.

Do not add success ticks, completion percentages, or verification claims.

#### 5. Connected technical model

Heading: `A connected mental model`

Show the supported technical chain:

```text
Tokenization
  ── prerequisite ──▶ Embedding
  ── prerequisite ──▶ Self-Attention
  ── part-of ───────▶ Transformer
  ── prerequisite ──▶ Large Language Model
```

The drawn layout must make clear that the edges connect consecutive nodes, not that Tokenization has every displayed relation. A preferred horizontal rendering is:

```text
Tokenization ─▶ Embedding ─▶ Self-Attention ─▶ Transformer ─▶ Large Language Model
 prerequisite    prerequisite      part-of         prerequisite
```

Add the visible qualifier: `Current provenance: mainly TAICA 生成式 AI.`

This section demonstrates concept relationships, not cross-course breadth. Keep Neural Network Training outside the primary chain on the homepage. Its application to Transformer parameter learning belongs on the Neural Network Training detail page, where the evidence and limitation can remain together.

#### 6. Concept register

Heading: `Explore the prototype concepts`

Do not use three identical icon cards. Use a vertical editorial register:

- one wider featured row for Neural Network Training;
- two offset rows for Softmax and Cross Entropy;
- a large concept number, name, one-sentence definition, recorded mastery label, source badges, one key relationship, and `Read concept` link in each row.

The row hierarchy may vary, but all three concepts must remain equally reachable and must use the approved content verbatim or as a faithful short excerpt.

#### 7. Project rules

Heading: `Rules that travel with the project`

Use an inverse aubergine field. Explain that `AGENTS.md` keeps implementation work aligned with the knowledge-system constraints. Show three concise rules:

- one concept, one canonical node;
- provenance and uncertainty stay visible;
- unconfirmed knowledge does not become permanent knowledge.

Do not reproduce the whole project manual or imply that these are the only rules.

#### 8. Footer

Close with an oversized crop of the merge mark, the project name, and text links to Overview and Concepts. Keep the footer functional; do not add social links or legal links that do not exist.

### Homepage desktop wireframe

```text
┌──────────────────────────────────────────────────────────────────────┐
│ merge mark  AI Knowledge System              Overview   Concepts     │
├──────────────────────────────────────────────────────────────────────┤
│ WEEK 9 PROTOTYPE             │ course A ─┐                         │
│ AI Knowledge                 │           ├━━ SOFTMAX               │
│ System                       │ course B ─┘                         │
│ one connected mental model   │                                     │
│ [Explore concepts]           │                                     │
├──────────────────────────────────────────────────────────────────────┤
│ From course folders          │ separate sources → canonical network │
│ to concepts                  │                                     │
├──────────────────────────────────────────────────────────────────────┤
│ One concept, many perspectives                                     │
│ [Softmax] [Cross Entropy] [Neural Network Training]                 │
│ course contribution ─┐       canonical       ┌─ course contribution │
│                      └━━━━━━━━ node ━━━━━━━━━┘                       │
├──────────────────────────────────────────────────────────────────────┤
│ Source → AI learning → check → intake → CONFIRMATION → permanent    │
├──────────────────────────────────────────────────────────────────────┤
│ A connected mental model                                            │
│ Tokenization → Embedding → Self-Attention → Transformer → LLM       │
│ Current provenance: mainly TAICA 生成式 AI                           │
├──────────────────────────────────────────────────────────────────────┤
│ 01  Neural Network Training                         Read concept →   │
│        02  Softmax                                  Read concept →   │
│ 03  Cross Entropy                                   Read concept →   │
├────────────────────── inverse field ─────────────────────────────────┤
│ Rules that travel with the project                                  │
│ one concept / visible provenance / confirmation before permanence   │
├──────────────────────────────────────────────────────────────────────┤
│ AI Knowledge System                                 Overview Concepts│
└──────────────────────────────────────────────────────────────────────┘
```

## 6. Concept index specification

### Purpose

The index makes the current prototype scope understandable without turning course names into categories. It distinguishes three full concept pages from seven supporting graph nodes.

### Grouping

Each concept appears once in a primary thematic group:

#### Learning and training

- Neural Network — supporting node
- Neural Network Training — full page
- Backpropagation — supporting node
- Cross Entropy — full page

#### Representation and attention

- Tokenization — supporting node
- Embedding — supporting node
- Self-Attention — supporting node

#### Language generation

- Transformer — supporting node
- Large Language Model — supporting node
- Softmax — full page

The groups are browsing aids, not canonical ontological claims. Relationships remain the authoritative connection mechanism.

### Index item anatomy

Every item shows:

- concept name;
- one-sentence definition or faithful canonical summary;
- recorded mastery state, explicitly labelled `Recorded mastery`;
- source badges that identify provenance;
- one supported key relationship where useful;
- `Full prototype page` or `Supporting graph node` availability text.

Only the three full concepts are links. Supporting nodes use plain text and must not have empty `href` values, disabled buttons, or fake hover states.

### Index layout

Use one continuous register divided by large typographic group headings. Vary row width and indentation slightly to show structure. Do not use a three-column card grid.

### Index wireframe

```text
┌───────────────────────────────────────────────────────────────┐
│ Navigation                                                    │
├───────────────────────────────────────────────────────────────┤
│ Concepts                                                      │
│ Full pages and supporting nodes in one concept-oriented view. │
├───────────────────────────────────────────────────────────────┤
│ LEARNING AND TRAINING                                         │
│ Neural Network                     supporting graph node      │
│ Neural Network Training  🟨 recorded   full page        →     │
│ Backpropagation                    supporting graph node      │
│ Cross Entropy            🟨 recorded   full page        →     │
├───────────────────────────────────────────────────────────────┤
│ REPRESENTATION AND ATTENTION                                  │
│ Tokenization / Embedding / Self-Attention                     │
├───────────────────────────────────────────────────────────────┤
│ LANGUAGE GENERATION                                           │
│ Transformer / Large Language Model                            │
│ Softmax                  🟨 recorded   full page        →     │
├───────────────────────────────────────────────────────────────┤
│ Evidence note: recorded mastery is not independently verified │
└───────────────────────────────────────────────────────────────┘
```

## 7. Concept detail template

All three full pages use the same semantic order, while diagram content and emphasis change by concept.

### Required order

1. Global navigation and `All concepts` return link.
2. Concept masthead.
3. Why it matters.
4. Prerequisites.
5. Core idea.
6. Cross-course perspectives.
7. Concept relationships.
8. Applications or examples.
9. My Explanation / Learning Evidence, when present.
10. Mastery.
11. Sources.
12. Evidence limitations.

This order follows the approved content rather than rewriting it into a marketing-page pattern.

### Concept masthead

Show:

- concept name as H1;
- the approved one-sentence definition;
- `Recorded mastery: 🟨` with explanatory text nearby;
- source badges for 人工智慧程式設計 and TAICA 生成式 AI;
- a clear note that this is prototype presentation content derived from one canonical concept.

Do not display `Mastered`, `Verified`, or a progress percentage.

### Cross-course perspectives

This is the most visually prominent detail-page section after the masthead.

- Place the canonical concept name in a solid central junction.
- Place course contributions on opposite sides on desktop and above/below on mobile.
- Keep each contribution's source label attached.
- End with the approved synthesis and relationship type.
- Do not imply that each course creates a different version of the concept.

Concept-specific synthesis:

- Neural Network Training: **theory ↔ practice** between the TAICA causal loop and the AI Programming Keras workflow.
- Softmax: the same concept has different **applications** in classification and probabilistic next-token generation; the approved page also records a theory ↔ practice relationship.
- Cross Entropy: **theory ↔ practice** between distribution/information framing and implemented classification-loss usage, with language-model training as an application.

### Learning evidence

If the page contains `我的理解` or similar first-person material:

- label it `Recorded learning evidence`;
- preserve the wording from the approved content;
- show the limitation that authorship or explicit confirmation metadata is unavailable;
- visually separate it from canonical definition text.

Do not use quotation styling that implies verified authorship.

### Evidence ledger

The final part of every detail page combines Sources and Evidence Limitations into an easy-to-audit ledger while keeping their headings distinct.

- Sources identify canonical files and course/source notes.
- Evidence limitations identify unverified mastery, incomplete provenance, OCR uncertainty, unresolved mathematics, or synthesis boundaries exactly where recorded.
- The ledger is visible in the page body, not hidden in a modal or tooltip.

### Detail-page wireframe

```text
┌───────────────────────────────────────────────────────────────┐
│ Navigation                                      All concepts  │
├───────────────────────────────────────────────────────────────┤
│ CONCEPT                                                       │
│ Softmax                                                       │
│ one-sentence definition                                      │
│ Recorded mastery: 🟨   sources: [AI Programming] [TAICA]      │
├───────────────────────────────────────────────────────────────┤
│ Why it matters                  │ Prerequisites               │
├───────────────────────────────────────────────────────────────┤
│ Core idea                                                    │
├───────────────────────────────────────────────────────────────┤
│ Cross-course perspectives                                    │
│ AI Programming ───────▶ SOFTMAX ◀─────── TAICA                │
│ contribution              one node        contribution        │
│ supported synthesis and typed relationship                   │
├───────────────────────────────────────────────────────────────┤
│ Concept relationships                                        │
│ Applications / examples                                      │
├───────────────────────────────────────────────────────────────┤
│ Recorded learning evidence + authorship limitation            │
├───────────────────────────────────────────────────────────────┤
│ Mastery: recorded state, not independently verified           │
├──────────────────────── evidence ledger ──────────────────────┤
│ Sources                         │ Evidence limitations        │
└───────────────────────────────────────────────────────────────┘
```

## 8. Knowledge-map and relationship design

### Node types

#### Course/source node

- smaller rectangular strip or file-tab shape;
- explicit `Course source` label;
- course name and concise contribution;
- never used as the main navigation category.

#### Full concept node

- solid aubergine fill with blush text;
- concept name and `Full page` text;
- linked to its detail page;
- no course-specific duplicates.

#### Supporting concept node

- blush-surface fill with aubergine text;
- concept name and `Supporting node` text;
- not linked until a real page exists.

#### Confirmation gate

- a full-width solid block in the intake flow;
- labelled `User Confirmation`;
- visually distinct from a concept node so it is not mistaken for knowledge content.

### Edge rules

- Use 3–4 px solid connectors with clear arrowheads where direction matters.
- Put the relationship label beside the edge in readable text.
- Allowed labels are: prerequisite, part-of, cause/effect, evolution, application, contrast, theory ↔ practice, and cross-domain analogy.
- Do not use a generic `related to` edge.
- Do not draw an edge merely because two nodes occur on the same page.
- When a relationship is a presentation-level synthesis rather than an explicit canonical field, keep the supporting prose available next to it.

### Approved prototype edges

| Source | Target | Type | Evidence treatment |
|---|---|---|---|
| Neural Network | Neural Network Training | prerequisite | Show on the training detail page; supported by the approved concept's prerequisites. |
| Backpropagation | Neural Network Training | part-of | Show on the training detail page; supported by the approved training sequence and relationships. |
| Cross Entropy | Neural Network Training | part-of | Show on the training detail page; supported by the approved loss/training sequence. |
| Neural Network Training | Transformer parameter learning | application | Express as prose or an application edge on the training page, not as a new canonical node; the approved page attributes this application to TAICA Week 4. |
| Tokenization | Embedding | prerequisite | Use in the technical chain; Embedding records Tokenization as a prerequisite. |
| Embedding | Self-Attention | prerequisite | Use in the technical chain; Self-Attention records Embedding as a prerequisite. |
| Self-Attention | Transformer | part-of | Use in the technical chain; the canonical material describes Self-Attention as a core Transformer mechanism. |
| Transformer | Large Language Model | prerequisite | Use in the technical chain; Large Language Model records Transformer as a prerequisite. |

Cross-course perspective relationships are shown within their concept sections rather than as duplicate concept nodes:

- TAICA Neural Network Training framing ↔ AI Programming implementation: theory ↔ practice.
- Softmax → classification and Softmax → next-token generation: application.
- TAICA Cross Entropy framing ↔ AI Programming loss implementation: theory ↔ practice.

### Layout behavior

- Use a deterministic small diagram, not a force-directed canvas.
- No drag, zoom, physics, or hidden off-screen nodes are needed.
- Keep edge crossings to zero in the primary diagrams.
- Every graph has a nearby text list that repeats the node sequence and relationship labels.
- Hover may reinforce a connection, but no information may depend on hover.

## 9. Responsive behavior

### Navigation

- Desktop: horizontal wordmark and two links.
- Mobile: wordmark plus a text `Menu` control, or show both links inline if they fit at 320 px without crowding.
- Do not use a hamburger icon without a text label.

### Hero

- Desktop: copy and merge diagram share the grid.
- Mobile: copy first, action second, diagram third.
- The H1 stays within two lines at 320 px.

### Cross-course comparison

- Desktop: course contributions flank the central concept junction.
- Mobile: source A, source B, then the shared canonical concept. Connectors become short vertical rules.
- The concept switcher becomes a stacked text control or a full-width segmented list with square corners.
- All controls retain 44 px touch targets.

### Understanding-first workflow

- Desktop: horizontal if labels remain readable.
- Mobile: vertical sequence.
- The User Confirmation gate becomes a full-width horizontal band across the vertical path.

### Technical chain

- Desktop: horizontal node sequence.
- Mobile: vertical ordered list with relationship labels between nodes.
- Do not require horizontal scrolling or pinch zoom.

### Concept register and index

- Rows become full width on mobile.
- Metadata wraps below the concept name in a predictable order: availability, recorded mastery, sources, relationship.
- Indentation used on desktop resets on mobile so no row becomes too narrow.

### Concept detail

- Masthead metadata stacks below the definition.
- Cross-course contributions stack around one shared concept junction.
- Prerequisites and Why It Matters become consecutive sections rather than narrow columns.
- Sources and Evidence Limitations stack while retaining separate headings.
- Code tokens wrap without forcing horizontal page scroll.

### Baseline responsive checks

Test at 320, 375, 768, 1024, and 1440 px. Also test keyboard navigation, 200% zoom, reduced motion, and long mixed Chinese/English course labels.

## 10. Technical approach

### Option A: plain HTML, CSS, and small vanilla JavaScript

Benefits:

- no package install or build pipeline;
- deploys directly to GitHub Pages;
- easy to inspect and explain in a Week 9 demonstration;
- the content and provenance remain visible in the generated pages;
- progressive enhancement is sufficient for the comparison switcher and mobile menu.

Costs:

- shared page structures are repeated across three concept pages;
- approved Markdown must be transferred carefully into semantic HTML;
- changes to the source content require manual synchronization.

Mitigation:

- use one shared stylesheet and one small script;
- define and reuse the semantic patterns in section 11;
- keep approved Markdown as the content source of truth;
- add source-path comments in the HTML during implementation;
- perform a content parity review after rendering.

### Option B: Astro with Markdown content collections

Benefits:

- Markdown can remain close to the rendering source;
- shared layouts and components reduce repeated markup;
- schema validation can make content fields consistent;
- the site still produces static output for GitHub Pages.

Costs:

- requires dependencies, configuration, a build step, and likely a deployment action;
- adds framework concepts that are not necessary for five routes;
- increases implementation and troubleshooting surface for a short prototype phase.

### Recommendation

Use **plain semantic HTML, one shared CSS file, and minimal vanilla JavaScript**.

The prototype is small, content is already approved, and its evaluation depends more on transparent provenance and visual explanation than on content-pipeline automation. JavaScript should only enhance the cross-course concept switcher and, if needed, mobile navigation. The default HTML must remain complete without JavaScript.

A later implementation may use this shape:

```text
week09-prototype/
└── site/
    ├── index.html
    ├── concepts/
    │   ├── index.html
    │   ├── neural-network-training.html
    │   ├── softmax.html
    │   └── cross-entropy.html
    └── assets/
        ├── styles.css
        └── site.js
```

This is a proposed implementation structure only. It is not created in this phase.

## 11. Reusable component patterns

These are semantic design patterns, not a requirement to introduce a JavaScript component framework.

### SiteNav

Wordmark, Overview link, Concepts link, current-page state, and mobile menu behavior.

### MergeMark

The compact course-stream-to-canonical-node symbol used in the wordmark, hero, and footer. It must remain recognizable without animation.

### SectionHeading

Optional sentence-case eyebrow, two-line maximum heading, and short explanatory lead.

### MasteryLabel

Always renders the phrase `Recorded mastery`, the recorded symbol or state, and—where space permits—`not independently verified`. It never renders a success badge.

### SourceBadge

Rectangular text label for a course or source. It communicates provenance only and never acts as a primary category link.

### RelationshipLabel

Displays one allowed relationship type next to an edge or within a text list. It must not abbreviate the label into an unexplained icon.

### SourceNode

Course name, contribution summary, and source role. Used only inside comparison or provenance diagrams.

### ConceptNode

Concept name, availability state, and optional recorded mastery. Variants distinguish linked full-page nodes from unlinked supporting nodes without duplicating the concept.

### CrossCourseComparison

Concept selector, two source contributions, central canonical concept, typed synthesis, and no-JavaScript fallback. This is the homepage's one intentionally interactive element.

### KnowledgeFlow

The six-stage source-to-permanent-knowledge sequence with a distinct User Confirmation gate and adjacent text alternative.

### KnowledgeMap

Deterministic node-and-edge diagram plus accessible relationship list. It renders only approved nodes and edges.

### ConceptRegisterItem

Concept name, short definition, recorded mastery, source provenance, one key relationship, page availability, and link when a page exists.

### ConceptMasthead

Concept title, approved definition, recorded mastery, sources, and prototype/canonical distinction.

### PerspectivePanel

One source's contribution to a shared concept. Two panels converge into one canonical junction rather than appearing as competing concept cards.

### EvidenceLedger

Sources and evidence limitations in two clearly labelled regions. It preserves unresolved details rather than smoothing them into definitive copy.

### SiteFooter

Closing merge mark, project name, and existing navigation links only.

## 12. Content and interaction rules for implementation

- Use the approved content files as the only source for substantive concept copy.
- Do not “improve” a concept page with generic machine-learning facts.
- Do not shorten evidence limitations in a way that changes their meaning.
- Preserve code formatting, course names, and stated Week references.
- Do not convert first-person evidence into a site-authored explanation.
- Do not add mastery scoring, progress bars, quizzes, or completion states.
- Do not add a search box unless the prototype later contains enough pages to make search meaningful.
- Do not add account, save, edit, comment, or course-filter controls.
- Do not make supporting nodes clickable until their pages exist.
- Use visible text for all relationship types and provenance states.

## 13. Decisions requiring approval before implementation

1. **Interface language:** use English interface copy while preserving original Chinese course names. A bilingual interface would require approved translations and more mobile layout work.
2. **Font delivery:** load General Sans from an approved web source with a system sans-serif fallback, or use the fallback only for a fully local prototype.
3. **Palette:** approve the blush-and-aubergine editorial direction before coding; it is intentionally distinct from generic blue or neon AI styling.
4. **Homepage comparison:** include all three approved concepts in the switcher. The simpler alternative is a static Softmax comparison.
5. **Technical graph scope:** keep the homepage chain focused on Tokenization → Embedding → Self-Attention → Transformer → Large Language Model, and show the Neural Network Training → Transformer application only on the training detail page.

Recommended defaults are the first option in each item and the focused graph scope described in item 5.

## 14. Design acceptance criteria

The design is ready for implementation when:

- the first screen communicates concept-oriented cross-course integration;
- the cross-course proof uses only approved contributions;
- the understanding gate is visually and textually unambiguous;
- courses remain provenance, not top-level content categories;
- the technical chain is labelled as mainly TAICA-supported;
- full-page and supporting nodes are visually distinguishable without broken links;
- recorded mastery never reads as verified mastery;
- first-person evidence retains its authorship limitation;
- every drawn relationship has an allowed label and an evidence basis;
- the home, index, and detail compositions work at 320 px without horizontal scrolling;
- the site remains understandable with JavaScript disabled;
- no unsupported content, source, relationship, or user-understanding claim is introduced.
