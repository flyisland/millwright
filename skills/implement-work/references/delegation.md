# Delegated implementation

Read when the user requires subagents or you choose to delegate implementation. Direct execution remains valid otherwise. Delegation transfers bounded work, not the coordinating agent's responsibility to return a verified result or a clear blocker. This reference owns the immediate assignment/check/fix loop; reach `manage-task` for persistent tracking, claims, dependencies, or cross-session handoff under its policy. Task and change closure remain with their lifecycle owners.

## Choose an execution context

Follow the user's requested division of work and the host's agent guidance. Do not invent provider IDs, notification guarantees, or unavailable operations. If required delegation is unavailable, report the limitation and seek an alternative; do not silently substitute direct implementation. If delegation was optional, direct execution is a valid fallback.

Prefer a fresh worker for a new independently describable objective, and reuse the worker for fixes or additional checks within the same objective. Reuse across closely coupled steps when the relevant context clearly saves more than it risks. A worker assignment need not map one-to-one to tracker tasks.

Reconsider reuse when scope, permissions, or environment changes materially, or when obsolete instructions, repeated exploration, or confused progress outweigh the useful context. Do not wait for a token limit or restart every fixed number of tasks. A fresh context still needs to verify supplied facts; it is not automatically an independent judgment.

Choose workspace isolation separately from context isolation. In a shared workspace, assign non-overlapping writes or serialize them. In isolated workspaces, identify who integrates the result and which integrated baseline must be checked. Do not inspect a moving working tree as though it were a stable final baseline.

## Send a bounded brief

Provide only what the worker needs:

- Goal, exclusions, acceptance subset, and authoritative request/task/spec/design pointers.
- Workspace and baseline, existing edits to preserve, allowed edit areas, and other active writers.
- Authorized operations, required checks, and material decisions that must return to the coordinator.
- Progress facts needed by the coordinator, including actual implementation start for a parent change; report them without waiting for the final return.
- Expected return: changed entry points, actual commands/results, checked baseline, unresolved findings and limits, and relevant decisions.
- A stopping condition: return the bounded result or blocker; do not continue into unrelated work or close lifecycle records.

For a fresh worker, add relevant verified facts, unfinished changes, and useful failed approaches with their reasons. Prefer source and evidence pointers over copying the full transcript. Keep the coordinator's context focused on scope, decisions, progress, and evidence, not every tool log. Exclude secrets and unnecessary data. Neither continuation nor delivery should depend on one worker remembering the whole history.

## Establish continuation before dispatch

Name the result recipient, the next action, and how completion, failure, or a decision request will reach that recipient. Use the host's supported notification, wait, or explicit handoff mechanism; no particular API or automatic callback is required. If continuation needs a person to resume the session, state that condition instead of promising automatic progress.

Follow host semantics for messages to a running worker. Do not assume a follow-up was accepted or a cancellation completed. Before replacing a worker, reconcile its partial work and ensure overlapping writes have stopped. A retry must not accidentally dispatch the same assignment twice.

When a result arrives, perform the next authorized action or identify the actual blocker. A progress-only reply saying that review will start is not the review itself. Do not treat a worker's idle/finished signal as evidence of acceptance.

## Receive, check, and repair

1. Inspect actual edits and confirm the returned baseline, scope, and evidence. Identify omissions and out-of-scope changes rather than relying on the worker's completion claim.
2. Apply [verification methods](verification.md) and the required review through `review-work` or the project method. The coordinator can review when qualified under project requirements; no extra reviewer agent is mandatory. Disclose implementation involvement, and do not substitute an implementer's self-review for required independent approval.
3. Return actionable findings and reproduction evidence for bounded repair, normally to the same worker. A speed request narrows unnecessary work, not the acceptance conditions. Escalate material requirement choices through the decision boundary in `implement-work`.
4. Recheck affected behavior and obtain required re-review on the resulting baseline, including integration when needed. Earlier results do not automatically cover later edits.
5. Return the final evidence or specific remaining blocker under `implement-work`. Distinguish dispatched, implementation returned, and conditions verified; lifecycle owners decide Done/Completed.

A coordinator assigned only coordination and review should not silently take over implementation. Clarify a changed division of work when necessary, and reassess review independence if the coordinator contributes implementation.
