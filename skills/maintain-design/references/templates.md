# Current design templates

Create only the document a reader needs. These are prompts, not mandatory section counts. Combine short map and module entries where appropriate.

## System map

```markdown
# System design

## Purpose and boundaries
What the system does and deliberately does not own.

## Responsibilities and ownership
Major domains/modules, their responsibilities, and owned state/data.

## Relationships and key flows
How the parts collaborate. Link the few important end-to-end flows.

## Design navigation
Links to authoritative module rules, glossary, and relevant external contracts.

## Open questions
Explicitly non-normative observations or contradictions, with inspected baseline.
```

## Module or domain entry

```markdown
# Domain/module

## Responsibility and boundary
Owned behavior and what belongs elsewhere.

## Contracts and dependencies
Public collaboration points, state ownership, and links to detailed rules.

## Implementation and verification entry points
Verified locations, not a complete inventory of internal files.

## Decision sources
Key change records or ADRs explaining consequential choices.
```

## Lifecycle or algorithm

```markdown
# Rule title

Applicability: version / feature gate / current confirmed scope

## Semantics
State meanings or algorithm inputs/outputs and their business meaning.

## Rules
Transitions with guards and effects, or ordering and conflict-resolution steps.

## Invariants and edge cases
Invalid, duplicate, delayed, failing, or recovering operations as relevant.

## Examples and verification
Representative cases; implementation and tests that enforce the rule.

## Decision sources
Important historical reasons and sources.
```

## End-to-end flow

```markdown
# Flow title

## Trigger and intended result

## Responsibility sequence
For each meaningful step: owner, input/event, next owner, state written.

## Failure and recovery boundaries

## Related contracts and verification
```

Do not fill missing semantics with plausible defaults. Keep unknown behavior as a question pending confirmation.
