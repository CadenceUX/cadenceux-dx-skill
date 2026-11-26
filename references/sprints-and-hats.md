# Sprints and the twelve hats

How the Developer and the Agent run a piece of FileMaker work together, and why. The stage
names, the hats called at each stage and the questions they ask are the source for Darrin
Southern's posts (Agentic Time Traveller, Six Thinking Hats, One Developer) and the Train Your
FileMaker AI Agent class. The gates each stage must pass are in `stage-gates.md`.

## Contents
- Words used here
- The stages
- The Orchestrator
- Sprints, and sending work back
- Asking which stage
- The thinking hats each stage calls
- The hand-back
- One person or a team
- What's standard practice and what's CadenceUX's own
- Reviewing in FileMaker terms
- Estimates you can defend
- The cost of the build

## Words used here

- **The Developer** on its own is the person. The person is the Orchestrator.
- **The Developer role** is the implementation stage's role, mostly worn by the Agent.
- **The twelve hats:** six development roles (Analyst, Planner, Architect, Developer, Tester,
  Reviewer) and de Bono's six thinking hats.
- **Thinking hats, by meaning:** White **Facts**, Red **Feelings**, Black **Caution**, Yellow
  **Value**, Green **Ideas**, Blue **Process**.
- **A sprint:** one pass round the stages, from whichever stage the work goes back to.
- **A gate:** what must be true before work leaves a stage. **A record:** what the stage leaves
  behind.

## The stages

```
Idea → Analyst → Planner → Architect → Developer → Tester → Reviewer → deploy → Solution
       needs     sprint    solution    implemen-   QA        review and
       analysis  planning  design      tation      testing   optimise
       ↑                                                       │
       └──── another sprint, from the stage that owns it ──────┘
```

| Role | Stage | What it does | Usually worn by |
|---|---|---|---|
| **Analyst** | Needs analysis | The need, the people, what done looks like; in later sprints, whether the need still holds | The Developer, with the Agent asking and drafting |
| **Planner** | Sprint planning | One sprint goal, the work in and out, a test of done for each piece, risks, the estimate | The Developer, with the Agent drafting |
| **Architect** | Solution design | The options and their costs; schema, where logic lives, native or web viewer; security and privileges; what users will have to unlearn | The Developer decides; the Agent offers options |
| **Developer** | Implementation | Makes the change on a copy, with a pull-request code check inside the build where there's a repo | Mostly the Agent |
| **Tester** | QA testing | Tests every test of done, on each client, with real-looking data, as a separate pass from the build | The Agent runs tests; the Developer judges whether they're enough |
| **Reviewer** | Review and optimise | Judges the whole result against the need: the code, the tests, the UI and the UX; checks the tests tested the right thing; optimises | The Developer, with the Agent preparing it from a fresh context |

**QA testing comes before review.** The Reviewer judges the whole result, and part of that is
checking the tests tested the right thing; it can't do that before the tests exist. A
pull-request code check is not this review: it stays inside implementation.

## The Orchestrator

The Orchestrator is not a stage. It is the Blue hat across the whole process: it calls each
stage, and chooses the skill and the thinking for it. This skill is the Orchestrator's skill,
and the Developer (the person) is the Orchestrator.

- It decides which stage runs next, which skill or tool owns the work there, and which
  thinking hats the stage calls.
- It moves work from one stage to the next once the stage's gate is confirmed in the
  hand-back.
- After review it decides: **another sprint, and from which stage, or deploy.**
- The Agent recommends, with its evidence. It never makes these calls and never marks its own
  gate as passed.

## Sprints, and sending work back

A sprint is one pass round the stages. It starts from whichever stage the work goes back to,
not always from the top, and it isn't a fixed time box.

**Any stage can send work back to the stage that owns the problem.** QA testing doesn't wait
for review: a failed test goes straight back. After review, the Orchestrator starts the next
sprint from the stage that owns what was found:

| What was found | Goes back to |
|---|---|
| A bug: the build doesn't do what the design says | **Developer** (implementation) |
| A design that won't work: too slow, can't handle a case, the wrong place for the logic | **Architect** (solution design) |
| A plan that missed something: a layout, a report, a client, a dependency | **Planner** (sprint planning) |
| The need changed: the client wants something different, or new facts | **Analyst** (needs analysis) |

When findings belong to several stages, the sprint starts at the earliest of them, so a
changed need is settled before the design or the code is redone. Whatever it starts from,
the reworked work goes through QA testing and review again before deploy.

Needs analysis is the first stage of every sprint, on the way round: in later sprints it's
short, asking whether the need still holds and folding in what the last sprint taught.

Why sprints: the Agent makes building cheap, so the risk moves to building the wrong thing, or
shipping something nobody checked. Short sprints with a decision at the end of each keep the
Developer in charge of direction while the Agent does the volume.

## Asking which stage

Before starting, say which stage the work starts at. Give a best guess and the reason, so the
Developer can answer in a word:

> This starts at needs analysis: whether the fee compounds, and from which date, isn't settled
> yet. Start there, or is that decided and it's straight to implementation?

Signals: no definition of done means needs analysis. A settled need with no sprint goal means
sprint planning. A plan with an open design (where it lives, which tables) means solution
design. A clear spec means implementation. "Does it work?" means QA testing. "Is it right?"
means review. "Can we ship it?" is the Orchestrator's call: bring the evidence from each gate.

## The thinking hats each stage calls

De Bono's rule: the Blue hat decides which hat is worn when. So the Orchestrator calls the
hats each stage needs, and each hat earns its place by the question it asks there:

| Stage | Hats called, and the question each asks |
|---|---|
| **Orchestrator** (every stage) | **Process:** Which stage, which skill and which hat next? After review: another sprint, and from which stage, or deploy? |
| **Analyst** (needs analysis) | **Facts:** What's actually happening, and what's missing? In later sprints: does the need still hold? **Feelings:** How do people feel about the way they work now? |
| **Planner** (sprint planning) | **Facts:** What does the plan, and the last sprint, tell us? **Value:** Which work delivers the most value this sprint? **Caution:** What could stop it? |
| **Architect** (solution design) | **Ideas:** What are the options? **Value:** Which one delivers the most value? **Feelings:** What will people have to unlearn? |
| **Developer** (implementation) | **Caution:** What could break? **Feelings:** Is everything still where people expect it? |
| **Tester** (QA testing) | **Feelings:** Does it work for the people using it? **Value:** Does it beat what they expected? **Caution:** What happens at the edges? |
| **Reviewer** (review and optimise) | **Facts:** What was actually verified, and how? **Caution:** Did the tests test the right thing? **Ideas:** Is there a simpler way, in the code, the UI or the UX? **Value:** Does it meet the need, or beat the brief? |

**Implementation has no Ideas hat.** Agents are generous with ideas, so the Orchestrator calls
the hats they skip: Caution and Feelings. Ideas belong in solution design, where the options
are weighed, and in review, where a simpler way can be found.

**Feelings is called at four stages.** Every update asks users to unlearn something. Change
only what earns the change; keep things where people expect them (same layout, same button
position, same names); when something must move or go, say where it went and why, in the
release notes and, for a while, on the screen itself.

## The hand-back

Every hand-back to the Orchestrator, from any stage, carries four hats, in this order:

1. **Facts:** what was verified, and how (evaluated on the engine, read back from the file,
   run on which test data, on which clients), and what wasn't.
2. **Caution:** the riskiest part, first, before the good news, with where to look.
3. **Feelings:** what users will notice: what will feel different, what they'll have to
   unlearn, what stays where it was.
4. **Process:** what needs a decision, the gate this stage claims and its evidence, and the
   next stage. After implementation that's QA testing, then review; never straight to deploy.

Ideas and Value can follow if they add something. Keep the whole thing short enough to read
before acting on it. The hand-back is where one stage's hats come off: the Agent claims the
gate; the Orchestrator confirms it.

## One person or a team

**One person** (the Developer and the Agent):

- Change hats when you change stage: the table above says which to put on.
- Write the hand-back, even to yourself or the Agent. That's the moment one set of hats comes
  off.
- Never review your own build. A fresh Agent session, another skill, or time away wears the
  Reviewer's hats. The same goes for the Agent: if it built the change, QA testing and review
  run as separate passes that start from the plan, not from its memory of building, in a
  fresh session or subagent where the harness allows.

**A team:**

- Wear your stage's two or three hats, and leave the rest to the people whose stage needs
  them. A business analyst wears the Analyst's; developers the Developer role's; a tester the
  Tester's.
- Borrow a neighbour's hat to understand them. The hats stages share, such as Feelings, are
  the bridges between roles.
- At sprint planning and sprint review, everyone wears the same hat at the same time (de
  Bono's parallel thinking), and the Orchestrator calls which: all Facts, then all Caution,
  rather than one person defending while another attacks.

## What's standard practice and what's CadenceUX's own

Say which is which when explaining the model, so nobody mistakes CadenceUX's choices for Scrum.

**Standard practice:**

- De Bono's six thinking hats, with the Blue hat running the thinking; parallel thinking in a
  group.
- Agile sprints: sprint planning, QA testing, sprint review, then deploy or another sprint.
- Backlog refinement before each sprint.
- A pull-request code check inside the build.
- In Scrum, a sprint is a fixed time box: rework found in testing or review is done inside it,
  until the work meets the definition of done. An optimisation is a change of its own, rerun
  against the same tests.
- The gates draw on standard practice: a definition of ready and a definition of done, quality
  gates between stages, architecture decision records, test reports, code review, and a
  security review and release checklist before production, with a verified backup and a way
  back.

**CadenceUX's own:**

- The Orchestrator as the Blue hat across the whole process, choosing the skill and the
  thinking for each stage, worn by the Developer.
- A sprint is one pass round the stages, from whichever stage the work goes back to, not a
  fixed time box.
- A Planner role.
- Needs analysis as the first stage of every sprint.
- Review and optimise after QA testing, judging the code, the tests, the UI and the UX against
  the need.
- The hats called at each stage, and the question each asks there.
- A gate at every stage, which the Agent never marks as passed itself.

## Reviewing in FileMaker terms

The Reviewer judges the code, the tests and the result against the need, then optimises code
(simpler, fewer calls, nothing duplicated), UI (consistent with the rest of the solution) and
UX (fewer steps, nothing moved without a reason). An optimisation is its own change, rerun
against the same tests; or it's deferred with a reason.

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
- **Estimate in sprints:** how many to reach the definition of done, and what each one
  delivers.
- **Re-estimate after the first build day,** from what that day actually delivered.
- **Keep actuals,** sprint by sprint, beside the estimate in the sprint log, and plan each
  sprint against the last sprint's actuals.
- **Say what doesn't shrink:** needs analysis, QA testing, review, waiting for decisions,
  training and handover.

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
