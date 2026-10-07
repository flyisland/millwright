---
name: review-work
description: Review branch, commit, working-tree, or bounded current-state work against requirements and engineering standards. Return evidence-backed findings without modifying implementation or closing work.
---

# Review Work

## 1. Pin the target

| Request | Establish |
| --- | --- |
| Branch or commit comparison | Resolved refs and comparison semantics: changes since divergence and differences between exact snapshots are not the same. |
| Working-tree changes | Base commit, staged/unstaged changes, and relevant untracked files; git diff alone is incomplete. |
| Current project or module | Bounded system area and inspected baseline; no historical diff required. |

State reasonable assumptions; ask when ambiguity materially changes scope. Report invalid refs or an empty requested diff without silently widening the review.

## 2. Identify the review basis

Read the request, task conditions, parent spec/amendments when present, relevant current design, and project engineering standards. A standalone request is a valid requirement source; no tracker or formal spec is necessary.

For a child task, assess its acceptance subset, not future slices. Whole-change review covers full confirmed scope and integration requirements. Expose missing or conflicting intent as specific questions; continue independent checks without inventing requirements.

## 3. Assess two axes

Read [review policy](references/review-policy.md) for finding quality, priority, and reporting.

- **Requirements:** behavior, omissions, unintended additions, edge cases, and verification coverage against the requested scope.
- **Engineering:** correctness, safety, maintainability, and applicable standards/contracts.

Trace relevant callers, data, tests, and failure paths, including enough unchanged context to establish impact. For current-state review, trace representative flows. Run safe, authorized checks where useful. Sequential review is sufficient; optional parallel reviewers need the same target and sources, and their findings need verification.

Keep review read-only: return findings rather than auto-fixing implementation, committing, or changing remote records. Checks affecting durable data or external services require appropriate authorization.

## 4. Report and hand back

Use the policy's report structure. Return actionable defects to `implement-work` or the implementer, disputed intent to `manage-change`, task evidence to `manage-task`, and current-rule discrepancies to `maintain-design`. These are explicit handoffs, not permission to rewrite requirements, waive checks, or close work. Report missing companions as unperformed operations.
