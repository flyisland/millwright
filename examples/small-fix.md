# Example: a small focus fix

Illustrative scenario, not a report of executed tests.

## Request

Escape closes search but fails to return keyboard focus to the message input. The existing interaction contract already requires focus restoration.

## Classification

Use manage-task. This restores a defined behavior without a new trade-off; no formal change record is needed. Verification effort still follows regression risk.

## Conversational brief

- Goal: restore focus after Escape closes search.
- Boundary: preserve search results and shortcut precedence.
- Completion: regression test for focus behavior and the project's required checks.

No issue is needed if this is completed in the current session. If the environment prevents verification and work must continue later, persist the task with the blocker and unblock condition.

## Execution and closure

Use `implement-work` or the existing implementation and testing workflow. Return actual modifications, the checked baseline, and verification gaps. Use `review-work` or the project's review method if required. These reports are evidence, not status changes: manage-task marks Done only after required verification and review are satisfied, disclosing optional unperformed device checks separately.

Expected artifacts: code/tests and ordinary commit or PR history according to project policy. No spec, outcome, or architecture document is created.

## Escalation variant

Investigation reveals ambiguous ownership between two focus managers. If fixing it requires choosing a new responsibility contract, pause that decision and use manage-change to classify and confirm the expanded work. Preserve completed investigation as evidence, not retroactive approval.
