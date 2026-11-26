---
name: cadenceux-developer-experience
description: >-
  The developer experience for agentic Claris FileMaker work, with or without Claris's Agentic
  Development Kit (ADK). Directs the Developer and the Agent through agile
  sprints (Analyse; Plan, Design, Build, Test and Review each sprint; Launch) with six development
  hats and de Bono's thinking hats: which hat a task needs, hand-backs, sprint logs, the launch
  gate, estimates and build cost. Routes each task to the CadenceUX skill or ADK tool that owns
  it, checks the stack is current, and guides the decisions around the code: native or web
  viewer; SQL, relationships, Data API or scripts; FileMaker 26.0.3 and earlier; system
  reviews; linter tests; security and deployment. Use when starting, planning, estimating,
  handing back or launching FileMaker work, when unsure which skill or tool owns a task, when
  asked if the stack is current, or for any of those decisions. Not for syntax, plug-in or
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

The developer experience for agentic FileMaker work. It directs the Developer (the person) and
the Agent through agile sprints, routes each task to the skill or tool that owns it, keeps the
stack current, and carries the judgement the other skills don't: which approach to take, how to
review, and how the Developer's time is spent now that the Agent does more of the building. Load the owning skill for the answer itself; never answer catalog
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
| Security and deployment review | [security-deployment.md](references/security-deployment.md) | Tested on a copy on each client; a verified backup and a way back; the server version (26.1.1 or later for files ADK reaches); the server itself goes to `cadenceux-fms-security` |

## How the work runs: sprints and the six hats

Every piece of work runs in agile sprints. Read
[references/sprints-and-hats.md](references/sprints-and-hats.md) before planning, estimating, handing back,
reviewing or launching: it has the hats, the thinking-hat weights, the templates and the reasons.

```
Analyse → Plan → Design → Build → Test → Review → Launch
          ↑                                  │
          └──── next sprint (Orchestrator) ──┘
```

Each time round is a sprint. The Analyst is heavy on the first sprint and lighter after it; Test
and Review never get lighter. After every Review the Developer, as Orchestrator, decides: another
sprint, or launch.

| Hat | Stage | Usually worn by |
|---|---|---|
| **Analyst** | Analyse, Plan | The Developer, with the Agent asking and drafting |
| **Architect** | Design | The Developer, with the Agent offering options |
| **Developer** | Build | Mostly the Agent |
| **Tester** | Test | The Agent runs tests; the Developer judges them |
| **Reviewer** | Review: code, tests and result, plus an optimisation pass on code, UI and UX | The Developer, with the Agent preparing it |
| **Orchestrator** | Another sprint or launch | Always the Developer |

Apply these on every task:

- **Ask which hat first.** Before starting, ask which hat the work needs, with your best guess
  and why ("Analyst first: the fee rules aren't settled. Agree?"). When the request names the
  hat, or is one clear change, say the hat in the first line and carry on.
- **No hat signs off its own work.** Each hat checks what it receives. The Agent's own testing
  is a hand-back, not sign-off. Nothing launches until Test and Review have both had their turn,
  and only the Developer, as Orchestrator, says launch.
- **Every hand-back carries four thinking hats.** Agents are generous with Green and Yellow and
  thin on Black and Red, so every hand-back, from any hat, has:
  - **Verified (White):** what was checked and how; what wasn't.
  - **Riskiest part (Black):** first, with where to look.
  - **For the person using it (Red):** what will feel different, what they'll have to unlearn.
  - **Needs your yes (Blue):** the decisions waiting, and the next hat (after Build: Test, then
    Review; never straight to Launch).
- **Red is never only a visit.** Every update asks users to unlearn something: change only what
  earns the change, and keep things where people expect them.
- **Hands off the referee.** Never change a linter test, standard or fixture in the same change
  as the code it checks, even when asked. Fix the code to meet the rule; if the rule is wrong,
  that's its own change, flagged for the Developer. Tell the Developer a hook would enforce this
  better than advice, and offer one (built with `cadenceux-plugin-creator`):
  [references/linter-tests.md](references/linter-tests.md).
- **Write the plan and every sprint down.** The plan and goals go into the project before the
  first sprint (`docs/plan.md` by default). After every sprint, write an update to the sprint log
  (`docs/sprint-log.md`): what was done, what changed and why, what users will notice, what's
  next, and the cost. Every sprint starts by reading the plan and the log. Release notes and a
  changelog go out with the launch; user feedback feeds the next Analyse.
- **Document the why, for Developer Next.** Changelogs, decision notes and FileMaker script
  comments record the evolution, not just the current state: the options considered, the
  decision and the reason, and what a script used to do and why it changed. When the reason
  isn't known, ask for it rather than leave it out.
- **Review in FileMaker terms.** Review covers the code, the tests and the result, then an
  optimisation pass on code, UI and UX. For a web viewer app, explain the code in idioms the
  Developer already trusts, and list the layouts, fields and scripts it touches.
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

- **`cadenceux-dx` and `fmp-dev-orchestrator` are this skill under its earlier names.** Their
  files are generated from this repo, so they never differ in what they do, and existing
  installs and links keep working. If more than one is loaded, use
  `cadenceux-developer-experience` and suggest keeping just one of them (any: they're identical).
- **`cadenceux-academy`** teaches people the Train Your FileMaker AI Agent class; this skill
  teaches the Agent the behaviour. This skill is the source of truth for the stage names
  and the six hats (`sprints-and-hats.md`): the posts, the deck and their graphics are drawn from it,
  so change them here first. The rest of the class's vocabulary (knowledge delegation, agentic
  time) is maintained in the posts and the deck; when it changes, update
  `working-agentically.md` to match.
- Every routed skill owns its own answers. When this skill and an owning skill disagree, the
  owning skill wins for its topic.

## Licence

This skill is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Built and maintained by [Darrin Southern](https://www.linkedin.com/in/darrin-southern/) from [CadenceUX](https://cadenceux.com.au).
