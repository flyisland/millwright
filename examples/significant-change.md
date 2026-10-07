# Example: message retry

Illustrative workflow; acceptance examples are not claims about an existing product.

## Change record

Manual message retry introduces execution-attempt identity and duplicate-event rules. Use manage-change to create a spec and confirm those semantics before implementation.

Example acceptance scope:

- Retrying a failed message creates a new execution attempt under the same logical message.
- A delayed event from an older attempt cannot overwrite the active attempt's state.
- Manual retry does not imply automatic retry on reconnect.

The spec links existing lifecycle rules and explicitly proposes changes. It does not overwrite current design with unshipped behavior.

## Tasks, if useful

Use manage-task to propose verifiable slices:

1. Retry a failed message end to end, including attempt identity and a minimal user entry point. Verify that retry creates a new attempt, late events cannot overwrite it, and reconnect alone does not trigger retry. These invariants travel with the first usable path, not a later hardening task.
2. Verify the complete retry flow in the target reconnect/event-delivery environment, including delayed and duplicate event sequences; blocked by the first slice. This integration task supplements the slice's checks rather than postponing their first execution.

All three acceptance conditions are implemented and locally verified by task 1; task 2 supplies required target-environment evidence. This narrow example may stay as one task if the same worker can reliably execute both parts. Broader capabilities can add further behavioral slices, not separate UI/API/storage stages.

Each task links the spec and its acceptance coverage. Confirm the decomposition; use the existing tracker rather than duplicating local tickets.

## Implementation and review

Use `implement-work` or the project method for an authorized slice. Supply its acceptance subset, parent spec, current rules, and required checks. The implementer returns actual modifications, evidence, and gaps without closing tasks or changing approved semantics.

Use `review-work` or the project reviewer to assess requirements and engineering quality separately. A slice review does not report later slices as missing; whole-change review covers all confirmed scope. Fixes require fresh relevant checks and any required re-review. Missing independent review remains a gap, not a successful self-review.

For a small enough change, skip explicit tasks and return engineering evidence directly to manage-change. No Matt skill or automatic commit is needed.

## Material deviation

Suppose implementation exposes an incompatibility in attempt identity. The implementer reports evidence and alternatives. The spec remains authoritative: dropping delayed-event isolation requires an explicit scope decision, not just editing a ticket's checkbox.

## Current design

Use maintain-design to update the lifecycle contract and, if ownership changed, the system map. Link the original spec for rationale. Scope applicability to the actual rollout or gate.

## Closure

Each task closes against its own evidence. The change closes only after full acceptance coverage, required integration verification, design synchronization, and remaining-work disposition are reconciled in the outcome.

If integration fails, task completion counts do not justify marking the change Completed. Preserve the blocker and continue work.
