# cadenceux-developer-experience

A [Claude skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
for the developer experience of agentic Claris FileMaker work, with or without Claris's
FileMaker Agentic Development Kit (ADK). It directs you and the agent through agile sprints,
calling each stage, the thinking it needs and the gate it must pass; routes each task to the
skill or tool that owns it; checks your stack is current; and guides the decisions around the
code.

It replaces [`cadenceux-dx`](https://github.com/CadenceUX/cadenceux-dx-skill) (and, before it,
`fmp-dev-orchestrator`): if either is installed, uninstall it.

Built and maintained by [Darrin Southern](https://www.linkedin.com/in/darrin-southern/) from [CadenceUX](https://cadenceux.com.au).

## What it does

**Runs the work in agile sprints, with you as the Orchestrator.** Six stages, then deploy:

| Role | Stage | Thinking hats called |
|---|---|---|
| Analyst | Needs analysis | Facts, Feelings |
| Planner | Sprint planning | Facts, Value, Caution |
| Architect | Solution design | Ideas, Value, Feelings |
| Developer | Implementation (mostly the agent) | Caution, Feelings |
| Tester | QA testing | Feelings, Value, Caution |
| Reviewer | Review and optimise: the code, the tests, the UI and UX, against the need | Facts, Caution, Ideas, Value |

The Orchestrator isn't a stage: it's the Blue hat (Process) across the whole process, calling
each stage and choosing the skill and the thinking for it. That's you, and this skill is your
skill. After review you decide: another sprint, starting from the stage that owns the problem
(a bug, a design that won't work, a plan that missed something, a changed need), or deploy.
Six development roles plus de Bono's six thinking hats make the twelve hats.

**Gates at every stage.** Each stage has questions to ask, things that must be true before the
work moves on, and a record it leaves (needs brief, sprint plan, design decision record, build
hand-back, test report, review notes). Before deploy: a security sweep, testing on a copy on
each client, a verified backup and rollback, release notes with the why, and the client's yes.
The agent never marks its own gate as passed, so it can't jump from a working build straight
to production.

**Sized to the job.** A one-off change names its stage and gate in a line. Multi-step work gets
a sprint plan and a sprint log. A project gets the full cycle.

**One person or a team.** On your own: change hats when you change stage, write the hand-back
even to yourself, and never review your own build. In a team: wear your stage's hats, borrow a
neighbour's, and at sprint planning and review everyone wears the same hat at once.

**Says what's standard and what isn't.** De Bono's hats, sprint planning and review, quality
gates, decision records and release checklists are standard practice. A sprint as one pass
round the stages (not a fixed time box), needs analysis in every sprint, the Planner role, the
Orchestrator and the hats called at each stage are CadenceUX's own.

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

If `cadenceux-dx` or `fmp-dev-orchestrator` is still installed, uninstall it: this skill replaces them.

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
