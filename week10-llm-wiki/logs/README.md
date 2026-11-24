# Execution Log Contract

Execution logs preserve evidence of the actual Week 10 workflow. They are not Wiki content.

## Required event fields

Each log event must record:

- `timestamp`: ISO 8601 with timezone;
- `run_id`: stable identifier shared by events in one execution;
- `event_id`: unique event identifier;
- `event_type`: ingest, validation, retry, graph-return-route, decision, or confirmation;
- `source_ids`: affected source manifest IDs, if any;
- `artifact_paths`: affected project-relative paths;
- `action`: what the workflow attempted;
- `status`: started, passed, failed, returned, retried, blocked, confirmed, or rejected;
- `reason`: evidence-based explanation;
- `from_state` and `to_state`: workflow transition;
- `next_route`: next planned workflow node;
- `related_event_ids`: prior events that caused or informed this event.

## Logging rules

- Use append-only records in practice. Correct an event with a later event; do not erase the earlier history.
- A retry must point to the failed validation or ingest event that caused it.
- A graph return route must identify the failed gate and the staging node to which work returned.
- Important automatic decisions, including canonical-match decisions and source exclusions, belong in `logs/decisions/`.
- Human confirmations must identify the confirmed object and scope without inventing confirmation history.
- Do not log secrets, tokens, credentials, or unnecessary personal data.

No execution event has been created in Phase 2 because no ingest or Wiki workflow run has begun.
