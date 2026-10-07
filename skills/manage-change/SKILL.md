---
name: manage-change
description: Classify significant software changes, synthesize or revise their specs, and close delivery records. Use for scope decisions, outcomes, follow-ups, cancellation, and supersession.
---

# Manage Change

Own the change record and its lifecycle, not implementation technique. Read [change policy](references/change-policy.md) for recording thresholds, authority, states, and history rules.

## 1. Locate and classify

Read project conventions, relevant current design, and any existing record. Choose with a brief reason: no formal record, update an existing record, or create one. Prior investigation is evidence, not prior approval.

For the lightweight path, pass the goal, boundaries, and verification needs to `manage-task` or ordinary execution. No separate classification report is needed.

## 2. Work in the requested phase

Read [templates](references/templates.md) only when creating or restructuring a document; reuse project equivalents.

### Plan or resume

- Read enough design and implementation to locate affected behavior and responsibilities.
- For discussion synthesis or draft clarification, use [synthesis](references/synthesis.md); update the canonical spec with the result.
- Record who confirmed which scope before marking Ready under the policy. Reuse unchanged confirmations.
- For authorized implementation, pass useful task decomposition to `manage-task`, or pass the confirmed spec directly to `implement-work`/the project method. A planning-only request stops at the spec.

### Revise during implementation

Distinguish execution detail from material requirement changes. Obtain the needed decision before affected implementation continues; safe independent work may proceed. Update the active spec and dated decision note, preserving earlier intent and deviations.

Notify `manage-task` of affected acceptance/evidence, and `maintain-design` of confirmed rule changes and their implementation status.

### Close

Compare delivery with full confirmed acceptance, not task counts. Gather verification and required review evidence using `review-work` or the project method. Reconcile unfinished tasks through `manage-task` and affected current rules through `maintain-design`.

Write the outcome and apply the policy's Completed gate. If it is unmet, identify the missing check, decision, design update, or unfinished-work disposition instead of closing.

### Follow up, cancel, or supersede

Apply the policy's amendment/successor and history rules. Record disposition and links; send affected task pointers to `manage-task` for execution reconciliation. Track an active follow-up separately from the parent's historical result.

## 3. Return the record state

Report the canonical path, status, decisions/blockers, and next action. Use host mechanisms or explicit handoffs; report unavailable companion operations as unperformed.

Creating or updating remote records, committing, publishing, and destructive actions require project/user authorization. A tracker location is not write permission; prepare proposed content and request authorization when missing.
