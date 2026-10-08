# Synthesize and clarify a spec

Use for existing discussions or draft gaps. The change policy owns confirmation and status; the templates supply document structure.

## Separate decisions from discussion

Classify source material as confirmed decisions, proposals, observations, or unanswered questions. Check factual assumptions against current design and relevant implementation; code can expose a contradiction without deciding intended behavior.

Synthesize the problem, behavior, boundaries, affected responsibilities, consequential choices, and acceptance. Retain meaningful rejected alternatives, not a transcript or a quota of user stories. Keep execution sequencing in tasks.

## Resolve only relevant unknowns

For synthesis-only requests, return a draft with explicit gaps. For clarification, investigate discoverable facts first, then ask focused decision questions with options and consequences. Group independent questions; defer those dependent on unsettled answers. Reuse confirmed scope and verification decisions.

Use project terminology and concrete counterexamples to expose ambiguous identity, ownership, or lifecycle semantics. A terminology agreement is not approval of new behavior. Send confirmed durable terms/rules to `maintain-design` for placement; proposals remain in the spec.

## Preserve usable investigation results

When implementation depends on an investigation result, retain the smallest permitted usable artifact or a reproducible retrieval method, with source, scope, and access prerequisites. Aggregate counts or anonymous examples may support a conclusion without providing the identifiers or contracts needed to implement it. Link existing evidence rather than repeating the investigation or creating a report by default. If safe retention is not possible, expose the remaining retrieval or authorization prerequisite; do not invent the missing details or preserve sensitive data merely for reuse.

## Make acceptance observable

Connect intended behavior and edge cases to checkable results. Prefer existing public verification boundaries; propose new ones when necessary. Expose any gap that prevents implementation. Agreement on test boundaries alone does not confirm all scope and behavior.
