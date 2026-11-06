---
name: tool-for-games
description: "Design, build, improve, debug, or review tools for game production using technical-design thinking. Use for editor extensions, debug menus, tuning and preview tools, asset or localization pipelines, batch editors, QA reproduction, telemetry, and build or content review; also use when repeated manual work, ineffective controls, or preview/save/game mismatches reveal a tooling problem, even if the user does not say 'tool'. Support designers, artists, audio and narrative authors, engineers, QA, localization, production, and live operations by their actual task. For an isolated content edit or an ordinary gameplay feature, complete that work directly unless a tool or workflow change is requested."
metadata:
  version: "0.2.0"
---

# Tool for Games

Help a game developer complete real work, make an informed decision, and pass a trustworthy result to its next consumer. Apply technical-design thinking: connect the user's intent, the production workflow, and the actual game or pipeline behavior.

Use the user's language and established project terms. The user owns creative intent. Make routine, reversible implementation choices and carry an authorized implementation through to a usable result.

## Scale the work

For a small fix, inspect the failing path, repair it, check relevant neighboring paths, and explain the observed result in a few sentences. For a new or substantially changed workflow, work through the five steps below, combining steps when the evidence is already clear. Do not require a questionnaire, a design document, or approval after each step, and do not recite the steps in the final answer.

Honor the requested deliverable: implement when asked to build or fix; stop at a design or review when that is what was asked. Follow the project's engineering conventions. Do not introduce a general framework to solve one task.

For a first-version design, deliver: one scenario sentence, the core interaction, the write scope, and the 3–5 checks that would prove it works. Put everything else in a one-line "later, if needed" list. Expand only when asked.

## 1. Reconstruct the work and the decision

Read available instructions, feedback, screenshots, real assets, and existing tools before asking questions. Follow one actual attempt from its starting point to the moment the user can judge the result.

Identify who operates the tool, who decides whether its output is acceptable, what consumes it next, and which mistake causes the most costly rework. One person may hold all these roles. A job title suggests context; it does not determine the needed controls.

Describe the intended use concretely: what the person brings in, what they change or inspect, what decision that enables, and where the result goes. For example: “Enter a new line, compare two character voices on that same line, then save the chosen character default while retaining an existing line-specific performance.” Treat this as a working interpretation, not a confirmation gate.

Separate explicit requirements, project facts, and your own assumptions. Ask the smallest useful question only when evidence cannot resolve an assumption that materially affects behavior, cost, creative direction, or existing content; otherwise proceed with a reversible default and state it when relevant. For an unfamiliar task or conflicting needs, read [work-patterns.md](references/work-patterns.md).

## 2. Follow one real item through the system

Trace a representative item from its authoritative source through editing, preview or processing, saving or export, consumption (the game, a pipeline, another author, a QA report or a decision), and reopening.

Establish the engine or tool version and the actual integration points; [integration-points.md](references/integration-points.md) lists where common engines expose them. Locate the source of truth, generated artifacts, caches, identifiers, units, defaults, overrides, and existing validation. Read the consumer as well as the editor: a successful write does not prove that the consumer uses it.

Find where paths diverge: old versus new assets, preview versus game, defaults versus overrides, local versus shared data. Reuse existing loaders and evaluation logic when feasible; if a faster approximation is needed, make clear which decisions it supports.

Research comparable tools only to settle an actual design question, and check whether their prerequisites hold here; see [research.md](references/research.md).

## 3. Choose the smallest useful intervention

Compare using an existing facility, extending the current workflow, and building a separate tool by frequency, waiting and rework, lifespan, integration burden, and maintenance. A command, spreadsheet, inspector action, or short script can be the right interface. Put the tool where its operators already work.

| Concern | Design question |
| --- | --- |
| Usability | Can the operator use familiar terms and reach useful feedback with little repeated setup? |
| Generality | Which operations preserve the same intent across a second real object or user, and which differences matter to their work? |
| Extensibility | What next change is actually expected, and how can it enter without damaging existing content or requiring hidden setup? |

Share selection, comparison, saving, and review behavior when the intent is shared; keep task-specific feedback such as a timing readout, a game-camera view, a missing-string report, or an asset budget. Add separate modes only for distinct decisions worth maintaining.

Preserve the effort spent reaching a test state: selected object, camera, input text, locale, filter, random seed, or reproduction steps. Reset only what must reset for a meaningful comparison, and make that reset understandable.

Describe controls by their purpose and effect, and make errors actionable. Keep examples and placeholders separate from approved creative direction; do not turn temporary content or an agent preference into character canon, balance intent, or final approval.

## 4. Make the riskiest promise work first

Implement the smallest complete operation that could invalidate the design: a meaningful A/B, a reproducible encounter state, a truthful batch-change preview, a round-trip import, or a report tied to the right build. Use real project material when accessible; label results that come only from fixtures.

Verify what a control promises at the output, not in its handler, log, or success message. When one control fails, inspect related controls and shared processing routes. Choose representative cases by how the implementation branches.

Before implementing a tool that writes content (edits, saves, imports, batch changes, or changes to defaults and overrides) or produces slow or asynchronous results, read [production-checks.md](references/production-checks.md). Above all, change review must come from the actual pending write: old value, new value, affected objects, and meaningful exclusions.

## 5. Accept the tool through a production task

Run the intended operation from its normal entry point with representative material. Check the saved or exported result and its consumer where accessible, reopening it when persistence matters. Confirm that validators actually ran on the intended objects; an empty error list is not evidence of coverage.

For reusable tools, try a second object that exercises a meaningful difference. If onboarding future content is part of the tool's purpose, also bring a fresh item through create or import, discovery, preview or validation, save or export, consumption, and editing again.

Use objective checks for correctness and give the author suitable evidence for creative judgment: an audio difference does not establish a preferred performance, and schema-valid text does not establish good localization. Report separately what ran, what it proves, what needs human judgment, and what was unavailable. Never claim to have heard, seen, launched, or verified something you did not inspect. Add regression tests only where a concrete repeated failure or costly consequence justifies them.

Deliver the working change or requested design, the shortest path to using it, the scope and destination of its outputs, and relevant verification limits. For reusable tools, leave brief next-item instructions and maintenance notes on the authoritative data and integration point, outside the operator's main flow.
