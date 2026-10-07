# Working on Millwright

- Read `GLOSSARY.md` before changing object names or relationships.
- Read `docs/philosophy.md` before changing lifecycle ownership or authority rules.
- For skill edits, read its `SKILL.md` and the reference files reached by the affected branch. Keep each policy owned by one skill; link rather than duplicate it.
- Keep distributable skill references inside that skill directory. Companion skills are reached by name, not repository-relative sibling paths.
- Skills must work without a specific tracker, agent API, subagent tool, or automatic commit behavior.
- Add or revise cases in `tests/scenarios.md` when behavior changes. Run `python3 tests/check.py` after edits.
- Distinguish static validation, manual scenario review, and actual agent runs in reports. Never label an unexecuted scenario as passing.
- Use English for maintained documentation. Do not add a license, publish, or install globally without approval.
