# cadenceux-dx — Changelog

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
