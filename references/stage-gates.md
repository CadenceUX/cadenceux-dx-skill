# Stage gates

What each stage asks, what must be true before the work moves on, and the record it leaves.
The gates are there because an Agent makes it easy to jump from a working build straight to
deploy, with no QA testing, no optimisation and no security sweep. No stage is skipped because
the Agent is confident.

## Contents
- How a gate works
- How much of this a job needs
- The gates
- Before deploy
- Where the records go
- What's standard practice and what's CadenceUX's own

## How a gate works

1. The stage does its work, asking its questions with the hats the Orchestrator called
   (`sprints-and-hats.md`).
2. Its hand-back says which gate items are met, with the evidence for each, and which aren't.
3. The Orchestrator (the Developer) confirms the gate and moves the work on, or sends it back.

**The Agent never marks its own gate as passed.** It claims the gate in its hand-back; the
Orchestrator confirms it. An Agent's "it works" is evidence for the gate, not the gate. When
an item can't be met (no second client to test on, no time for the sweep), say so plainly and
let the Orchestrator decide; never tick it.

## How much of this a job needs

Size the work before starting, and say which size it is:

| Size | What it is | What it gets |
|---|---|---|
| **One-off change** | One change with a known outcome, done in one go: rename a button, add a field to a layout, fix one script step | Name the stage and its gate inline, in a line ("Implementation: one button label. Gate: done on the copy, nothing else on the layout moved; hand-back below"). A short hand-back. No sprint plan, needs brief or sprint log |
| **Multi-step work** | Several changes towards one goal, over more than one session or hand-back: a feature, an integration | A sprint plan and a sprint log in the project, and each stage's gate in its hand-back |
| **A project** | A new system, a rebuild, or anything with a client brief and several sprints | The full cycle: every stage, every gate, every record below |

Whatever the size, nothing reaches production without the before-deploy checks. For a
one-off change they can be one line each.

When unsure between two sizes, take the larger and say so: the Developer can wave it down in a
word, but a skipped plan can't be added back after the build.

## The gates

| Stage | Ask | Confirm before moving on | Record |
|---|---|---|---|
| **Analyst** (needs analysis) | Who uses this, and what are they doing today? What problem are we solving, and how will we know it's solved? What's out of scope? In later sprints: does the need still hold? | The need and the definition of done are written down. The client has confirmed them. | **Needs brief:** the need, the people, what done looks like |
| **Planner** (sprint planning) | What is this sprint's one goal? Which work is in, and what's left out? What could stop it, and who has to say yes? How many sprints to done, from what we know now? | One sprint goal, and a test of done for each piece of work. Risks and decisions listed. The estimate is in sprints, against last sprint's actuals. | **Sprint plan:** goal, work in and out, risks, estimate |
| **Architect** (solution design) | What are the options, and what does each cost? Native, web viewer or both? Where does the logic live? What will people have to unlearn? Which privileges and data does it touch? | The choice is recorded, with the options and the reason. The impact on users is stated. Security and privileges are part of the design. | **Design decision record:** options, choice, why, what users lose |
| **Developer** (implementation) | What could break? Is everything still where people expect it? Did the build change a test, a standard or a linter rule? (It mustn't.) | Built and run on a copy, never on production. The hand-back is written. No test, standard or linter rule changed in the same change as the code. | **Build hand-back:** in the sprint log, with what changed and why |
| **Tester** (QA testing) | Does it work for the people using it, on each client? Does it beat what they expected? What happens at the edges, with real-looking data? | Every test of done has passed on each client. Failures have gone back for rework. Testing was a separate pass from the build. | **Test report:** cases, clients, data, results |
| **Reviewer** (review and optimise) | What was actually verified, and how? Did the tests test the right thing? Is there a simpler or faster way, in the code, the UI or the UX? Is anything exposed that shouldn't be: privileges, data, ports? Does it meet the need, or beat the brief? | No open issues, or each one sent back. Optimisation done, or deferred with a reason (an optimisation is its own change, rerun against the same tests). A code-level security check done. | **Review notes:** findings, optimisations, security, verdict |

A failed QA test goes straight back to the stage that owns it (usually implementation), and
the fix is tested again on every client before review. Review doesn't start with a test
failing.

## Before deploy

The Orchestrator's gate. It asks: has every gate above been confirmed, not assumed? Has the
security sweep been run on the solution and the server? Is there a verified backup, and a way
back? Do users know what's changing?

Confirm before deploying:

- **Every stage gate confirmed** for this sprint's work, including QA testing and review.
- **A security sweep, clean or with the findings accepted in writing.** The solution side
  (accounts, privileges, secrets, the Agent's access) is in `security-deployment.md`; the
  server side (exposure, CVEs, logs, backups) goes to `cadenceux-fms-security`.
- **Tested on a copy, on each client** the users have.
- **A verified backup and a rollback plan:** what to restore, and how long it takes.
- **Release notes and a changelog, with the why:** what's new, what moved, what's gone and why.
- **The client's yes.**

**Record: Release checklist,** with each item and its evidence. A keen client, a deadline or
the Agent's confidence changes how small the sprint should be, not which checks run. If an item
isn't done by the agreed time, say so and recommend moving the date.

After deploy, collect what users say and do: it feeds the next needs analysis.

## Where the records go

In the project, unless it already has a place for them, under `docs/`:

| Record | Default file |
|---|---|
| Needs brief | `docs/needs-brief.md` |
| Sprint plan | `docs/sprint-plan.md`, the current sprint's plan at the top, earlier ones below |
| Design decision records | `docs/decisions.md`, one entry per decision, newest first |
| Build hand-back, test report, review notes | `docs/sprint-log.md`: one entry per sprint, newest first, with a section for each |
| Release checklist | `docs/release-checklist.md`, one per deploy, newest first |

The sprint log starts with one line that tells the next reader where to begin, then the
entries, newest first:

```markdown
# Sprint log: bookings

Newest first. Every sprint starts by reading the needs brief, the sprint plan and this log.

## Sprint 3, 2026-11-26: bookings screen (started from: solution design)

### Build hand-back
**Done:** what was built.
**Changed, and why:** each change with its reason, and the options considered.
**Facts:** verified how, and on what. Not verified: what wasn't, plainly.
**Caution:** the riskiest part. **Feelings:** what users will notice and have to unlearn.
**Process:** gate claimed, and what needs a decision.

### Test report
Cases, clients, data, results. Failures and where they went back to.

### Review notes
Findings, optimisations (done or deferred, and why), security check, verdict.

**Next:** another sprint from [stage], or deploy. **Waiting on:** decisions.
**Cost:** tokens and time where the harness reports them; estimate against actual.
```

**Every sprint starts by reading the needs brief, the sprint plan and the sprint log,** before
any other file. That's how a fresh session, a helper agent or Developer Next picks up where
the last one stopped. Where a fact is missing (why a button was dropped, what the logs
covered), write what's known, mark the gap, and ask; never invent the reason.

## What's standard practice and what's CadenceUX's own

**Standard practice:** a definition of ready and a definition of done; quality gates between
stages; architecture decision records; test reports; code review; a security review and a
release checklist before production, with a verified backup and a way back.

**CadenceUX's own:** a gate at every stage, confirmed in the hand-back before the Orchestrator
moves the work on; the questions and the record for each stage; the Agent never marking its
own gate as passed; the size threshold for how much of this a job needs.
