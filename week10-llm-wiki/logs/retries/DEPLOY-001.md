# DEPLOY-001 — retries

Timestamp: 2026-11-25T00:39:55+08:00

| Retry | Failure | Responsible node | Local correction | Outcome |
|---|---|---|---|---|
| R1 | The first syntax command referenced a nonexistent historical `app.js` filename. | Regression command | Enumerated the actual presentation JavaScript files and checked `hub.js`, `topics.js`, and `topic.js`. | PASS; no application file changed. |
| R2 | The first browser regression could not resolve a repository path containing spaces because the validator used undecoded `import.meta.url.pathname`. | Validation portability | Changed only the validator to use `fileURLToPath(import.meta.url)`. | Full browser regression PASS. |

