# Using Millwright

Use Millwright **inside the project you want to develop**, not inside the Millwright source repository. Install the three complete core skill directories, optionally add `implement-work` and `review-work`, then follow [project adoption](adoption.md) to identify existing trackers, specifications, and design documents.

These examples express intent, not a required invocation format. State the goal and any phase or permission boundary; the skills supply the method. When context is clear, a short request such as “Break this spec into tasks” is enough. In a new or ambiguous context, include the relevant path or reference.

Naming a skill is optional when the host supports automatic discovery; name it explicitly when routing needs help. Slash-command syntax and discovery vary by host. The expected results below describe skill responsibilities, not instructions you must repeat.

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
Help me adopt Millwright in this project. First inspect our existing conventions.
```

**Expected result:** a short mapping of existing conventions and any unresolved setup decisions. Installation or discovery alone should not generate task cards, specs, or an architecture archive. See [Adoption](adoption.md) for project navigation and optional defaults.

## 1. Complete a small fix

**When:** the desired behavior is already clear and the work probably needs no new long-lived decision.

**Prompt:**

```text
Fix this: closing search with Escape should return focus to the message input.
```

**Expected result:** a brief goal, boundaries, implementation, actual verification, and remaining limits. A simple restoration of an existing rule should not require a formal change record.

**Files:** usually code/tests only, with ordinary commit or PR history according to project policy. A task that can finish in this session needs no separate task file. See the [small fix example](../examples/small-fix.md).

## 2. Hand off or resume a task

**When:** work must survive this conversation or transfer beyond an immediately supervised delegation. See `manage-task` for persistence policy.

**Handoff prompt:**

```text
Prepare this task for handoff to another session.
```

**Resume prompt:**

```text
Resume <task reference>.
```

**Expected result:** enough verified context to resume without replaying the whole chat, and a status consistent with actual progress.

**Files:** update the canonical tracker. Without a tracker, use Git-ignored `.tasks/NNN-slug.md` for local recovery, not a competing copy of a remote task. Follow [task policy](../skills/manage-task/references/task-policy.md) for cross-workspace transfer and post-closure cleanup.

## 3. Plan an important change without implementing it

**When:** you want a significant capability, behavior change, or consequential design decision clarified first.

**Prompt:**

```text
Plan manual message retry and draft a spec. No implementation yet.
```

**Expected result:** a draft spec, focused questions where needed, and an identified design impact. It becomes Ready only after the appropriate scope confirmation, not merely because the document was generated.

**Files:** normally `docs/changes/NNN-message-retry/spec.md` and its index entry, or an update to an existing relevant record. No second full spec should be published to the tracker.

## 4. Turn an approved spec into execution work

**When:** the spec is confirmed and the work needs explicit slices or multiple sessions.

**Prompt:**

```text
Break this spec into tasks. Show me the proposal before creating them.
```

**Expected result:** `manage-task` proposes verifiable slices, acceptance coverage, and real dependencies, then publishes under the project’s confirmation and write permissions. Splitting preserves the parent requirements; a confirmed spec does not itself authorize implementation.

If the spec is not already clear from context, provide its path. To accept the proposal and authorize local task creation, say: “Create the tasks as proposed.”

**Files:** tracker tasks or local task files as needed. A short important change can be implemented directly from its spec without a redundant task card.

**To authorize implementation instead:**

```text
Start implementing this spec; split into tasks if needed.
```

## 5. Handle a material deviation

**When:** investigation or implementation reveals that the approved plan needs to change.

**Prompt:**

```text
The planned retry behavior cannot prevent duplicate execution. Assess the impact on this spec.
```

**Expected result:** a clear distinction between implementation detail and a change to promised behavior. Confirmed revisions update the active spec and affected execution inputs; unresolved decisions block the affected work.

**Files:** the existing spec and relevant task records may change. A replacement approach may warrant a successor record rather than rewriting closed history.

## 6. Synchronize current design after a change

**When:** confirmed work changes a lasting rule, contract, responsibility, or key flow.

**Prompt:**

```text
Synchronize the current design for <change reference>.
```

**Expected result:** current rules that can be understood without assembling historical specs, with important source and verification links. Unresolved contradictions are exposed rather than silently resolved.

**Files:** existing design documents where possible; otherwise the needed documents under `docs/design/`. The system map changes only if its responsibilities or relationships need updating.

## 7. Close an important change

**When:** implementation appears complete and you want a reliable delivery conclusion.

**Prompt:**

```text
Close <change reference> if its completion conditions are satisfied.
```

**Expected result:** an honest outcome and either a justified Completed status or specific blockers. Missing required verification remains a blocker, not a successful result.

**Files:** normally `outcome.md` beside the spec, plus the appropriate spec status update. The outcome links design updates and records deviations, evidence, and remaining work.

## 8. Recover the big picture of an existing system

**When:** specs and code have accumulated, but you can no longer easily explain how the whole system works.

**Prompt:**

```text
Map the current messaging system, focusing on submission, result delivery, and reconnect recovery.
```

**Expected result:** a navigable map and a small set of meaningful flow or contract documents. Findings may expose work that still needs a decision or implementation; documenting it does not fix it.

**Files:** current design and navigation, not necessarily a new change record. See [recovering the system view](../examples/recover-system-view.md).

## 9. Implement bounded work directly

**When:** the request or spec is clear and you want implementation, not another planning pass.

```text
Implement <request, task, or confirmed spec>.
```

**Expected result:** implementation and baseline-specific verification evidence. Test-first methods are available where useful, not forced on every edit. Required review uses `review-work` or the project method. Missing checks or reviews remain explicit gaps; core owners determine closure. A small clear request needs no task card or spec merely to use this skill.

When implementation is delegated, `implement-work` loads its optional delegation reference for assignment, context reuse, continuation, and the check/fix loop. Host guidance supplies agent operations; direct implementation needs no subagent setup or extra tracking.

## 10. Review without changing the implementation

**When:** you want a branch, working-tree, or bounded current-state assessment.

```text
Review <branch comparison, uncommitted changes, or module> against <request or spec>. Do not make changes.
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

Express the current phase without restating the workflow:

```text
Plan this feature first. No implementation yet.
```

After confirming the spec, say “Start implementing it” when ready. Skills supply the handoffs within the authorized scope; they do not turn planning approval into execution permission.

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
