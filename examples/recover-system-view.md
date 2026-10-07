# Example: recover the system view

## Starting problem

The repository has many completed specs, a glossary, a few ADRs, and working code. Understanding a message's lifecycle requires reading several unrelated histories.

## Scope

Invoke maintain-design in reconstruct mode for message execution, at an identified commit. Start with sending a message, receiving completion, and recovering after reconnect. Do not attempt a full repository encyclopedia.

## Evidence classification

- A confirmed ADR assigns execution state to one module: candidate normative ownership rule.
- Current code lets an adapter write the same state: observed conflict, not a new approved architecture.
- An old spec proposed automatic retries but no delivery evidence is found: unresolved intent, not current behavior.

## Output

Create or update a concise map of responsibilities, the key execution flow, and a lifecycle contract for confirmed rules. Link implementation/tests and the relevant historical decisions.

Keep conflicts in an explicit non-normative open-questions section, with the inspected baseline. Ask the responsible decision-maker whether the conflicting implementation is a defect or the intended new rule.

## History and next work

Preserve old specs; add a pointer to the current contract instead of deleting their state models. A document's relocation does not supersede its decisions.

Pure consolidation needs no new change record. If resolving a conflict requires selecting new behavior, hand that proposal to manage-change. Any resulting repair work becomes a task; writing a map does not fix the code.
