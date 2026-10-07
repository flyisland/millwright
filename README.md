# Millwright

**Build features. Keep the whole system in view.**

Millwright combines three core skills for work and knowledge lifecycles with optional engineering skills for implementation and review.

It helps agents build software while preserving significant decisions and an understandable current system design. It does not replace your issue tracker or impose a mandatory development pipeline.

## Choose a skill

### Core skills

| Situation | Skill | Result |
| --- | --- | --- |
| Define, split, resume, hand off, or close work | [manage-task](skills/manage-task/SKILL.md) | An actionable task and an honest execution status |
| Plan, revise, or close a significant software change | [manage-change](skills/manage-change/SKILL.md) | A spec, decisions, and an outcome |
| Update a contract or recover the system picture | [maintain-design](skills/maintain-design/SKILL.md) | A navigable, current description of confirmed rules |

### Optional engineering skills

| Situation | Skill | Result |
| --- | --- | --- |
| Implement a clear request, task, or confirmed spec | [implement-work](skills/implement-work/SKILL.md) | Implementation, verification evidence, and explicit gaps |
| Review a change or bounded project area | [review-work](skills/review-work/SKILL.md) | Separate requirements and engineering findings |

Engineering skills return evidence; core skills own scope decisions, lifecycle closure, and current design. Use either engineering skill directly without creating a task or spec solely to satisfy it.

Small work can stay in a conversation. Significant work gets a durable change record. Long-lived rules belong in current design documents, not only in historical specs.

## Install

Copy the three core directories (`manage-task`, `manage-change`, `maintain-design`) and any desired engineering directories (`implement-work`, `review-work`) from `skills/` into your agent's configured skill directory. Preserve each directory's `references/` subtree. Use your host's documented skill installation mechanism; invocation syntax and automatic discovery differ by host.

The skills have no required runtime, tracker, subagent tool, or dependency on Matt Pocock's skills. They use standard `name` and `description` frontmatter and ordinary Markdown instructions. Cross-skill handoffs also work without an automatic invocation tool.

The three core directories are intended to be installed together. Engineering skills are optional and can also be used directly. If a companion skill is unavailable, the active skill reports the missing capability and hands off explicitly instead of claiming to have run it. Existing project implementation and review methods remain valid alternatives.

Then follow [Adoption](docs/adoption.md) to connect the skills to your project, and [Usage](docs/usage.md) for copyable prompts and everyday workflows. Installation alone does not configure a project or create records.

## Read more

- [Vocabulary](GLOSSARY.md)
- [Design principles](docs/philosophy.md)
- [Project adoption](docs/adoption.md)
- [Everyday usage and example prompts](docs/usage.md)
- [Engineering skill collaboration](docs/integrations.md)
- [Small fix example](examples/small-fix.md)
- [Significant change example](examples/significant-change.md)
- [Recovering the system view](examples/recover-system-view.md)

## Development and validation

Run `python3 tests/check.py` with Python 3.9 or newer for structural checks (standard library only). See [scenario checks](tests/scenarios.md) for behavioral acceptance cases. Passing structural checks does not prove an agent follows the workflows.

## Acknowledgements

Inspired by [Prowl's write-ai-doc](https://github.com/onevcat/Prowl/blob/main/.claude/skills/write-ai-doc/SKILL.md) and [Matt Pocock's engineering skills](https://github.com/mattpocock/skills). Millwright's instructions are independently written around its own lifecycle and ownership model.

This initial repository does not yet declare an open-source license.
