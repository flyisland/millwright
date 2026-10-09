# Task policy

## Unit and ownership

A task has a goal and observable completion conditions. It may stand alone or have one primary parent change record. Cross-change shared work uses references and dependency edges instead of multiple competing requirement owners.

A change does not require an explicit task when it can be executed directly. Tasks organize execution; parent specs own behavior. An independent task uses the user's request and applicable current design as its requirements.

## Persistence

- Same-session, immediately executable work, including a bounded delegation supervised through its return: a short conversational brief and result suffice.
- Queued, cross-session, blocked-across-session, or work handed off beyond that supervised exchange: use the existing tracker. Delegation alone does not require a new task record; reuse an existing canonical task when present.
- No tracker and persistence is needed: use `.tasks/NNN-slug.md` and add `/.tasks/` to the root `.gitignore`. Allocate an unused ID after inspecting existing tasks; coordinate concurrent allocation. Preserve existing project locations unless migration is authorized.

Persist the canonical task only once. A tracker link is preferable to a duplicate Markdown task. Map project statuses to their meaning instead of forcing renames. Creating remote artifacts requires existing authorization; otherwise prepare the proposed content and request permission.

Local persistence supports cross-session recovery, not permanent archival. Git-ignored files do not transfer across clones or worktrees; use a shared tracker or explicit artifact transfer for cross-workspace handoffs.

## Retention and cleanup

After closure, local task records may be removed under project/user cleanup authorization. First transfer outstanding work and retain necessary delivery evidence in the outcome or project evidence store, and confirmed rules through `maintain-design`. Repair references before deletion; active consumers must not depend on disposable records. A standalone task needs no archive without a retention requirement. Done alone does not authorize deletion.

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

When parent scope changes, reconcile affected task acceptance and the applicability of existing evidence before further execution or closure. Preserve valid historical completion; use a new task for new scope, or reopen only under the rule above. When a parent is cancelled or superseded, stop affected dispatch and record which unfinished tasks are cancelled, deferred, or transferred to the successor. Inform active workers; a status edit alone does not stop their execution.

## Decomposition and dependencies

Prefer slices with observable end-to-end behavior, sized for reliable execution and handoff. Do not force all work into UI/API/database slices or arbitrary file-count limits. Investigations and migrations can have non-code deliverables. Read [decomposition](decomposition.md) when proposing or revising a breakdown; it owns the step-by-step method and examples.

Confirm a consequential decomposition with the responsible decision-maker before publishing its graph or dispatching parallel work. Publish only with the existing artifact-creation authorization; agreement on task granularity is not blanket permission for remote writes. Preserve canonical requirement pointers and map project statuses rather than applying an automatic ready label.

A blocker gates starting or completing a task; distinguish it from merely related work. Validate the dependency graph for cycles. Start only tasks whose start-blockers are resolved. Shared changes may need coordination even without a semantic dependency; represent that execution constraint explicitly. If no reliable claim or ID-allocation mechanism exists, serialize the conflicting operations instead of assuming a recheck makes concurrent writes safe.

Avoid creating a redundant parent-task hierarchy when a change record already supplies the shared goal. Some trackers require parent issues; use them as pointers rather than a second full spec.

## Completion evidence

Capture a concise result, commands or check methods actually used, their results, the inspected baseline, and unresolved limits. A review assertion or passing unit test does not substitute for other required acceptance checks. Never infer that all work succeeded merely because a tool exited successfully.

Keep persisted handoffs sufficient to resume without replaying the entire chat: task/spec pointers, current workspace or branch, verified facts, unfinished changes, blockers, result recipient, and next action with its responsible party and resume condition. Record how continuation will occur; if it requires a person to resume the work, say so rather than promise automatic progress. Check for sensitive content before persisting.
