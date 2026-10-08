# Verification methods

## Choose observable boundaries

Identify the public operation, output, or artifact that demonstrates each acceptance condition. Prefer existing test boundaries and project test conventions over inventing interfaces solely for a test. Use more than one boundary when one cannot adequately exercise the risk.

Reuse already-confirmed verification decisions. Confirm a materially new public interface or a consequential verification trade-off; routine test selection within approved scope does not need repeated permission. Check failure cases and relevant security, compatibility, recovery, and integration behavior, not just the happy path.

Expected results come from requirements, worked examples, or independent known values. A test that recomputes the implementation's answer or only asserts its internal calls can agree with incorrect behavior. Use test doubles at real external boundaries when needed; preserve tests of the actual integrations where required.

## Isolate checks before execution

Before running checks that can read or write data, inspect their working directory, environment, configuration and input discovery, default paths, and output targets. Use authorized synthetic fixtures and isolated resources unless broader access is explicitly authorized. Assume the behavior under test, including rejection and safety checks, may fail completely: test isolation must not depend on that behavior working. A temporary output directory, disabled network, or mocked service alone does not isolate local inputs.

If a check crosses an authorization boundary or causes unexpected unsafe effects, stop affected operations and promptly report the known scope, evidence, and uncertainties to the responsible decision-maker or coordinator. Do not continue the affected run to collect more evidence or treat the incident as authorized acceptance. Keep safe isolation fixes separate from incident investigation or cleanup; additional access, scans, deletion, or other remediation still require appropriate authorization.

## Reuse evidence within its scope

For an existing implementation, integration, or prior check, identify the source, checked baseline/environment, and behavior it supports. Compare the relevant differences in the new work; inspect or test those differences rather than restarting the entire investigation or treating past success as universal compatibility. Distinguish established facts, assumptions, and remaining unknowns.

Ground test doubles in documented contracts or observed behavior with traceable source pointers. Check that request/response shapes and relevant supported variants match the new implementation, especially where it adds stricter validation. Synthetic success proves behavior under those inputs, not compatibility with an external system. Preserve required final integration checks and their authorization boundaries.

## Optional test-first loop

When using TDD:

1. Select one observable behavior and write a focused test for its expected result.
2. Run it and inspect the failure. A syntax, dependency, or environment error is not evidence of the intended failing behavior.
3. Make the smallest coherent implementation that satisfies this behavior; run the test again.
4. Improve structure within scope while keeping checks green. Repeat for the next behavior rather than prebuilding a large speculative test suite.

For bug fixes, reproduce the original failure with a regression test where practical. If automated reproduction is infeasible, record the manual method, observations, and limits. Do not claim red-before-green if that sequence was not executed.

## Other work and broader checks

Documentation, configuration, migrations, and mechanical edits may need structural validation, dry runs, compatibility checks, manual inspection, or integration tests rather than a forced unit-test loop. Choose methods that can actually detect the relevant failure and follow project requirements.

Use focused checks during edits, then the required broader suite and risk-relevant checks before returning the final result. A full suite is not automatically necessary for every prose edit, but a required full suite cannot be replaced by one passing unit test. Distinguish pre-existing failures from regressions only with evidence; neither should disappear from the report.

## Evidence freshness and limits

Associate observations with the checked baseline and environment. After a fix, rerun affected checks and any broader checks required by the project. Do not present pre-fix results as verification of the final state.

Record method/command, scope, actual result, and remaining limits. Report passed, failed, and not run distinctly. If a required environment is unavailable, state the missing prerequisite and next action; do not infer success from inspection or a tool exit code. Exclude secrets and unnecessary transcripts.

Capture critical evidence when it occurs, not only at final delivery: retain the command or method, actual result, checked baseline/environment, limits, and a retrievable source pointer where available. Before context compaction or handoff, preserve relevant authorization changes, incident metadata, unresolved findings, and key verification evidence in a permitted location that survives the transition. Use concise records or pointers, not full conversations or sensitive payloads; no new task or formal report is inherently required.

Treat missing original results as unverified. Use supported host mechanisms to locate the original evidence when useful and authorized; a summary is not a substitute for a missing result. Keep conclusions within what the observation proves, such as a path being absent at check time rather than proof that no copies exist or data was securely erased.
