# Engineering skill collaboration

Millwright has three core lifecycle skills and two optional engineering skills. No Matt Pocock skill, tracker setup command, subagent facility, or automatic commit is required. Existing project methods can provide implementation or review instead.

## Ownership and handoffs

| Operation | Owner | Return or next owner |
| --- | --- | --- |
| Synthesize discussion, confirm or revise significant behavior | `manage-change` | Canonical spec and decision boundary |
| Split, coordinate, persist, or close execution work | `manage-task` | Tasks, acceptance subsets, and actual status |
| Implement and verify bounded work | `implement-work` | Evidence to the task owner, or directly to the change owner |
| Assess requirements and engineering quality | `review-work` | Findings to the implementer and evidence to the lifecycle owner |
| Place confirmed applicable rules and synchronize design | `maintain-design` | Current-rule pointers and unresolved conflicts |

Implementation and review do not close work. Task completion does not close a change. A review finding can reveal an implementation defect, unresolved intent, or stale documentation; send it to the relevant owner rather than automatically changing all three.

## Handoff inputs and results

Use pointers and a small delta:

- The request, canonical task, and parent spec or approved amendment when present.
- Applicable current design, approved scope, and acceptance subset.
- Completion conditions and required verification or review.
- Baseline/workspace, existing edits, actual findings, and unresolved decisions.
- Operation requested: synthesize, split, implement, review, confirm, synchronize, or close.

Return actual results, evidence, deviations, and remaining work. State which baseline tests and review cover. After fixes, obtain fresh checks or review where required. If the receiving capability is absent, report the handoff and unperformed action. Self-review is not independent approval.

## Direct use and lightweight work

A clear user request plus applicable current rules can support direct implementation or review. Do not generate a spec just to satisfy an engineering skill. Use `manage-task` when coordination or persistence is needed and `manage-change` when significant decisions need classification and confirmation.

For child-task reviews, state the acceptance subset so future slices are not falsely reported missing. Whole-change closure assesses the full confirmed scope and integration requirements. A current-state assessment needs a bounded system area and baseline, not an artificial historical diff.

## Methods absorbed from external references

Matt Pocock's skills are design references, not dependencies or commands to invoke. Millwright independently expresses selected methods under its own ownership model:

| Reference capability | Millwright placement |
| --- | --- |
| `to-spec` and focused interviewing | `manage-change` synthesis reference; drafts preserve unknowns and confirmed scope is not re-interviewed |
| `to-tickets` | `manage-task` decomposition; verifiable slices, real dependencies, bounded migration batches |
| `implement` and TDD | `implement-work`, with optional test-first methods in its verification reference |
| `code-review` | `review-work`; separate requirements and engineering axes, with no required parallel agents |
| Domain modeling | Focused terminology and responsibility checks in `manage-change` and `maintain-design` |

No separate spec-publishing or ticket-creation workflow is retained. Prototype, deep diagnosis, and other specialist skills are not shipped in this first engineering set; use project methods and add skills only when independent use warrants them. Test-first development is a method, not a requirement for every edit.

## Platform and authorization boundaries

Skills use ordinary Markdown and portable `name` and `description` frontmatter. Invocation, discovery, confirmation interfaces, and installation paths depend on the host. Companion skills are reached by name or explicit handoff, never repository-relative sibling paths.

Project/user permissions govern commits, remote writes, deployment, and destructive operations. Configuring a tracker location or invoking implementation does not itself grant these permissions. If another installed workflow conflicts, choose one clearly designated method rather than assuming a wrapper silently overrides its instructions.
