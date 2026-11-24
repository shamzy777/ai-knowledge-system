---
artifact_id: TEACH-DECK-001-REDESIGN-STORYBOARD
date: 2026-11-24
status: implemented
source_boundary: published Week 10 Wiki only
---

# TEACH-DECK-001 Redesign Storyboard

## Continuous story

The presentation follows one unresolved sentence through one complete causal loop:

`Text → Tokens → Representation + position → Context → Transformer → Prediction → Probability → Selection → Append → Repeat`

Persistent example: `The cat sat on the mat because it was [ ? ]`.

Token boundaries are explicitly illustrative and are not presented as the output of a named tokenizer.

| Section | Problem | Mechanism | Bridge to next section | Learning-value interaction |
|---|---|---|---|---|
| 1. Challenge | What comes next? | Reveal the full route as an unanswered map. | Raw text must first enter the model. | Generate next token reveals the pipeline. |
| 2. Tokenization | A model cannot operate directly on an undivided sentence. | Show illustrative token chips. | Tokens need computable representations. | Tokenize toggles raw text to tokens. |
| 3. Representation | A token identity is not yet a numerical input. | Separate token embedding from positional information. | A token vector still needs context. | Select a token to inspect its embedding lane. |
| 4. Context need | The meaning/use of “it” depends on surrounding tokens. | Make a human relevance hypothesis. | The model needs a numerical relevance mechanism. | Choose “cat” or “mat”. |
| 5. Q/K/V roles | Relevance and carried information need distinct functions. | Query asks, Key advertises, Value contributes. | These roles must be combined. | Q/K/V focus selector. |
| 6. Self-Attention | Individual comparisons must become usable context. | Scores → attention Softmax → weighted Values → contextual representation. | One attention operation belongs inside a larger architecture. | Choose focus token; redraw illustrative attention lines. |
| 7. Transformer | Attention is not the whole model. | Zoom from architecture to block to Self-Attention. | Processed context supports a prediction task. | Three-level zoom selector. |
| 8. LM → LLM → Inference | What is the model producing at inference time? | Language Modeling → Large Language Model → Inference → candidate scores. | Scores need interpretable probabilities. | Reveal candidate scores. |
| 9. Softmax | Scores are not yet a probability distribution. | Normalize scores into `[0.70, 0.29, 0.01]`. | A distribution still does not choose a token. | Predict then reveal the distribution. |
| 10. Sampling | Highest probability is not the only possible selection rule. | Contrast argmax with sampling. | The selected token must return to the context. | Sample once or Generate 10×. |
| 11. Repeat and limits | Generation is not complete after one token. | Append → re-tokenize/represent → process context → predict again. | Rebuild the loop; separate fluency from factual verification. | Run one repeat loop, then enter quiz. |

## Persistent visual grammar

- Token identity: gold chip.
- Representation: pink/violet vector lane plus a separate white positional lane.
- Attention/context: cobalt connectors and stages.
- Transformer placement: teal zoom stack.
- Probability: green bars/distribution.
- Selection: orange outcome.
- Factuality warning: red boundary note, never used as decoration.
- Repeated token-chamfer shape: identifies stages, controls, and information packets.

## Quiz continuity

Six one-at-a-time questions test ordering, Q/K/V mechanism, Softmax versus Sampling, non-zero probability reasoning, context-change transfer, and fluency versus factual verification. Each incorrect answer receives misconception-specific feedback and a route back to its teaching section.

