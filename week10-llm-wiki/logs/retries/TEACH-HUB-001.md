# TEACH-HUB-001 — retries

Timestamp: 2026-11-24T19:56:53+08:00

| Retry | Failure | Responsible node | Local correction | Outcome |
|---|---|---|---|---|
| R1 | Initial Week 10 filesystem move was outside the then-active write scope. | Execution setup | Requested write access only for the isolated Week 10 project. | Hub/topic split completed without touching the permanent system. |
| R2 | A combined patch attempted to delete and re-add the render checker in one operation. | Validation tooling | Split the change into separate operations and verified the resulting script. | Checker restored and syntax-valid. |
| R3 | Static fidelity markers still expected pre-translation English wording. | Static validation | Updated only the validator markers to match the approved Traditional Chinese wording. | Static grounding validation passed. |
| R4 | Language parser concatenated the two-line brand title without a separator. | Language validation | Joined nested text nodes with spaces. | The valid proper name no longer produced a false failure. |
| R5 | First visual review found a three-line mobile Hub title and a three-line footer statement. | Hub typography | Preserved the `AI Knowledge` line and widened the footer statement measure. | Hub headings remain within two lines. |
| R6 | Topic visual review found a three-line `Contextual Representation（上下文表示）` mechanism label. | Self-Attention visual | Kept the English term as the heading and moved the Chinese explanation to the supporting line. | Mechanism label passed at all widths. |
| R7 | Shrinking mobile pipeline labels prevented broken English words but produced sub-13px text. | Mobile topic navigation | Returned to a readable 13px control and made the pipeline an intentional scrollable step navigator that centers the active step. | Readability and overflow checks passed. |
| R8 | Browser checker compared document width to the requested emulation width even when Chromium reported a rounded inner width of 377px for the 375px profile. | Render validation | Compared document width to measured `innerWidth`. | False overflow failure cleared; no visual offender existed. |

