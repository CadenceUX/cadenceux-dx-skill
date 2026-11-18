# cadenceux-dx — Changelog

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
