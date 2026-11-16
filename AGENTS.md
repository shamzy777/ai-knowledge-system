# Week 9 AI Knowledge System Prototype

## Scope

This directory contains an isolated presentation prototype for the Week 9 assignment. It is derived from the larger AI Knowledge System in the parent directory, but it is not the permanent knowledge base.

- Work only inside `week09-prototype/` unless the user explicitly authorizes a broader scope.
- Treat the parent AI Knowledge System as read-only source material.
- Do not move, rename, rewrite, or reorganize the permanent knowledge files.
- Do not copy permanent concept content into this prototype without explicit user approval.
- Keep prototype decisions and presentation code separate from permanent knowledge decisions.

## Project purpose

Build one connected AI mental model across multiple courses. The system is concept-oriented, not course-oriented.

> Courses are knowledge sources, not the final knowledge structure.

When multiple courses discuss the same underlying concept, maintain one canonical concept and integrate the distinct perspectives, applications, or explanations into it.

## Understanding-first workflow

This is not an automatic AI summarization system. Knowledge must move through this sequence:

```text
Source Material
→ AI-assisted Learning
→ Understanding Check
→ Knowledge Intake
→ User Confirmation
→ Permanent Knowledge
```

An AI-generated summary is not evidence that the user understands a concept. Only user-confirmed knowledge belongs in the permanent knowledge layer.

## Knowledge layers

### Source Layer

Original materials such as course slides, handwritten notes, papers, articles, and external references.

### Learning / Staging Layer

Material still being learned, discussed, checked, or prepared for integration. This may include:

- AI explanations;
- the user's own explanations;
- understanding checks;
- proposed relationships;
- proposed mastery levels;
- Knowledge Intake records.

### Permanent Knowledge Layer

Canonical concepts that have been understood and confirmed by the user. The prototype website should mainly visualize this layer while preserving provenance and uncertainty.

## Concept rules

Only actual knowledge concepts can be concept nodes.

Valid examples:

- Softmax
- Cross Entropy
- Neural Network Training
- Transformer

Invalid examples:

- TAICA Week 3
- AI Programming Homework 2
- Generative AI Course

Course names, weeks, assignments, and source documents are metadata or source records, not concepts.

### One concept, one canonical node

Before adding a concept:

1. Search for an existing concept with the same or closely related meaning.
2. Determine whether it is the same underlying concept.
3. If it is the same, update the existing canonical concept rather than creating another node.
4. Never encode course identity into a canonical concept filename.
5. If the distinction is unclear, ask the user before creating or merging anything.

Never create course-specific duplicates such as:

```text
ai-programming-softmax.md
taica-softmax.md
```

Use one canonical file such as:

```text
softmax.md
```

Different sources may contribute different perspectives, applications, or explanations to that one concept.

### Creating a new permanent concept

Do not create a permanent node because a term appears once. A term may remain in the learning/staging layer until it has meaningful independent content, supported relationships, and sufficient user-confirmed understanding.

## Required concept-page schema

Every future permanent concept page must contain:

- One-sentence Definition
- Why It Matters
- Prerequisites
- Core Idea
- Concept Relationships
- Mastery Level
- Sources

Optional sections:

- Different Source Perspectives
- Applications / Examples
- My Explanation / Learning Evidence

Presentation-layer concept files may be created inside `content/concepts/` when explicitly authorized by the current implementation phase. This does not authorize changes to permanent canonical concepts.

## Mastery rules

Use these levels:

- 🟥 不理解
- 🟧 聽過但模糊
- 🟨 可以解釋
- 🟩 可以運用
- 🟦 可以和其他概念建立連結

AI may suggest a mastery level but must not permanently change one without user confirmation. If confirmation history is unavailable, display the existing recorded status and state that it has not been independently verified.

## Relationship rules

Supported relationship types:

- prerequisite
- part-of
- cause/effect
- evolution
- application
- contrast
- theory ↔ practice
- cross-domain analogy

Prefer the most precise supported relationship over a vague `related to` edge. AI may propose relationships, but permanent new relationships require user confirmation. Never invent connections to make the graph appear denser.

## Source and provenance rules

Keep these provenance categories distinct:

- Course Material
- External Research
- Model Knowledge
- User Interpretation / Analogy

Course materials have priority for course-derived knowledge. Do not silently blend external research or model knowledge into course content. Do not invent sources, confirmation history, mastery evidence, or first-person understanding statements.

## Prototype narratives

The eventual prototype should demonstrate two complementary ideas.

### Cross-course integration

Plan three full concept pages:

1. Neural Network Training
2. Softmax
3. Cross Entropy

The presentation should show:

- **Neural Network Training:** TAICA's conceptual training mechanism integrated with AI Programming's Keras and validation workflow.
- **Softmax:** one canonical concept used for classification in AI Programming and probabilistic generation in TAICA.
- **Cross Entropy:** implementation-focused classification loss integrated with entropy/distribution framing and next-token training.

These are planned narratives, not authorization to copy or rewrite their permanent content.

### Connected technical model

Plan these supporting graph nodes:

- Neural Network
- Backpropagation
- Tokenization
- Embedding
- Self-Attention
- Transformer
- Large Language Model

Visualize this technical chain:

```text
Tokenization
→ Embedding
→ Self-Attention
→ Transformer
→ Large Language Model
```

Do not describe this chain as cross-course; its current provenance is mainly TAICA.

## Planned website architecture

### Home

Plan for:

- project title and short philosophy;
- the statement “Courses are knowledge sources, not the final knowledge structure.”;
- the understanding-first workflow;
- a cross-course knowledge map;
- the technical knowledge chain.

### Concept Index

Organize concepts by concept-oriented categories and relationships, not primarily by course.

### Concept Page

Use one consistent schema for all full concept pages.

## File conventions

- Use lowercase kebab-case for future content and implementation files.
- Do not include course names in canonical filenames.
- Examples: `softmax.md`, `cross-entropy.md`, `neural-network-training.md`, `large-language-model.md`.
- Keep source metadata separate from concept identity.

## Prototype Content Authorization

- The parent AI Knowledge System remains read-only unless the user explicitly authorizes changes.
- `week09-prototype/content/concepts/` may contain presentation-layer content derived from existing canonical concepts.
- These files are **not permanent canonical knowledge nodes**.
- Prototype content must preserve provenance, uncertainty, mastery limitations, and the one-concept-one-canonical-node principle.
- Do not use the prototype to promote new or unconfirmed knowledge into the permanent knowledge system.
- Creating or modifying prototype content is allowed when explicitly authorized by the current implementation phase.

## Quality and evidence constraints

Preserve these known limitations in future presentation work:

- the strongest cross-course evidence currently comes mainly from two courses;
- the image-generation course has no usable integrated content yet;
- recorded mastery has no formal confirmation history;
- existing `我的理解` text has no authorship metadata;
- some concept provenance metadata is incomplete;
- the Tokenization-to-LLM chain is mostly single-course.

Do not conceal these limitations or convert uncertainty into certainty.
