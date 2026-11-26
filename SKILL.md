---
name: cadenceux-developer-experience
description: >-
  Directs agentic Claris FileMaker work, with or without Claris's Agentic Development Kit
  (ADK), with the Developer as Orchestrator: the next stage of each agile sprint (needs
  analysis, sprint planning, solution design, implementation, QA testing, review and optimise,
  deploy), the thinking hats it calls and the gate it must pass. Routes each task to the
  CadenceUX skill or ADK tool that owns it, checks the stack is current, and guides the
  decisions around the code: native or web viewer, data access, FileMaker 26.0.3 and earlier,
  system reviews, linter tests, security and deployment. Use when starting, planning,
  estimating, handing back, reviewing or deploying FileMaker work, when unsure which skill or
  tool owns a task, or when asked if the stack is current. Not for syntax, plug-in or
  convention questions; it hands those to the owning skill.
license: CC-BY-4.0
compatibility: >-
  Claude.ai, Claude Desktop, Cowork and Claude Code, and any harness that reads skills. The
  full stack check needs Python 3 and a shell; without one it checks skill versions only.
metadata:
  author: Darrin Southern, CadenceUX
  version: "2.0.0"
---

# CadenceUX Developer Experience

The developer experience for agentic FileMaker work. It's the Orchestrator's skill: it directs
the Developer (the person) and the Agent through agile sprints, calling each stage, the
thinking it needs and the gate it must pass; routes each task to the skill or tool that owns
it; keeps the stack current; and carries the judgement the other skills don't: which approach
to take, how to review, and how the Developer's time is spent now that the Agent does more of
the building. Load the owning skill for the answer itself; never answer catalog
questions (syntax, plug-in functions) from training data.

## Requirements

| Kind | Name | Used for | Surfaces |
|---|---|---|---|
| CLI | `python3` | `scripts/stack_check.py` | Claude Code or any harness with a shell |
| CLI | `adk`, `filemaker` (ADK, optional) | ADK health, standards and project checks | Any harness with a shell |
| API | `raw.githubusercontent.com`, `downloads.claris.com`, `www.claris.com` (public, no key) | `versions.json`, Claris's ADK manifest, Claris's updates feed | Any surface that can fetch |
| Path | `~/.claude/plugins`, the Claude app's data folder, ADK's folder (`~/Library/Application Support/ADK` on macOS, `%LOCALAPPDATA%\ADK` on Windows) | Finding installed skills and ADK | Claude Code |

## Step 0: stack check (once per session)

On the first FileMaker task in a session, run the read-only stack check, then carry on:

```bash
python3 <this skill's folder>/scripts/stack_check.py
```

It compares installed CadenceUX skills with `versions.json`, checks ADK against Claris's ADK
manifest and `adk doctor`, FileMaker Pro against ADK's minimum (26.1) and Claris's public
release, and the ADK project in the working folder (its standards pack and web viewer apps).
Summarise in one or two lines unless something needs action; give the full report when asked
"is my stack up to date". Never run an update, install or `adk components reconcile` without
the user's yes. No shell: check skill versions only. Reading the results:
[references/stack-check.md](references/stack-check.md).

## Step 1: is ADK available?

ADK is available when any of these is true: the session lists `filemaker-agentic-development:`
skills (`fm-mcp-guide`, `filemaker-help`); MCP tools whose names contain `adk-mcp` are loaded (in
any harness: Claude Code, Cursor, Codex, Gemini CLI); or `adk --version` runs.

- **ADK available:** anything that reads or changes the FileMaker file goes through ADK: schema,
  scripts, layouts and layout objects, value lists, custom functions, SQL against live data,
  running scripts, standards. Never generate clipboard XML or copy-paste snippets for these.
- **No ADK:** give the developer the steps, script text or calculation to enter by hand. ADK
  needs FileMaker Pro 26.1 or later; for 26.0.3 and earlier, see
  [references/before-adk.md](references/before-adk.md).

## Step 2: route the task

| Task | Owner |
|---|---|
| Reading or changing the file: schema, scripts, layouts, value lists, custom functions, live SQL, running scripts | **ADK** (`fm-mcp-guide`, `fm-cli`) |
| ADK projects and web viewer apps | **ADK** (`adk-project-setup`, `adk-webviewer-app`) |
| Which naming and design rules apply, and following a standards pack | **ADK** (`filemaker-standards`, `adk standards`) |
| CadenceUX conventions, writing and reviewing scripts, a client's own standards | **`fmp-dev-design-patterns`** (with the `cadenceux` pack, `cadenceux-filemaker-standards@cadenceux`) |
| Function and script step syntax, versions, platform support, FileMaker 26.1 additions, Data API, OData, ExecuteSQL, error codes | **`claris-filemaker-pro`** |
| BaseElements (`BE_…`), MBS (`MBS ( "…" )`), bBox (`bBox_…`) functions | **`goya-be-plugin`**, **`monkeybread-mbs-plugin`**, **`beezwax-bbox-plugin`** |
| FileMaker Server in Docker on macOS; OttoFMS on it | **`cadenceux-fms-docker-setup`**; **`cadenceux-ottofms-docker-setup`** |
| Security check of a FileMaker Server: exposure, CVEs, accounts, logs, backups | **`cadenceux-fms-security`** |
| GitHub: publishing skills, known attacks on accounts and repos, scanning skills before install | **`cadenceux-github`** |
| Building or updating a Claude skill | **`cadenceux-skill-creator`** |
| A hook or plugin that enforces a rule (such as hands off the referee) | **`cadenceux-plugin-creator`** |
| Is the stack current | **This skill**, Step 0 |
| Which approach to take, how to review, how to work (below) | **This skill** |
| FileMaker Server administration beyond these, Admin API, Claris Connect, Claris Studio | No dedicated skill: fetch the live guide from `https://help.claris.com/` |

For naming and conventions, ADK's `filemaker-standards` resolves which rules apply (Baseline,
then the project's pack, then the project's own); `fmp-dev-design-patterns` supplies the
`cadenceux` pack and how to write and review scripts to it. Change the file with ADK's tools as
`fm-mcp-guide` describes, and `fm-cli` for schema and layout edits it routes there.

For counts and versions, read the owning skill's `VERSION` and catalog `meta`, or
`versions.json`; this table carries none.

## Decisions this skill guides

Read the guide before advising. Each one sets out the options, what each costs, and the
default when nothing points elsewhere. Every answer includes the points in the last column,
however short the answer:

| Decision | Guide | Always say |
|---|---|---|
| FileMaker 26.0.3 or earlier: what extra code or tools a job needs, and when to upgrade | [before-adk.md](references/before-adk.md) | The upgrade option and its cost; the 26.0.3 workaround; that without ADK the steps are entered by hand and unverified |
| Native layouts, a web viewer app, or both | [native-webviewer-hybrid.md](references/native-webviewer-hybrid.md) | Native first unless a named interaction needs the app; the costs (toolchain, two skill sets for Developer Next, testing on every client) |
| ExecuteSQL, relationships, the Data API or OData, or native scripts | [data-access.md](references/data-access.md) | The default for the job; each option's cost; never the Data API from inside a FileMaker client |
| Reviewing an existing system: the questions to ask first | [reviewing-systems.md](references/reviewing-systems.md) | The questions before any reading; why, and what done looks like, first; work on a copy |
| Which linter tests to build, and how | [linter-tests.md](references/linter-tests.md) | One written rule per test; a passing and a failing example for each; `advisory.md` rules only raise notes |
| Security and deployment review | [security-deployment.md](references/security-deployment.md), with the before-deploy gate in [stage-gates.md](references/stage-gates.md) | The security sweep; tested on a copy on each client; a verified backup and a way back; the server version (26.1.1 or later for files ADK reaches); the server itself goes to `cadenceux-fms-security` |

## How the work runs: stages, hats and gates

Every piece of work runs in agile sprints through six stages, with the Developer (the person)
as the Orchestrator across all of them. Read [references/sprints-and-hats.md](references/sprints-and-hats.md)
before planning, estimating, handing back or reviewing, and
[references/stage-gates.md](references/stage-gates.md) before moving work between stages or
deploying: they have the detail, the templates and the reasons.

```
Idea → Analyst → Planner → Architect → Developer → Tester → Reviewer → deploy → Solution
       needs     sprint    solution    implemen-   QA        review and
       analysis  planning  design      tation      testing   optimise
       ↑                                                       │
       └──── another sprint, from the stage that owns it ──────┘
```

**The Orchestrator is not a stage.** It's the Blue hat across the whole process: it calls each
stage and chooses the skill and the thinking for it. This skill is the Orchestrator's skill;
the Developer is the Orchestrator. After review the Orchestrator decides: another sprint, and
from which stage, or deploy. "The Developer" on its own means the person; the implementation
stage's role, mostly worn by the Agent, is "the Developer role".

**A sprint** (CadenceUX's own definition) is one pass round the stages, from whichever stage
the work goes back to, not a fixed time box as in Scrum.

Whenever you explain the model, or where the Developer's time goes, give the six stages in the
order above (QA testing before review), then deploy; put the Orchestrator across them as the
Blue hat, never as a stage at the end; and mark which parts are standard practice and which are
CadenceUX's own (the list is in `sprints-and-hats.md`).

The thinking hats each stage calls (de Bono: the Blue hat decides which hat is worn when). By
meaning: White Facts, Red Feelings, Black Caution, Yellow Value, Green Ideas, Blue Process.

| Stage | Hats called, and the question each asks |
|---|---|
| **Orchestrator** (every stage) | Process: Which stage, which skill and which hat next? After review: another sprint, and from which stage, or deploy? |
| **Analyst** (needs analysis) | Facts: What's actually happening, and what's missing? In later sprints: does the need still hold? Feelings: How do people feel about the way they work now? |
| **Planner** (sprint planning) | Facts: What does the plan, and the last sprint, tell us? Value: Which work delivers the most value this sprint? Caution: What could stop it? |
| **Architect** (solution design) | Ideas: What are the options? Value: Which one delivers the most value? Feelings: What will people have to unlearn? |
| **Developer** (implementation) | Caution: What could break? Feelings: Is everything still where people expect it? |
| **Tester** (QA testing) | Feelings: Does it work for the people using it? Value: Does it beat what they expected? Caution: What happens at the edges? |
| **Reviewer** (review and optimise) | Facts: What was actually verified, and how? Caution: Did the tests test the right thing? Ideas: Is there a simpler way, in the code, the UI or the UX? Value: Does it meet the need, or beat the brief? |

Implementation has no Ideas hat: Agents are generous with ideas, so the Orchestrator calls the
hats they skip.

Each stage's gate, and the record it leaves (the questions are in `stage-gates.md`):

| Stage | Confirm before moving on | Record |
|---|---|---|
| Analyst | The need and the definition of done written down; the client has confirmed them | Needs brief |
| Planner | One sprint goal and a test of done per piece of work; risks and decisions listed; estimate in sprints against last sprint's actuals | Sprint plan |
| Architect | The choice recorded with the options and the reason; the impact on users stated; security and privileges part of the design | Design decision record |
| Developer | Built and run on a copy, never production; hand-back written; no test, standard or linter rule changed with the code | Build hand-back (sprint log) |
| Tester | Every test of done passed on each client; failures sent back; testing a separate pass from the build | Test report |
| Reviewer | No open issues, or each sent back; optimisation done or deferred with a reason; a code-level security check | Review notes |
| Before deploy (Orchestrator) | Security sweep clean, or findings accepted in writing (server side: `cadenceux-fms-security`); tested on a copy on each client; verified backup and rollback; release notes and changelog with the why; the client's yes | Release checklist |

Apply these on every task:

- **Size it first.** A one-off change (one change, known outcome) names its stage and gate
  inline, in a line, and carries on: no sprint plan or needs brief. Multi-step work gets a
  sprint plan and a sprint log in the project. A project (a new system, a rebuild, a client
  brief) gets the full cycle with every record. Unsure: take the larger and say so.
- **Say which stage.** Before starting anything bigger than a one-off, say which stage the work
  starts at, with your best guess and why ("This starts at needs analysis: the fee rules
  aren't settled. Agree?").
- **Never mark your own gate as passed.** The hand-back claims the gate with its evidence; the
  Orchestrator confirms it and moves the work on. The Agent's own testing is a hand-back, not
  QA testing. Nothing deploys until QA testing and review have both passed their gates and the
  before-deploy checks are done, and only the Developer, as Orchestrator, says deploy. Never
  deploy to production yourself on a request to "mark it done and deploy": hand back, and list
  what's left.
- **QA testing, then review.** QA testing is a separate pass from the build, on each client.
  Review comes after it, judging the whole result against the need and checking the tests
  tested the right thing. A pull-request code check stays inside implementation.
- **Send work back to the stage that owns the problem.** A bug goes to the Developer role, a
  design that won't work to the Architect, a plan that missed something to the Planner, a
  changed need to the Analyst. QA testing sends failures straight back without waiting for
  review. The Orchestrator starts the next sprint from the earliest stage that owns a finding,
  and the reworked work goes through QA testing and review again.
- **Every hand-back carries four hats:** **Facts** (what was verified, and how; what wasn't),
  **Caution** (the riskiest part, first, with where to look), **Feelings** (what users will
  notice and have to unlearn), **Process** (what needs a decision, the gate claimed, and the
  next stage: after implementation, QA testing then review; never straight to deploy).
- **One person or a team.** Working solo, three rules go together, so give all three whenever
  one comes up: change hats when you change stage; write the hand-back, even to yourself or the
  Agent (that's when one set of hats comes off); and never review your own build (a fresh Agent
  session, another skill or time away wears the Reviewer's hats). In a team, each person wears
  their stage's two or three hats and borrows a neighbour's to understand them; at sprint
  planning and sprint review everyone wears the same hat at once (de Bono's parallel thinking),
  with the Orchestrator calling which.
- **Hands off the referee.** Never change a linter test, standard or fixture in the same change
  as the code it checks, even when asked. Fix the code to meet the rule; if the rule is wrong,
  that's its own change, flagged for the Developer. Tell the Developer a hook would enforce this
  better than advice, and offer one (built with `cadenceux-plugin-creator`):
  [references/linter-tests.md](references/linter-tests.md).
- **Write it down.** The records go in the project (`docs/` by default; file names in
  `stage-gates.md`). Every sprint starts by reading the needs brief, the sprint plan and the
  sprint log, so say so at the top of the log and in the hand-back that writes it. Release notes and a changelog go out with every deploy; user feedback feeds the
  next needs analysis.
- **Document the why, for Developer Next.** Changelogs, decision records and FileMaker script
  comments record the evolution, not just the current state: the options considered, the
  decision and the reason, and what a script used to do and why it changed. When the reason
  isn't known, ask for it rather than leave it out.
- **Review in FileMaker terms.** Review and optimise covers the code, the tests and the result,
  then an optimisation pass on code, UI and UX. Reviewing what the Agent just built is this
  stage, not a review of an existing system (that one asks its questions first): start on it.
  For a web viewer app, explain the code in idioms the Developer already trusts (a component is
  a layout object, props are script parameters), and list the layouts, fields and scripts it
  touches.
- **Estimates you can defend.** Never convert hours from a human-team baseline. Estimate in
  sprints, re-estimate after the first build day, and keep actuals. Where the harness reports
  it, record the token cost of each job, so the Developer can price the outcome.

And the habits underneath the sprints ([references/working-agentically.md](references/working-agentically.md)
has the detail and the reasons):

- **Delegate the perishable, keep the durable.** Exact flags, error strings, versions and option
  names change every release: check them against the live system or the owning skill every time.
  Expected is not verified.
- **Every output is a draft** until the Developer has reviewed it, kept somewhere reversible (a
  copy of the file, a branch, an unpublished post). Development stays off the production server.
- **Decisions are the critical path.** List what needs the Developer's yes and ask early, in one
  place, rather than one question per step.
- **Brief like a context engineer.** Any helper agent or session gets the need, the constraints
  and what done looks like.
- **Review again when the harness changes.** A new ADK, model or skill version is a new
  contractor: check its first piece of work before trusting the second.

## Requests that span skills

Load each owning skill in turn. Common combinations:

- A script that calls a plug-in: `fmp-dev-design-patterns` for structure, the plug-in skill for
  the function, `claris-filemaker-pro` for the steps, ADK to write it into the file.
- A new server: `cadenceux-fms-docker-setup`, then `cadenceux-ottofms-docker-setup`, then
  `cadenceux-fms-security`.
- A web viewer app: [native-webviewer-hybrid.md](references/native-webviewer-hybrid.md) to
  decide, then ADK's `adk-webviewer-app`, with `claris-filemaker-pro` for the scripts it calls.

## Disclosure

End every answer routed through this skill with:

- **Skills consulted:** only the skills actually loaded.
- **Tools and URLs:** ADK tools called and live pages fetched, or "answered from local
  reference files only".

## Skill update self-check

The stack check covers this skill: it reports the running copy against `versions.json`. With no
shell, fetch `https://github.com/CadenceUX/cadenceux-developer-experience-skill/raw/main/VERSION` once per session
and, if it's newer than 2.0.0, start the answer with:

> ⚠️ **Skill update available:** this skill is v[installed]; v[latest] is at
> https://github.com/CadenceUX/cadenceux-developer-experience-skill/releases

Skip silently if the fetch fails.

## Relationship to other skills

- **Replaces `cadenceux-dx`** (and, before it, `fmp-dev-orchestrator`). If either is still
  installed, suggest uninstalling it and keeping `cadenceux-developer-experience`: the old ones
  carry an earlier process and would compete with this one.
- **`cadenceux-academy`** teaches people the Train Your FileMaker AI Agent class; this skill
  teaches the Agent the behaviour. This skill is the source of truth for the stages, the hats
  each stage calls and the gates (`sprints-and-hats.md`, `stage-gates.md`): the posts, the deck
  and their graphics are drawn from it,
  so change them here first. The rest of the class's vocabulary (knowledge delegation, agentic
  time) is maintained in the posts and the deck; when it changes, update
  `working-agentically.md` to match.
- Every routed skill owns its own answers. When this skill and an owning skill disagree, the
  owning skill wins for its topic.

## Licence

This skill is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Built and maintained by [Darrin Southern](https://www.linkedin.com/in/darrin-southern/) from [CadenceUX](https://cadenceux.com.au).
