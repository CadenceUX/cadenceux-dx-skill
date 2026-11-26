# Building the right linter tests

When an agent writes most of the code, the checks the developer trusts are what keep it right.
A linter test turns a rule into something that runs on every change, so a review starts from
what failed rather than from reading everything.

## Contents
- Default: one rule, one test, from a written standard
- What's worth a test
- Where the tests run
- Writing one
- Hands off the referee
- Keeping them honest

## Default: one rule, one test, from a written standard

Every test checks exactly one rule that's written down: in the project's standards (ADK's
Baseline, the `cadenceux` pack, the project's `.adk/standards/`), or in a decision the
developer made and recorded. A test with no written rule behind it argues with the developer
instead of helping them. Rules in `naming.md` and `patterns.md` can fail a test; rules in
`advisory.md` only raise a note for review.

## What's worth a test

Test what's cheap to check mechanically and expensive to miss:

| Rule | Example |
|---|---|
| Naming that can be read from the name | Script names match `Domain: Action`; globals end `_g`; no `Table 2` |
| Required structure | Every table has `ID` and the four housekeeping fields; every base table has a blank layout |
| Required script shape | Every script starts with the header steps; error capture on; a `PURPOSE` comment |
| Things that break silently | Hardcoded file names in calculations; empty parentheses in script names; `Halt Script` |
| References | Scripts, layouts or fields nothing calls (report, don't delete) |

Leave to review what needs judgement: whether a script does what its name says, whether a
relationship is the right design, whether a comment is true.

## Where the tests run

- **With ADK:** read the schema, scripts and layouts through ADK's tools or the `filemaker` CLI
  (`fm-cli` lists its read commands) and test the structured output with a small script kept in
  the project. ADK's `filemaker-standards` skill also reviews work against the resolved layers:
  use it as the review step after the tests.
- **FileMaker 26.1's own checks:** the engine can validate scripts and calculations; see
  `claris-filemaker-pro` for what each check reports and where it runs. Prefer FileMaker's own
  check to a test that re-implements it.
- **Without ADK:** test a Save a Copy as XML export with code. It's a snapshot: re-export before
  each run.

## Writing one

1. Quote the rule and where it's written.
2. Give a passing and a failing example, and run the test on both before trusting it.
3. Make the message say what failed, where, and what the rule wants: "Script `Find Staff`
   (folder Staff): name isn't `Domain: Action` (naming.md, Scripts)".
4. Allow named exceptions (a list in the project), never silent skips.

## Hands off the referee

Linter tests, standards and test fixtures are the referee. **They never change in the same
change as the code they check,** however small the change and even when the Developer asks
for both together. A test loosened alongside the code that failed it proves nothing: the
change passes because the rule moved, and the history no longer shows the rule was broken.

When a check fails:

1. **Fix the code to meet the rule.** For a script name, rename the script to the written
   convention (for example `Invoice: Calculate Late Fee`) and update what calls it.
2. **If the rule itself is wrong,** say so and offer the rule change as its own change: the
   written standard first, then the test, each with a passing and a failing example, flagged
   for the Developer to approve. Only after that lands does the code change go in against it.
3. **One script that shouldn't follow the rule** goes on the project's named exceptions list,
   also as its own change.

Advice bends under pressure ("just loosen it, it's late"). A hook that blocks any change
touching both the tests (or standards, or fixtures) and the code they check enforces this
properly: suggest one, and route building it to `cadenceux-plugin-creator`.

## Keeping them honest

- Rerun the passing and failing examples when ADK, FileMaker or the standards pack changes.
- A test that fails often and is always overridden is a rule nobody wants: change the rule or
  drop the test.
- Report counts by rule, not one long list, so the developer sees which rules are drifting.
