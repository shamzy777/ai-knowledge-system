---
type: source-scope-and-conflict-register
run_id: RUN-004
source_ids: [S08, S09]
status: complete
publication_status: unpublished
---

# RUN-004 — Source differences and conflict review

## Scope differences, not factual conflicts

1. **Original architecture versus modern causal LLM.** S08 describes the 2017 encoder–decoder Transformer. S09's beginner LLM path emphasizes a causal decoder block. Both perspectives are retained with their locators; the later scope is not retroactively attributed to S08.
2. **Position representations.** S08 uses sinusoidal positional encodings and notes learned alternatives. S09 also teaches learned absolute and later relative approaches. This is an original-design versus later-variant distinction, not a contradiction.
3. **Word versus token terminology.** Course slides sometimes use 字/word pedagogically. S09 defines tokenization and subword units. Existing course wording remains attributed, while canonical LLM claims now use token where S09 supplies that evidence.
4. **Hallucination scope.** S04 uses a broad creative-generation framing; S09 uses a narrower reliability framing for fluent but ungrounded or incorrect output. Both are preserved and the difference remains visible on the concept page.

## Exclusions

Time-sensitive model rankings, product lists, parameter counts, and universal claims about current systems were not promoted from the dated S09 manuscript. Benchmark-superiority claims from S08 were not used as timeless architecture definitions.

## Human gate

No new irreconcilable factual conflict was found in RUN-004. The pre-existing Hallucination framing difference remains a publication-treatment confirmation item because the page already carries `conflict_status: requires-user-confirmation-before-publication`.
