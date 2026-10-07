---
name: maintain-design
description: Synchronize lasting rules after confirmed changes or reconstruct a bounded system view. Maintain maps, responsibilities, flows, and contracts while exposing unresolved intent and implementation conflicts.
---

# Maintain Design

Own the current system view and placement of durable rules. Read [design policy](references/design-policy.md) for authority, applicability, extraction, retirement, and completion requirements.

## 1. Bound the maintenance

Choose **synchronize** for rules/navigation affected by a confirmed change, or **reconstruct** for recovering a named system or module. Establish the baseline, sources, and existing documentation entry points before proposing files. Synchronization is not a whole-repository survey.

## 2. Classify candidate knowledge

Inspect relevant approved decisions, current design, implementation, and tests. Engineering reports are source pointers to verify against their baseline. In reconstruct mode, trace representative end-to-end flows to identify responsibilities and relationships.

Separate:

- confirmed intent with applicable implementation evidence;
- observed behavior without confirmed intended status;
- proposals, contradictions, and unresolved inference.

Publish under the policy's authority rules. If a portion requires choosing behavior or resolving conflicting intentions, pause it and reach `manage-change` for classification and confirmation; independent factual updates may continue.

## 3. Locate and update the rule

Place terminology in the existing glossary, current behavior in its responsible domain/module contract, and historical rationale in its change record or ADR. Use a separate ADR only when independent decision management is warranted.

Check identity and ownership language against real flows; use concrete edge cases to expose unresolved meanings rather than settling them through a glossary edit.

Update the smallest complete rule and its navigation. Change the system map only when responsibilities, ownership, dependencies, or key flows change. Apply the policy's history, applicability, and link-verification rules. Read [templates](references/templates.md) only when a new document is needed.

**Complete when:** the policy's completion requirements hold for the affected view, with material conflicts explicitly exposed.

## 4. Return the maintenance result

Report changed documents, confirmed rules, open questions, and verification limits. For change-driven work, return these pointers to `manage-change`. Route implementation repairs to `manage-task` or the execution owner; this maintenance result does not close repair work.

Use host mechanisms or explicit handoffs. Report unavailable companion operations as unperformed.
