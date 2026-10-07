# Design principles

## Three views, three owners

- `manage-task` owns execution scope, dependencies, progress, and task closure.
- `manage-change` owns significant-change specs, decisions, deviations, and outcome closure.
- `maintain-design` owns the current system view and placement of durable rules.

A task can exist without a change record. A change record can be implemented without explicit tasks. Design maintenance can happen independently of delivery work.

## Authority is explicit

For work attached to a change, the spec and applicable approved amendments define the change's intended behavior. Tasks refine execution without replacing that specification. Current design defines the confirmed rules currently in force. A proposed spec may intentionally change those rules, but does not silently make a future rule current.

Code and runtime evidence establish observed behavior, not automatically intended behavior. When approved intent, current design, and implementation disagree, expose the discrepancy and obtain a decision from the responsible person; do not automatically select code or prose as correct.

Project conventions own locations, tracker mappings, approval roles, and verification requirements. Skill policies provide defaults. Surface a conflict affecting authority, safety, or closure rather than silently overriding it.

## Record selectively; verify proportionately

Recording effort follows durable decision value. Verification effort follows risk. A small fix with no new design decision may still need rigorous security review.

Conversations can hold short-lived work. Persist work when it must survive a session, wait in a queue, or transfer to another worker. Keep operational logs out of long-lived design documents.

## Separate history from current knowledge

Closed specs and outcomes preserve their time-bound meaning. Current design is updated in place. Extracting a rule transfers maintenance responsibility, not historical content: preserve the source and link the current rule.

Keep one authoritative definition of each current rule in its smallest complete ownership scope. The system map links these definitions; it does not copy them all.

## Preserve human control

Skills can propose and organize work without implicitly authorizing behavior changes, destructive actions, external publication, or commits. Use the project's existing approval and execution boundaries.

Record decisions when they are confirmed. Later reconstruction must be identified as retrospective, not described as prior approval.

## Start small

No mandatory tracker migration, framework runner, ADR directory, or task graph. Add structure when it solves a real persistence, ownership, or coordination problem. Use existing engineering tools for implementation and review.
