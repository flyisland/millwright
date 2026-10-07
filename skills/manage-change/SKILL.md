---
name: manage-change
description: Manage specs, decisions, and outcomes for significant software changes. Use when deciding whether work needs a durable change record, planning or revising such a change, closing delivery, or handling follow-ups and supersession. Not a general task tracker.
---

# Manage Change

Own the significant change's record, not its implementation method. A change record preserves intent, important decisions, and actual delivery; a spec is its authoritative change specification.

## 1. Locate and classify

Read the project's documentation instructions, relevant current design, and any existing record for this work. Follow [change policy](references/change-policy.md) for recording thresholds, authority, and lifecycle rules.

Choose one result with a brief reason: no formal record, update an existing record, or create a new record. Investigation already performed is evidence, not evidence of prior approval.

If no record is warranted, hand the goal, boundaries, and verification needs to `manage-task` or the project's ordinary execution workflow. Do not write a report about why no record was created.

**Done when:** the record and target phase are identified, or the lightweight path is explicit.

## 2. Enter the appropriate phase

Load [templates](references/templates.md) only when creating or restructuring a document. Reuse the project's existing equivalents.

### Plan or resume

- Read relevant design and enough implementation to identify affected responsibilities and behavior.
- Clarify unresolved goals, scope, edge cases, and validation. Use existing interviewing or prototyping methods when useful.
- Create or update the spec. Keep execution steps out of the behavioral contract.
- Record confirmation by the user or authorized project decision-maker before marking Ready. Ask only about decisions that remain unresolved; do not ask to reapprove unchanged, already-confirmed scope.
- If explicit tasks are useful, hand the spec pointer, acceptance scope, and dependencies to `manage-task`.

**Done when:** a coherent scope is confirmed and Ready, or a Draft names the decisions blocking implementation.

### Revise during implementation

- Distinguish execution detail from changes to scope, public behavior, ownership, safety, or acceptance.
- For a material change, record the proposal and obtain the required decision before continuing affected implementation. Unaffected work may continue if safe.
- Update the active spec and a short dated decision note; keep the original intent and eventual deviation recoverable.
- Notify affected tasks. When durable rules change, hand their references and implementation status to `maintain-design`.

**Done when:** the change is confirmed and reflected in affected inputs, or blocked pending a specific decision.

### Close

- Compare the actual delivery against the full acceptance scope, not just task completion counts.
- Gather actual verification results and known gaps. Reference evidence; do not invent test runs or approval.
- Reconcile linked tasks: unfinished work needs explicit cancellation, deferral, or a continuing owner/location.
- Use `maintain-design` for affected current rules. Preserve pending or gated applicability instead of describing unshipped behavior as current.
- Write the outcome, including deviations and remaining work. Apply the policy's closure gate before marking Completed.

**Done when:** the result is honestly closed, or the missing verification/decision/design update is explicitly blocking closure.

### Follow up, cancel, or supersede

Use the policy to choose an amendment versus a new record. Preserve closed history, link successors, and explain cancellation or replacement. An active follow-up has its own visible pending work; the old Completed status is not proof that the follow-up shipped.

**Done when:** the disposition, affected work, and next authoritative location are clear.

## Handoffs and output

Report the record path, status, important decisions or blockers, and next action. Prefer context pointers over duplicated specs. A companion skill may be reached through the host's mechanism or an explicit handoff; if unavailable, state what remains unperformed. Do not claim the whole workflow ran because documentation was written.
