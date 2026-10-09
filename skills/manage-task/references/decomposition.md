# Vertical-slice decomposition

Use when splitting large work or revising a breakdown. [Task policy](task-policy.md) owns confirmation, persistence, dependencies, and status; this reference supplies the splitting method.

## Choose the first complete path

A **vertical slice** delivers a narrow observable behavior through the layers it needs, including verification. Start from the confirmed acceptance scope, existing tasks, and current implementation. Choose a small real path from entry point to result, preferably one that exercises an important integration or high-risk assumption early.

Include the interface, logic, storage, and external interactions only where needed. A backend event flow needs no invented UI. Independent verification means demonstrating the result against declared prerequisites, not having zero dependencies or being independently releasable.

Keep authorization, isolation, compatibility, and other invariants necessary for valid behavior in the first usable slice. A happy path that violates the contract is not a complete slice. Placeholders alone do not demonstrate the real path.

Distinguish evidence needed to start implementation from evidence needed for final acceptance. Consider applicable existing contracts and prior integration evidence before proposing new investigation. Make an unknown a start-blocker only when it prevents a responsible implementation path; otherwise assign it a verification owner and completion gate. Prior evidence can enable implementation without replacing required final checks.

If uncertainty blocks selecting a responsible path, propose a bounded investigation: question, evidence, stopping condition, and decision enabled. Return material behavior choices to `manage-change`; investigation is not approval.

## Grow by behavior

Add slices by action, scenario, supported variant, or bounded data population, not by technical layer. For each, identify what becomes possible and how to demonstrate it.

- Size for reliable implementation, verification, and handoff in a focused session, not a file-count or token quota.
- Split unrelated outcomes; merge fragments with no meaningful result or check of their own. Keep small work as one task.
- Include each slice's tests and required review. Combined verification supplements these checks rather than postponing them all.
- Keep small prerequisite refactors within a slice. Separate preparation only for a concrete blocker or coordination need, with a bounded, behavior-preserving check.

## Explain dependencies and exceptions

For each blocking edge, name the consumed result and whether it gates starting or completion. List edit coordination separately; numbering or a preferred order is not a dependency.

Assign combined checks an owner and completion condition, using an integration task when useful. If intermediate work needs a shared integration baseline, name it and specify what can actually be checked before integration; do not promise independently releasable batches.

For broad mechanical migrations, use **expand → migrate → contract**: introduce a compatible form, migrate bounded populations with checks, then remove the old form after every migration and required rollout condition is verified. Batches depend on expand, not automatically on each other. Where batches cannot stay valid alone, declare the shared baseline and final integrate-and-verify work.

## Propose and check coverage

Present each slice with:

- **Result and boundary:** observable outcome and exclusions.
- **Acceptance:** source pointers to its subset.
- **Verification:** demonstration/check method and required review.
- **Dependencies:** start/completion gates with reasons; separate coordination needs.
- **Integration limits:** only where relevant.

Before presenting the graph as execution-ready, map every in-scope criterion to implementing slices and verification. Use a compact `Criterion → Implementation → Check → Gap` table when useful; no formal spec or permanent extra plan is required. Cross-cutting invariants may need checks in several slices.

Resolve unowned criteria or expose them as blockers; a scope reduction needs the requirements owner's decision. Recheck coverage when the breakdown changes. This is planned coverage, not evidence of completed checks. Return the proposal to manage-task for confirmation and publication under its policy.

## Example: bookmarks

Confirmed scope: users can save, remove, and list their own bookmarks; saves survive refresh, repeats do not duplicate entries, and access is isolated by user. Identity support already exists.

**Horizontal:** tables → all APIs → all UI → all tests. Early tasks cannot demonstrate the promised behavior.

**Vertical:**

| Slice | Observable result and checks | Prerequisite |
| --- | --- | --- |
| A: Save | Save through the real entry point; verify refresh, repeated saves, and unauthorized-write rejection. | Existing identity support |
| B: Remove | Remove a saved item; verify persistence and ownership enforcement. | A's saved-item path |
| C: List | Show own saved items; verify empty/populated states and user isolation. | A, not B |
| D: Integration | Check save → list → remove → refresh and cross-user access on the target baseline. | A, B, C |

A–C each include their necessary layers and checks; D adds combined evidence. Together they cover all stated acceptance, with isolation checked across A–C. Existing fixtures may remove a prerequisite: explain edges rather than copying the example mechanically. This is an illustrative proposal, not a test result; a small feature may remain one task.
