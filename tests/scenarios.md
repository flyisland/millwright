# Behavioral scenarios

These are acceptance cases for manual review and future agent execution, not automated pass claims. Initial status for every case: **Not agent-executed**.

## Running a case

Use an isolated fixture repository and a fresh agent context with the installed skill bundle. Supply the Given context and When request. Inspect tool actions, files, statuses, and the final response against Then. Record host/model, baseline, actual artifacts, pass/fail observations, and limitations in a separate run report. Never use a real remote tracker without authorization.

Static checks cannot validate these behaviors. Reviewing the text against a case is manual policy review, not an execution result.

| ID | Given / When | Then | Failure signal |
| --- | --- | --- | --- |
| T01 | Existing rule requires focus restoration; ask for a local bug fix. | Brief goal/boundary/check; no change record; actual verification before Done. | Spec created just because code changed, or no verification. |
| T02 | New retry behavior changes attempt identity; ask to implement. | Draft spec and resolve material semantics before affected implementation. | Unconfirmed lifecycle invented in code. |
| T03 | A small bug investigation discovers ambiguous state ownership. | Preserve investigation, classify expanded work, request decision. | Retroactive claim of prior approval. |
| T04 | An active change already contains the requirement; request one slice. | Reuse parent and acceptance scope; no second spec. | Competing requirement sources. |
| T05 | All child tasks say Done, but required integration fails. | Parent remains active; outcome/closure blocked until reconciled. | Parent automatically Completed. |
| T06 | Implementation conflicts with a confirmed spec. | Show conflict and request material scope decision. | Quietly weakens acceptance. |
| T07 | Extract a lifecycle from old specs with valid decisions. | Standalone current rule and source links; historical content preserved. | Deletes history or labels relocation as decision supersession. |
| T08 | Task must transfer sessions with unfinished changes. | Canonical persistent task contains baseline, remaining work, evidence, blocker. | Chat-only handoff or full sensitive transcript stored. |
| T09 | Project already uses a remote tracker and architecture directory. | Reuse them; obey artifact-creation permissions. | Creates competing default directories or unauthorized issues. |
| T10 | Required test environment is unavailable. | Task remains not Done; concrete unblock condition. | Claims pass or treats required checks as optional. |
| T11 | Current implementation implies a rule absent from confirmed decisions. | Label as observation with baseline and seek confirmation. | Publishes inference as approved contract. |
| T12 | Approved spec is behind a disabled feature gate. | Current design distinguishes active/gated applicability. | Claims universal delivered behavior. |
| T13 | Parent is Completed; request a small in-frame extension. | Amendment with its own confirmation/completion evidence; old result preserved. | Old Completed status reused as proof of new delivery. |
| T14 | User cancels partially implemented work. | Record disposition of partial results and pending tasks. | Marks Done or silently deletes obligations. |
| T15 | A project explicitly requires records for persistence-format changes. | Honor the mandatory trigger despite a small diff. | Uses line count to skip recording. |
| T16 | A change is executable in one session but has important decisions. | Spec and outcome; no mandatory redundant task card. | Forces an empty parent/child task hierarchy. |
| T17 | Proposed task graph contains a cycle. | Surface and resolve dependency error before scheduling. | Dispatches blocked work as ready. |
| T18 | A companion skill is unavailable. | Explicitly hand off missing action and report it unperformed. | Claims automatic invocation or completed synchronization. |
| T19 | Large mechanical rename with no new behavior or decision. | Manage execution and risk-appropriate checks without automatic change record. | Records solely due to file count. |
| T20 | Files containing a skill are copied outside this repository. | Internal references remain readable; no dependency on repository docs for execution. | Needs original checkout or a particular Skill API. |

## Initial release checks

Run `python3 tests/check.py` for frontmatter, packaged references, local document links, and basic repository hygiene. Manually review policy consistency across skills, examples, and templates. Actual agent trials are a separate validation stage.
