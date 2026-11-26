# Sprint log: cadenceux-developer-experience

Newest first. Every sprint starts by reading `docs/plan.md` and this file.

## Sprint 2, 2026-11-26: install and Test (open: Test not finished)

**Done:**

- Installed the skill on this Mac as a personal skill: `~/.claude/skills/cadenceux-developer-experience`,
  a symlink to this folder, so edits show live and removal is one link.
- The running session picked it up straight away, and this sprint was run through it.
- Added `docs/ export-ignore`, so the plan and this log stay out of release archives.
- Wrote the plan and the sprint 1 log.
- Renamed the folder to `cadenceux-developer-experience-skill` (Skill Masters' `<name>-skill`
  pattern) and repointed the install. The git remote stays `CadenceUX/cadenceux-dx-skill` until the
  GitHub repo is renamed at Launch.
- Ran Test as a separate pass: a fresh agent working from `docs/plan.md`, with no part in the
  build.

**Changed, and why:** No skill content changed in this sprint. Test reports; it doesn't fix.

**For users:**

- With the `cadenceux-dx` plugin still enabled, sessions on this Mac load both the 1.0.2
  four-hat skill and the 2.0.0 six-hat skill.
- The stack check says "keep one", but nothing chooses for them.
- The README's install line won't work until the marketplace entry exists.

**Verified (Tester):**

| Test | Result |
|---|---|
| Stack check, draft `versions.json` with the new name and `same_as` | Pass: running copy OK, symlinked install found, "same skill ... keep one" on both rows |
| Both twins built and validated | Pass: cadenceux-dx 2.0.0 and fmp-dev-orchestrator 4.0.0, descriptions 1,013 of 1,024 characters |
| Release archive preview (temporary index) | Partial: excludes are right, but the four blog-post files at the top level would ship |
| House style | Pass: no em-dashes, no personal paths, "loop" only where it names the old word |
| Fresh session picks the skill and asks which hat | Blocked: the standalone `claude` CLI isn't signed in (OAuth expired) |
| Hand-back with White, Black, Red, Blue in a fresh session | Blocked: same |

**Not verified:**

- The plan's "used before release" item: which skill a fresh session picks, the hat question
  and the hand-back, in a real session.
- Which skill wins when both names are installed.

**Next:** Finish Test: re-run the two blocked tests once the CLI is signed in, or in a fresh
session in the Claude app. Then the owner's Review.

**Waiting on:**

- Signing in the CLI.
- Where the blog-post files go.
- Whether to disable `cadenceux-dx` while trying 2.0.0.
- Launch or Release.

**Cost:**

- The blocked `claude -p` runs cost $0 (they failed before any model call).
- The Tester pass took 101,689 tokens and about 2 minutes (from its completion notice).
- The main session's tokens aren't reported to the Agent.

**Lesson for the skill:** installing first found three things publishing first would have
shipped:

- the blog files in the archive;
- two copies of the skill competing;
- the new name missing from `versions.json`, which shows UNKNOWN in the stack check.

## Sprint 1, 2026-11-26: build 2.0.0 (Developer hat, mostly the Agent)

**Done:** Built the release in the working folder, uncommitted on `main`:

- `references/sprints-and-hats.md` (new), and the rules in SKILL.md's "How the work runs".
- Hands off the referee in `linter-tests.md`; document the why in `working-agentically.md`.
- The rename, with `maintainer/build_twins.py`, the stack check's same-skill groups, README,
  CHANGELOG, plugin.json, VERSION.
- 10 new eval cases, and a results file.

**Changed, and why:**

- **Four hats became six,** adding the Reviewer and the Orchestrator. The blog post's process
  needs a hat that checks the Agent's work and a hat that decides when to stop, and both are
  the Developer's.
- **The thinking hats are weighted, not mapped one to one.** Options considered: one thinking
  hat per development hat (what the no-skill baseline suggested), or all six on every hat at
  different weights. Chose weights, because one-to-one leaves Red and Black out of most stages,
  and those are the two an Agent skimps on.
- **The rules sit in SKILL.md; the detail sits in the reference.** Haiku skipped the hook and
  the optimisation pass until each was a SKILL.md rule. A rule an Agent must follow on every
  task can't depend on it opening a second file.
- **Renamed to `cadenceux-developer-experience`, version 2.0.0.** The owner's call: "dx" isn't
  known yet. Earlier names stay as generated twins so nothing breaks.
- **"Loop" became "sprint".** The owner asked for known agile terms.
- **The description was shortened to 952 characters.** Each twin adds a line, and a twin over
  1,024 characters would fail validation. The twin builder test found this.

**For users:** People who know `cadenceux-dx` have to learn:

- a new name;
- six hats instead of four;
- being asked which hat a task needs, which may feel like friction on small jobs (the skill
  says to state the hat and carry on for one clear change);
- two new files in their projects (`docs/plan.md`, `docs/sprint-log.md`).

The routing, the stack check and the decision guides stay where they were.

**Verified:**

- Evals in fresh subagents: 10 new cases on Haiku, Sonnet and Opus, 9 of 10 passing, with
  `six-hats` partial (the hats are named; the stage order isn't recited). Both baselines
  (released 1.0.2 and no skill, Sonnet) scored 0 of 10.
- Regression: routing, linter, deploy and earlier names pass on Haiku and Sonnet.
- `validate_skill.py` clean.
- Stack check group logic tested with faked installs.
- Twin builder run into scratch git checkouts.

**Not verified:**

- The skill installed and used in a real session (this sprint read the folder through
  subagents, not as an installed skill).
- The stack check against a real `versions.json` that lists the new name.
- A release archive built from a tag.
- Trigger tuning of the new description.
- Windows.

**Next:** Sprint 2: install locally, Test as a separate pass from `docs/plan.md`, then the
owner's Review.

**Waiting on:**

- Launch or Release as the last stage's name.
- Where the four blog-post files at the repo's top level should go.
- Whether to disable the `cadenceux-dx` plugin while 2.0.0 is being tried, so the two don't
  compete.

**Cost:**

- About 4.6 million subagent tokens over 65 eval runs: baselines 1.25 million (20 runs),
  2.0.0 about 3.35 million (45 runs).
- The main session's own tokens aren't reported to the Agent; read them from Claude Code's
  usage for this session.
- Estimate: one sprint for the build. Actual: one sprint (one session).

**Lesson for the skill:** the plan was written after this sprint, not before. The brief and
the owner's answers lived only in the conversation, so no fresh session could have picked the
work up from the repo. That's the case for "write the plan before the first sprint".
