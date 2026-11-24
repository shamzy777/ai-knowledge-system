# TEACH-PATH-001 Decision Events

## bounded-topic-selection
- timestamp: `2026-11-24T10:00:00+08:00`; teaching_path_id: `TEACH-PATH-001`; event_type: `workflow-decision`
- action: Bound the teaching topic to “LLM 是怎麼從文字產生下一個 token 的？ / How Does an LLM Generate the Next Token?” using the approved eight-concept path.
- status: `proposal-created-awaiting-human-approval`
- reason: The published Wiki is broader than one teachable presentation; this path selects a single causal mechanism.
- input_paths: `wiki/concepts/`, `wiki/relationship-registry.md`
- output_paths: `teaching/paths/TEACH-PATH-001-proposal.md`
- next_route: `proposal-validation-then-human-approval`

## wiki-only-evidence-boundary
- timestamp: `2026-11-24T10:05:00+08:00`; teaching_path_id: `TEACH-PATH-001`; event_type: `workflow-decision`
- action: Restrict factual evidence to published Wiki concept pages; allow just-in-time supporting concepts only when required by the causal explanation.
- status: `applied`
- reason: No additional source ingest, external retrieval, or model knowledge is authorized.
- input_paths: `wiki/concepts/tokenization.md`, `wiki/concepts/embedding.md`, `wiki/concepts/self-attention.md`, `wiki/concepts/transformer.md`, `wiki/concepts/language-model.md`, `wiki/concepts/large-language-model.md`, `wiki/concepts/softmax.md`, `wiki/concepts/sampling.md`
- output_paths: `teaching/paths/TEACH-PATH-001-proposal.md`
- next_route: `evidence-map`

## scope-exclusions
- timestamp: `2026-11-24T10:10:00+08:00`; teaching_path_id: `TEACH-PATH-001`; event_type: `workflow-decision`
- action: Exclude training mechanics, Cross Entropy, specific tokenizer algorithms, and temperature/top-k/top-p details from the main causal path; retain them only as future extensions where applicable.
- status: `applied`
- reason: These details are valid Wiki knowledge but would dilute the inference-time next-token objective.
- output_paths: `teaching/paths/TEACH-PATH-001-proposal.md`
- next_route: `teaching-outline`

## interaction-and-density-boundary
- timestamp: `2026-11-24T10:15:00+08:00`; teaching_path_id: `TEACH-PATH-001`; event_type: `workflow-decision`
- action: Limit the proposal to three learning-value interactions and eleven causal sections; route density failures to section drafting rather than source retrieval.
- status: `applied`
- reason: Interaction and additional evidence must serve comprehension, not decoration or content expansion.
- output_paths: `teaching/paths/TEACH-PATH-001-proposal.md`
- next_route: `proposal-validation`

## human-approval-and-clarifications
- timestamp: `2026-11-24T11:00:00+08:00`; teaching_path_id: `TEACH-PATH-001`; event_type: `human-confirmation`
- action: Record approval for HTML implementation with separate Embedding/position mechanisms, `Language Modeling → LLM → Inference` progression, and no Sampling → Hallucination causal implication.
- status: `approved-for-implementation`
- reason: User supplied explicit teaching clarifications at the human gate.
- input_paths: `teaching/paths/TEACH-PATH-001-proposal.md`
- output_paths: `teaching/drafts/TEACH-DECK-001-section-draft.md`, `teaching/reviews/TEACH-DECK-001-fidelity-check.md`
- next_route: `html-render`
