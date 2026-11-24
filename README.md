# cadenceux-dx

A [Claude skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
for the developer experience of agentic Claris FileMaker work, with or without Claris's
FileMaker Agentic Development Kit (ADK). It routes each task to the skill or tool that owns it,
checks your stack is current, and guides the decisions around the code.

Also published as [`fmp-dev-orchestrator`](https://github.com/CadenceUX/fmp-dev-orchestrator-skill),
its earlier name: the same skill, built from this repo. Install one, not both.

Built and maintained by [Darrin Southern](https://www.linkedin.com/in/darrin-southern/) from [CadenceUX](https://cadenceux.com.au).

## What it does

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

**And how the work runs:** knowledge delegation, agentic time, the four hats (analyst,
architect, developer, tester), briefing helper agents, and reviewing again when the harness
changes.

## Install

**Claude Code** (from the `cadenceux` plugin marketplace):

```bash
claude plugin marketplace add https://github.com/CadenceUX/cadenceux-skills.git
claude plugin install cadenceux-dx@cadenceux
```

If `fmp-dev-orchestrator` is also installed, keep one: they're the same skill.

**claude.ai and Cowork:** Customize → Plugins → Add marketplace from GitHub →
`CadenceUX/cadenceux-skills`, then install **cadenceux-dx**.

**Claude desktop app (macOS):** download [`cadenceux-dx.skill`](https://github.com/CadenceUX/cadenceux-dx-skill/releases/latest/download/cadenceux-dx.skill) and
double-click it.

**Claude.ai in a browser, as a single skill:** Customize → Skills → upload
[`cadenceux-dx.zip`](https://github.com/CadenceUX/cadenceux-dx-skill/releases/latest/download/cadenceux-dx.zip).

> Both files are attached to the latest [release](https://github.com/CadenceUX/cadenceux-dx-skill/releases).
> Don't use GitHub's green **Code → Download ZIP** button or a release's **Source code (zip)**:
> those are snapshots of the repository, not a packaged skill, and Claude won't install them
> as one.

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Use it, fork it, adapt it. Attribute it.

Built and maintained by [Darrin Southern](https://www.linkedin.com/in/darrin-southern/) from [CadenceUX](https://cadenceux.com.au).
