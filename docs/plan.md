# Plan: cadenceux-developer-experience 2.0.0

The plan and goals for this release, written the way the skill asks every project to write
them. Kept in the repo for the maintainer and Developer Next; left out of release archives
(`docs/ export-ignore`).

Written after sprint 1, not before it. The Analyse work happened (the brief from the blog post
session, the owner's answers in the conversation), but it wasn't written down before the build.
That gap is the reason this skill now says "the plan is written before the first sprint": a
fresh session couldn't have picked this work up from the repo alone.

## The need

The CadenceUX post "Six Thinking Hats, One Developer" maps de Bono's six thinking hats onto six
development hats: the four from "Agentic Time Traveller" plus the Reviewer and the Orchestrator.
The post says this skill should direct both the Developer and the Agent through that process.
The post and its graphic will be redrawn from the skill, so the skill's stage names and hat
assignments are the source of truth.

Who uses it:

- FileMaker developers working with an Agent (Claude Code, with or without Claris's ADK).
- The Agent itself, which needs rules it follows on every task, not an essay.
- The owner (Darrin Southern, CadenceUX), as Reviewer and Orchestrator of this release.
- Developer Next, maintaining the skill without having been in the room.

House rules: plain, known agile terms (no metaphors), Australian English, no em-dashes in
anything user-facing.

## Goals

1. Sprints: Analyse on the way in; Plan, Design, Build, Test, Review each sprint; Launch. After
   every Review the Orchestrator (the Developer) decides: another sprint, or launch.
2. Six development hats, each with its stage and who wears it. The Agent asks which hat a task
   needs. Nothing launches until Test and Review have both had their turn. No hat signs off its
   own work.
3. All six thinking hats on every development hat (lead, support, visit). Every hand-back
   carries White, Black, Red and Blue. Red is never only a visit.
4. Hands off the referee: linter tests, standards and fixtures never change with the code they
   check. Say a hook would enforce it better.
5. The plan and goals written before the first sprint; a sprint update after every sprint; the
   next sprint reads it first; release notes and changelog at launch; feedback into Analyse.
6. Document the why: options, decision, reason; what a script used to do and why it changed.
7. Review in FileMaker terms, with the layouts, fields and scripts a web viewer app touches.
8. Estimates in sprints, re-estimated after the first build day, with actuals.
9. Token cost per job where the harness reports it.

## Definition of done

- The skill teaches goals 1 to 9, and its evals for them pass on Haiku, Sonnet and Opus and beat
  the released 1.0.2 and a no-skill baseline.
- **Installed on this machine and used before release:** a fresh session picks the installed
  skill up and follows it (asks which hat, hands back with the four thinking hats).
- The stack check, the twins builder and the validator run clean against the new name.
- CHANGELOG and version updated.
- Test and Review have both had their turn, and the owner, as Orchestrator, has made the launch
  call.

## Out of scope for this release

- The hook that enforces hands off the referee (a plugin, through `cadenceux-plugin-creator`).
- Updating `cadenceux-academy` and the DigFM deck from four hats to six.
- The blog post and its graphic (another session, drawing from this skill).
- Description trigger tuning with `run_loop.py`.

## Decisions so far

| Decision | Options considered | Chosen, and why | Who, when |
|---|---|---|---|
| Name | Keep `cadenceux-dx`; `cadenceux-dev-exp-dx`; `cadenceux-dev-experience`; `cadenceux-developer-experience` | `cadenceux-developer-experience`: "dx" isn't widely known yet, and `dev-exp-dx` says the same thing twice | Owner, 2026-11-26 |
| Earlier names | Retire them; keep them as generated twins | Twins: existing installs and links keep working, built by `maintainer/build_twins.py` | Owner, 2026-11-26 |
| Version | 1.1.0 as briefed; 2.0.0 | 2.0.0: installs change name, and four hats become six | Owner, 2026-11-26 |
| Terms | "Loop", "lap", "sprint" | "Sprint": a known agile term | Owner, 2026-11-26 |
| Branch | A release branch; `main` | `main`, uncommitted until the owner says | Owner, 2026-11-26 |
| Plan and log location | Repo root; `maintainer/`; `docs/` | `docs/`, excluded from release archives: they're for the maintainer, not the skill's job | Agent, 2026-11-26; for the owner's review |
| Folder | Keep `cadenceux-dx-skill`; copy to a new folder; rename the folder | Renamed to `cadenceux-developer-experience-skill`, matching Skill Masters' `<name>-skill` folders and the skill's name. One folder per repo: a copy would invite edits in the wrong one. Frees `cadenceux-dx-skill` for the generated twin | Owner asked, 2026-11-26 |
| Release order | Publish, then test; install, test and review, then publish | Install here first and use it: the skill's own launch gate applies to the skill | Owner, 2026-11-26 |

## Estimate

Three sprints, then Launch:

1. Build the content and the evals (done, one session).
2. Install locally, Test as a separate pass, the owner's Review, fixes.
3. Only if Review sends it round again.

Launch itself is a set of owner actions (commit, tag, GitHub renames, `versions.json`, the
marketplace entry, the twins' releases), listed in the sprint log when it's reached.
