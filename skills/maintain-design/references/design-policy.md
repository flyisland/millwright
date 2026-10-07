# Current design policy

## Durable knowledge

Record information future work must reliably know: object identity, lifecycle and transitions, business algorithms, invariants, responsibility boundaries, data ownership, public contracts, consistency/recovery behavior, and important cross-module relationships.

Do not promote a local implementation choice solely because it is complex or appears more than once. Ask whether alternate implementations could preserve the same promised behavior. Record implementation constraints only when their rationale matters, such as an approved performance or compatibility requirement.

A first occurrence can warrant documentation; repetition is not required for a safety invariant. Conversely, repetition alone does not authorize a global rule.

## Location and authority

Reuse existing design, architecture, contract, glossary, and ADR locations. Otherwise start at `docs/design/README.md`, then create the smallest needed domain/module documents lazily. A map may live in that README until a separate overview earns its existence.

The map explains system purpose, boundaries, responsibility and data ownership, major relationships, and routes to details. It is not a file tree. Key flows connect responsibilities across the system. Module rules supply deeper semantics.

Current design is a maintained statement of confirmed applicable intent. Code describes observed implementation; historical records explain time-bound intent and rationale. None automatically resolves contradictions among them. Publish unresolved observations as explicitly non-normative findings, with their baseline and open question, not as confirmed contracts.

## Synchronization and applicability

Changes to existing contracts require corresponding design synchronization as part of delivery, not an extraction candidate deferred indefinitely. New immature generalizations may remain candidates with a reason. Purely factual consolidation of established rules needs no new change record.

An approved future spec is not necessarily shipped. State version, feature gate, rollout, or deployment limits when needed. Do not claim behavior applies to all users just because code exists on a branch.

For states, cover meaning, valid transitions, guards, side effects, invalid/repeated/late events, terminality, and recovery where relevant. A diagram supports these semantics but does not replace them.

For algorithms, cover input/output meaning, ordering, conflict resolution, boundary cases, and invariants. Avoid copying implementation line by line.

## Extraction and retirement

Preserve historical specs and outcomes after extraction. Add a current-rule pointer without rewriting old decisions to match the present. Link important sources from current design, not every patch. A source link to history explains rationale; it must not be required to assemble the current rule.

Update current documents in place. When a rule is retired, remove or clearly retire its current definition, update inbound navigation, and retain rationale in the relevant history. Supersession means a decision changed, not that a paragraph moved.

## Evidence and completion

Verify current implementation/test links. Historical paths may be retained with a commit or explicit historical label. Proposed paths are marked proposed.

Maintenance is complete when the affected current view is readable independently, has one owner per rule, is reachable from navigation, distinguishes evidence from inference, and exposes all material conflicts. A discovered implementation defect still needs execution work; documenting it is not fixing it.
