# TEACH-DECK-001-REDESIGN-001 — retries

Date: 2026-11-24

| Retry | Failure | Responsible node | Local correction | Outcome |
|---|---|---|---|---|
| R1 | Initial shell command used an incorrect Week 10 workdir. | Execution setup | Re-resolved the isolated project path before writing. | Continued without touching the permanent system. |
| R2 | First write attempt was blocked by filesystem permission. | Execution setup | Requested and received write permission only for the isolated Week 10 project. | Redesign files written in scope. |
| R3 | No-JavaScript validator looked for the old `.slide-frame` selector. | Render validation | Updated the checker to inspect `[data-slide]`. | No-JS fallback passed. |
| R4 | First redesign inspection found hero overlap, small body text, deep mobile wrapping, and a scrolling pipeline. | Visual review → CSS/layout | Adjusted hero scale/grid, body/support type, mobile pipeline, and bridge measures. | Desktop overlap and text-size failures cleared. |
| R5 | Mobile 3×3 sticky pipeline covered later headings. | Visual review → mobile navigation | Returned to a lower 5×2 pipeline. | Mobile coverage cleared. |
| R6 | Tablet 6+3 pipeline covered bridge text while sticky. | Visual review → tablet navigation | Changed tablet to a single nine-stage row with manual word-break opportunities. | Tablet visual gate passed. |
| R7 | ArrowDown scrolled but the IntersectionObserver reset progress to 1/11. | Interaction check → keyboard state | Added a short navigation lock during smooth scrolling. | Browser test passed at 2/11. |

