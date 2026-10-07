# Task policy

## Unit and ownership

A task has a goal and observable completion conditions. It may stand alone or have one primary parent change record. Cross-change shared work uses references and dependency edges instead of multiple competing requirement owners.

A change does not require an explicit task when it can be executed directly. Tasks organize execution; parent specs own behavior. An independent task uses the user's request and applicable current design as its requirements.

## Persistence

- Same-session, immediately executable work: a short conversational brief and result suffice.
- Queued, cross-session, blocked-across-session, or handed-off work: use the existing tracker.
- No tracker and persistence is needed: default to `docs/tasks/NNN-slug.md`; allocate an unused ID after inspecting existing tasks. Recheck before creation and coordinate concurrent allocation.

Persist the canonical task only once. A tracker link is preferable to a duplicate Markdown task. Map project statuses to their meaning instead of forcing renames. Creating remote artifacts requires existing authorization; otherwise prepare the proposed content and request permission.

## States and transitions

| State | Meaning |
| --- | --- |
| Todo | Goal and completion conditions are defined; execution has not started. |
| Doing | Work is actively in progress. |
| Blocked | Progress depends on a named unmet condition. Record the reason, next action, and responsible party if known. |
| Done | All required completion conditions, checks, and reviews are satisfied with evidence. |
| Cancelled | Work will not continue. Record why and where remaining obligations went. |

Normal path: Todo → Doing → Done. Todo or Doing may become Blocked; return to Todo or Doing when the blocker is actually resolved. Active states may become Cancelled. Reopen Done only when the recorded completion was invalid or incomplete; new scope normally gets a new task.

Awaiting an available review can remain Doing with an explicit next action. If the review cannot proceed because of an unmet dependency, use Blocked. A separate review state is optional under project conventions.

Missing required verification prevents Done. Optional unperformed checks must be disclosed. Changing completion conditions requires the responsible decision-maker's agreement; if parent acceptance changes, update the parent decision first. Risk controls cannot be waived merely by editing a task.

## Decomposition and dependencies

Prefer slices with observable end-to-end behavior, sized for reliable execution and handoff. Do not force all work into UI/API/database slices or arbitrary file-count limits. Investigations and migrations can have non-code deliverables.

A blocker gates starting or completing a task; distinguish it from merely related work. Validate the dependency graph for cycles. Start only tasks whose start-blockers are resolved. Shared changes may need coordination even without a semantic dependency; represent that execution constraint explicitly.

Avoid creating a redundant parent-task hierarchy when a change record already supplies the shared goal. Some trackers require parent issues; use them as pointers rather than a second full spec.

## Completion evidence

Capture a concise result, commands or check methods actually used, their results, the inspected baseline, and unresolved limits. A review assertion or passing unit test does not substitute for other required acceptance checks. Never infer that all work succeeded merely because a tool exited successfully.

Keep durable handoffs sufficient to resume without replaying the entire chat: task/spec pointers, current workspace or branch, verified facts, unfinished changes, blockers, and next action. Check for sensitive content before persisting.
