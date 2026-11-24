# TEACH-DECK-001 — dedicated learning-mechanism review

Date: 2026-11-24  
Result: PASS (9/9)

| # | Reviewer question | Presentation answer | Wiki grounding |
|---|---|---|---|
| 1 | How does a token become a numerical vector representation? | A discrete token is identified, passed through an Embedding lookup / learned representation, and output as an operable embedding vector. | Embedding |
| 2 | Why is positional information separate from token embedding? | Token Embedding represents the token; Positional Information provides its sequence position. They are combined for the Transformer input but are not the same mechanism. | Embedding; Positional Encoding |
| 3 | Which token's Query is used? | The fixed update target is `it`; its Query is compared with visible-token Keys. | Query / Key / Value |
| 4 | What is compared with what to produce attention relevance? | The Query of `it` is compared with the Keys of visible tokens to produce relevance / attention scores. | Query / Key / Value; Self-Attention |
| 5 | What do Values do after weights exist? | The normalized weights determine how much information from each Value is combined. | Query / Key / Value; Self-Attention |
| 6 | What changes before vs after Self-Attention? | Before: the current-position representation has not received this contextual update. After: visible-position Values have been weighted and combined into an updated contextual representation. | Self-Attention |
| 7 | Where does Self-Attention sit? | It is a mechanism inside a Transformer block; blocks form a stack inside the Transformer model. It is not the whole Transformer. | Self-Attention; Multi-Head Attention; Transformer |
| 8 | When does the selected next token first exist in the loop? | It first appears at Selection, after Prediction and Probability. It is absent from the initial sentence and earlier states. | Language Model; Softmax; Sampling; Inference |
| 9 | Why does the selected token enter the next Context? | Append adds the selected token to the current sequence; the updated sequence is the next inference cycle's Context. | Language Model; Inference; Sampling |

## Evidence limitations preserved

- The published Wiki supports a token identity stage but does not provide an actual tokenizer-specific numeric token ID for this sentence; none is invented.
- Vector bars, relevance links, scores, and attention weights are schematic mechanism cues, not measured output from a real model.
- The Transformer zoom is intentionally partial. It shows only the supported orientation components needed to locate Self-Attention.
- The original Transformer and modern causal-decoder scopes remain explicitly distinguished.

