# cadenceux-developer-experience

A [Claude skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
for the developer experience of agentic Claris FileMaker work, with or without Claris's
FileMaker Agentic Development Kit (ADK). It directs you and the agent through agile sprints with
six development hats, routes each task to the skill or tool that owns it, checks your stack is
current, and guides the decisions around the code.

Also published under its earlier names, [`cadenceux-dx`](https://github.com/CadenceUX/cadenceux-dx-skill)
and [`fmp-dev-orchestrator`](https://github.com/CadenceUX/fmp-dev-orchestrator-skill): the same
skill, built from this repo. Install one, not more.

Built and maintained by [Darrin Southern](https://www.linkedin.com/in/darrin-southern/) from [CadenceUX](https://cadenceux.com.au).

## What it does

**Runs the work in agile sprints.** Analyse on the way in; then Plan, Design, Build, Test and
Review as a sprint, as many times as it takes; then Launch. After every Review, you decide:
another sprint, or launch.

| Hat | Stage | Usually worn by |
|---|---|---|
| Analyst | Analyse, Plan | You, with the agent asking and drafting |
| Architect | Design | You, with the agent offering options |
| Developer | Build | Mostly the agent |
| Tester | Test | The agent runs tests; you judge them |
| Reviewer | Review: code, tests, result, and an optimisation pass on code, UI and UX | You, with the agent preparing it |
| Orchestrator | Another sprint or launch | Always you |

The agent asks which hat a task needs before it starts. No hat signs off its own work, and
nothing launches until Test and Review have both had their turn. Every hand-back uses de Bono's
thinking hats: what was verified and how (White), the riskiest part first (Black), how it will
feel to the people using it (Red), and what needs your yes (Blue). The agent writes the plan
down before the first sprint and a sprint update after every one, never changes a linter test
alongside the code it checks, records the why behind each change for Developer Next, estimates
in sprints rather than hours from a human-team baseline, and records the token cost of each job
where the harness reports it.

**Routes the work.** Anything that reads or changes the FileMaker file goes through ADK when
it's available. Everything else goes to the skill that owns it:

| Topic | Owner |
|---|---|
| Schema, scripts, layouts, value lists, custom functions, live SQL, web viewer apps, standards | Claris ADK |
| Functions, script steps, error codes, Data API, OData, ExecuteSQL | `claris-filemaker-pro` |
| CadenceUX conventions and patterns, client standards | `fmp-dev-design-patterns` with the [`cadenceux` pack](https://github.com/CadenceUX/cadenceux-filemaker-standards) |
| BaseElements, MBS and bBox plug-ins | `goya-be-plugin`, `monkeybread-mbs-plugin`, `beezwax-bbox-plugin` |
| FileMaker Server and OttoFMS in Docker | `cadenceux-fms-docker-setup`, `cadenceux-ottofms-docker-setup` |
| Server security checks | `cadenceux-fms-security` |
| GitHub, and scanning skills before you install them | `cadenceux-github` |
| Building Claude skills | `cadenceux-skill-creator` |

**Checks the stack**, once per session and read-only: installed CadenceUX skills, ADK against
Claris's latest, FileMaker Pro against ADK's minimum (26.1; hosted files need FileMaker Server
26.1.1), and your ADK project's standards pack and packages. Ask "is my FileMaker stack up to
date?" for the full report. It never updates anything without asking.

**Guides the decisions:**

- FileMaker 26.0.3 and earlier: what extra code a job needs, and when to upgrade
- Native layouts, a web viewer app, or hybrid
- Relationships, ExecuteSQL, the Data API or OData, or native scripts
- Reviewing an existing system: the questions to ask first
- Which linter tests to build
- Security and deployment review

**And the habits underneath:** knowledge delegation, agentic time, briefing helper agents,
and reviewing again when the harness changes.

## Install

**Claude Code** (from the `cadenceux` plugin marketplace):

```bash
claude plugin marketplace add https://github.com/CadenceUX/cadenceux-skills.git
claude plugin install cadenceux-developer-experience@cadenceux
```

If `cadenceux-dx` or `fmp-dev-orchestrator` is also installed, keep one: they're the same skill.

**claude.ai and Cowork:** Customize → Plugins → Add marketplace from GitHub →
`CadenceUX/cadenceux-skills`, then install **cadenceux-developer-experience**.

**Claude desktop app (macOS):** download [`cadenceux-developer-experience.skill`](https://github.com/CadenceUX/cadenceux-developer-experience-skill/releases/latest/download/cadenceux-developer-experience.skill) and
double-click it.

**Claude.ai in a browser, as a single skill:** Customize → Skills → upload
[`cadenceux-developer-experience.zip`](https://github.com/CadenceUX/cadenceux-developer-experience-skill/releases/latest/download/cadenceux-developer-experience.zip).

> Both files are attached to the latest [release](https://github.com/CadenceUX/cadenceux-developer-experience-skill/releases).
> Don't use GitHub's green **Code → Download ZIP** button or a release's **Source code (zip)**:
> those are snapshots of the repository, not a packaged skill, and Claude won't install them
> as one.

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Use it, fork it, adapt it. Attribute it.

Built and maintained by [Darrin Southern](https://www.linkedin.com/in/darrin-southern/) from [CadenceUX](https://cadenceux.com.au).
