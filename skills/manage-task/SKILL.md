---
name: manage-task
description: Define, split, track, resume, hand off, or close execution tasks. Use for standalone work or tasks under a change record, including blocked work and cross-session coordination. Keep single-session work lightweight and use the project's existing tracker for durable tasks.
---

# Manage Task

Own the execution lifecycle, not the coding method or the parent change's specification.

Read [task policy](references/task-policy.md) for persistence, state transitions, dependencies, and completion gates. Discover the project's tracker, verification requirements, current design pointers, and any parent spec before creating work.

## 1. Establish the work

- Locate the existing task or determine that a new one is needed.
- State its goal, boundaries, and completion conditions. For a child task, identify the parent spec and acceptance scope without copying the full spec.
- Check whether the requested behavior is already defined. If it introduces consequential behavior, contract, ownership, safety, or migration decisions, reach `manage-change` for record classification before implementing the affected decision.
- Choose conversation-only or durable tracking. Use [local task template](references/local-task-template.md) only when persistent work has no existing tracker convention.

**Done when:** the task is actionable, or specific unresolved questions block execution; its storage and relationship to a change are clear.

## 2. Split only when useful

For work too large to execute or hand off reliably, propose independently verifiable end-to-end slices. Record only genuine blocking dependencies. Confirm a consequential decomposition with the user before publishing a graph or dispatching parallel work.

For broad mechanical refactors, prefer expand → migrate in bounded batches → contract over artificial feature slices. If slices cannot remain valid independently, state the shared integration requirement and final verification task.

**Done when:** each task has a bounded result and completion conditions; the graph has no cycles and no invented blockers. Otherwise keep one task.

## 3. Execute, resume, or hand off

- Claim or mark Doing using the project's coordination mechanism before concurrent execution.
- Supply the implementer with the task pointer, parent spec if any, relevant design, completion conditions, and known limits. Use the project's implementation, diagnosis, testing, and review methods.
- Track actual blockers with a reason and an unblock condition. A guess that another task is finished is not dependency evidence.
- On resume, inspect existing changes and results before repeating work. For handoff, persist completed work, remaining steps, blockers, evidence, and workspace/commit pointers. Exclude credentials and unnecessary logs.
- Return proposed changes to the parent's behavior or acceptance to `manage-change`; report new current-design implications to `maintain-design` after confirmation.

**Done when:** execution can continue safely, a specific blocker is recorded, or another worker has sufficient persistent context to resume.

## 4. Close against evidence

Compare the result with every completion condition, including required checks and reviews. Record what changed, actual verification, known limits, and related commits/PRs. Mark Done only when the policy's gate is satisfied; otherwise keep it active or blocked. Record reasons for cancellation and destinations for any still-needed work.

For parented work, report acceptance coverage and deviations back to the change. Completing tasks does not close the parent change.

**Done when:** status and evidence agree, and the next owner/location of remaining work is clear.

## Output and boundaries

For a tiny task, a short conversational goal and final result are enough. Do not create administrative artifacts just to satisfy a template. For persisted work, update the canonical tracker rather than a competing local copy.

Use available host mechanisms for companion skills or explicitly hand off the missing operation. Creating remote issues, committing, publishing, or destructive actions follows project/user authorization; task management itself grants none of those permissions.
