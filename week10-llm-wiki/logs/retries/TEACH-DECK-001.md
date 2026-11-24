# TEACH-DECK-001 — retry record

Date: 2026-11-24

| Retry | Failure / observation | Responsible node | Scoped action | Result |
|---|---|---|---|---|
| R1 | Local visual inspector could not bind localhost under the sandbox (`EPERM`). | Technical render tooling | Re-ran the local-only inspector with approved local browser permission. | Reached runtime check. |
| R2 | Inspector required Node 22+; default runtime was Node 20.18.0. | Technical render tooling | Used the bundled Node 24.22.3 runtime. | Inspector ran. |
| R3 | First visual inspection: three-line hero, low-contrast provenance labels, 14 px body heuristic, asymmetric/edge measurements, and reveal/blank-gap findings. | HTML render → CSS/layout | Changed only type scale, contrast, provenance layout, hero measure, and responsive reveal/full-height rules. | Reduced to four then two findings. |
| R4 | Static validator treated slide id `s10` as prohibited source S10 and did not reliably associate evidence footers. | Validation script | Made the S10 check case-sensitive and simplified slide/evidence parsing. | Static deck validation passed. |
| R5 | Legacy Wiki/proposal validators still enforced the earlier pre-approval no-HTML gate. | Validation workflow | Made authorization conditional on the already-recorded approved proposal metadata. | Both legacy checks passed without changing Wiki rules/content. |
| R6 | Visual review found reverse-layout evidence appearing before headings. | Render check → affected layout | Set explicit copy → visual → evidence order. | Hierarchy corrected. |
| R7 | Final five-width inspection found mobile fixed navigation covering text and a three-line Softmax heading at 1280 px. | Visual review → mobile navigation / Slide 9 heading | Changed mobile nav to sticky non-overlapping flow and composed Slide 9 heading as two intentional lines. | Final inspector: 0 failures, 0 warnings. |

No factual fidelity failure, evidence insufficiency, quiz-support failure, or teaching-sequence failure occurred. Therefore no retry returned to Wiki retrieval or source ingest.
