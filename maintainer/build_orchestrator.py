#!/usr/bin/env python3
"""Generate fmp-dev-orchestrator from this repo: the same skill under its earlier name.

cadenceux-dx is the one source. fmp-dev-orchestrator is published from its own repo so the
installs and links that name it keep working, and its files are written by this script, never
edited by hand. Run it after every cadenceux-dx change, then release both.

Usage: python3 maintainer/build_orchestrator.py /path/to/fmp-dev-orchestrator-skill

What it writes in the orchestrator repo: SKILL.md, references/, scripts/, evals/evals.json,
VERSION and the version in .claude-plugin/plugin.json. README.md and CHANGELOG.md there are
written by hand. Versions: the orchestrator is cadenceux-dx's version with the major number
plus 2 (dx 1.0.2 -> 3.0.2), because the orchestrator had already reached 2.2.0 when the two
were joined; the mapping means no separate version bookkeeping.

Each change below is an exact replacement that must match once. If cadenceux-dx's wording
changes and a replacement no longer matches, the script stops and names it: fix the
replacement here rather than editing the orchestrator's files. Standard library only.
"""
import json
import os
import shutil
import sys

DX = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = "fmp-dev-orchestrator"
REPO = "https://github.com/CadenceUX/fmp-dev-orchestrator-skill"
MAJOR_OFFSET = 2  # orchestrator 2.2.0 was its last release before the join

DX_RELATIONSHIP = """- **`fmp-dev-orchestrator` is this skill under its earlier name.** Its files are generated from
  this repo, so the two never differ in what they do, and existing orchestrator installs and
  links keep working. If both are loaded, use `cadenceux-dx` and suggest uninstalling one of
  them (either: they're identical).
"""
COPY_RELATIONSHIP = """- **This is `cadenceux-dx` under its earlier name.** Its files are generated from the
  cadenceux-dx repo, so the two never differ in what they do. If `cadenceux-dx` is also loaded,
  use it and leave this copy alone, and suggest uninstalling one of them (either: they're
  identical).
"""


def fail(msg):
    sys.exit("build_orchestrator: " + msg)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def replace_once(text, old, new, what):
    n = text.count(old)
    if n != 1:
        fail(f"SKILL.md: expected 1 match for {what}, found {n}. Update the replacement in this script.")
    return text.replace(old, new)


def main():
    if len(sys.argv) != 2:
        fail("usage: python3 maintainer/build_orchestrator.py /path/to/fmp-dev-orchestrator-skill")
    target = os.path.abspath(sys.argv[1])
    manifest = os.path.join(target, ".claude-plugin", "plugin.json")
    # Guard: only ever write into a git checkout of the orchestrator repo.
    if not os.path.isdir(os.path.join(target, ".git")):
        fail(f"{target} is not a git checkout")
    try:
        plugin = json.loads(read(manifest))
    except (OSError, ValueError) as e:
        fail(f"can't read {manifest}: {e}")
    if plugin.get("name") != NAME:
        fail(f"{manifest} names {plugin.get('name')!r}, not {NAME!r}")

    dx_ver = read(os.path.join(DX, "VERSION")).strip()
    parts = dx_ver.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        fail(f"cadenceux-dx VERSION {dx_ver!r} isn't X.Y.Z")
    ver = ".".join([str(int(parts[0]) + MAJOR_OFFSET)] + parts[1:])

    skill = read(os.path.join(DX, "SKILL.md"))
    for old, new, what in [
        ("name: cadenceux-dx\n", f"name: {NAME}\n", "the name"),
        ("description: >-\n  The developer experience",
         "description: >-\n  The same skill as cadenceux-dx, under its earlier name.\n  The developer experience",
         "the description's opening"),
        (f'version: "{dx_ver}"', f'version: "{ver}"', "metadata.version (does it match VERSION?)"),
        ("# CadenceUX DX\n", "# CadenceUX DX (fmp-dev-orchestrator)\n", "the heading"),
        ("https://github.com/CadenceUX/cadenceux-dx-skill/raw/main/VERSION", f"{REPO}/raw/main/VERSION",
         "the self-check VERSION URL"),
        (f"if it's newer than {dx_ver},", f"if it's newer than {ver},", "the self-check version"),
        ("https://github.com/CadenceUX/cadenceux-dx-skill/releases", f"{REPO}/releases", "the releases URL"),
        (DX_RELATIONSHIP, COPY_RELATIONSHIP, "the relationship bullet"),
    ]:
        skill = replace_once(skill, old, new, what)
    if "cadenceux-dx-skill" in skill:
        fail("SKILL.md still links to the cadenceux-dx repo after the replacements; add a replacement")
    write(os.path.join(target, "SKILL.md"), skill)

    ignore = shutil.ignore_patterns("__pycache__", ".DS_Store")
    for folder in ("references", "scripts"):
        dst = os.path.join(target, folder)
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.copytree(os.path.join(DX, folder), dst, ignore=ignore)

    evals = json.loads(read(os.path.join(DX, "evals", "evals.json")))
    evals["skill"], evals["version"] = NAME, ver
    evals["notes"] = f"Generated from cadenceux-dx {dx_ver}'s evals by maintainer/build_orchestrator.py. " + evals.get("notes", "")
    os.makedirs(os.path.join(target, "evals"), exist_ok=True)
    write(os.path.join(target, "evals", "evals.json"), json.dumps(evals, indent=2, ensure_ascii=False) + "\n")

    write(os.path.join(target, "VERSION"), ver + "\n")
    plugin["version"] = ver
    write(manifest, json.dumps(plugin, indent=2, ensure_ascii=False) + "\n")

    print(f"fmp-dev-orchestrator {ver} written from cadenceux-dx {dx_ver} into {target}")
    print("Still by hand: its CHANGELOG.md entry and README.md, then validate and release both.")


if __name__ == "__main__":
    main()
