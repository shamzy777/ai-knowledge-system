---
type: teaching-path-proposal
teaching_path_id: TEACH-PATH-001
title: "LLM 是怎麼從文字產生下一個 token 的？ / How Does an LLM Generate the Next Token?"
status: approved-for-html-implementation
knowledge_source: "published Week 10 Wiki only"
wiki_publication: PUB-RUN-001
planned_section_count: 11
html_authorized: true
mastery_changed: false
---

# TEACH-PATH-001 — Next-Token Generation

This is a bounded teaching-path proposal, not the final HTML presentation. Every factual teaching claim must be recoverable from a published Week 10 Wiki concept page. Source labels below are inherited from those pages; no external or model knowledge is added.

## 1. Learning objective

After completing the presentation, a beginner should be able to explain, in causal order, how:

1. input text is converted into tokens;
2. tokens become vector representations;
3. Self-Attention uses Q/K/V to build context-dependent representations;
4. a Transformer processes those representations for language modeling;
5. a Language Model / Large Language Model produces scores for possible next tokens;
6. Softmax turns the scores into a probability distribution;
7. Sampling selects one token, appends it to the context, and allows the process to repeat.

The learner should also be able to explain why “highest probability” and “sampled next token” are not always the same choice, and why fluent generation alone does not guarantee grounded correctness.

## 2. Prerequisite check

### Minimum before starting

| Concept | Required understanding | Wiki page | Handling |
|---|---|---|---|
| Neural Network（神經網路） | A trained network is a parameterized function that transforms numeric inputs into outputs. | [Neural Network](../../wiki/concepts/neural-network.md) | One-sentence check only; do not reteach training. |
| Distribution（機率分布） | A probability distribution assigns probabilities across possible outcomes. | [Distribution](../../wiki/concepts/distribution.md) | Brief visual check before Softmax. |

### Introduced just in time inside the path

| Supporting concept | Why it is needed | First section |
|---|---|---|
| Positional Encoding（位置編碼） | Token vectors need sequence-position information in an attention-only model. | T03 |
| Query, Key, and Value（查詢、鍵、值） | Makes the Self-Attention mechanism explainable without treating it as a black box. | T05 |
| Multi-Head Attention（多頭注意力） | Connects one attention operation to the Transformer block. | T07 |
| Inference（推論） | Separates model use and repeated decoding from parameter-updating training. | T08 |

### Explicitly not required in this bounded path

- Cross Entropy, Backpropagation, Optimizer, and Pretraining details: important to how a model learns, but not required to explain one inference-time next-token step.
- Byte-Pair Encoding implementation details: Tokenization is required; the specific tokenizer algorithm is optional.
- Temperature, top-k, and top-p details: valid Sampling Strategies, but outside the minimum causal explanation. They may be named only as a future extension.

## 3. Wiki evidence map

The section IDs below are the future presentation sections. “Allowed claims” are the maximum factual scope for drafting; a later HTML draft must not silently expand them.

| Section | Canonical Wiki page(s) | Carried provenance | Claims allowed to teach |
|---|---|---|---|
| T01 — The complete one-token loop | [Language Model](../../wiki/concepts/language-model.md); [Large Language Model](../../wiki/concepts/large-language-model.md); [Inference](../../wiki/concepts/inference.md); [Sampling](../../wiki/concepts/sampling.md) | S03/S04 Course Material; S09 Reliable Educational Reference | A causal language model uses preceding context to produce a next-token distribution, selects a token during inference, appends it, and can repeat. An LLM is a scaled language-model framing with a broader lifecycle. |
| T02 — Text becomes tokens | [Tokenization](../../wiki/concepts/tokenization.md) | S09 Reliable Educational Reference | Tokenization deterministically segments text into tokens; the chosen token inventory affects sequence length, vocabulary identity, and what the model predicts. `詞元化` is the canonical Chinese term in this Wiki. |
| T03 — Tokens become vectors with position | [Embedding](../../wiki/concepts/embedding.md); [Positional Encoding](../../wiki/concepts/positional-encoding.md) | S04 Course Material; S08 Research Paper; S09 Reliable Educational Reference | Embeddings are learned dense vectors. Position information is combined with token representations so an attention-based model can distinguish order. Original sinusoidal and later learned/relative variants remain distinct scopes. |
| T04 — Why context must change the representation | [Embedding](../../wiki/concepts/embedding.md); [Self-Attention](../../wiki/concepts/self-attention.md) | S04 Course Material; S08 Research Paper; S09 Reliable Educational Reference | A token starts with a learned representation, then Self-Attention lets each position form a context-dependent representation using relationships with other positions. Do not call the vector literal human understanding. |
| T05 — Q, K, and V roles | [Query, Key, and Value](../../wiki/concepts/query-key-and-value.md) | S04 Course Material; S08 Research Paper; S09 Reliable Educational Reference | Q/K/V are learned projections. Queries compare with keys; normalized comparison weights determine how values are combined. The comparison representation and carried information have distinct roles. |
| T06 — One Self-Attention operation | [Self-Attention](../../wiki/concepts/self-attention.md); [Softmax](../../wiki/concepts/softmax.md) | S02–S06 Course Material; S08 Research Paper; S09 Reliable Educational Reference | Self-Attention computes query-key scores, scales and normalizes them with Softmax, then uses the weights to combine values. The result is a context-dependent representation. |
| T07 — From attention to a Transformer | [Multi-Head Attention](../../wiki/concepts/multi-head-attention.md); [Transformer](../../wiki/concepts/transformer.md); [Positional Encoding](../../wiki/concepts/positional-encoding.md) | S04 Course Material; S08 Research Paper; S09 Reliable Educational Reference | Multiple learned Q/K/V heads run in parallel, are concatenated and projected. A Transformer also includes position-wise feed-forward layers, residual connections, normalization, and position information. S08's original encoder–decoder and S09's causal decoder are scope/evolution differences. |
| T08 — Transformer as a language model / LLM | [Transformer](../../wiki/concepts/transformer.md); [Language Model](../../wiki/concepts/language-model.md); [Large Language Model](../../wiki/concepts/large-language-model.md); [Inference](../../wiki/concepts/inference.md) | S04 Course Material; S08 Research Paper; S09 Reliable Educational Reference | A Transformer can represent the preceding context for next-token prediction. A Language Model scores possible next tokens; an LLM extends the language-model framing at scale. During inference, the trained parameters are used without being updated. |
| T09 — Scores become probabilities | [Softmax](../../wiki/concepts/softmax.md); [Distribution](../../wiki/concepts/distribution.md); [Language Model](../../wiki/concepts/language-model.md) | S02–S06 Course Material; S08 Research Paper; S09 Reliable Educational Reference | Softmax converts scores into non-negative relative values that sum to one. In the language-model output route this becomes a next-token distribution. Do not teach “winner takes all” as the technical definition. |
| T10 — Sampling chooses the next token | [Sampling](../../wiki/concepts/sampling.md); [Softmax](../../wiki/concepts/softmax.md); [Inference](../../wiki/concepts/inference.md) | S03/S04 Course Material; S09 Reliable Educational Reference | Sampling selects according to a probability distribution rather than always taking the highest-probability token. S04's `[0.70, 0.29, 0.01]` example may be used; lower-probability outcomes remain possible. |
| T11 — Append, repeat, and know the boundary | [Language Model](../../wiki/concepts/language-model.md); [Inference](../../wiki/concepts/inference.md); [Sampling](../../wiki/concepts/sampling.md); [Hallucination](../../wiki/concepts/hallucination.md) | S03/S04 Course Material; S09 Reliable Educational Reference | The selected token becomes part of the context and generation repeats. Fluency is not factual verification. Use S09's narrower ungrounded/incorrect-output definition of Hallucination and retain S04 only as an attributed Course Perspective. |

## 4. Teaching narrative — 11 sections/slides

### T01 — Start with the whole causal loop

Open with one question: “Given the text so far, how does one more token appear?” Show the entire pipeline once, without explaining every box. The learner receives a mental map before details: text → tokens → vectors/position → Transformer/context → next-token scores → Softmax distribution → Sampling → append and repeat.

**Teaching move:** promise that every following section explains one arrow in this loop.

### T02 — Text is not the model's input unit

Use a short bilingual string split into token tiles, but do not claim a particular segmentation unless it comes from an actual tokenizer. Emphasize that Tokenization defines the sequence of units the model will represent and later predict.

**Causal link:** no tokens → no embedding lookup and no defined next-token candidate vocabulary.

### T03 — A token ID needs a vector and a position

Transform token tiles into vector tiles. Add a separate position band to show that identity and order information are different ingredients. Mention original sinusoidal versus later learned/relative approaches only as variants; no formula is required.

**Causal link:** token identity plus position becomes the input representation processed by the Transformer.

### T04 — Context is the problem attention solves

Show the same token appearing in two short contexts. Keep its initial token identity visually stable, then show the contextual representation as the part that can differ after attention. Avoid anthropomorphic language such as “the model understands the sentence.”

**Causal link:** next-token prediction needs a representation informed by preceding context, not isolated token identity alone.

### T05 — Q, K, and V divide the attention job

Introduce one focus position. Its Query asks what information is relevant; Keys are compared with the Query; Values carry the information to be combined. Present these as learned projections, not three separate stored word meanings.

**Causal link:** Q/K comparisons determine weights; the weights determine how V information is combined.

### T06 — Self-Attention builds one contextual representation

Animate the path `Q·K scores → scale → Softmax weights → weighted combination of V`. Keep the attention Softmax visually distinct from the final vocabulary Softmax: they use the same normalization concept in different locations.

**Causal link:** the weighted value mixture becomes a context-dependent representation for the focus position.

### T07 — The Transformer is more than one attention arrow

Zoom out from one head to Multi-Head Attention, then to a simplified causal Transformer block. Show only evidence-backed components: multi-head attention, feed-forward layers, residual connections, normalization, position information, and causal masking where the S09 perspective is being taught.

**Causal link:** stacked Transformer processing produces a context representation that can support language-model prediction.

### T08 — Language Model, LLM, and inference

Clarify the terms instead of adding a new mechanism: the Language Model is the next-token probability task; an LLM is the scaled modern model/lifecycle framing; inference is the use phase where trained parameters produce outputs without being updated.

**Causal link:** the processed context is used to score possible next tokens.

### T09 — Softmax turns scores into a distribution

Show three unnamed candidate tokens with raw score bars, then normalized probability bars summing to one. Do not imply Softmax itself chooses a token. Briefly point back to attention: Softmax also normalized attention scores earlier, but this Softmax is over next-token candidates.

**Causal link:** scores are not yet a selected output; they become a distribution from which a choice can be made.

### T10 — Sampling makes one choice

Use the Wiki-supported `[0.70, 0.29, 0.01]` example. Run repeated illustrative draws to show that the highest-probability candidate is common but not guaranteed. Contrast sampling with always choosing the maximum, without expanding into temperature/top-k/top-p.

**Causal link:** one candidate token is selected and becomes visible output.

### T11 — One token becomes a sequence

Append the selected token to the input row and send the updated context back to the beginning of the loop. End with a learner explanation prompt: “Trace one token from text input to sampled output.” Add one boundary statement: this process explains fluent continuation, not factual verification.

**Transfer link:** if the earlier context changes, the contextual representation, next-token scores, distribution, and sampled outcome may also change.

## 5. Visual explanation plan

### V01 — Full next-token-generation mental model

**Used in:** T01 and again as the recap frame in T11.

```text
Text so far
  → Tokenization
  → Token IDs
  → Embeddings + position information
  → Transformer / Self-Attention context processing
  → next-token scores
  → Softmax distribution
  → Sampling
  → selected token
  → append to context and repeat
```

Design rule: keep the whole pipeline visible in a muted state and highlight only the current section. This preserves causal continuity and prevents eight disconnected definition slides.

### V02 — Q/K/V and Self-Attention

**Used in:** T05–T06.

- One focus token supplies the highlighted Query.
- All visible context positions expose Keys for comparison.
- The same positions expose Values that flow into a weighted combination.
- A separate small strip shows `scores → Softmax weights → weighted V mixture`.
- Do not invent attention numbers or claim a head has a human-readable fixed meaning.

### V03 — Transformer zoom levels

**Used in:** T07.

Three nested frames: one attention operation → multiple heads → simplified Transformer block. Include position information, feed-forward layer, residual path, and normalization. Label “original encoder–decoder scope: S08” and “causal decoder teaching scope: S09” rather than blending them into one historical architecture.

### V04 — Softmax and Sampling

**Used in:** T09–T10.

- Left: raw score bars with no probability claim.
- Middle: Softmax probabilities summing to one.
- Right: one sampling marker selects a candidate.
- Use only S04's explicit `[0.70, 0.29, 0.01]` teaching example for numeric probabilities.

## 6. Interaction plan

Only three interactions are proposed; the presentation must remain understandable without them.

| Interaction | Learning value | Behavior | Non-interactive fallback |
|---|---|---|---|
| Pipeline spotlight | Reinforces ordering and preserves the full mental model while focusing attention. | Previous/next controls highlight one pipeline stage and its input/output. | All stages remain visible with the active stage emphasized in the static slide sequence. |
| Q/K/V focus selector | Tests whether the learner can distinguish comparison roles from information flow. | Select a focus position; highlight its Query, compared Keys, and incoming Values without fabricated numeric weights. | A fixed annotated diagram shows the same routes. |
| Re-sample the same distribution | Demonstrates that sampling is probabilistic and the maximum is not guaranteed. | Repeatedly draw from `[0.70, 0.29, 0.01]` and tally outcomes; label results illustrative, not model output. | Show a short precomputed sequence containing both high- and lower-probability outcomes. |

No decorative carousel, hover-only definition, free-form chatbot, or temperature control is proposed. Those interactions would add navigation novelty or scope rather than necessary learning value.

## 7. Quiz plan

Each answer must cite the listed Wiki page(s) in the future artifact.

| ID | Skill tested | Question | Expected answer / rationale | Wiki support |
|---|---|---|---|---|
| Q1 | Concept ordering | Put these stages in order: Sampling, Embedding, Tokenization, Softmax, Self-Attention. | Tokenization → Embedding → Self-Attention → Softmax → Sampling. Transformer/LM processing surrounds the middle-to-output route, but among the supplied items this is the supported causal order. | Tokenization; Embedding; Self-Attention; Softmax; Sampling |
| Q2 | Mechanism understanding | In Self-Attention, which roles determine comparison weights, and which role carries the information being combined? | Query is compared with Keys; the resulting normalized weights combine Values. | Query, Key, and Value; Self-Attention |
| Q3 | Mechanism distinction | Does Softmax select the next token? | No. Softmax turns scores into a distribution; Sampling or another decoding choice selects a token. | Softmax; Sampling |
| Q4 | Probability reasoning | Given `[0.70, 0.29, 0.01]`, can the third candidate be sampled? | Yes. It is unlikely but remains possible unless the candidate set is restricted. | Sampling |
| Q5 | Transfer | If an earlier context token changes, which later stages may change before the next token is selected? | Context-dependent attention representations may change, so next-token scores, Softmax probabilities, and the sampled result may change. | Self-Attention; Language Model; Softmax; Sampling |
| Q6 | Mental-model transfer | Explain why a fluent next-token continuation is not automatically a verified fact. | The mechanism generates from a learned next-token distribution; the Wiki's Hallucination concept distinguishes fluent output from grounded correctness. | Language Model; Hallucination; LLM Evaluation |

Quiz scoring is formative only. It must not change or infer any Wiki mastery status.

## 8. Provenance plan

### Visible on every teaching section

- A compact `Wiki concepts` footer linking to the canonical concept pages used by that section.
- Source-type badges inherited from the Wiki: `Course Material`, `Research Paper`, and `Reliable Educational Reference`.
- A short source-ID/locator line copied from the relevant Wiki evidence, such as `S08 pp. 3–6` or `S09 book pp. 196–201`; never invent a locator.

### Available on demand

- An evidence drawer mapping each visible claim to a Wiki page section and its principal sources.
- A scope note when the Wiki preserves perspectives, especially original versus causal Transformer and the Hallucination Course Perspective.

### Boundaries

- The teaching artifact cites the published Wiki as its knowledge layer and exposes the Wiki's inherited source provenance.
- No new direct-source interpretation, external URL, model-knowledge supplement, or first-person understanding claim may be introduced during HTML drafting.
- Chapter/navigation pages may guide ordering but do not count as evidence for factual claims.

## 9. Teaching validation criteria

| Gate | Pass condition | Failure signal |
|---|---|---|
| Wiki-only factual grounding | Every factual sentence maps to at least one published `wiki/concepts/*.md` page; all linked evidence paths resolve inside the Week 10 project. | External/model claim, missing Wiki page, or claim broader than the page's allowed scope. |
| Concept coverage | All eight primary concepts appear in causal order: Tokenization, Embedding, Self-Attention, Transformer, Language Model, Large Language Model, Softmax, Sampling. | Missing primary concept or concept used only as an unexplained label. |
| Prerequisite order | Distribution is checked before output Softmax/Sampling; Q/K/V appears before Self-Attention mechanism; position and embeddings appear before Transformer; inference framing appears before repeated decoding. | A mechanism depends on a concept not yet checked or introduced. |
| Citation mapping | Every section has canonical Wiki links, inherited source types, source IDs, and only locators already present in the Wiki. | Orphan claim, invented locator, or provenance category collapsed into “source.” |
| Quiz-answer support | Every expected answer is entailed by the named Wiki pages and uses no hidden teaching claim. | Correct answer requires external knowledge or an unintroduced concept. |
| Content density | 10–12 sections; each section has one causal job, at most two central factual claims, and no more than about 90 visible prose words before provenance details. | Definition pile-up, more than one mechanism transition, or citation text dominating the learning surface. |
| Beginner comprehensibility | A reader with the prerequisite check can verbally trace the pipeline and distinguish Q/K/V, Softmax, and Sampling without formulas beyond the optional attention expression. | Learner can name terms but cannot explain inputs, transformations, and outputs. |
| Visual integrity | Diagrams preserve direction, distinguish attention Softmax from vocabulary Softmax, and label illustrative values. | Diagram implies Softmax samples, embeddings are human meaning, or attention heads have fixed interpretable roles. |
| Accessibility and fallback | Meaning does not rely only on color; every interaction has text labels, keyboard operation, and a static explanation. | Interaction hides required content or a diagram is unusable without animation/color. |
| Scope and isolation | No HTML is created until approval; Wiki, mastery, permanent system, and source manifests remain unchanged. | Any write outside `teaching/paths/`, workflow validation, or logs during this phase. |

## 10. Graph routing / workflow returns

```text
Wiki publication
  → evidence map
  → teaching outline
  → section draft
  → visual / interaction / quiz draft
  → teaching validation
  → human approval
  → later HTML phase
```

| Failure | Return destination | Required correction | Must not do |
|---|---|---|---|
| Insufficient evidence | Wiki retrieval / evidence mapping | Retrieve another already-published supporting concept or narrow the allowed claim. | Do not browse, ingest a source, or fill the gap with model knowledge. |
| Poor learning sequence | Teaching outline | Reorder sections or move a prerequisite check earlier. | Do not rewrite canonical Wiki pages to fit the outline. |
| Unsupported claim | Corresponding teaching section | Remove, narrow, or remap the claim to published Wiki evidence. | Do not silently attach a loosely related citation. |
| Excessive content density | Section draft | Split, shorten, defer detail, or convert prose into a supported diagram. | Do not return to source retrieval merely to add more information. |
| Visual semantic error | Visual plan for that section | Correct direction, labels, or scope using the mapped concept pages. | Do not preserve a visually appealing but false mental model. |
| Quiz answer not supported | Quiz item | Rewrite or remove the question/answer and remap evidence. | Do not add an unintroduced fact to make the quiz work. |
| Provenance mismatch | Evidence map and section footer plan | Restore exact Wiki source types, IDs, locators, and perspective notes. | Do not blend S08/S09 into Course Material. |

## Approval boundary

`TEACH-PATH-001` stops here. Human approval is required before drafting section copy beyond this bounded plan or creating any HTML, CSS, JavaScript, image, or interactive artifact.

## Approval clarifications

Approved on 2026-11-24 for HTML implementation with these binding clarifications:

1. Token Embedding and Positional Encoding must appear as distinct mechanisms that contribute different information to the Transformer input.
2. The later progression must read `Language Modeling → Large Language Model → Inference`, while retaining the Wiki-supported relationship scopes.
3. Sampling controls token selection from a predicted distribution. The presentation must not state or imply that Sampling causes Hallucination. Fluent or high-probability generation still does not guarantee factual grounding.
