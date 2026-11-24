# TEACH-MECHANISM-001 — retries

Date: 2026-11-24

| Retry | Failure | Responsible node | Local correction | Outcome |
|---|---|---|---|---|
| R1 | A stylesheet patch attempt did not execute because the approval channel was temporarily unavailable. | Execution setup | Retried the same scoped patch after continuation. | CSS applied; no scope expansion. |
| R2 | `py_compile` could not write `__pycache__` in the execution environment. | Syntax validation | Parsed the validator sources with Python `ast.parse` and ran each validator directly. | Syntax and runtime validation passed. |
| R3 | Browser inspection first ran under Node 20, while the inspector requires Node 22+. | Visual validation runtime | Re-ran with the bundled Node 24 runtime. | Inspector executed successfully. |
| R4 | First visual pass treated five long teaching mechanisms as short `data-ui` fragments. | Visual semantics | Reclassified only those long explainers as `data-mechanism-ui` and preserved motion selectors. | False UI-wrapper finding cleared. |
| R5 | First final visual pass flagged `Zoom 1–4` as decorative eyebrow labels. | Transformer visual | Removed the redundant labels; the four explicit zoom buttons retain the hierarchy. | Final visual inspector: 0 findings. |

