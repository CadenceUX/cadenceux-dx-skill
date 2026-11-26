# cadenceux-developer-experience: Changelog

Earlier entries are under the skill's previous name, cadenceux-dx.

## [2.0.0] - 2026-11-26

Renamed to `cadenceux-developer-experience`, and the skill now directs the Developer and the
Agent through agile sprints with six development hats. The stage names and hat assignments in
`references/sprints-and-hats.md` are the source for the "Six Thinking Hats, One Developer" post and
its graphic.

### Changed: the name

- `cadenceux-dx` becomes `cadenceux-developer-experience`: "dx" isn't widely known yet, and the
  full words say what the skill is. Major version because installs change name.
- `cadenceux-dx` and `fmp-dev-orchestrator` stay as generated twins, so existing installs and
  links keep working. `maintainer/build_orchestrator.py` becomes `maintainer/build_twins.py`
  and builds either one (`cadenceux-dx` at this version, `fmp-dev-orchestrator` at the major
  number plus 2, so 4.0.0). The description now leaves room for the line each twin adds.
- `scripts/stack_check.py` treats `same_as` as a group: any number of names for one skill, none
  listed as not installed while another is, and a "keep one" note naming every other installed
  copy. `references/stack-check.md` updated to match.
- Self-check and README links point to `CadenceUX/cadenceux-developer-experience-skill`.

### Added

- **`references/sprints-and-hats.md`:** sprints (Analyse; Plan, Design, Build, Test and Review in
  sprints; Launch, with the Orchestrator deciding after every Review); the six development hats
  (Analyst, Architect, Developer, Tester, Reviewer, Orchestrator) and who wears each; asking
  which hat a task needs; de Bono's six thinking hats on every development hat at lead, support
  and visit weights; the hand-back (White, Black, Red, Blue); the plan and the sprint log
  (`docs/plan.md`, `docs/sprint-log.md`) with a template; launch (release notes, changelog,
  feedback into the next Analyse); reviewing web viewer apps in FileMaker terms; estimates in
  sprints with a real re-estimate case; recording token cost per job.
- **SKILL.md, "How the work runs":** sprints, the hat table and nine rules that apply to every
  task: ask which hat first; no hat signs off its own work; every hand-back carries four
  thinking hats; Red is never only a visit; hands off the referee; write the plan and every
  sprint down; document the why; review in FileMaker terms; estimates you can defend.
- **`linter-tests.md`, "Hands off the referee":** linter tests, standards and fixtures never
  change in the same change as the code they check; the rule change is its own change, flagged
  for the Developer; a hook would enforce it (routed to `cadenceux-plugin-creator`, now in the
  routing table).
- **`working-agentically.md`, "Document the why":** changelogs, decision notes and script
  comments record the options considered, the decision and the reason, and what a script used
  to do and why it changed, with a script history example.

### Changed

- The four hats become six. `working-agentically.md`'s hat section now shows where the
  Developer's time goes across all six, and points to `sprints-and-hats.md`.
- "Relationship to other skills": this skill is the source of truth for the stage names
  and the six hats; the posts, deck and graphics are drawn from it.
- Eval cases: `four-hats` replaced by `six-hats`; `orchestrator-same-skill` becomes
  `earlier-names`; nine new cases (`which-hat`, `hands-off-referee`, `sprint-update`,
  `hand-back`, `launch-gate`, `thinking-hats`, `estimate`, `script-why`, `webviewer-review`)
  and a near-miss for de Bono outside FileMaker.

### Verified

- Evals: see `evals/results-2026-11-26-v2.0.0.md`. Baselines (released cadenceux-dx 1.0.2 and
  no skill, Sonnet) scored 0 of 10 on the new cases.
- `scripts/stack_check.py`'s group logic tested with faked installs (none, the source only, a
  twin only, two names, all three).
- `maintainer/build_twins.py` run for both twins into scratch git checkouts.
- `validate_skill.py` clean.

## [1.0.2] — 2026-11-24

`fmp-dev-orchestrator` returns as this skill under its earlier name, built from this repo.

### Added

- `maintainer/build_orchestrator.py` writes `fmp-dev-orchestrator` (3.0.2 for this release:
  this version with the major number plus 2) from this repo's SKILL.md, `references/`,
  `scripts/` and evals. It changes only the name, version, self-check links and the
  relationship note, and stops if any of those no longer match.

### Changed

- "Relationship to other skills", the README and `references/stack-check.md` call
  `fmp-dev-orchestrator` this skill's earlier name rather than a retired one. If both are
  loaded, use `cadenceux-dx` and suggest uninstalling either.
- `scripts/stack_check.py` reads `same_as` in `versions.json`: when both names are installed it
  notes "same skill as …: keep one", and neither is listed as not installed while the other is.
- Eval case `retired-orchestrator` replaced by `orchestrator-same-skill`.

### Verified

- Evals: `orchestrator-same-skill` passes on Haiku, Sonnet and Opus for both cadenceux-dx 1.0.2
  and fmp-dev-orchestrator 3.0.2 (the released versions fail it on Sonnet), and the orchestrator
  copy passes `add-field-adk` on all three; see `evals/results-2026-11-24-v1.0.2.md`.
- Stack check run on macOS against the new `versions.json`; the both, one and neither cases
  tested.
- `validate_skill.py` clean on both; `cadenceux-github` scanners clean.

## [1.0.1] — 2026-11-24

Claris's FileMaker Agentic Development Kit (ADK) 0.17.0, which adds 64-bit Windows.

### Fixed

- `scripts/stack_check.py` looked for ADK only in its macOS folder, so on Windows it reported
  ADK as not installed unless `adk` was on PATH. It now looks in `%LOCALAPPDATA%\ADK\bin\adk.exe`
  on Windows. FileMaker Pro's version still can't be read on Windows; the check says so and how
  to find it, as before.

### Verified

- Stack check run against ADK 0.17.0 (build 60) on macOS: ADK, plugin, MCP server and standards
  pack all read correctly. The Windows path checked by loading the script with Windows settings;
  not run on a Windows machine.
- Every ADK command the guides name is still in `adk --help` for 0.17.0.
- `validate_skill.py` clean.

## [1.0.0] — 2026-11-19

First release, using `cadenceux-skill-creator` 2.4.2. Replaces `fmp-dev-orchestrator` (2.1.3),
which is retired: its routing and stack check move here, rewritten for Claris's FileMaker
Agentic Development Kit (ADK 0.16.0), and the skill now carries the developer-experience
judgement the other CadenceUX skills don't.

### Added

- **Decision guides**, each with the options, their costs and a default:
  `before-adk.md` (FileMaker 26.0.3 and earlier: workarounds 26.1 replaces, reading a solution
  without ADK, when a plug-in is the answer), `native-webviewer-hybrid.md`, `data-access.md`
  (relationships, ExecuteSQL, the Data API and OData, scripts), `reviewing-systems.md` (the
  questions to ask before reading a solution), `linter-tests.md` and
  `security-deployment.md`.
- **`working-agentically.md`:** knowledge delegation, agentic time, the four hats (analyst,
  architect, developer, tester), briefs, documentation and reviewing when the harness changes,
  from the Train Your FileMaker AI Agent class and the DigFM talk.
- Routing for the `cadenceux` standards pack (`cadenceux-filemaker-standards@cadenceux`),
  `cadenceux-fms-security` and `cadenceux-github`.

### Changed from fmp-dev-orchestrator 2.1.3

- ADT is now ADK. ADK detection works in any harness (skills, `adk-mcp` tools, or the `adk`
  command), and the rule stands: anything that reads or changes the file goes through ADK.
- `scripts/stack_check.py` checks ADK against Claris's ADK manifest and `adk doctor`, FileMaker
  Pro against ADK's minimum (26.1, from `versions.json` `requirements`), flags testing builds
  newer than Claris's public release and old ADT preview installs, and reads the ADK project's
  standards pack and each web viewer app's `@adk/fmdapi` version. It reports its own version
  under the running skill's name.
- Version numbers are published now that ADK is public; the preview-version rules are gone.

### Verified

- `scripts/stack_check.py` run against ADK 0.16.0 (build 54), FileMaker Pro 26.1.1 and 26.1.2,
  and an ADK project using the `cadenceux` pack.
- Every ADK command the guides name checked against `adk --help` for 0.16.0.
- Evals: 10 cases on Haiku, Sonnet and Opus, all passing after fixes (orchestrator 2.1.3
  baseline 1 of 10); see `evals/results-2026-11-19-v1.0.0.md`.
- `validate_skill.py` clean; `cadenceux-github` scanners clean.
