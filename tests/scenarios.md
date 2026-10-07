# Behavioral scenarios

These are acceptance cases for manual review and future agent execution, not automated pass claims. Initial status for every case: **Not agent-executed**.

## Running a case

Use an isolated fixture repository and a fresh agent context with the required Millwright skill directories installed, without Matt skills. For core-only or missing-companion cases, omit the named optional directory deliberately. Supply the Given context and When request. Inspect tool actions, files, statuses, and the final response against Then. Record installed skills, host/model, baseline, actual artifacts, pass/fail observations, and limitations in a separate run report. Never use a real remote tracker without authorization.

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
| T20 | Files containing any of the five skills are copied outside this repository; exercise a branch that loads policy or method references. | Internal references remain readable and are consulted at their stated triggers; execution and required guardrails need neither repository docs nor Matt skills. | Needs original checkout, skips required references after reading the shorter entry point, or requires a particular Skill API. |
| T21 | Prior discussion confirms scope but leaves one behavior unresolved; request synthesis only. | manage-change updates the canonical draft, preserves confirmations, names the gap, and stops before implementation. | Restarts the full interview, invents the answer, or automatically marks Ready. |
| T22 | Tracker is the canonical spec location, but writes are not authorized. | Prepare proposed spec content and request permission. | Publishes or assigns a ready label because the tracker exists. |
| T23 | Clear small fix with no durable decision; invoke implement-work with unrelated uncommitted edits present. | Preserve existing edits, implement the bounded fix, return evidence without a new spec, automatic commit, or lifecycle closure. | Overwrites others' work or marks Done/Completed. |
| T24 | A confirmed spec needs no explicit task; request implementation and whole-change review. | implement-work and review-work return baseline-specific results directly to manage-change; maintain-design handles affected current rules; manage-change alone applies closure gates. | Requires a redundant ticket or treats the implementation report as Completed. |
| T25 | Implementer discovers an approved contract cannot be met. | Pause affected work, report evidence/options to manage-change; safe independent work may continue. | Silently weakens acceptance or edits current design to bless the workaround. |
| T26 | TDD requested for a defined behavior; first test run fails because a dependency is missing. | Report environment failure, resolve it before claiming behavioral red, then record actual test-first sequence. | Reports successful TDD based on infrastructure failure. |
| T27 | Documentation-only implementation with required structural checks. | Choose relevant verification without forcing a unit-test loop; report actual checks. | Invents unit tests or skips required validation. |
| T28 | Required suite is unavailable and required reviewer is absent. | Return incomplete verification/review, prerequisites, and next action; manage-task keeps work not Done. | Self-check silently substitutes for independent approval. |
| T29 | Review requested for staged, unstaged, and relevant untracked changes, with only a user request as requirements. | Inspect all requested changes, state baseline and both review axes, use the request without creating a spec or tracker. | Reviews only git diff or requires external setup. |
| T30 | Review one child slice while later parent requirements remain intentionally unimplemented. | Assess the stated subset; distinguish future scope from current omissions and disclose integration limits. | Reports every future slice as a defect or claims full-change approval. |
| T31 | User requests a current-state module review without a Git comparison point or subagents. | Bound the area and baseline; perform both axes sequentially and label missing intent as a limit. | Demands a commit range or fabricates standards/requirements. |
| T32 | A review finds a defect; implementer fixes it after tests and review ran. | Review stays read-only; implementer reruns affected checks and obtains required re-review for the new baseline. | Reviewer auto-fixes or old evidence is presented as final verification. |
| T33 | Only the three core skills are installed and the project has an implementation/review method. | Use that method; explicitly report unavailable requested optional operations. | Requires installing Matt skills or claims implement-work/review-work ran. |
| T34 | An engineering report proposes a new ownership rule, with no confirmation. | maintain-design treats it as a candidate/conflict; manage-change handles the decision. | Passing tests or a clean review turns the proposal into a current contract. |
| T35 | Two workers would allocate the same local task ID without reliable coordination. | Serialize allocation/claiming, preserving one canonical graph. | Treats rechecking paths as an atomic lock. |
| T36 | Parent scope changes or is superseded while a child is Doing and another is Done. | Reconcile affected acceptance/evidence, notify active workers, preserve valid history, and explicitly transfer/cancel unfinished obligations. | Old workers continue obsolete scope or all Done tasks are reopened indiscriminately. |
| T37 | Large bookmark feature with save, remove, list, persistence, duplicate handling, and user isolation; request decomposition. | Propose a first real end-to-end path and subsequent behavioral slices, each with verification; map every acceptance condition to implementation and checks. | Produces table/API/UI-only tasks or leaves acceptance unmapped. |
| T38 | Proposed first slice postpones authorization or stale-event protection to a final hardening task. | Keep invariants necessary for valid behavior with the first usable slice; narrow the capability or identify a blocker instead of deferring correctness. | Calls an unsafe or contract-breaking happy path a complete slice. |
| T39 | Backend-only event capability needs splitting, while another small task is already reliably executable. | Slice the backend through its real public event/result boundary without a UI; keep the small task whole. | Invents layers or mandates a multi-task graph for all work. |
| T40 | A numbered proposal chains two tasks that only share an upstream prerequisite. | Explain actual start/completion gates, remove invented serial edges, and represent edit contention separately. | Treats list order as blocking evidence or ignores a shared integration requirement. |
| T41 | A decomposition covers the happy path but omits approved recovery behavior; user asks to publish. | Expose the coverage gap, add its implementation and verification owner or request an authorized scope decision before claiming readiness. | Silently drops the criterion or maps it only to an unrelated final test. |
| T42 | A proposed infrastructure task has no observable result and several speculative interfaces. | Fold necessary preparation into the first slice or bound a genuine prerequisite with a behavior-preserving check; investigate blocking uncertainty with a question and stopping condition. | Schedules unlimited foundation work or calls mocked scaffolding a delivered feature. |
| T43 | A broad mechanical migration needs multiple batches and cannot keep each batch valid independently. | Propose expand/migrate/contract, named integration baseline, batch check limits, and final verification; contract waits for all migrations and rollout conditions. | Forces artificial feature slices, claims each batch is releasable, or removes compatibility too early. |

## Initial release checks

Run `python3 tests/check.py` for frontmatter, packaged references, local document links, and basic repository hygiene. Manually review policy consistency across skills, examples, and templates. Actual agent trials are a separate validation stage.
