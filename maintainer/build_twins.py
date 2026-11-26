#!/usr/bin/env python3
"""Generate the skill's earlier names from this repo: the same skill under each.

cadenceux-developer-experience is the one source. Its earlier names, cadenceux-dx and
fmp-dev-orchestrator, are published from their own repos so the installs and links that name
them keep working. Their files are written by this script, never edited by hand. Run it for
each twin after every change here, then release all three.

Usage: python3 maintainer/build_twins.py <twin-name> /path/to/<twin-name>-skill
       twin-name: cadenceux-dx or fmp-dev-orchestrator

What it writes in the twin's repo: SKILL.md, references/, scripts/, evals/evals.json, VERSION
and the version in .claude-plugin/plugin.json. README.md and CHANGELOG.md there are written by
hand. Versions: each twin is this skill's version with its major number plus the twin's offset,
so there's no separate version bookkeeping:
  cadenceux-dx          offset 0  (it was 1.0.2 when renamed; the source restarted at 2.0.0)
  fmp-dev-orchestrator  offset 2  (it had reached 2.2.0 before the first join, at dx 1.0.2)

Each change below is an exact replacement that must match once. If SKILL.md's wording changes
and a replacement no longer matches, the script stops and names it: fix the replacement here
rather than editing a twin's files. Standard library only.
"""
import json
import os
import shutil
import sys

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_NAME = "cadenceux-developer-experience"
SOURCE_REPO = "https://github.com/CadenceUX/cadenceux-developer-experience-skill"
TWINS = {
    "cadenceux-dx": {"repo": "https://github.com/CadenceUX/cadenceux-dx-skill", "offset": 0},
    "fmp-dev-orchestrator": {"repo": "https://github.com/CadenceUX/fmp-dev-orchestrator-skill", "offset": 2},
}

SOURCE_RELATIONSHIP = """- **`cadenceux-dx` and `fmp-dev-orchestrator` are this skill under its earlier names.** Their
  files are generated from this repo, so they never differ in what they do, and existing
  installs and links keep working. If more than one is loaded, use
  `cadenceux-developer-experience` and suggest keeping just one of them (any: they're identical).
"""
TWIN_RELATIONSHIP = """- **This is `cadenceux-developer-experience` under an earlier name.** Its files are generated
  from the cadenceux-developer-experience repo, so the two never differ in what they do. If
  `cadenceux-developer-experience` is also loaded, use it and leave this copy alone, and suggest
  keeping just one of them (any: they're identical).
"""


def fail(msg):
    sys.exit("build_twins: " + msg)


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
    if len(sys.argv) != 3 or sys.argv[1] not in TWINS:
        fail("usage: python3 maintainer/build_twins.py <" + "|".join(TWINS) + "> /path/to/twin-repo")
    name, target = sys.argv[1], os.path.abspath(sys.argv[2])
    repo, offset = TWINS[name]["repo"], TWINS[name]["offset"]
    manifest = os.path.join(target, ".claude-plugin", "plugin.json")
    # Guard: only ever write into a git checkout of the named twin's repo, never into this one.
    if os.path.realpath(target) == os.path.realpath(SRC):
        fail("the target is this repo; give the twin's own checkout")
    if not os.path.isdir(os.path.join(target, ".git")):
        fail(f"{target} is not a git checkout")
    try:
        plugin = json.loads(read(manifest))
    except (OSError, ValueError) as e:
        fail(f"can't read {manifest}: {e}")
    if plugin.get("name") != name:
        fail(f"{manifest} names {plugin.get('name')!r}, not {name!r}")

    src_ver = read(os.path.join(SRC, "VERSION")).strip()
    parts = src_ver.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        fail(f"VERSION {src_ver!r} isn't X.Y.Z")
    ver = ".".join([str(int(parts[0]) + offset)] + parts[1:])

    skill = read(os.path.join(SRC, "SKILL.md"))
    for old, new, what in [
        (f"name: {SOURCE_NAME}\n", f"name: {name}\n", "the name"),
        ("description: >-\n  The developer experience",
         f"description: >-\n  Same skill as {SOURCE_NAME}, earlier name.\n  The developer experience",
         "the description's opening"),
        (f'version: "{src_ver}"', f'version: "{ver}"', "metadata.version (does it match VERSION?)"),
        ("# CadenceUX Developer Experience\n", f"# CadenceUX Developer Experience ({name})\n", "the heading"),
        (f"{SOURCE_REPO}/raw/main/VERSION", f"{repo}/raw/main/VERSION", "the self-check VERSION URL"),
        (f"if it's newer than {src_ver},", f"if it's newer than {ver},", "the self-check version"),
        (f"{SOURCE_REPO}/releases", f"{repo}/releases", "the releases URL"),
        (SOURCE_RELATIONSHIP, TWIN_RELATIONSHIP, "the relationship bullet"),
    ]:
        skill = replace_once(skill, old, new, what)
    if SOURCE_REPO.rsplit("/", 1)[1] in skill:
        fail("SKILL.md still links to the source repo after the replacements; add a replacement")
    write(os.path.join(target, "SKILL.md"), skill)

    ignore = shutil.ignore_patterns("__pycache__", ".DS_Store")
    for folder in ("references", "scripts"):
        dst = os.path.join(target, folder)
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.copytree(os.path.join(SRC, folder), dst, ignore=ignore)

    evals = json.loads(read(os.path.join(SRC, "evals", "evals.json")))
    evals["skill"], evals["version"] = name, ver
    evals["notes"] = f"Generated from {SOURCE_NAME} {src_ver}'s evals by maintainer/build_twins.py. " + evals.get("notes", "")
    os.makedirs(os.path.join(target, "evals"), exist_ok=True)
    write(os.path.join(target, "evals", "evals.json"), json.dumps(evals, indent=2, ensure_ascii=False) + "\n")

    write(os.path.join(target, "VERSION"), ver + "\n")
    plugin["version"] = ver
    write(manifest, json.dumps(plugin, indent=2, ensure_ascii=False) + "\n")

    print(f"{name} {ver} written from {SOURCE_NAME} {src_ver} into {target}")
    print("Still by hand: its CHANGELOG.md entry and README.md, then validate and release.")


if __name__ == "__main__":
    main()
