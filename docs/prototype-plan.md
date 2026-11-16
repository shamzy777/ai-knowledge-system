# Week 9 Prototype Plan

## Prototype goal

Create a presentation prototype that demonstrates how an AI Knowledge System can integrate knowledge by concept across multiple courses. The prototype should make course provenance visible without using courses as the primary navigation structure.

This directory is separate from the permanent AI Knowledge System. No permanent knowledge should be copied, rewritten, or reclassified until the user explicitly approves the relevant content work.

## Demo narrative 1: cross-course integration

The main narrative is that multiple courses can contribute different perspectives to one canonical concept.

### Planned full concept pages

1. **Neural Network Training**
   - AI Programming contribution: Keras `compile`, `fit`, `predict`, and `evaluate`; batches and epochs; validation and test data; implementation workflow.
   - TAICA contribution: prediction → loss → gradient → parameter update; conceptual training mechanism.
   - Intended relationship: theory ↔ practice.

2. **Softmax**
   - AI Programming contribution: classification output activation, mutually exclusive classes, contrast with sigmoid, and classification examples.
   - TAICA contribution: probability distribution, argmax versus sampling, next-token probability, and probabilistic generation.
   - Intended message: one canonical concept, different course applications.

3. **Cross Entropy**
   - AI Programming contribution: classification loss, binary/categorical use, and implementation examples.
   - TAICA contribution: entropy/distribution framing and language-model next-token training.
   - Intended message: implementation and mathematical/generative framing integrated into one concept.

These descriptions define the future presentation structure only. They are not permanent concept content and must not be converted into full pages without source review and user confirmation.

## Demo narrative 2: connected technical model

The supporting technical chain is:

```text
Tokenization
→ Embedding
→ Self-Attention
→ Transformer
→ Large Language Model
```

This demonstrates prerequisite and part-of relationships within a connected technical mental model. It should not be presented as cross-course because its current provenance is mainly TAICA.

## Supporting graph nodes

- Neural Network
- Backpropagation
- Tokenization
- Embedding
- Self-Attention
- Transformer
- Large Language Model

Supporting nodes do not require full Week 9 concept pages. Their graph labels and relationships must remain grounded in the existing knowledge system.

## Planned page architecture

### Home

The future home view should contain:

- project title;
- a concise project philosophy;
- “Courses are knowledge sources, not the final knowledge structure.”;
- the flow `Source → Learning → Understanding Check → Knowledge Intake → Permanent Knowledge`;
- a cross-course knowledge map;
- the Tokenization-to-LLM technical chain.

### Concept Index

The future index should be concept-oriented. It may group concepts by domain, function, learning path, or precise relationship, but it must not use course identity as the primary structure.

### Concept Page

Every future full concept page should use a consistent schema:

1. One-sentence Definition
2. Why It Matters
3. Prerequisites
4. Core Idea
5. Concept Relationships
6. Mastery Level
7. Sources

Optional sections may show different source perspectives, applications/examples, and confirmed personal learning evidence.

## Next implementation phase

After explicit user approval, the next phase may:

- choose the presentation stack;
- build the Home, Concept Index, and shared Concept Page layout;
- implement the cross-course knowledge map;
- implement the technical-chain visualization;
- prepare the three planned concept pages from reviewed source material;
- verify that provenance, mastery caveats, and relationship types are visible.

The next phase must not silently promote staging material into permanent knowledge. Any new mastery level, relationship, or first-person explanation requires user confirmation.

## Evidence limitations

- The strongest cross-course evidence currently comes mainly from two courses.
- The image-generation course currently has no usable integrated content.
- Recorded mastery does not include formal confirmation history.
- Existing `我的理解` text has no authorship metadata.
- Some concept provenance metadata remains incomplete.
- The Tokenization → Large Language Model technical chain is mostly single-course.

These limitations are part of the prototype's honest evidence model and must remain visible in future design decisions.

## Current phase completion boundary

This phase ends with the directory structure and specification files only. `content/concepts/`, `site/`, and `assets/` remain empty. No website, concept HTML page, or copied permanent knowledge is included.
