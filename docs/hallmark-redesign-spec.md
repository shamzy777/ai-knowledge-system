# Hallmark Knowledge Explorer Redesign Specification

## Status and boundary

This document specifies a future full redesign of the Week 9 prototype. It does not implement the redesign, change the approved prototype content, or change any file in the parent AI Knowledge System.

The parent vault remains the source of truth. Any future presentation copy must be traceable to the canonical files and course/source notes listed here. Prototype pages remain presentation-layer views, not new canonical nodes.

### Hallmark redesign read

- **Audience:** an instructor or reviewer who understands AI but has not seen this knowledge system.
- **Visitor job:** enter a small concept network, understand one concept, and continue along supported relationships.
- **What stays:** the aubergine/blush/neutral palette, General Sans, editorial research-tool character, merge-junction, course-versus-concept distinction, provenance, evidence limitations, understanding-first workflow, existing routes, and supported content.
- **What changes:** the static Concept Index becomes a Knowledge Explorer; the homepage becomes shorter; concept pages share an evidence architecture but use different mechanism visualizations.
- **What is broken now:** the site explains a connected mental model but does not let a visitor move through one. The Hallmark audit also found wide-screen, density, wrapping, token, mastery-icon, and repeated-motif problems that must be solved at component-system level.
- **Redesign depth:** full, when implementation is authorized. This is not a restyle or a patch collection.

### Design thesis

The redesigned prototype is a compact, deterministic knowledge browser. Its signature is a selected canonical concept surrounded by its prerequisites, downstream concepts, course contributions, relationship evidence, and learning state. It does not use a force-directed graph, dashboard metrics, generic AI imagery, or decorative motion.

The central promise is experiential:

> Courses contribute evidence. Canonical concepts organize it. Typed paths let the visitor continue learning.

---

## A. New user journey

### Primary journey

```text
Home
→ see the problem of isolated course notes
→ see one Softmax cross-course proof
→ understand the confirmation gate
→ enter Knowledge Explorer
→ search or select a concept
→ read a concise selected-concept sheet
→ inspect prerequisites, downstream concepts, sources, and relation types
→ follow one supported path
→ open a full concept experience when available
→ continue through Explore next without returning to the page top
```

### Explorer task loop

```text
Find concept
→ orient: definition + recorded learning state
→ locate: prerequisites + downstream roles
→ verify: sources + evidence status
→ move: choose a related concept
```

### Questions answered on every concept experience

1. **Where am I?** Concept name, domain cluster, canonical/presentation distinction.
2. **What did I need before this?** Explicit prerequisite paths.
3. **How does it work?** A short mechanism visualization grounded in the vault.
4. **Who contributed what?** Source/course contributions shown as provenance, not categories.
5. **What can I trust?** Recorded mastery, learning evidence, unresolved questions, and synthesis limits.
6. **Where can I go next?** Two to four meaningful downstream or contrast paths.

### Secondary journeys

- **Source lens:** filter by a course to see which canonical concepts it contributes to, without creating a course notebook view.
- **Learning-state lens:** view a concept's recorded state and caveat; do not rank, score, or imply verified progress.
- **Evidence audit:** expand source and limitation details without leaving the concept context.

---

## B. Sitemap

Existing routes are preserved.

```text
/
└── index.html                              Home / orientation

/concepts.html                              Knowledge Explorer
├── #concept-neural-network-training        selected concept state
├── #concept-softmax
├── #concept-cross-entropy
└── #concept-<supporting-concept>

/concepts/
├── neural-network-training.html            Tier 1 full experience
├── softmax.html                             Tier 1 full experience
└── cross-entropy.html                       Tier 1 full experience

/index.html#agents                          System rules / AGENTS context
```

### Global navigation

```text
[merge mark] AI Knowledge System     Home     Knowledge Explorer     System rules
```

- `Home` explains why the system exists.
- `Knowledge Explorer` is the primary product experience.
- `System rules` preserves the existing `#agents` destination and explains the governance boundary.
- Full concept pages add a visible `Back to Explorer` link near the top and an `Explore next` region before the footer.
- Source/provenance context remains attached to concepts; no course landing pages are introduced.

### Page classification for the future Hallmark run

| Route | Hallmark scope | Reason |
|---|---|---|
| `index.html` | Page | A short orientation and proof narrative. |
| `concepts.html` | App screen | A search/select/filter tool someone works in; no marketing hero or screen word budget. |
| Three concept pages | Long-document page | Reading experiences with one concept-specific mechanism and evidence trail. |

---

## C. Knowledge Explorer desktop wireframe

The explorer uses a search-led, two-region workbench rather than a graph canvas or analytics dashboard. At a 1440px viewport, the capped content area is approximately 1312px: a 360px concept register, a 32px gap, and the remaining selected-concept workspace.

```text
┌──────────────────────────────────────────────────────────────────────────┐
│ AI Knowledge System       Home   Knowledge Explorer   System rules       │
├──────────────────────────────────────────────────────────────────────────┤
│ Knowledge Explorer                                                        │
│ Search concepts, definitions, sources, or relationship terms              │
│ [ Search field......................................................... ] │
│ Cluster: [All] [Training] [Representation] [Language]                     │
│ Source:  [All sources] [AI Programming] [TAICA]   [Full experiences only] │
├───────────────────────────────┬──────────────────────────────────────────┤
│ Concept register              │ Selected canonical concept                │
│                               │                                           │
│ Training                      │ Softmax                                   │
│ Neural Network                │ Converts multiple scores into a relative  │
│ Neural Network Training       │ distribution whose values sum to one.     │
│ Loss Function                 │                                           │
│ Cross Entropy                 │ Recorded state: 可以解釋                   │
│ Backpropagation               │ Not independently verified                │
│                               │ Sources: 人工智慧程式設計 · TAICA 生成式 AI  │
│ Representation               │                                           │
│ Tokenization                  │ Mental-model position                     │
│ Embedding                     │ Activation Function ─ prerequisite ─┐     │
│ Self-Attention                │ Classification ───── prerequisite ──┤     │
│ Transformer                   │                                  Softmax  │
│                               │                                     ├ application
│ Language                      │ Classification                       │     │
│ Language Model                │ Language Model generation            │     │
│ Large Language Model          │                                           │
│                               │ Mechanism preview                         │
│ selected item is explicit     │ scores → Softmax → distribution           │
│ and keyboard focusable        │                    ├ argmax               │
│                               │                    └ sampling             │
│                               │                                           │
│                               │ [Open full concept experience]            │
│                               │ Explore next: Distribution · Sampling     │
├───────────────────────────────┴──────────────────────────────────────────┤
│ Evidence boundary: relationships may formalize supported prose; mastery   │
│ states have no independent confirmation record.                           │
└──────────────────────────────────────────────────────────────────────────┘
```

### Desktop behavior

- The concept register is an index, not a stack of large cards.
- The selected sheet is the visual signature and receives most of the width.
- Concept selection changes the selected sheet and URL state; it does not open a modal.
- A relationship receives emphasis only when focused, hovered, or selected. Both endpoints and the text label highlight together.
- Course source panels appear inside the selected sheet only when useful; course names never become the left-side information architecture.
- Full-page availability is an action within the selected concept, not a visual class of course material.

### Filters

Only three controls materially improve this small dataset:

1. **Conceptual cluster:** Training, Representation, Language. This reduces scanning and reflects the two demonstration clusters without claiming a permanent ontology.
2. **Source course:** All sources, 人工智慧程式設計, TAICA 生成式 AI. This demonstrates cross-course integration while keeping sources secondary.
3. **Full experience only:** a simple checkbox/toggle for the three Tier 1 pages.

Do not add mastery or relationship-type filters in Week 9:

- mastery has only two recorded states in the selected scope and no verified history;
- relationship role is more useful as an exploration path than as a global filter;
- more filters would turn a small learning tool into a dashboard.

### Search

Search indexes visible DOM data for:

- canonical name and aliases;
- one-sentence definition;
- official source names;
- relationship labels and named endpoints.

Progressive enhancement contract:

- without JavaScript, all concept rows and the default Softmax sheet remain readable, and anchor links reach concept sections;
- with JavaScript, the search narrows rows, updates a visible result count, and preserves the selected concept when it still matches;
- empty state: `No concepts match these filters.` plus a `Clear filters` action;
- URL state records selection and active filters so a view can be revisited or shared;
- no substantive concept copy exists only in JavaScript.

---

## D. Mobile Explorer wireframe

The mobile pattern is a linear explorer, not a miniature graph and not a modal bottom sheet.

```text
┌──────────────────────────────┐
│ AI Knowledge System          │
│ Knowledge Explorer           │
├──────────────────────────────┤
│ [ Search concepts......... ] │
│ [Cluster] [Source] [Full]    │
├──────────────────────────────┤
│ Results                      │
│ Softmax              selected│
│ Cross Entropy                │
│ Neural Network Training      │
│ Distribution                 │
│ Sampling                     │
├──────────────────────────────┤
│ Selected concept             │
│ Softmax                      │
│ concise definition           │
│ Recorded · 可以解釋          │
│ not independently verified   │
│                              │
│ Prerequisites                │
│ Activation Function          │
│ Classification               │
│                              │
│ Mechanism                    │
│ scores                       │
│   ↓                          │
│ Softmax                      │
│   ↓                          │
│ distribution                 │
│   ├ argmax                   │
│   └ sampling                 │
│                              │
│ Sources [show evidence]      │
│ Explore next                 │
│ Distribution   Sampling      │
│ [Full concept experience]    │
│ [Back to results]            │
└──────────────────────────────┘
```

### Mobile behavior

- Search comes first; filters open as native disclosures or a compact fieldset, never an icon-only drawer.
- Results remain a normal list with 44px targets. Selection scrolls to `Selected concept` and updates the hash.
- `Back to results` returns to a stable anchor and restores keyboard focus.
- Relationship paths become vertical labelled sequences; nothing requires horizontal scrolling or pinch zoom.
- Evidence uses native `<details>` with a clear summary. The core definition, state, prerequisites, and next paths remain visible when details are closed.
- The selected sheet is part of document flow so browser Back, text selection, zoom, and screen readers behave predictably.

---

## E. Concept depth tiers

### Tier 1 — Full Concept Experience

Keep exactly three Tier 1 concepts:

1. **Neural Network Training** — strongest theory-to-practice mapping, rich implementation examples, and a complete causal loop.
2. **Softmax** — clearest proof that one canonical mechanism supports different course applications.
3. **Cross Entropy** — connects implementation, probability/information framing, classification, and language-model training while preserving unresolved mathematics.

Do not add a fourth Tier 1 page in Week 9:

- **Neural Network** has enough content, but it is broad and would duplicate both the training and architecture paths. It is more useful as a rich explorer hub.
- **Self-Attention** has a strong mechanism and worked classroom example, but current provenance is mainly one TAICA course.
- **Transformer** and **Large Language Model** are substantial but also mainly single-course and are better demonstrated as a connected path.

### Tier 2 — Rich Explorer Concepts

These ten concepts have enough evidence for a concise selected sheet with definition, mechanism, sources, mastery, relationships, unresolved questions, and Explore next:

1. Neural Network
2. Loss Function
3. Backpropagation
4. Activation Function
5. Distribution
6. Language Model
7. Embedding
8. Self-Attention
9. Transformer
10. Large Language Model

### Tier 3 — Graph Nodes

These eight nodes materially clarify the two clusters without requiring a rich sheet:

1. Weight and Bias
2. Gradient
3. Optimizer
4. Epoch and Batch
5. Classification
6. Sampling
7. Tokenization
8. Query, Key, and Value

Tier 3 selection is intentionally controlled. The following canonical concepts are inspected but deferred from the Week 9 explorer:

- **Forward Propagation:** show it as a labelled stage inside Neural Network Training rather than another standalone node.
- **Learning Rate:** keep it inside the Optimizer/Gradient explanation for this prototype.
- **Prompt Engineering** and **Hallucination:** useful downstream LLM branches, but outside the two core Week 9 demonstration paths.
- **Sigmoid:** no root-level canonical `Sigmoid.md` exists. It may appear only as a supported contrast term; it must not be rendered as a canonical node.

---

## F. Full concept-page architecture

The pages share evidence semantics, navigation, and component language. They do not share one rigid ten-section layout.

```text
Global navigation + Back to Explorer
↓
Concept masthead
  name · one-sentence definition · recorded state · sources
↓
At a glance
  role · prerequisites · downstream concepts · full-page evidence caveat
↓
Mental-model position
  compact prerequisite/current/downstream path
↓
Problem / role
  one short section explaining why the mechanism exists
↓
Primary mechanism visualization
  concept-specific; the page's visual signature
↓
Cross-course perspectives
  both contributions visible; optional focus control highlights one
↓
Concrete example
  only a recorded classroom or canonical example
↓
Related paths
  typed relationships with evidence access
↓
Learning state
  recorded mastery + first-person-labelled evidence + caveat
↓
Open questions and source ledger
  unresolved details, provenance, synthesis boundaries
↓
Explore next
  two to four next concepts + Back to Explorer
```

### Density rules

- One idea per viewport; do not achieve density reduction by deleting evidence.
- Definition and state are concise; source details move into an expandable ledger.
- Use diagrams, comparison rows, and labelled paths before paragraph stacks.
- Keep evidence limitations available in the page body and visible without JavaScript; native disclosures may compact secondary detail.
- Merge `Concept relationships` and `Applications / examples` when they repeat the same endpoints.
- Keep first-person-labelled evidence visually separate from canonical definition text.

---

## G. Tier 1 primary visualizations

### Neural Network Training — parameter-learning loop

Use a loop around the model parameters, not a horizontal series of equal cards.

```text
                         prediction
                             ↓
data / batch → forward computation → loss
       ↑                          ↓
next iteration ← updated θ ← optimizer update
                              ↑
                    backpropagation computes gradients
```

Evidence-correct ordering matters. The canonical system says Backpropagation computes gradients and the Optimizer updates parameters. Do not use the suggested order `Gradient → Backpropagation` as though gradient exists before it is calculated.

Below the loop, use a two-row mapping rail:

```text
TAICA mechanism       prediction · loss · gradient calculation · parameter update
AI Programming       fit() · batch_size · epochs · validation · evaluate()
```

- `compile()` configures loss, optimizer, and metrics; it is not drawn as a loop stage.
- Validation is a branch after an epoch and explicitly performs no backpropagation or parameter update.
- Test/evaluate is a final-evaluation branch, not part of training updates.
- Application callouts may mention Embedding and Transformer parameter learning, attributed to TAICA Week 4.

### Softmax — distribution and decision fork

The mechanism is one central conversion with two downstream decisions.

```text
candidate scores
      ↓
   Softmax
      ↓
relative distribution
      ├── argmax ── classification
      └── sampling ─ generation
```

Use the recorded canonical example:

```text
[cat, dog, bird] → [0.66, 0.24, 0.10]
```

Do not invent input score values. Attach source contributions to downstream contexts:

- 人工智慧程式設計: classification output, mutually exclusive classes, sigmoid contrast.
- TAICA 生成式 AI: probability distribution, argmax/sampling, next-token generation.

Sigmoid appears in a compact contrast row labelled `contrast term, no canonical prototype node` until a canonical file exists.

### Cross Entropy — target/model comparison to training signal

Use two aligned distribution rows feeding one loss junction:

```text
target distribution P      [1, 0, 0]
model distribution Q       [0.6, 0.3, 0.1]
             \              /
              Cross Entropy
                    ↓
       penalty / training loss
                    ↓
        Neural Network Training
```

- Highlight the supported intuition: low probability on the correct target produces a larger loss.
- Split the application lane after the loss: classification implementation and next-token training.
- Keep `Q closer to P → Cross Entropy smaller → KL Divergence smaller` inside the evidence/open-question region, not as a completed derivation.
- State that the full mathematical derivation and task-dependent MSE comparison remain unresolved.

---

## H. Homepage changes

The homepage becomes a four-part orientation plus footer.

### Remain

- Project identity, merge mark, and the sentence `Courses are knowledge sources, not the final knowledge structure.`
- One Softmax source-to-canonical merge as the first-screen proof.
- The understanding-first flow with User Confirmation as a gate.
- A direct primary action to enter the Knowledge Explorer.

### Compress

- Hero: retain H1, one short sentence, the principle, one action, and the Softmax merge. Move the longer explanatory paragraph below the fold or fold it into the next section.
- `From course folders to concepts`: reduce to one problem/answer comparison immediately after the hero.
- `Rules that travel with the project`: reduce to three governance statements and a link to `#agents` context.

### Merge

- Merge the current problem section with the homepage explanation of concept-oriented organization.
- Merge the current concept register into the final Knowledge Explorer invitation; do not repeat three large concept cards on Home.
- Merge the detailed AGENTS explanation and evidence boundary into one concise system-rules section.

### Move

- Move the Tokenization → LLM technical chain into the Explorer as a preset path called `Language-model foundations`.
- Move all detailed concept browsing, source badges, mastery states, and relationship lists into the Explorer.
- Move the long future-agent example from the homepage to the System rules context.

### Disappear from Home

- The three repeated full-page concept cards.
- The large standalone technical-chain section.
- The long six-item future-agent task example.
- Repeated mastery disclaimers that are better attached to concepts and the Explorer evidence boundary.

### New homepage sequence

```text
1. Hero: problem + Softmax merge + Enter Explorer
2. Softmax cross-course proof: one mechanism, two applications
3. Understanding gate: AI output is not permanent knowledge
4. Explorer invitation: follow Training or Language-model foundations
5. Compact system rules + footer
```

---

## I. Component system

### Foundations

- **DesignTokens:** capped container, 12-column page grid, two breakpoints, colour/type/spacing/motion tokens, and Hallmark stamp.
- **SiteNav / SiteFooter:** shared routes, current-page state, no arrow suffixes, 44px targets.
- **MergeMark:** reserved for real convergence of sources into one canonical concept; not repeated as a generic side border.

### Explorer components

- **ExplorerShell:** search area, filter fieldset, concept register, selected workspace, evidence boundary.
- **ConceptSearch:** labelled input with result status and clear action; no search-only content.
- **ExplorerFilters:** cluster, source, and full-experience controls with URL state.
- **ConceptRegister:** semantic list grouped by browsing cluster.
- **ConceptRow:** name, short definition when selected, source count, recorded state text, availability.
- **SelectedConceptSheet:** definition, state, sources, mental-model position, mechanism preview, evidence disclosure, full-page action, Explore next.
- **RelationshipPath:** deterministic nodes and labelled edges; accessible list equivalent.
- **ExploreNext:** two to four evidence-backed paths; never a generic recommendation carousel.
- **EmptyResults:** names the empty condition and offers `Clear filters`.

### Knowledge/evidence components

- **CanonicalConceptNode:** solid aubergine field; one concept identity only.
- **SupportingConceptNode:** neutral/blush field with text availability; clickable only when it selects real Explorer content.
- **SourceContribution:** paper-like source block with official course name and contribution. It is not a navigation category.
- **SourceLens:** highlights a course's contribution across selected concepts without hiding the canonical concept.
- **RelationshipLabel:** always prints an allowed relation type.
- **LearningState:** CSS marker + `Recorded state` + vocabulary label + independent-verification caveat.
- **EvidenceDisclosure:** native `<details>` for source paths, synthesis basis, first-person evidence limitations, and unresolved questions.
- **EvidenceLedger:** full visible source and limitation record on Tier 1 pages.

### Tier 1 components

- **ConceptMasthead:** title, one sentence, recorded state, source summary, Back to Explorer.
- **AtAGlance:** role, prerequisites, downstream endpoints, knowledge-layer note.
- **MentalModelPosition:** compact path, not a generic graph.
- **MechanismFigure:** concept-specific content; no shared card sequence.
- **CrossCoursePerspective:** both contributions visible with optional focus, never course-specific duplicate concepts.
- **ConcreteExample:** one recorded example with exact evidence boundary.
- **LearningEvidence:** preserves first-person-labelled text and unavailable authorship/confirmation metadata.

### Learning-state visual language

Do not use emoji glyphs as interface icons or a progress bar that implies verified advancement.

```text
Recorded state
[patterned CSS marker] 可以解釋
Not independently verified
```

- The marker is a CSS square/short bar whose colour and pattern vary by state.
- The vocabulary label is always printed; colour is redundant.
- `Recorded state` and `Not independently verified` appear at first use on every page.
- A full five-state legend may appear in the System rules context, not repeated on every concept.
- The underlying permanent vocabulary remains: 不理解, 聽過但模糊, 可以解釋, 可以運用, 可以和其他概念建立連結.

### Source visual language

- Official course names are preserved exactly.
- `TAICA` remains uppercase because it is the official source name.
- Source identity uses body type at 16px or larger, normal tracking, and a distinct paper/file-tab surface.
- Use `Source` as a semantic `<dt>` or panel heading, not as a decorative eyebrow.
- Course contribution text follows the source name; no thick left border is required.

### Relationship visual language

Every edge includes visible text. Colour may reinforce but never define type.

| Type | Text label | Line/position treatment |
|---|---|---|
| prerequisite | `prerequisite` | solid directional line entering the concept from the left/top |
| part-of | `part of` | bracket or double-stem entering the containing concept |
| cause/effect | `causes` / `produces` | solid directional line between mechanism stages |
| application | `applied in` | solid line leaving the concept toward a use case |
| contrast | `contrast` | two parallel endpoints separated by a vertical rule; no directional arrow |
| theory ↔ practice | `theory ↔ practice` | bidirectional line between two source contributions |
| evolution | `evolves into` | dashed directional line with chronological order stated in text |
| cross-domain analogy | `analogy` | dotted bidirectional line with an adjacent caveat |

No `is-a` relation is introduced. Taxonomic statements remain prose in this prototype.

---

## J. Interaction system

Only interactions with a learning or navigation purpose are included.

| Interaction | Purpose | No-JavaScript behavior |
|---|---|---|
| Search | Find a concept by name, definition, source, or relation term. | Full register remains readable. |
| Concept selection | Replace the selected sheet and orient the visitor. | Anchor links reach static concept sections; Softmax is the default sheet. |
| Three filters | Reduce scanning by cluster, source, or full-page availability. | All concepts remain visible. |
| Relationship focus | Show the selected edge's endpoints and evidence label. | All paths and labels remain visible. |
| Evidence disclosure | Reduce wall-of-text while keeping audit detail available. | Native `<details>` works without custom JS; important caveats stay outside closed details. |
| Source focus | Compare one contribution while retaining both sources and the canonical node. | Both perspectives remain fully visible. |
| Explore next | Continue along a supported relationship. | Normal links/anchors work. |

### Interaction rules

- Keyboard selection and pointer selection produce the same state.
- Focus appears instantly and never relies on colour alone.
- Search/filter/selection state is reflected in the URL when JavaScript is active.
- No content appears only on hover.
- No decorative parallax, counters, animated graph physics, or page-load reveals.
- Motion, if any, is limited to short opacity/transform state feedback with reduced-motion fallback.
- Controls implement default, hover, focus, active, disabled, loading, error, and success only where those states genuinely apply. Search has default/hover/focus/filled/empty-result states; it does not invent a server success state.

---

## K. Hallmark floor fixes mapped to components

| Audit finding | System-level redesign response | Owning component/foundation |
|---|---|---|
| Wide-screen container | Replace `118rem` with one centred 1312px content measure inside a 1440px container; grids do not gain columns at 1920px. | DesignTokens, ExplorerShell, page layouts |
| Missing `html` overflow guard | Apply `overflow-x: clip` to both `html` and `body`; never use `100vw`. | Base CSS |
| Excessive screen density | One short selected sheet region per screen; compact source summaries; native evidence disclosure; merge repeated sections rather than delete evidence. | SelectedConceptSheet, Tier 1 architecture |
| Arrow characters in links | Link labels are verbs without arrow glyphs: `Open full concept`, `Back to Explorer`, `Explore Softmax`. Relationship arrowheads remain diagram geometry with text alternatives. | SiteNav, ExploreNext, link styles |
| Mastery emoji icons | Replace visible emoji with a CSS state marker and printed vocabulary label. | LearningState |
| Raw spacing outside tokens | All margin, padding, gap, control sizes, and optical nudges use named tokens; allowed optical exceptions are recorded. | DesignTokens and every component |
| TAICA small-cap trigger | Preserve official spelling at body size, normal tracking, within a source-identity block rather than a tiny badge. | SourceContribution, SourceLens |
| Relationship wrapping | Use `minmax(0, 1fr)`, `min-width: 0`, breakable concept titles, short action labels, and vertical mobile paths. | RelationshipPath, ConceptRow, ExplorerShell |
| Technical-chain overflow | Move chain to deterministic Explorer preset; desktop uses measured rows/paths, mobile uses a vertical ordered list. | RelationshipPath |
| Thick left-border overuse | Reserve heavy junctions for actual convergence; use surface changes, hairlines, brackets, and spacing elsewhere. | MergeMark, SourceContribution, section surfaces |

Additional Hallmark requirements for future implementation:

- first CSS line is the completed Hallmark redesign stamp, followed by critique and any valid Reflex waivers;
- all colour and font values are tokenized;
- display heads use `overflow-wrap: break-word` and `min-width: 0`;
- every interactive element has instant `:focus-visible`;
- content is visible without scripting;
- no invented figures, claims, testimonials, or source counts;
- concept-page hero/masthead content fits at 1280×800;
- page-scope sections remain around 80 words per viewport; Explorer uses app-screen scope instead.

---

## L. Content extraction matrix

### Reading key

- **AI Programming:** `Courses/人工智慧程式設計/2026-09-29 手寫筆記整理.md` and/or `多層感知器的學習、訓練與驗證流程.md`.
- **TAICA W2/W3/W4:** the corresponding `Courses/TAICA 生成式 AI/` course notes.
- **AI Methods:** `Courses/人工智慧方法與工具/人工智慧方法與工具.md`; for neural-network concepts this is usually an index reference, not a substantive distinct explanation.
- Every `我的理解` or `我實際用過` section is first-person-labelled learning evidence whose authorship and confirmation metadata is unavailable unless explicitly stated otherwise.

### Training cluster

| Concept / canonical file | Supported extraction | Sources | Recorded state / learning evidence | Supported relationships | Unresolved or incomplete | Website tier |
|---|---|---|---|---|---|---|
| Neural Network — `Neural Network.md` | Parameterized `fθ`; neurons, layers, representations, architecture/function space, training loop, MNIST and myna examples. | AI Programming; TAICA W2/W4; AI Methods index. | 🟨; extensive `我的理解`; `我實際用過` empty. | prerequisites Weight/Bias, Activation, Hidden Layer; connects Training, Loss, Gradient, Backprop, Softmax, Transformer, Self-Attention. | CNN/RNN/Transformer internals, universal approximation, stopping/overfitting. | Tier 2 |
| Neural Network Training — `Neural Network Training.md` | Data → forward → loss → backprop gradients → optimizer update; batch/epoch; validation/test; Keras mappings and three examples. | AI Programming; TAICA W2/W4; AI Methods index only. | 🟨; first-person definition and recorded Keras use. | prerequisites Neural Network, Weight/Bias, Loss; contains Forward, Loss, Gradient, Backprop, Optimizer, Learning Rate, Epoch/Batch; application to Embedding/Transformer parameters; theory ↔ practice. | Full multilayer backprop, optimizer differences, stopping, batch/epoch interaction. | Tier 1 |
| Weight and Bias — `Weight and Bias.md` | Learnable parameters `θ`; weighted sum plus bias; parameter updates; MNIST Dense-layer use. | AI Programming; TAICA W2; AI Methods metadata. | 🟨; definition plus recorded classroom use. | prerequisite/component of Neural Network; updated by Optimizer after gradients; followed by Activation. | Interpretability of individual deep-network parameters. | Tier 3 |
| Loss Function — `Loss Function.md` | Scalar mismatch between prediction and target; differentiable training objective; loss-versus-metric distinction; MNIST example. | AI Programming; TAICA W2/W3; AI Methods metadata. | 🟨; first-person definition and Keras compile use. | Gradient describes change; Training minimizes; Cross Entropy specialization/application. | Task-based loss selection; loss/metric combinations. | Tier 2 |
| Cross Entropy — `Cross Entropy.md` | Cost of model distribution Q relative to target P; low correct-target probability gives larger loss; myna, mushroom, MNIST, next-token uses. | AI Programming MLP note; TAICA W3/W4. | 🟨; first-person definition and implementation use. | prerequisites Distribution, Information, Entropy, Softmax; part of Training; application Classification/Language Model; theory ↔ practice; MSE contrast unresolved. | Full derivation and MSE-versus-CE conditions. | Tier 1 |
| Gradient — `Gradient.md` | Vector of partial derivatives; direction and rate of loss change; `θ ← θ - η∇L`; numeric example. | AI Programming; TAICA W2; AI Methods metadata. | 🟨; first-person definition and SGD use. | Backprop computes it; Optimizer uses it; Learning Rate scales update. | High-dimensional geometry, saddle points, oscillation, parameter scales. | Tier 3 |
| Backpropagation — `Backpropagation.md` | Chain-rule reverse computation; reuses intermediates; computes gradients but does not update parameters; MNIST example. | AI Programming; TAICA W2/W4; AI Methods metadata. | 🟧; first-person distinction and framework use. | part of Training; depends on Loss/Gradient/Activation derivative; contrast with Optimizer/Gradient Descent. | Hand calculation for multilayer networks; vanishing/exploding gradients. | Tier 2 |
| Optimizer — `Optimizer.md` | Receives gradients and updates weights/biases; basic update equation; Keras compile use. | AI Programming MLP note. | 🟨; first-person definition and implementation use. | follows Backprop; uses Gradient and Learning Rate; part of Training. | SGD/Momentum/Adam mechanisms and choice. | Tier 3 |
| Learning Rate — `Learning Rate.md` | Hyperparameter controlling update size; too large/too small effects; numeric update example. | AI Programming MLP note. | 🟨; first-person definition and numeric use. | modifies Optimizer/Gradient update; affects Training stability and convergence. | Selection by surface, batch size, and optimizer. | Deferred; nested under Optimizer |
| Epoch and Batch — `Epoch and Batch.md` | Batch is one update group; one pass over all training samples is an epoch; validation after epoch without update. | AI Programming MLP note. | 🟨; definition present; practical-use field empty. | part of Training; connected to TensorBoard and Overfitting. | Effects on convergence, generalization, and compute. | Tier 3 |
| Activation Function — `Activation Function.md` | Adds nonlinearity after weighted sum; hidden/output role; ReLU, sigmoid, Softmax examples; MNIST use. | AI Programming; TAICA W2; AI Methods metadata. | 🟨; first-person explanation and recorded MNIST use. | prerequisite/component of Neural Network; Softmax specialization; contrast task outputs. | No current specific question; later empirical comparison planned. | Tier 2 |
| Softmax — `Softmax.md` | Scores → sum-to-one relative distribution; competition; argmax versus Sampling; classification and next-token applications; recorded distribution example. | AI Programming; TAICA W2/W3/W4. | 🟨; first-person explanation and myna/MNIST use. | prerequisites Activation/Classification; applications Classification/Language Model; connects Distribution/Sampling; sigmoid contrast; theory ↔ practice. | Further multi-class practice expected; no formal mastery history. | Tier 1 |
| Sigmoid — no canonical file | Supported only as an output-activation contrast in Activation Function, Softmax, Classification, and AI Programming notes. | AI Programming; TAICA W2 mentions sigmoid generally. | No canonical mastery or first-person record. | contrast with Softmax; binary/multi-label output use recorded in other canonical files. | Canonical identity, sources, mastery, relationships, and independent content are absent. | Contrast term only; not a node |
| Classification — `Classification.md` | Discrete-label prediction; binary, mutually exclusive multi-class, and multi-label output patterns; mushroom example. | AI Programming notes. | 🟨; first-person definition; practical-use field empty. | Softmax application; sigmoid contrast; Sampling/generation contrast; relates Data/Dataset/ML. | Later binary/multi-class implementation validation planned. | Tier 3 |
| Forward Propagation — `Forward Propagation.md` | Input through parameters and activations to prediction; single-neuron equations; Keras fit/predict use. | AI Programming MLP note. | 🟨; first-person definition and framework use. | first half of Training; precedes Loss; supplies intermediates to Backprop. | Tensor-shape changes in complex architectures. | Deferred; mechanism label inside Tier 1 Training |

### Generative and language cluster

| Concept / canonical file | Supported extraction | Sources | Recorded state / learning evidence | Supported relationships | Unresolved or incomplete | Website tier |
|---|---|---|---|---|---|---|
| Distribution — `Distribution.md` | Relative possibilities; Softmax conversion; argmax versus Sampling; classification, generation, entropy, CE/KL uses. | TAICA W3; AI Methods course is listed, but the canonical source section is malformed. | 🟨; first-person explanation; course links appear under `我實際用過`, so use evidence cautiously. | connects Softmax, Sampling, Language Model, Entropy, Cross Entropy, KL Divergence, Generative AI. | Continuous/discrete definition and calibration are misplaced under `課程來源`; provenance structure incomplete. | Tier 2 with visible provenance warning |
| Sampling — `Sampling.md` | Draws from a probability distribution; preserves variety; argmax contrast; coffee/tea/milk example. | TAICA W3/W4. | 🟨; explanation present; practical-use field empty. | prerequisites Distribution/Softmax; application Language Model/Generative AI; Sampling Strategies downstream. | Choosing sampling parameters by task. | Tier 3 |
| Language Model — `Language Model.md` | Previous tokens → scores → Softmax → distribution → Sampling → append/repeat; next-token generation example. | TAICA W3/W4. | 🟨; detailed first-person mechanism; practical-use field empty. | prerequisites Neural Network, Softmax, Distribution, Sampling, Tokenization, Embedding; connects Transformer, Cross Entropy, LLM. | Masked attention and how next-token objective yields broader capability. | Tier 2 |
| Tokenization — `Tokenization.md` | Text → tokens → token IDs → embeddings; token may be subword or symbol. | TAICA W4. | 🟧; first-person definition; practical-use field empty. | prerequisite for Embedding/Language Model; linked to vocabulary and sequence length. | BPE, WordPiece, SentencePiece. | Tier 3 |
| Embedding — `Embedding.md` | Learnable dense token vector; lookup layer; updated through loss/backprop; initial versus contextual representation. | TAICA W4. | 🟨; first-person definition; practical-use field empty. | prerequisites Tokenization/Weight-Bias/Backprop; connects Word2Vec, Transformer, Self-Attention. | Dimension interpretability; static versus contextual embeddings. | Tier 2 |
| Query, Key, and Value — `Query, Key, and Value.md` | Learned projections with distinct search, match, and information roles; Q compared with all visible K; classroom hand calculation. | TAICA W4. | 🟨; first-person explanation and recorded simplified hand calculation. | prerequisite/component of Self-Attention; QKᵀ → Softmax weights → weighted V; trained with Transformer. | Division of labor among attention heads. | Tier 3 |
| Self-Attention — `Self-Attention.md` | Context-dependent integration using `softmax(QKᵀ/√dK)V`; two-token worked example. | TAICA W4. | 🟨; first-person mechanism and hand calculation. | prerequisites Embedding/QKV/Softmax; part of Transformer; turns initial into contextual representation. | Scaling, masking, multi-head mathematics. | Tier 2 |
| Transformer — `Transformer.md` | Tokenization/embedding/position → attention → FFN/residual/normalization → stacked contextual representations; RNN contrast. | TAICA W4. | 🟨; first-person explanation; practical-use field empty. | prerequisites Tokenization/Embedding/Self-Attention/Neural Network; uses QKV; foundation for LLM. | Positional encoding, multi-head/FFN/residual/norm; architecture variants. | Tier 2 |
| Large Language Model — `Large Language Model.md` | Large-data/large-parameter Language Model; next-token task; Transformer generation; text-task applications. | TAICA W4. | 🟨; first-person explanation and recorded use for course concept Q&A. | prerequisites Language Model/Transformer/Tokenization/Embedding; connects Sampling, Prompt Engineering, Hallucination. | Scaling capabilities; pretraining, fine-tuning, alignment. | Tier 2 |
| Prompt Engineering — `Prompt Engineering.md` | Goal + data + constraints + format + examples as context; recorded course-note organization use. | TAICA W4. | 🟨; first-person definition and real usage. | application of LLM/Language Model context; affects Transformer next-token distribution; mitigates but does not eliminate Hallucination. | Systematic prompt evaluation; RAG/agents not developed. | Deferred from Week 9 explorer |
| Hallucination — `Hallucination.md` | Fluent but unsupported/false generation; probability is not fact verification; documented source-checking practice. | TAICA W4. | 🟨; first-person definition and recorded verification behavior. | risk of Language Model/LLM/Sampling; Prompt Engineering mitigation is limited. | Which hallucination types RAG, tools, and verifiers reduce. | Deferred from Week 9 explorer |

### Extraction procedure for future implementation

For each Tier 1 or Tier 2 concept:

1. Copy the one-sentence definition only from its canonical `我的理解` and `它解決什麼問題？` sections.
2. Extract prerequisites and downstream endpoints from explicit wiki-links and causal prose.
3. Treat relationship labels formalized from prose as presentation-layer labels and expose their evidence note.
4. Record official course names and exact note paths; distinguish index-only provenance from substantive note content.
5. Copy `learning_status` as a recorded state only.
6. Preserve first-person-labelled wording and attach the authorship/confirmation limitation.
7. Put `我還不理解` items into Open questions without answering them.
8. Reject generic model knowledge, unlinked equivalences, and new mastery claims.

---

## M. Files to modify during future implementation

No files in this list are modified by this specification phase.

### Edit

```text
week09-prototype/index.html
week09-prototype/concepts.html
week09-prototype/concepts/neural-network-training.html
week09-prototype/concepts/softmax.html
week09-prototype/concepts/cross-entropy.html
week09-prototype/assets/css/style.css
```

### Create

```text
week09-prototype/assets/js/explorer.js
```

The JavaScript reads semantic concept data already rendered in `concepts.html`; it must not become the only copy of substantive knowledge. Do not create a second canonical data store.

### Preserve without editing unless separately authorized

```text
week09-prototype/content/concepts/index.md
week09-prototype/content/concepts/neural-network-training.md
week09-prototype/content/concepts/softmax.md
week09-prototype/content/concepts/cross-entropy.md
week09-prototype/AGENTS.md
```

### Parent vault

Every parent canonical file and course note remains read-only. Future implementation copies only reviewed presentation excerpts and source paths into the prototype.

### Delete

None. Existing routes, links, ids, and semantic headings must be recorded with Hallmark `--before` and checked with `--kept` during implementation.

---

## N. Risks and evidence limitations

1. **Mastery is recorded, not verified.** No formal confirmation date or independent validation record is stored.
2. **First-person authorship is uncertain.** `我的理解` and `我實際用過` are labelled as first-person evidence, but authorship/approval metadata is unavailable.
3. **Cross-course breadth is concentrated.** The strongest substantive overlap is mainly between 人工智慧程式設計 and TAICA 生成式 AI. AI Methods is often only an index reference for neural-network concepts.
4. **The language-model chain is mainly single-course.** Do not describe Tokenization → LLM as cross-course integration.
5. **Distribution provenance is malformed.** Its course links and unresolved questions appear under the wrong headings; the prototype must not silently normalize this into stronger provenance.
6. **Sigmoid is not canonical.** It is a supported contrast term but has no root-level concept file, mastery, or independent source ledger.
7. **Some edges are presentation-level formalizations.** A causal sentence can support a labelled edge, but no separately confirmed graph-edge record exists for many relationships.
8. **Mathematics remains unresolved.** Cross Entropy/KL derivation, MSE comparison, self-attention scaling/masking, and several training details must remain open questions.
9. **Search can overstate completeness.** Results cover only the selected prototype cluster, not the whole parent vault; label the scope visibly.
10. **Source filtering can become course navigation.** Filters must highlight contributions while keeping concepts as the register's primary units.
11. **Progressive enhancement can fail silently.** Core content, selection anchors, evidence, and normal links must remain usable when JavaScript is unavailable.
12. **Mixed Chinese/English strings can wrap unpredictably.** Test official course names, relationship phrases, and long concept names at all target widths and 200% zoom.

---

## O. Definition of Done for the future redesign

### Knowledge and provenance

- Every substantive statement maps to a canonical file or named course/source note in the extraction matrix.
- No generic model knowledge, invented source, invented relationship, invented first-person statement, or new mastery claim is present.
- One concept has one canonical identity across Explorer and full pages.
- Official course names remain visible as provenance, never primary knowledge categories.
- Index-only provenance is labelled as such.
- Recorded mastery always includes `recorded` language and the independent-verification caveat.
- First-person-labelled evidence preserves the missing authorship/confirmation limitation.
- Open questions remain unresolved; Cross Entropy does not present an unrecorded derivation.
- Sigmoid is not rendered as a canonical node unless the parent system later gains an authorized canonical file.

### Explorer experience

- A visitor can enter, select a concept, see definition/state/sources, identify prerequisites and downstream concepts, and continue to another concept.
- Search covers names, definitions, sources, and relationship terms.
- Only cluster, source, and full-experience filters ship.
- Selected concept and filters are reflected in the URL with JavaScript.
- Without JavaScript, the complete register, default concept sheet, anchors, evidence, and links remain usable.
- No graph drag, zoom, physics, hidden off-canvas nodes, or dashboard metrics are introduced.
- Empty search results explain the state and provide a clear reset.

### Navigation

- Home, Knowledge Explorer, System rules, and all three full concept pages are mutually reachable.
- Every Tier 1 page has `Back to Explorer` near the top and `Explore next` before the footer.
- Browser Back and keyboard focus behave predictably after concept selection.
- Existing routes, hrefs, ids, and headings are either preserved or explicitly recorded in the Hallmark kept/dropped ledger.

### Responsive and accessibility

- No horizontal page scroll from 320 to 1920 CSS pixels.
- Explorer changes to the explicit mobile list → selected sheet pattern under 60rem.
- Relationship paths stack vertically on mobile; long names do not create slivers or overflow.
- All controls have 44px touch targets and instant visible `:focus-visible` states.
- Interaction does not depend on hover or colour alone.
- Diagrams have adjacent text/list equivalents.
- The site works at 200% zoom and with reduced motion.
- Mixed Chinese/English labels are tested at 320, 375, 414, 768, 1024, 1280, 1440, and 1920.

### Hallmark floor and craft

- The first non-empty CSS line contains the completed Hallmark redesign stamp and critique; valid Reflex waivers/Finish answers follow it.
- `html` and `body` both use `overflow-x: clip`; no `100vw` or `transition: all` exists.
- All colours, fonts, spacing, control sizes, and motion values use tokens.
- The content container is capped and centred; gutters grow at 1920px.
- No visible mastery emoji is used as a UI icon.
- Link labels contain no glued arrow characters.
- `TAICA` is presented as an official name at readable body size with normal tracking.
- Thick left borders are not the default component motif; the merge junction appears only where sources truly converge.
- Page-scope hero/masthead essentials fit at 1280×800 and long pages respect the one-idea-per-screen discipline.
- Explorer is swept as `--scope app`; homepage and concept pages are swept in page scope.
- Final Hallmark render covers all five routes and all required widths with `0 FAIL`; every Reflex is fixed or has a specific valid waiver, every warning is confirmed/dismissed, and every Finish item is answered.

### Verification and handoff

- Run Hallmark `--before` on the current site before implementation and `--kept` after implementation.
- Compare before/after screenshots and state what the old design did better.
- Verify all internal links and hash targets.
- Verify search/filter keyboard operation and JavaScript-disabled behavior.
- Confirm the git diff contains only the authorized prototype files.
- The parent AI Knowledge System remains unchanged.

---

## Future implementation order

1. Record Hallmark before-state and link/heading inventory.
2. Lock the existing visual identity as the redesign system; do not deal a replacement theme.
3. Refactor foundation tokens and Floor fixes.
4. Build the Knowledge Explorer semantic no-JavaScript state.
5. Add progressive-enhancement search, filters, selection, and URL state.
6. Shorten the homepage and move exploration into the Explorer.
7. Recompose the three Tier 1 pages around their distinct mechanism figures.
8. Add Explore next and evidence disclosure patterns.
9. Run content parity, link, accessibility, responsive, Hallmark, and kept-wiring checks.

Implementation stops if any proposed copy cannot be traced to the extraction matrix or its named source.
