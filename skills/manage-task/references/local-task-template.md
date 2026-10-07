# Local task template

Use only when a task needs to survive the conversation and the project has no existing tracker convention. Default location: `docs/tasks/NNN-slug.md`. An index is optional; the task file owns its status.

```markdown
# NNN — Task title

Status: Todo
Parent change: None, or a spec link
Owner: If assigned
Blocked by: None, or actual task/condition references

## Goal and boundaries
What this task delivers and what remains unchanged.

## Completion conditions
- Observable result, linked to parent acceptance where applicable.
- How to demonstrate or check this result, plus required review.
- Shared integration check and owner, if this task alone cannot establish acceptance.

## Progress and handoff
Only facts needed to continue: current baseline/workspace, completed work,
remaining work, blocker and unblock condition. Omit when unnecessary.

## Result
Actual modifications or findings, evidence and limits; pending until execution.
```

Remove irrelevant fields instead of filling them with invented information. Do not store credentials, full tool transcripts, or design rules that belong in current design.
