# Change templates

Use project equivalents when present. Keep sections short; state None or Not applicable where it prevents ambiguity. The change policy governs authority, links, and closure.

## spec.md

```markdown
# NNN — Title

Status: Draft
Current design: [relevant rules](...)
Related work: ...
Confirmation: Pending (later record who/where and what scope was confirmed)

## Problem and goals
User/system problem and intended improvement.

## Scope and non-goals
Included behavior and explicit boundaries.

## Behavior and acceptance
Observable scenarios, edge cases, and success conditions.
Assign stable criterion IDs only when useful for task coverage.

## Approach and trade-offs
Consequential choices and worthwhile rejected alternatives.

## System position and design impact
Owning responsibilities, affected end-to-end flows, existing rules changed,
and proposed durable rules. Link rather than duplicate current contracts.

## Verification
How acceptance will be checked, including required review and environment limits.

## Open decisions
Blocking questions, or None.

## Decision notes and follow-ups
Dated material revisions and links, only when needed.
```

## outcome.md

```markdown
# NNN — Title: Outcome

Delivery baseline: commit/PR/version, or explicitly uncommitted state

## Delivered result
What actually exists and verified implementation entry points.

## Deviations
Changes from the confirmed intent, reasons, and decision references; or None.

## Verification
| Criterion | Method | Observed result | Evidence / baseline |
| --- | --- | --- | --- |

Distinguish passed, failed, and not checked. Summarize rather than embed full logs.

## Current design updates
Updated documents, justified extraction candidates, or an explicit no-update rationale.

## Remaining work and risks
Unverified optional checks, residual risks, and explicit destinations for unfinished work.
```

## amendments/NNN-topic.md

```markdown
# Follow-up title

Status: Draft
Parent: [spec](../spec.md)

## Context and scope
Why the follow-up is needed and what changes.

## Decisions and confirmation
Behavior, trade-offs, and confirmation for material changes.

## Completion conditions and verification plan
What must be true before this follow-up is complete.

## Result and evidence
Fill after execution; include deviations, design updates, and remaining work.
```
