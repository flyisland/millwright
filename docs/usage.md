# Using Millwright

Use Millwright **inside the project you want to develop**, not inside the Millwright source repository. Install the three complete core skill directories, optionally add `implement-work` and `review-work`, then follow [project adoption](adoption.md) to identify existing trackers, specifications, and design documents.

The prompts below use ordinary language. A host may also expose slash commands, but their syntax and automatic skill discovery vary. Naming a skill explicitly is a useful way to make your intention clear.

## Pick the starting point

| What you need now | Start with |
| --- | --- |
| Fix something small, resume work, or organize execution | `manage-task` |
| Define or revise an important change, or close its delivery record | `manage-change` |
| Update lasting rules or understand how the current system fits together | `maintain-design` |
| Implement a clear request, task, or confirmed spec | `implement-work` (optional) |
| Review a change or bounded current system area | `review-work` (optional) |

You do not need to run all five for every request. A skill may hand work to another capability when needed; it is not an automatic workflow engine. Use the optional engineering skills or your project's existing implementation, testing, and review methods. No Matt skills are needed.

The file locations below are defaults for projects without existing conventions. Replace example paths with your project's real paths.

## First use in an existing project

**When:** the skills are installed, but the project has not adopted their conventions.

**Prompt:**

```text
Use Millwright in this project. First identify our existing task tracker,
specification location, and architecture/design documentation. Reuse them;
do not migrate or duplicate them. Tell me which conventions are missing
and ask about decisions that need my input before configuring anything.
```

**Expected result:** a short mapping of existing conventions and any unresolved setup decisions. Installation or discovery alone should not generate task cards, specs, or an architecture archive. See [Adoption](adoption.md) for project navigation and optional defaults.

## 1. Complete a small fix

**When:** the desired behavior is already clear and the work probably needs no new long-lived decision.

**Prompt:**

```text
Use manage-task to fix this issue: closing search with Escape does not return
focus to the message input. Check the existing behavior contract, state the
scope and verification method, then implement and report the actual result.
If the fix requires a new design decision, explain that before expanding scope.
```

**Expected result:** a brief goal, boundaries, implementation, actual verification, and remaining limits. A simple restoration of an existing rule should not require a formal change record.

**Files:** usually code/tests only, with ordinary commit or PR history according to project policy. A task that can finish in this session needs no separate task file. See the [small fix example](../examples/small-fix.md).

## 2. Hand off or resume a task

**When:** work must survive this conversation or transfer beyond an immediately supervised delegation. See `manage-task` for persistence policy.

**Handoff prompt:**

```text
Use manage-task to prepare a persistent handoff for this work in our existing
tracker. Capture the current branch/workspace, completed work, actual checks,
remaining work, blockers, and the next action. Do not mark unfinished work Done.
```

**Resume prompt:**

```text
Use manage-task to resume task <task reference>.
Inspect the current code and recorded evidence before repeating work or choosing
the next step. Tell me if the task's assumptions no longer match the project.
```

**Expected result:** enough verified context to resume without replaying the whole chat, and a status consistent with actual progress.

**Files:** the canonical tracker is updated. Without a tracker, a durable local task can use `docs/tasks/NNN-slug.md`. Avoid maintaining both a remote task and a competing local copy.

## 3. Plan an important change without implementing it

**When:** you want a significant capability, behavior change, or consequential design decision clarified first.

**Prompt:**

```text
Use manage-change to plan manual message retry. Read the current message and
execution model first. Help me resolve behavior, edge cases, non-goals, and
acceptance criteria, then prepare the spec. This round is planning only:
do not start implementation. Keep unresolved decisions explicit.
```

**Expected result:** a draft spec, focused questions where needed, and an identified design impact. It becomes Ready only after the appropriate scope confirmation, not merely because the document was generated.

**Files:** normally `docs/changes/NNN-message-retry/spec.md` and its index entry, or an update to an existing relevant record. No second full spec should be published to the tracker.

## 4. Turn an approved spec into execution work

**When:** the spec is confirmed and the work needs explicit slices or multiple sessions.

**Prompt:**

```text
Use manage-task to break <spec path> into independently verifiable execution
slices. Show me the proposed results and real blocking dependencies first.
After I confirm the breakdown, create the tasks in our existing tracker.
Each task should point to the parent spec and its acceptance coverage.
```

**Expected result:** a manageable task graph, not separate database/backend/UI tasks that only become useful when all are finished. Splitting must not redefine the parent requirements.

**Files:** tracker tasks or local task files as needed. A short important change can be implemented directly from its spec without a redundant task card.

**Continue prompt:**

```text
Continue task <task reference> using our normal implementation and testing
workflow. Respect its parent spec and completion conditions. Bring material
behavior or scope changes back for confirmation before implementing them.
```

## 5. Handle a material deviation

**When:** investigation or implementation reveals that the approved plan needs to change.

**Prompt:**

```text
Use manage-change to assess this deviation in <spec path>: the planned retry
behavior cannot currently prevent duplicate execution. Explain the evidence,
impact, and options. Do not remove or weaken acceptance criteria just to match
the implementation. Ask for the necessary scope decision first.
```

**Expected result:** a clear distinction between implementation detail and a change to promised behavior. Confirmed revisions update the active spec and affected execution inputs; unresolved decisions block the affected work.

**Files:** the existing spec and relevant task records may change. A replacement approach may warrant a successor record rather than rewriting closed history.

## 6. Synchronize current design after a change

**When:** confirmed work changes a lasting rule, contract, responsibility, or key flow.

**Prompt:**

```text
Use maintain-design to synchronize the design affected by <change reference>.
Focus on execution-attempt identity, late-event handling, and state ownership.
Check the confirmed decisions against implementation and tests. Update only
the affected current rules and navigation, not a full repository survey.
Preserve historical records and label any rollout or feature-gate limits.
```

**Expected result:** current rules that can be understood without assembling historical specs, with important source and verification links. Unresolved contradictions are exposed rather than silently resolved.

**Files:** existing design documents where possible; otherwise the needed documents under `docs/design/`. The system map changes only if its responsibilities or relationships need updating.

## 7. Close an important change

**When:** implementation appears complete and you want a reliable delivery conclusion.

**Prompt:**

```text
Use manage-change to assess whether <change reference> can close. Compare actual
delivery with the full confirmed spec, inspect verification evidence, reconcile
unfinished tasks, and check necessary current-design updates. Write the outcome.
Do not close the change merely because every task is marked Done.
```

**Expected result:** an honest outcome and either a justified Completed status or specific blockers. Missing required verification remains a blocker, not a successful result.

**Files:** normally `outcome.md` beside the spec, plus the appropriate spec status update. The outcome links design updates and records deviations, evidence, and remaining work.

## 8. Recover the big picture of an existing system

**When:** specs and code have accumulated, but you can no longer easily explain how the whole system works.

**Prompt:**

```text
Use maintain-design to reconstruct the current system view. Start with message
submission, execution-result delivery, and reconnect recovery at the current
code baseline. Separate confirmed design, observed implementation, and unresolved
inferences. First show me responsibilities, ownership, and conflicts; after we
resolve the necessary questions, write a concise map and only the needed details.
Do not backfill invented history or treat every current implementation choice
as an approved architectural constraint.
```

**Expected result:** a navigable map and a small set of meaningful flow or contract documents. Findings may expose work that still needs a decision or implementation; documenting it does not fix it.

**Files:** current design and navigation, not necessarily a new change record. See [recovering the system view](../examples/recover-system-view.md).

## 9. Implement bounded work directly

**When:** the request or spec is clear and you want implementation, not another planning pass.

```text
Use implement-work for <request, task, or confirmed spec>. Read the applicable
current design and completion conditions. Preserve existing workspace changes,
implement this acceptance subset, and run the required checks. Return actual
results and remaining gaps; do not commit or close the task/change. Ask before
implementing material behavior or acceptance changes.
```

**Expected result:** implementation and baseline-specific verification evidence. Test-first methods are available where useful, not forced on every edit. Required review uses `review-work` or the project method. Missing checks or reviews remain explicit gaps; core owners determine closure. A small clear request needs no task card or spec merely to use this skill.

When implementation is delegated, `implement-work` loads its optional delegation reference for assignment, context reuse, continuation, and the check/fix loop. Host guidance supplies agent operations; direct implementation needs no subagent setup or extra tracking.

## 10. Review without changing the implementation

**When:** you want a branch, working-tree, or bounded current-state assessment.

```text
Use review-work to review <branch comparison, uncommitted changes, or module>.
State the baseline and scope. Review requirements against <request/task/spec>
and engineering quality against project standards and current design. Keep the
two axes separate and distinguish defects, risks, and questions. Report checks
actually run and limitations. Do not modify code or close work.
```

**Expected result:** actionable, evidence-backed findings and verification limits. A current-state review needs no invented diff; a working-tree review includes relevant untracked files. No formal spec or parallel subagents are required. A self-review is labelled and does not substitute for independent approval.

## Combining the skills

For an important change, the typical collaboration is:

| Moment | Responsible capability |
| --- | --- |
| Clarify and confirm behavior | `manage-change`, with interviewing/prototyping as useful |
| Organize execution if needed | `manage-task` |
| Implement and verify | `implement-work` or the project implementation method |
| Review requirements and engineering quality | `review-work` or the project review method |
| Reconsider material deviations | `manage-change` |
| Synchronize lasting rules | `maintain-design` |
| Reconcile delivery and close | `manage-change` |

You can express this intent once:

```text
Use Millwright for this feature. Begin by clarifying and confirming the spec.
Then organize execution only as needed. Ask before material scope changes.
At delivery, synchronize affected current design and complete the outcome.
For now, do planning only; do not implement yet.
```

This is an instruction to collaborate, not a guarantee of automatic orchestration. Host capabilities determine whether a companion skill is invoked directly or reached through an explicit handoff. Missing capabilities and unperformed steps should be reported.

## Control the phase

Short boundaries help preserve your control:

- **Planning only:** clarify and prepare the spec; stop before implementation.
- **Continue execution:** resume a named task or confirmed spec.
- **Review only:** inspect requirements and evidence without modifying implementation.
- **Close out:** reconcile actual results; do not silently repair or redefine missing requirements.

These boundaries do not authorize commits, remote publication, deployment, or destructive operations. Those follow your project's existing permissions.

## A useful first trial

1. Try a small fix to see whether task management stays lightweight.
2. Reconstruct one bounded system area to see whether design maintenance restores useful context.
3. Run the next important change from spec to outcome to test the full lifecycle.

These are suggested trials, not proof that every model or host will follow the skills reliably. The repository's [behavior scenarios](../tests/scenarios.md) provide additional evaluation cases; structural checks alone do not validate agent behavior.
