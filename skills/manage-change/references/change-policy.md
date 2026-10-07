# Change policy

## Record threshold

Create or update a record when the work introduces a significant user capability or materially changes behavior; establishes or changes a durable contract, lifecycle, responsibility, or data owner; involves a consequential non-obvious trade-off; carries significant migration, deletion, security, or reversibility risk; or reveals a root cause whose resulting constraint must guide future changes. Honor explicit user requests to record work.

Mechanical edits, routine upgrades, fixes that simply restore an already-defined rule, test additions, audits, and pure knowledge synchronization normally need no new record. Reclassify if investigation exposes one of the triggers above. Duration, line count, and file count are not independent reasons to record.

For ambiguous work ask: what intent, trade-off, or delivery boundary would be lost without a record, and is it already recorded elsewhere? Ask the user about a specific unresolved impact rather than generating precautionary documentation.

## Locations and identity

Follow existing project conventions. Otherwise use `docs/changes/NNN-kebab-slug/` with `spec.md` and, at closure, `outcome.md`. Inspect existing entries before allocating the next number; recheck for collisions before creating, and coordinate concurrent writers through the project's normal mechanism.

Maintain a compact index in `docs/changes/README.md` when records exist. Avoid a second manually maintained status table: link each record, whose spec owns its status. Do not create an empty archive.

The spec is the authoritative specification for the change. Tracker issues and tasks link to it; project conventions may instead designate an existing tracker spec as authoritative. Choose one, never two synchronized full copies.

## Spec states

| State | Meaning and transition condition |
| --- | --- |
| Draft | Decisions needed for the proposed scope remain open. |
| Ready | Scope, behavior, and acceptance have been confirmed by the authorized decision-maker; blocking questions are resolved. |
| In progress | Implementation has actually started. |
| Completed | Delivered scope is reconciled, required evidence and reviews are satisfied, necessary design updates are done, and outcome plus unfinished-work disposition are recorded. |
| Cancelled | Work is intentionally stopped, with reason and disposition of partial results. |
| Superseded | A linked successor replaces this record's approach; preserve the predecessor and link both ways. |

Ordinary path: Draft → Ready → In progress → Completed. Ready may return to Draft when confirmation is invalidated. Material uncertainty during implementation is explicitly recorded and blocks affected work; status alone is not approval. Active records may be cancelled or superseded.

Completed means the confirmed final scope is settled, not that every original idea shipped. Scope reductions require explicit confirmation and visible deviations. Missing mandatory verification blocks completion unless an authorized change to requirements or risk acceptance is recorded and project policy permits it. Optional unverified checks and residual risks remain visible in the outcome.

## Revisions and history

Active specs can evolve. Use dated decision notes for consequential scope or semantic changes; Git supplies detailed textual history. Never silently weaken acceptance to fit the implementation.

Closed records remain time-bound history. Correct factual errors with an explicit dated correction. Later rule changes belong in a follow-up or successor, not a rewrite of the old intended behavior. Sensitive material may require removal and separate history-remediation procedures.

An in-frame follow-up can use `amendments/NNN-topic.md`, with scope, decisions, status, result, and evidence. A new independent objective or replacement approach gets a new change record. Link amendments from the parent spec. An amendment is not a license to skip confirmation or verification.

When knowledge is extracted, keep historical content and add a current-design pointer. Mark a decision superseded only when the decision changed, not merely because its current definition moved.

## Current design boundary

Specs may propose future rules. Current design describes confirmed rules currently applicable, with explicit version, rollout, or feature-gate limits where necessary. Pair affected design updates with implementation delivery where practical. Pure synthesis of existing approved rules does not require a new change record; choosing different behavior does.
