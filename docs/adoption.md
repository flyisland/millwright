# Adopt Millwright in a project

## 1. Install the skills

Copy the complete `manage-task`, `manage-change`, and `maintain-design` directories from Millwright's `skills/` into the skill location supported by your agent host. Preserve relative reference files. Add `implement-work` and/or `review-work` if you want Millwright's optional engineering methods; no external skill set is needed. This repository does not yet provide a package-manager release or a platform plugin.

Installing does not authorize changes to project conventions. You can invoke a skill manually before adding automatic discovery pointers.

## 2. Discover existing conventions

Identify:

- The task tracker, statuses, task-creation permissions, and handoff conventions.
- The authoritative specification location and existing RFC/change history.
- Current architecture, contract, glossary, and ADR entry points.
- Who confirms scope and risky decisions; required tests and reviews.

Keep working conventions. Do not migrate the tracker or duplicate its specs merely to match Millwright's examples. Choose the installed engineering skills or existing project methods explicitly; a required independent review cannot be replaced by an implementer's self-review.

## 3. Add a short project pointer

With project authorization, add a concise navigation block to the existing agent instructions. Adapt this example; do not copy unresolved placeholders:

```text
Use manage-task for execution tracking; durable tasks live in <tracker>.
Use manage-change for significant behavior, contract, ownership, or risk changes;
change records live in <location>. Read <project change policy> when classifying work.
Use maintain-design when confirmed changes affect long-lived rules or when
recovering a system view; current design starts at <design entry>.
Scope confirmation and required verification follow <existing project rules>.
If installed, use implement-work for implementation and evidence, and review-work
for requirements and engineering assessment. Core owners decide lifecycle closure.
```

Only point at existing documents. Before the first record, the installed skill's references can provide the default policy without a project policy file. Add project-specific mandatory triggers when known, for example persistence-format or authorization changes.

## 4. Start with one real piece of work

For a small fix, keep the brief in the conversation. Persist only if it must survive the session.

For an important change, create the spec before implementation. If work is already underway, state the reconstruction baseline and what decisions remain unconfirmed.

Default locations when no convention exists:

| Need | Default |
| --- | --- |
| Significant change | `docs/changes/NNN-slug/spec.md` and `outcome.md` |
| Durable local task | `docs/tasks/NNN-slug.md` |
| Current system view | `docs/design/README.md` plus needed detail |

Create directories only when there is actual content. Maintain a simple change index when records exist; the spec owns status.

## 5. Make rules project-owned only when necessary

The installed skill references own default lifecycle methods and templates. Project instructions own locations, special recording thresholds, approval roles, and required checks. A local override should be explicit, not a second copy that drifts silently.

If the project needs self-contained or customized templates, copy them deliberately and mark them project-owned; future Millwright updates will not automatically govern those copies. Record the source/version if available.

## 6. Review after a few tasks

Ask whether the process reduced lost decisions and repeated exploration. Remove unused fields and unnecessary persistence. Add structure only for actual recurring problems.

Existing projects should usually reconstruct a small current system map before backfilling many old specs. Missing history must not be invented.
