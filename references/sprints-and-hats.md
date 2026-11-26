# Sprints and the six hats

How the Developer and the Agent run a piece of FileMaker work together, and why. The stage
names and hat assignments here are the source for Darrin Southern's posts (Agentic Time
Traveller, Six Thinking Hats, One Developer) and the Train Your FileMaker AI Agent class.

## Contents
- Sprints
- The six development hats
- Asking which hat
- Thinking hats on every development hat
- The hand-back
- The plan and the sprint log
- Launch
- Reviewing in FileMaker terms
- Estimates you can defend
- The cost of the build

## Sprints

```
Analyse → Plan → Design → Build → Test → Review → Launch
          ↑                                  │
          └──── next sprint (Orchestrator) ──┘
```

- **Analyse** comes first, on the way in: the need, the people who use it, what done looks like.
- **Plan, Design, Build, Test, Review** repeat. Each time round is a sprint.
- **After every Review** the Developer, wearing the Orchestrator hat, decides: another sprint,
  or launch. The Agent recommends, with its evidence; it never makes this call.
- **The Analyst is heavy on the first sprint** (the need, the plan, the goals) and lighter after
  it (checking the plan still holds and folding in what the last sprint taught).
- **Test and Review never get lighter.** The Agent builds more each sprint, so there is more to
  check, not less.
- **After Launch,** user feedback goes into the next Analyse.

Why sprints: the Agent makes building cheap, so the risk moves to building the wrong thing, or
shipping something nobody checked. Short sprints with a decision at the end of each keep the
Developer in charge of direction while the Agent does the volume.

## The six development hats

The four hats from Agentic Time Traveller (Analyst, Architect, Developer, Tester), plus the
Reviewer and the Orchestrator.

| Hat | Stage | What it does | Who wears it |
|---|---|---|---|
| **Analyst** | Analyse, Plan | The need, the people, what done looks like; the plan and goals for each sprint | The Developer leads; the Agent asks and drafts |
| **Architect** | Design | Schema, where logic lives, native or web viewer, deployment; designs for what users will have to unlearn | The Developer decides; the Agent offers options with their costs |
| **Developer** | Build | Makes the change | Mostly the Agent |
| **Tester** | Test | Checks the build against the plan's definition of done: edge cases, each client, real-looking data | The Agent runs tests; the Developer judges whether they're enough |
| **Reviewer** | Review | Reviews the code, the tests and the result, then an optimisation pass on code, UI and UX | The Developer, with the Agent preparing it from a fresh context |
| **Orchestrator** | After each Review | Decides another sprint or launch; owns scope and the launch date | Always the Developer |

Two rules hold every sprint together:

- **No hat signs off its own work.** Each hat checks what it receives: the Tester checks the
  build, the Reviewer checks the build and the tests, the Orchestrator checks the review. When
  the Agent has built something, its own "it works" is a hand-back, not a test result. If the
  Agent also wears the Tester hat, it runs Test as a separate pass that starts from the plan, not
  from its memory of building, in a fresh session or subagent where the harness allows.
- **Nothing launches until Test and Review have both had their turn.** A keen client, a deadline
  or the Agent's confidence doesn't change that; it changes how small the sprint should be.

## Asking which hat

Before starting, ask which hat the work needs. Give a best guess and the reason, so the
Developer can answer in a word:

> This needs the Analyst first: whether the fee compounds, and from which date, isn't settled
> yet. Start there, or is that decided and it's straight to Build?

Signals: no definition of done means Analyst. A settled need with an open design (where it
lives, which tables) means Architect. A clear spec means Build. "Is it right?" means Tester or
Reviewer. "Can we ship it?" is the Orchestrator, which is the Developer's call; bring the
evidence.

When the request names the hat, or is one clear change with a known outcome, say the hat in
the first line ("Build: one field and one layout change") and carry on.

## Thinking hats on every development hat

Edward de Bono's six thinking hats: **White** (facts: what we know and how), **Red** (feelings:
how it will feel to use), **Black** (caution: what could go wrong), **Yellow** (benefits: what
it gains), **Green** (ideas: other ways to do it), **Blue** (process: what's decided, what's
next). Every development hat uses all six, at different weights:

- **Lead:** the main way of thinking for that hat.
- **Support:** always present.
- **Visit:** checked on purpose, briefly.

| Development hat | Lead | Support | Visit |
|---|---|---|---|
| Analyst | White, Blue | Red, Green | Black, Yellow |
| Architect | Green, Black | Red, White | Yellow, Blue |
| Developer | White, Green | Black, Red | Yellow, Blue |
| Tester | Black, White | Red, Green | Yellow, Blue |
| Reviewer | Black, Red | White, Green | Yellow, Blue |
| Orchestrator | Blue, Yellow | White, Black, Red | Green |

**Agents are generous with Green and Yellow** (options, and what's good about them) **and thin
on Black and Red** (what could go wrong, and how it will feel to use). Correct for it: keep
Green and Yellow visits short, and never skip Black or Red.

**Red is never only a visit.** Every update asks users to unlearn something. The Architect and
the Developer design and build for that:

- Change only what earns the change.
- Keep things where people expect them: same layout, same button position, same names.
- When something must move or go, say where it went and why, in the release notes and, for a
  while, on the screen itself.

## The hand-back

Every hand-back, from any hat, carries four of the thinking hats, in this order:

1. **Verified (White):** what was checked and how (evaluated on the engine, read back from the
   file, run on which test data, on which clients), and what wasn't.
2. **Riskiest part (Black):** first, before the good news, with where to look.
3. **For the person using it (Red):** what will feel different, what they'll have to unlearn,
   what stays where it was.
4. **Needs your yes (Blue):** the decisions waiting on the Developer, and the next hat. After a
   build that's Test, then Review; never straight to Launch.

Green and Yellow can follow if they add something. Keep the whole thing short enough to read
before acting on it.

## The plan and the sprint log

**Before the first sprint,** write the plan and goals into the project. Default: `docs/plan.md`,
unless the project already has a place for it. It holds the need, the goals and what done
looks like, what's out of scope, the decisions made so far, and the first estimate.

**After every sprint,** the Agent writes an update to the sprint log. Default:
`docs/sprint-log.md`, newest first:

```markdown
## Sprint 3, 2026-11-26: bookings screen

**Done:** what was built, tested and reviewed this sprint.
**Changed, and why:** each change with its reason, and the options considered where there was
a choice.
**For users:** what they'll notice, and what they have to unlearn.
**Verified:** how, and on what. **Not verified:** what wasn't, plainly.
**Next:** the next sprint's goal. **Waiting on:** decisions that need the Developer's yes.
**Cost:** tokens and time where the harness reports them; this sprint's estimate against actual.
```

**The next sprint reads the plan and the sprint log first,** before any other file. That's how
a fresh session, a helper agent or Developer Next picks up where the last one stopped. Where a
fact is missing (why a button was dropped, what the logs covered), write what's known, mark the
gap, and ask; never invent the reason.

## Launch

Launch only on the Orchestrator's word, after Test and Review. With the launch:

- **Release notes** for users: what's new, what moved, what's gone and why.
- **A changelog entry** for developers.
- The deployment checks: a verified backup, a way back, tested on a copy on each client.

After launch, collect what users say and do. It feeds the next Analyse.

## Reviewing in FileMaker terms

The Reviewer covers the code, the tests and the result, then an optimisation pass on all three
of code (simpler, fewer calls, nothing duplicated), UI (consistent with the rest of the
solution) and UX (fewer steps, nothing moved without a reason).

For a web viewer app, the Developer trusts FileMaker, not React. Explain the code in the
idioms they already know:

| In the web code | The FileMaker idiom |
|---|---|
| A component | A layout object, or a group of them reused across layouts |
| Props passed to a component | Script parameters |
| State held in the app | A global variable or global field scoped to the screen |
| An effect that runs on load or on change | A script trigger (OnLayoutEnter, OnObjectModify) |
| A call through the web viewer bridge | Perform Script with a parameter, reading the script result |
| The typed layout from typegen | The fields on that layout, as the Data API sees them |
| Routes | Layouts, and Go to Layout |

Then list everything the app touches, so the Developer can check it in FileMaker itself:

- **Layouts** it reads or writes through, by name.
- **Fields** on each, read or written.
- **Scripts** it calls, with the parameter it sends and the result it expects.

Read the list from the code and the typegen output, not from memory; with ADK, confirm each
name exists in the file.

## Estimates you can defend

- **No hours from a human-team baseline.** The Agent changes which parts take the time, so
  scaling a team's hours by a guessed factor gives a number nobody can defend.
- **Estimate in sprints:** how many to reach the plan's definition of done, and what each one
  delivers.
- **Re-estimate after the first build day,** from what that day actually delivered.
- **Keep actuals,** sprint by sprint, beside the estimate in the sprint log.
- **Say what doesn't shrink:** Analyse, Test, Review, waiting for decisions, training and
  handover.

A real case: a CadenceUX project with an Agent-assisted estimate of 1,200 hours was
re-estimated at 120 hours after two build days, and may finish at half of that. The first
figure would have priced the client out; only the re-estimate from actuals was defensible.

## The cost of the build

Where the harness reports it, record the token cost of each job (and the time) in the sprint
log: Claude Code reports session cost and usage, a subagent's completion notice carries its
tokens, and the API returns usage with each response. Where the harness doesn't report it, say
so rather than estimate it as if it were measured. Over a project, those figures let the
Developer price the outcome (value-based billing) instead of hours, and see what each kind of
job really costs.
