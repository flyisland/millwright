---
name: maintain-design
description: Maintain the current system map, responsibilities, key flows, domain rules, and contracts. Use when confirmed changes affect lasting rules, when extracting knowledge from change records, or when recovering the big picture of an existing system. Surface conflicts instead of inventing new design decisions.
---

# Maintain Design

Maintain the system's current view, not a chronological summary. Read [design policy](references/design-policy.md) for authority, extraction, history, and applicability rules.

## 1. Scope the maintenance

Choose a mode:

- **Synchronize:** update the rules and navigation affected by a specific confirmed change. Default during delivery; avoid a whole-repository survey.
- **Reconstruct:** recover the map and durable rules for a named system, module, or set of changes. Establish a code baseline and bounded scope before exploring.

Read project design conventions and existing entry points before proposing new files.

**Done when:** the scope, baseline, mode, and relevant sources are identified.

## 2. Gather and classify evidence

Inspect relevant approved specs/decisions, current design, implementation, and tests. In reconstruct mode, trace a small number of important end-to-end flows to find ownership and relationships, not just directory names.

For each candidate statement distinguish:

- confirmed intent with applicable implementation evidence;
- observed implementation whose intended status is not yet confirmed;
- proposed behavior, contradiction, or unresolved inference.

A test encodes behavior but is not by itself proof that the behavior was approved. Missing evidence belongs in an explicit question or gap.

**Done when:** each rule to publish has a known basis and applicability; conflicts are visible rather than resolved by guessing.

## 3. Select the smallest owner

Place terminology in an existing glossary; current behavior in the responsible domain/module contract; significant historical rationale in its existing change record or ADR. Create a separate ADR only when it needs independent decision management, not to duplicate the same rationale.

Use [templates](references/templates.md) when a new system map, module entry, flow, or rule document is actually needed. Locate each rule in one authoritative place and reference it elsewhere.

**Done when:** candidates have a clear owner or an explicit reason not to become durable documentation.

## 4. Update the current view

- Write a self-contained description of currently applicable rules, including meaningful edge cases and invariants.
- Update the system map only when responsibilities, ownership, dependencies, or key flows changed; otherwise update the relevant detail.
- Link implementation and verification entry points after checking them. Label proposed or historical paths instead of presenting them as existing.
- Add links to important decision sources. Preserve historical content and add a pointer back to the current rule when useful.
- Mark rollout/version/gate limits explicitly. Pending decisions stay outside the confirmed normative section.

If the work would change behavior, widen a constraint, or choose between conflicting intentions, stop that portion and hand the decision to `manage-change` for classification and confirmation. Independent factual updates may proceed.

**Done when:** readers can understand the affected current system without reconstructing it from history, and navigation reaches the rules.

## 5. Report and hand back

List changed documents, confirmed rules, unresolved questions, and verification limits. For change-driven work, return these pointers to `manage-change` for the outcome. For reconstruct work, report observations separately from approved rules; do not claim that documentation repairs implementation defects.

Use the host's skill mechanism or an explicit handoff. If a companion skill is unavailable, describe the decision needed rather than silently authorizing it.
