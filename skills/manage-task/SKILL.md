---
name: manage-task
description: Define, split, resume, hand off, or close execution tasks, standalone or under a change record. Use for lightweight session work, durable tracking, dependencies, and blocked-work coordination.
---

# Manage Task

Own execution scope, coordination, and task status. Read [task policy](references/task-policy.md) for persistence, dependencies, state transitions, and completion gates. Parent specs own behavior; engineering methods provide implementation and review.

## 1. Establish the work

Locate the existing task or establish its goal, boundaries, and completion conditions. Read project tracker conventions, applicable current design, required checks, and any parent spec. For child work, identify the acceptance subset without copying the spec.

If the work introduces consequential behavior, contract, ownership, safety, or migration decisions, reach `manage-change` for classification before implementing them.

Choose conversation-only or durable tracking under the policy. Use the [local task template](references/local-task-template.md) only when persistence is needed and no tracker convention exists.

## 2. Split when useful

For work too large to execute or hand off reliably, or a breakdown needing revision, read [vertical-slice decomposition](references/decomposition.md). Return its proposal for confirmation under the task policy, then publish authorized tasks in the canonical tracker. Otherwise keep one task.

**Ready to publish when:** every slice has an observable result and verification method; full in-scope acceptance is assigned; dependencies are valid; and required decisions and write permissions are resolved.

## 3. Execute, resume, or hand off

- Resolve start-blockers and claim work through the project's coordination mechanism before concurrent execution.
- Supply `implement-work` or the implementer with task/spec pointers, applicable design, acceptance subset, completion conditions, and baseline. Give `review-work` or the project reviewer the same scope when review is requested or required.
- Track actual blockers and unblock conditions. On resume, inspect existing changes/results before repeating work; persist handoffs using the policy's evidence requirements.
- Return parent requirement changes to `manage-change`. Reconcile affected tasks under the policy; send confirmed current-rule implications to `maintain-design`.

## 4. Close against evidence

Compare returned results with every completion condition and apply the policy's gate. Record actual outcome, verification, limits, and related commits/PRs in the canonical task. If the gate is unmet, keep work active or blocked; for cancellation, record remaining-work disposition.

For parented work, return acceptance coverage and deviations to `manage-change`; task completion does not close the parent. For conversational work, a short result is sufficient.

Use host mechanisms or explicit handoffs; report unavailable companion operations as unperformed. Task management grants no implicit permission for commits, publication, or destructive actions; follow project/user authorization.
