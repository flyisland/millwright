---
name: implement-work
description: Implement a bounded request, task, or confirmed spec, including resuming unfinished work. Return implementation and verification evidence without approving requirements or closing lifecycle records.
---

# Implement Work

## 1. Establish scope and baseline

Read project instructions, the request/task and parent spec or approved amendments, applicable current design, and required checks. Identify the acceptance subset; a clear small request needs no formal task or spec.

Inspect existing edits and prior results before continuing. Preserve unrelated work. If claiming, dependency reconciliation, splitting, or persistent handoff is needed, reach `manage-task`. For cancelled or superseded inputs, locate the current authorized work first.

**Decision boundary throughout execution:** pause affected work when behavior, contracts, ownership, safety, or acceptance require a material choice. Return evidence and options to `manage-change`, or to `manage-task`/the decision-maker for standalone task scope. Continue only safe, unaffected work; requirement changes are not implementation details.

Proceed when the result, baseline, scope, and checks are clear; otherwise name the blocker. When implementation of a parent change actually starts, report that fact through `manage-task`, or directly to `manage-change` when no task exists, so the lifecycle owner can update the record.

Direct implementation needs no subagent. When the user requires delegation or you choose it, read [delegated implementation](references/delegation.md) before dispatching; it covers bounded assignments, context reuse, continuation, and receiving results.

## 2. Implement and check incrementally

Read [verification methods](references/verification.md) when selecting and running checks. Use its test-first method when requested or appropriate; choose suitable validation for non-code work.

- Inspect the relevant path and reproduce reported defects where practical; distinguish a demonstrated cause from a hypothesis.
- Choose the smallest coherent implementation path and the checks that establish completion. Make a change tied to acceptance, then check it before widening the edit.
- Evaluate existing project capabilities, standard tools, and mature dependencies before building a common capability yourself. Choose by fit, compatibility, safety, and maintenance cost; neither adding a dependency nor avoiding one is an end in itself. Follow dependency authorization rules.
- Reuse project patterns and terminology. Additional exploration, abstraction, or refactoring needs a concrete in-scope reason; preserve behavior and rerun affected checks.
- Stop when the bounded result, required checks, and required review are satisfied. Requests for speed should narrow unnecessary work, not hide failures or waive required verification.

## 3. Review and address findings

Run the required final checks using the verification reference. When review is requested or required, use `review-work` or the project method with the baseline, acceptance subset, and evidence.

Address in-scope findings and rerun affected checks. Obtain required re-review after changes; earlier approval may not cover the new baseline. Label self-review, which cannot replace required independent approval. Missing review remains an explicit gap.

## 4. Return evidence

Report the final baseline, changed entry points, acceptance coverage, actual check results, review disposition, and remaining deviations/blockers. Include affected current-rule pointers and confirmed decisions for design synchronization.

Return task evidence to `manage-task`, or direct change evidence to `manage-change`; reach `maintain-design` for current-rule updates. These owners apply lifecycle policy. Implementation returns evidence, not Done/Completed status or a claim that design synchronization occurred.

Use host mechanisms or explicit handoffs; report unavailable companion operations as unperformed. Preserve user control: commits, branch switching, remote writes, deployment, and destructive operations follow project/user authorization. Implementation grants no implicit permission for them.
