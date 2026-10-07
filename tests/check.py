#!/usr/bin/env python3
"""Dependency-free structural checks; not a behavioral agent evaluator."""
from pathlib import Path
import re
import sys
import tempfile
import shutil

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "manage-task", "manage-change", "maintain-design",
    "implement-work", "review-work",
}
errors = []


def fail(path, message):
    errors.append(f"{path}: {message}")


def prose(text):
    """Exclude fenced examples, which deliberately contain template links."""
    return re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)


def local_links(text):
    for match in re.finditer(r"\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", prose(text)):
        target = match.group(1)
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        yield target.split("#", 1)[0]


def main():
    skills = ROOT / "skills"
    actual = {p.name for p in skills.iterdir() if p.is_dir()}
    if actual != EXPECTED:
        fail("skills", f"expected {sorted(EXPECTED)}, found {sorted(actual)}")

    markdown_files = sorted(ROOT.rglob("*.md"))
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if not text.endswith("\n"):
            fail(relative, "missing final newline")
        if "/Users/" in text or "/home/" in text:
            fail(relative, "machine-specific absolute path")
        for target in local_links(text):
            if target and not (path.parent / target).exists():
                fail(relative, f"broken local link: {target}")

    for name in sorted(EXPECTED):
        directory = skills / name
        entry = directory / "SKILL.md"
        if not entry.exists():
            fail(name, "missing SKILL.md")
            continue
        text = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.S)
        if not match:
            fail(name, "missing frontmatter")
            continue
        # Deliberately validate this project's simple scalar subset, not arbitrary YAML.
        fields = {}
        for line in match.group(1).splitlines():
            key, separator, value = line.partition(":")
            if not separator or key in fields:
                fail(name, f"invalid/duplicate frontmatter field: {line}")
                continue
            fields[key] = value.strip()
        if fields.get("name") != name:
            fail(name, "frontmatter name differs from directory")
        description = fields.get("description", "")
        if not description or len(description) > 1024:
            fail(name, "description must contain 1–1024 characters")
        if ": " in description or " #" in description:
            fail(name, "plain scalar description needs YAML quoting")

        # Copy each skill separately: all linked execution references must travel with it.
        with tempfile.TemporaryDirectory(prefix="millwright-check-") as temporary:
            copy = Path(temporary) / name
            shutil.copytree(directory, copy)
            reachable = {copy / "SKILL.md"}
            pending = list(reachable)
            while pending:
                document = pending.pop()
                for target in local_links(document.read_text(encoding="utf-8")):
                    destination = (document.parent / target).resolve()
                    if not destination.is_relative_to(copy.resolve()):
                        fail(name, f"reference escapes skill package: {target}")
                    elif not destination.exists():
                        fail(name, f"reference missing from isolated package: {target}")
                    elif destination.suffix == ".md" and destination not in reachable:
                        reachable.add(destination)
                        pending.append(destination)
            for reference in copy.rglob("*.md"):
                if reference.resolve() not in {p.resolve() for p in reachable}:
                    fail(name, f"unreachable reference: {reference.relative_to(copy)}")

    if errors:
        print("Structural checks FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: {len(markdown_files)} Markdown files; {len(EXPECTED)} isolated skill packages.")
    print("Checked: simple frontmatter, local links, packaged reference reachability, path hygiene.")
    print("Not checked: remote links, Markdown anchors, host discovery, or agent behavior.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
