# Integrate engineering skills

Millwright owns knowledge and work lifecycles, not implementation technique. Existing skills, manual development, and team workflows can provide the engineering work.

## Mapping from Matt Pocock's skills

These mappings describe concepts, not a runtime dependency or a claim that every installed version has identical behavior.

| Existing capability | Use with Millwright | Adjustment |
| --- | --- | --- |
| `grill-with-docs` / interviewing | Clarify a task or spec | Confirmed change decisions go into the canonical spec; terms into the existing glossary. |
| `to-spec` | Synthesize discussed requirements | Route its output into the canonical change spec, or let manage-change do synthesis. Do not publish a second authoritative spec. |
| `to-tickets` | Produce verifiable slices and dependencies | Use manage-task's tracker, parent links, and completion rules. |
| `implement` / `tdd` | Execute agreed work and provide evidence | Return material requirement changes for confirmation. Respect project commit policy, not a hard-coded automatic commit. |
| `implement-spec` | Optional parallel execution | Keep one authoritative task graph; communicate actual integration and verification state. |
| `code-review` | Review requirements and standards separately | Read task acceptance plus parent spec when present; read applicable current design alongside coding standards. |
| `domain-modeling` | Sharpen terminology and decision reasoning | Keep glossary, current rules, and historical rationale distinct; avoid duplicate ADRs. |
| `prototype` | Resolve uncertain interactions or state models | Save confirmed findings into the spec; a throwaway demo need not become production code or permanent documentation. |
| `diagnosing-bugs` | Investigate before fixing | Reclassify the work if diagnosis reveals a new durable contract or consequential decision. |
| `retro` | Improve navigation, checks, and tooling | Keep environment improvement separate from current product design maintenance. |

A read-only plugin may contain conflicting instructions. Do not assume a vague project note overrides them reliably: choose an adapted local skill or avoid that overlapping command. Millwright does not invoke user-only commands behind the user's back.

## Handoff contract

Use pointers and a small delta:

- Canonical task and parent spec, if any.
- Applicable current design and approved scope.
- Completion conditions and required verification.
- Baseline/workspace, actual findings, unresolved decisions.
- Operation requested: implement, review, confirm, synchronize, or close.

Return actual results, evidence, deviations, and remaining work. A tool's success code alone is not proof of acceptance. If the receiving capability is absent, report the required handoff instead of claiming completion.

## Review without a formal spec

Standalone tasks still have requirements: the user request, task completion conditions, and relevant current rules. Review against those. Ask for missing acceptance conditions rather than generating a formal change record solely to satisfy a review tool.

For child-task reviews, state the acceptance subset so future slices are not falsely reported missing. Before closing the entire change, assess the full confirmed scope and integration requirements.

## Platform neutrality

Skills use ordinary Markdown plus `name` and `description` frontmatter. Actual invocation, tools, confirmation interfaces, and installation paths are host-specific. No particular Skill API, browser, subagent facility, or issue-tracker integration is assumed.
