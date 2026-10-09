# Review policy

## Evidence before findings

A finding identifies an affected location or behavior, the triggering condition, observable impact, and the basis for expecting something else. Cite a verified path and narrow line range when possible; a requirement omission may instead point to the criterion and inspected implementation area.

Separate demonstrated defects, supported risks, unresolved questions, and optional improvements. Do not turn uncertainty into an asserted defect. Do not manufacture findings to fill a quota. A test gap can be a real risk or unmet requirement, but is not proof of a runtime bug.

For engineering judgments, consider whether unclear names hide responsibilities, duplication can drift, interfaces expose unnecessary internals, or a change forces unrelated modules to move together. Explain concrete consequences; avoid generic smell lists and speculative abstractions. Project conventions override stylistic preferences. Do not repeat formatter/linter complaints unless they reveal a consequential unresolved failure.

Assess affected user-facing behavior through representative end-to-end paths:

- **Usability:** entry points, prerequisites, established usage conventions, and observable results.
- **System status visibility:** start, progress, and completion; for long-running operations, inspect feedback before completion.
- **Error recovery:** actionable failure information and recovery after errors or interruptions.

Use safe synthetic checks where useful. Ground findings in concrete user impact and preserve existing contracts; material behavior choices require confirmation, not a prescribed interface.

When code and approved intent disagree, expose the conflict. Code is evidence of observed behavior, not permission to redefine the requirement. Verify that each finding belongs to the stated scope; label relevant pre-existing issues rather than attributing them to a new change.

## Priority

Use project severity conventions when available. Otherwise:

- **P0:** immediate critical harm with a demonstrated condition; stop affected unsafe activity and escalate.
- **P1:** a serious correctness, safety, or acceptance failure that should block delivery.
- **P2:** a material defect or risk needing correction, with bounded impact.
- **P3:** a minor issue or optional improvement; label preferences as such.

Priority describes impact and urgency, not confidence. State uncertainty separately and do not assign severe labels without supporting conditions. The reviewer recommends blockers; lifecycle owners apply their own completion gates and authorized risk decisions.

## Report

Start with the target, baseline, scope, and sources. Label self-review; it does not satisfy required independent approval. The report applies only to the inspected baseline, so later changes may require renewed checks or review.

Keep the body concise:

### Findings

Use one format: **priority · title · location · evidence/trigger · impact · basis · correction direction**. Group by axis:

- **Requirements:** cite the spec, request, or task; identify any scope that could not be assessed.
- **Engineering:** cite the contract, standard, or explicit engineering heuristic. Cross-reference findings already reported under Requirements rather than counting them twice.

### Verification and limits

List checks actually run and results, supplied evidence considered, unexecuted required checks, and unreviewed areas. Supplied results are not checks you performed. Separate static inspection, manual checks, automated tests, and agent behavior trials. A clean review means no supported findings in the inspected scope, not proof of correctness.

End with findings per axis, recommended next actions, and unresolved blockers. Zero findings is acceptable; avoid claiming unrestricted approval. Reports stay conversational unless persistence is requested or required by project conventions; remote publication requires authorization.
