# cadenceux-developer-experience: Changelog

Earlier entries are under the skill's previous name, cadenceux-dx.

## [3.0.0] - 2026-11-27

Skill selection and the stack check go back to `fmp-dev-orchestrator`, which is a separate
skill again (4.0.0). This skill runs the work: the stages, the thinking hats, the gates before
deploy and the decisions around the code. Major version because it no longer routes on its own.

### Changed

- SKILL.md: Steps 0 to 2 (stack check, is ADK available, route the task) and "Requests that
  span skills" move to `fmp-dev-orchestrator`. A short section, "Selecting skills and checking
  the stack", hands both over and gives the orchestrator's install line when it's missing. The
  rule that file changes go through ADK, never clipboard XML, stays.
- `scripts/stack_check.py` and `references/stack-check.md` move to `fmp-dev-orchestrator`.
- The self-check fetches this repo's VERSION when the orchestrator isn't there to check it.
- Description, README and `plugin.json`: what it directs and decides, and that it works with
  `fmp-dev-orchestrator`. "Relationship to other skills" names the orchestrator as the skill that
  answers the Orchestrator's "which skill" question.
- 2.0.0 said it replaced `fmp-dev-orchestrator`. It doesn't: install both.
- Eval cases: the routing and stack cases move to `fmp-dev-orchestrator`'s evals; new
  `dx-defers-routing` and `dx-defers-stack`; `replaces-dx` rewritten.

### Verified

- Evals: see `evals/results-2026-11-27-v3.0.0.md`, against the released 2.0.0.

## [2.0.0] - 2026-11-26 (updated 2026-11-27, pre-release)

Renamed to `cadenceux-developer-experience`, and the skill now directs agentic FileMaker work as
the Orchestrator's skill: six stages in agile sprints, the thinking hats each stage calls, and a
gate at every stage. 2.0.0 hadn't shipped (no tag pushed, no release, not on the marketplace),
so the first draft of 2.0.0 was reworked in place rather than bumped. The stages, hats and gates
in `references/sprints-and-hats.md` and `references/stage-gates.md` are the source for the "Six
Thinking Hats, One Developer" post and its graphic.

### Changed: the name

- `cadenceux-dx` becomes `cadenceux-developer-experience`: "dx" isn't widely known yet, and the
  full words say what the skill is. Major version because installs change name.
- It **replaces** `cadenceux-dx` (and, before it, `fmp-dev-orchestrator`). The generated twins
  from the first draft are gone: `maintainer/build_twins.py`, the twin version offsets, the
  "earlier names" note in SKILL.md and "Also published as" in `plugin.json`. SKILL.md, the README
  and `references/stack-check.md` now say to uninstall the old names.
- `scripts/stack_check.py` still reads `same_as` groups in `versions.json`; its comment no longer
  names the twins.
- Self-check and README links point to `CadenceUX/cadenceux-developer-experience-skill`.
- The description is shorter (849 of 1,024 characters, from 953) and leads with directing the
  process; routing and the stack check stay in it.

### Added

- **The stages, in order:** Analyst (needs analysis), Planner (sprint planning), Architect
  (solution design), Developer (implementation), Tester (QA testing), Reviewer (review and
  optimise), then deploy. Six development roles and six thinking hats are the twelve hats.
- **The Orchestrator is the Blue hat across the whole process, not a stage.** It calls each
  stage and chooses the skill and the thinking for it; the Developer (the person) is the
  Orchestrator, and this skill is the Orchestrator's skill. After review it decides: another
  sprint, and from which stage, or deploy.
- **QA testing before review.** The Reviewer judges the whole result against the need and
  checks the tests tested the right thing; a pull-request code check stays inside
  implementation.
- **Rework goes to the stage that owns the problem:** a bug to the Developer role, a design that
  won't work to the Architect, a plan that missed something to the Planner, a changed need to
  the Analyst. QA testing sends failures straight back. The next sprint starts at the earliest
  owning stage.
- **Thinking hats called by stage**, by meaning (Facts, Feelings, Caution, Value, Ideas,
  Process), each with the question it asks there. De Bono's rule: the Blue hat decides which
  hat is worn when. Implementation has no Ideas hat: Agents are generous with ideas, so the
  Orchestrator calls the hats they skip.
- **`references/stage-gates.md`:** for each stage, what to ask, what must be true before the
  work moves on, and the record it leaves (needs brief, sprint plan, design decision record,
  build hand-back, test report, review notes); the before-deploy gate (security sweep clean or
  findings accepted in writing, server side to `cadenceux-fms-security`; tested on a copy on
  each client; verified backup and rollback; release notes and changelog with the why; the
  client's yes) and its release checklist; default record files under `docs/`. The Agent never
  marks its own gate as passed.
- **A size threshold:** a one-off change names its stage and gate inline; multi-step work gets a
  sprint plan and a sprint log; a project gets the full cycle.
- **One person or a team:** solo, change hats when you change stage, write the hand-back even to
  yourself, never review your own build; in a team, wear your stage's two or three hats, borrow
  a neighbour's, and at sprint planning and review everyone wears the same hat at once.
- **Standard practice and CadenceUX's own, marked.** Standard: de Bono's hats and parallel
  thinking, sprint planning and review, backlog refinement, a pull-request check, Scrum's fixed
  time box, definitions of ready and done, quality gates, decision records, test reports, code
  review, release checklists. CadenceUX's own: the Orchestrator as Blue hat, a sprint as one
  pass from whichever stage the work goes back to, the Planner role, needs analysis in every
  sprint, the hats and questions per stage, a gate at every stage.
- Kept from the first draft: hands off the referee (`linter-tests.md`), document the why
  (`working-agentically.md`), reviewing web viewer apps in FileMaker terms, estimates in sprints
  with a real re-estimate case, token cost per job.

### Removed (from the first draft of 2.0.0)

- The lead, support and visit grid of thinking hats on every development hat.
- Launch as a stage, and the Orchestrator as the last hat. Deploy is the Orchestrator's gate.
- The generated twins and `maintainer/` (see above).

### Changed

- `working-agentically.md`: where the Developer's time goes, by stage; hand-backs use Facts,
  Caution, Feelings, Process.
- `security-deployment.md`: the before-deployment list now includes the security sweep, release
  notes with the why and the client's yes, and points to the before-deploy gate.
- `reviewing-systems.md`: "the questions, by hat" becomes "by role".
- Eval cases: 16 new or rewritten for this model (`replaces-dx`, `twelve-hats`, `which-stage`,
  `hats-per-stage`, `architect-stage`, `deploy-gate`, `agent-own-gate`, `hand-back`,
  `rework-routing`, `qa-sends-back`, `sprint-update`, `size-one-off`, `size-multi-step`,
  `solo-review`, `team-hats`, `standard-or-ours`); `earlier-names`, `six-hats`, `which-hat`,
  `launch-gate` and `thinking-hats` removed.

### Verified

- Evals: `evals/results-2026-11-27-v2.0.0.md`. On the 16 new and rewritten cases the released
  cadenceux-dx 1.0.2 (Sonnet) passed none in full (7 partly); the reworked 2.0.0 passed 16 of 16
  on Sonnet and Opus and 13 of 16 on Haiku (2 partly, 1 borderline fail), after five fixes from
  the first run (stage order and the Blue hat; reading the log first; the three solo rules
  together; the standard practice behind the gates listed in place; reviewing the Agent's build
  versus reviewing an existing system). Seven regression cases pass on Haiku and Sonnet.
- Not tested: near-miss and trigger tuning of the new description, use in a real session.
- `validate_skill.py` (cadenceux-skill-creator 2.4.3) clean.

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
