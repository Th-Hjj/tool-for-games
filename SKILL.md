---
name: tool-for-games
description: "Design, build, improve, debug, or review tools for game production using technical-design thinking. Use for editor extensions, debug menus, tuning and preview tools, asset or localization pipelines, batch editors, QA reproduction, telemetry, and build or content review; also use when repeated manual work, ineffective controls, or preview/save/game mismatches reveal a tooling problem, even if the user does not say 'tool'. Support designers, artists, audio and narrative authors, engineers, QA, localization, production, and live operations by their actual task. For an isolated content edit or an ordinary gameplay feature, complete that work directly unless a tool or workflow change is requested."
---

# Tool for Games

Help a game developer complete real work, make an informed decision, and pass a trustworthy result to its next consumer. Apply technical-design thinking by connecting the user's intent, the production workflow, and the actual game or pipeline behavior.

Use the user's language and established project terms. Treat the user as the owner of creative intent. Make routine, reversible implementation choices and carry an authorized implementation through to a usable result.

## Scale the work

For a small fix, inspect the failing path, repair it, check relevant neighboring paths, and explain the observed result. Keep discovery and tradeoffs to a few sentences. For a new or substantially changed workflow, work through the five steps below. Combine steps when the evidence is already clear; do not require a questionnaire, a design document, or approval after each step.

Honor the requested deliverable: implement when asked to build or fix; stop at a design or review when that is what the user requested. Use the project's existing engineering conventions and appropriate implementation tools. Avoid introducing a general framework to solve one task.

For an initial design, lead with the core interaction, editing scope, and critical acceptance evidence. Keep it brief enough to act on; expand into a detailed specification only when asked. Select conditional checks for real failure modes instead of accumulating them as first-release features. Do not recite the five stages in the final answer.

## 1. Reconstruct the work and the decision

Read available instructions, recent feedback, screenshots, real assets, and existing tools before asking questions. Follow one actual attempt from its starting point to the moment the user can judge the result.

Identify who operates the tool, who decides whether its output is acceptable, who or what consumes it next, and which mistake creates the most costly rework. One person may occupy all these roles and switch between them. A job title suggests context; it does not determine the needed controls or expertise.

Briefly describe the intended use in concrete terms: what the person brings in, what they change or inspect, what decision that enables, and where the result goes. For example: “Enter a new line, compare two character voices on that same line, then save the chosen character default while retaining an existing line-specific performance.” Use this as a shared working interpretation, not a mandatory confirmation gate.

Distinguish explicit requirements, facts found in the project, and assumptions in your reasoning. Surface only assumptions that materially affect behavior, cost, creative direction, or existing content. Ask the smallest useful question only when available evidence cannot resolve such a choice. Otherwise proceed with a reversible default and state it when relevant.

For an unfamiliar task or conflicting needs, read [work-patterns.md](references/work-patterns.md). Prefer a real workflow over a list of features inferred from the requester's role.

## 2. Follow one real item through the system

Trace a representative item from its authoritative source through editing, preview or processing, saving or export, consumption, and reopening. The consumer may be the running game, another author, a build pipeline, a QA report, or a production decision. For a read-only tool, trace the source to the decision and any exported evidence.

Establish the engine/tool version and actual integration points where relevant. Locate the source of truth, generated artifacts, runtime copies, caches, identifiers, units, defaults, inheritance, overrides, and existing validation entry points. Read the consumer as well as the editor; a successful write does not prove that the consumer uses it.

Identify where paths diverge: old versus new assets, preview versus game, global defaults versus individual overrides, local data versus shared data. Reuse existing loaders and evaluation logic when feasible. If a faster approximation is needed, make its limits clear enough that the user knows which decisions it supports.

Inspect current project APIs and use version-appropriate documentation when needed. Research comparable tools only to settle an actual design question. For each reference, determine the problem it solves, its prerequisites, and whether those prerequisites hold here. See [research.md](references/research.md) for examples and their limits; do not browse or load all references for a routine fix.

## 3. Choose the smallest useful intervention

Compare using an existing facility, extending the current workflow, and building a separate tool. Consider frequency, waiting and rework, expected lifespan, integration burden, and who will maintain it. A command, spreadsheet, inspector action, or short script can be the right interface. Put the tool where its operators already work unless a different surface has a clear benefit.

Resolve these three tradeoffs for the actual task:

| Concern | Design question |
| --- | --- |
| Usability | Can the operator use familiar terms and reach useful feedback with little repeated setup? |
| Generality | Which operations preserve the same intent across a second real object or user, and which differences matter to their work? |
| Extensibility | What next change is actually expected, and how can it enter without damaging existing content or requiring hidden setup? |

Prefer shared selection, comparison, saving, and review behavior when the intent is shared. Retain task-specific feedback: a timing readout, a game-camera view, a missing-string report, and an asset budget answer different questions. Add separate modes only when they support distinct decisions worth maintaining.

Preserve the effort spent reaching a test state: selected object, camera, input text, locale, filter, random seed, or reproduction steps. Reset the parts that must reset for a meaningful comparison, and make that reset understandable.

Describe controls by their purpose and effect. Expose implementation detail only when it helps that operator make a decision or troubleshoot. Make errors actionable. For slow work, keep the interface responsive and show which request produced the displayed result. Add cancellation, resumability, or batch progress where the actual cost warrants it.

Keep examples and placeholders separate from approved creative direction. Offer recommendations when useful, but do not turn temporary content or an agent preference into character canon, balance intent, or final approval.

## 4. Make the riskiest promise work first

Implement the smallest complete operation that could invalidate the design: a meaningful A/B, a reproducible encounter state, a truthful batch-change preview, a round-trip import, or a report tied to the right build. Use real project material when accessible. If only fixtures are available, label the result accordingly.

Verify what a control promises at the output, not only in its handler, log, or success message. When one control fails, inspect the related controls and shared processing routes. Choose representative cases by how the implementation branches; avoid both checking only the reported slider and exhaustively testing an irrelevant Cartesian product.

For tools that change content:

- Make the editing scope clear: session-only, an item, a template/default, or a batch. Show resolved values and the origin of overrides when inheritance matters.
- Make change review come from the actual pending write: old value, new value, affected objects, and meaningful exclusions. Use the same plan for applying changes or recheck it if the source changed. Do not present an empty diff for a real update.
- Keep previews connected to the settings and source revision that produced them. Do not let a stale result appear to validate a newer draft or silently save something other than the reviewed version.
- Preserve existing authored exceptions during changes to defaults unless the requested scope includes them. Provide a deliberate way to edit or remove an exception.
- Use an appropriate recovery path for the impact: editor undo, a local backup, a version-control diff, or a transaction. For bulk or destructive work, preview the scope and handle invalid items, conflicts, and partial failure. A single temporary control does not need a publishing system.

Read [production-checks.md](references/production-checks.md) for divergent preview paths, inherited or bulk edits, imports, asynchronous output, or misleading verification. Select checks that address the actual failure modes.

## 5. Accept the tool through a production task

Run the intended operation from its normal entry point with representative material. Check the saved or exported result and its actual consumer where accessible. Reopen it when persistence matters. Confirm that expected validators actually ran on the intended objects; an empty error list is not evidence of coverage. A screenshot or successful command alone cannot establish that the result is usable downstream.

For reusable tools, try a second representative object that exercises a meaningful difference. If creating or importing future content is part of the tool's purpose, also introduce a fresh item through the normal workflow: create/import, discover, preview or validate, save/export, consume, and edit again. Do not add this work to a narrow fix unrelated to content onboarding.

Use objective checks for correctness and give the author suitable evidence for creative judgment. An audio difference does not establish a preferred performance; a valid encounter state does not establish good combat pacing; schema-valid text does not establish good localization. Report separately what ran, what the output proves, what still needs human judgment, and any unavailable runtime or environment. Never claim to have heard, seen, launched, or verified something you did not inspect.

Keep validation proportionate. Use a targeted reproducible check or manual task walkthrough when sufficient; add regression tests where a concrete repeated failure or costly consequence justifies them. Do not build a large test harness or extend testing after the material risk is resolved.

Deliver the working change or requested design, the shortest path to using it, the scope and destination of its outputs, and relevant verification limits. For reusable tools, leave concise next-item instructions and enough maintenance context to identify the authoritative data and integration point. Keep technical maintenance notes out of the operator's main flow.

Judge success by whether the intended user can use their own material, make the intended decision, understand what changed, and confidently pass the result onward.
