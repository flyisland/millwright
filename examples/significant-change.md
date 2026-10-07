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

1. Retry a failed message end to end, including attempt identity and a minimal user entry point.
2. Exercise reconnect and delayed-event behavior against that delivered retry path; blocked by the first slice.
3. Verify the complete change in the target environment and finish any required delivery checks; blocked by the implementation slices.

Each task links the spec and its acceptance coverage. Confirm the decomposition; use the existing tracker rather than duplicating local tickets.

## Material deviation

Suppose implementation exposes an incompatibility in attempt identity. The implementer reports evidence and alternatives. The spec remains authoritative: dropping delayed-event isolation requires an explicit scope decision, not just editing a ticket's checkbox.

## Current design

Use maintain-design to update the lifecycle contract and, if ownership changed, the system map. Link the original spec for rationale. Scope applicability to the actual rollout or gate.

## Closure

Each task closes against its own evidence. The change closes only after full acceptance coverage, required integration verification, design synchronization, and remaining-work disposition are reconciled in the outcome.

If integration fails, task completion counts do not justify marking the change Completed. Preserve the blocker and continue work.
