# Week 10 LLM Wiki Prototype

## Scope and isolation

This directory is an isolated Week 10 prototype for a real LLM Wiki workflow. It may inform later improvements to the permanent AI Knowledge System, but it is not part of that system.

- Work only inside this Week 10 project unless the user explicitly authorizes a broader scope.
- Treat `/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/` as read-only source material.
- Do not create, edit, delete, move, rename, or reorganize anything in the permanent AI Knowledge System.
- Do not write back concepts, mastery, relationships, indexes, sources, logs, teaching material, or configuration to the permanent system.
- All source copies, manifests, staging data, Wiki content, relationships, mastery records, quizzes, teaching HTML, logs, and publication settings must remain inside this project until the user explicitly approves migration.

## Project purpose and audience

Prototype an auditable LLM Wiki workflow for mixed readers who have introductory background but are not specialists.

The Wiki topic is **從零開始認識 LLM**, spanning foundations, theory, core mechanisms, and applications. Explanations must be technically accurate while remaining accessible to beginners.

## Core philosophy

The system is concept-oriented, not source-oriented or course-oriented.

> Sources contribute evidence. Canonical concepts organize knowledge.

Follow an understanding-first workflow:

```text
Traceable Sources
→ Batch Ingest
→ Staging Drafts
→ Validation and Conflict Review
→ Teaching / Understanding Activities
→ Mastery Confirmation
→ User-approved Week 10 Publication
```

An AI-generated summary is not evidence of user understanding. Staged or published Week 10 content must never be silently promoted into the permanent AI Knowledge System.

## Knowledge layers

### Source layer

Traceable course materials, papers, official documentation, and reliable educational references. Store project-local source copies in `sources/inbox/` only when copying is authorized and lawful. Record source identity and locators in `sources/manifests/`.

### Staging layer

Unpublished outputs produced by batch ingest, including candidate concepts, chapter drafts, relationships, provenance notes, conflict records, and proposed mastery. Keep these under `staging/`.

### Week 10 Wiki layer

User-approved Week 10 canonical concepts and chapter pages under `wiki/`. This is still isolated prototype knowledge, not permanent-system knowledge.

### Teaching layer

Bounded learning paths, quizzes, diagrams, and interactive teaching demonstrations under `teaching/`. A teaching presentation selects one bounded path from the Wiki; it must not attempt to teach the entire Wiki at once.

## Concept and page rules

Use a two-layer content architecture:

1. one canonical concept per concept page;
2. chapter pages that connect closely related concepts into coherent learning paths without replacing the concept pages.

Only actual knowledge concepts can be concept nodes. Course names, weeks, assignments, source documents, and chapter pages are metadata, source records, or navigation structures—not canonical concepts.

### One concept, one canonical page

Before creating a concept:

1. search staged and published Week 10 concepts for the same or closely related meaning;
2. compare the core definition and mechanism, not only the term;
3. prefer updating the existing canonical concept;
4. create a new concept only when it has a genuinely independent core definition or mechanism;
5. express related distinctions with an approved relationship rather than duplicating the concept;
6. never encode source or course identity into a canonical filename.

Use lowercase kebab-case filenames, such as `self-attention.md` and `retrieval-augmented-generation.md`.

## Language rules

- Present the Wiki bilingually.
- Use English for technical terms.
- When a conventional Chinese translation exists, show it alongside the English term, for example `Self-Attention（自注意力）`.
- Validate terminology for consistent English and Traditional Chinese usage across pages.

## Provenance and citation rules

Every substantive paragraph or concept-page section must list its principal sources. Exact page, section, slide, or URL locators are encouraged when the source supports them; never invent locators.

Keep these provenance categories distinct:

- Course Material
- Research Paper
- Official Documentation
- Reliable Educational Reference
- Model Knowledge — Supplementary Only
- User Interpretation / Analogy

Model knowledge may be used only as clearly labelled supplementary knowledge. It must not be presented as course content, silently blended with traceable evidence, or counted toward the assignment requirement of at least five ingested sources.

The assignment's **5+ source requirement** must be satisfied by five or more separately identifiable, traceable source materials such as course materials, papers, official documentation, or reliable educational references. Internal canonical notes, Week 9 presentation files, indexes, source summaries without a resolvable underlying source, and model knowledge do not automatically count as independent ingests.

## Conflicting sources

When sources conflict:

- preserve each supported position;
- identify each source and relevant context;
- explain the nature and likely reason for the difference;
- do not force a false consensus;
- mark the conflict as requiring user confirmation before publication.

Source-conflict resolution is a mandatory human confirmation point.

## Ingest strategy

- Batch ingest of multiple sources is allowed.
- Do not write ingest output directly into `wiki/`.
- Produce source manifests, staged drafts, candidate relationships, and validation results first.
- Retain the boundary between source text, extracted claims, synthesis, model-supplied supplementary explanation, and user interpretation.
- Do not start an ingest unless the current phase explicitly authorizes it.

## Mastery model

Use the inherited five levels:

- 🟥 不理解
- 🟧 聽過但模糊
- 🟨 可以解釋
- 🟩 可以運用
- 🟦 可以和其他概念建立連結

AI may propose a mastery level, but only the user may confirm or change it. Never infer mastery from page completeness, quiz generation, AI summaries, or source ingestion.

## Relationship vocabulary

Use only:

- `prerequisite`
- `part-of`
- `cause/effect`
- `evolution`
- `application`
- `contrast`
- `theory ↔ practice`
- `cross-domain analogy`

A supported relationship may be added automatically to staging. Every relationship must have valid endpoints and recorded source support. Do not invent edges to make the graph appear complete or dense.

## Teaching HTML requirements

The downstream teaching HTML must:

- select one bounded learning path from the broader Wiki;
- order concepts for beginner comprehension;
- include a simple quiz for each teaching path;
- use diagrams or interactive demonstrations when they materially improve understanding;
- preserve provenance and uncertainty;
- remain understandable without interaction and accessible without relying only on color.

The teaching presentation must not attempt to teach the entire Wiki in one path.

## Validation requirements

Automated lint and validation must check, at minimum:

- required page schema;
- bilingual terminology consistency;
- principal-source citations and provenance labels;
- clear labelling of non-course and model-supplementary knowledge;
- broken internal links;
- duplicate or near-duplicate canonical concepts;
- relationship structural validity: approved vocabulary, valid endpoints, required schema, and cited-source presence;
- relationship semantic validity: an independent evidence review of whether the cited source actually supports the proposed type and direction;
- quiz questions and answer keys;
- isolation boundaries;
- required execution-log entries.

Validation failure returns work to staging and must not silently publish content.

### Relationship validation gates

Relationship validation has two distinct gates:

1. **Structural validation** checks only machine-verifiable form: approved vocabulary, endpoint existence, schema completeness, and presence of a source citation.
2. **Semantic validation** separately reviews the cited source evidence to decide whether the proposed relationship type and direction are actually supported.

A structurally valid edge is not automatically semantically valid. Semantic review must record `accepted`, `rejected`, or `returned-to-staging` with a rationale and cited source pages. Do not silently reverse, relabel, or rewrite a questionable edge. Preserve the original proposal, record the rejection or return route, and create a separately identified replacement proposal only when the evidence supports it.

## Human confirmation points

Only these actions require mandatory user confirmation:

1. resolution or publication treatment of source conflicts;
2. mastery assignment or change;
3. formal publication from staging into the Week 10 Wiki or teaching output.

Normal source extraction, staging drafts, canonical matching, relationship proposals, and automated validation may proceed without item-by-item confirmation when the phase authorizes them.

## Execution evidence and logs

Preserve evidence of one real workflow execution and its adjustment. Record every:

- ingest attempt;
- validation result;
- retry;
- graph return route or workflow back-edge;
- important workflow decision;
- human confirmation event.

Logs must be append-only in practice: do not rewrite history to make a run appear cleaner. Corrections should be new entries that reference the earlier event.

Use these locations:

- `logs/ingest/`
- `logs/validation/`
- `logs/retries/`
- `logs/graph-return-routes/`
- `logs/decisions/`

Each event must include a timestamp with timezone, run ID, source or artifact IDs, action, status, reason, input/output paths, and next route. Never record secrets or unnecessary personal data.

## Current execution boundary

RUN-001 through RUN-004 and `PUB-RUN-001` are complete. `TEACH-PATH-001` is approved and authorizes local HTML implementation of the bounded next-token teaching presentation using only the published Week 10 Wiki.

- No additional source ingest is authorized. S10 remains un-ingested.
- S08 provenance must remain `Research Paper`; S09 provenance must remain `Reliable Educational Reference`. Neither may be labelled Course Material.
- S10 and every other source remain un-ingested and unauthorized.
- Preserve OCR/handwriting uncertainty for S01 and S07 and never treat uncertain transcription as high-confidence evidence.
- Do not write to `wiki/` or `teaching/`, change mastery, publish, or modify the permanent AI Knowledge System.
- Follow `Wiki retrieval → evidence-mapped section draft → fidelity check → HTML render → render/interaction check → final deck`. Do not modify the published Wiki, change mastery, ingest sources, use external/model knowledge, or modify the permanent AI Knowledge System. Stop before public deployment.

## Project structure

```text
docs/                         requirements, audits, and proposals
sources/inbox/                authorized project-local source copies
sources/manifests/            source identity and provenance records
staging/ingests/              extracted source records
staging/concepts/             unpublished canonical concept drafts
staging/chapters/             unpublished chapter drafts
staging/relationships/        unpublished relationship records
wiki/concepts/                published Week 10 concept pages
wiki/chapters/                published Week 10 chapter pages
teaching/paths/               bounded teaching paths and presentations
workflow/schemas/             validation schemas
workflow/scripts/             ingest and validation tooling
logs/                         execution evidence by event type
```

Empty directories do not authorize filling them outside the current phase.
