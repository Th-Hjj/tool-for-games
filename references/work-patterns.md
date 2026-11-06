# Work patterns across game production

Read this when the operator's decision is unclear, several disciplines share a tool, or a familiar request hides different tasks. Use these as hypotheses to check against project evidence. Do not assign a workflow from a job title or build every capability in the table.

## Start from the decision

| Work context | Possible decision | Context that may need to survive | Useful result |
| --- | --- | --- | --- |
| Level or encounter design | Can the player read and respond to this encounter? | Entry route, camera, equipment, enemy phase, navigation, trigger history | Repeatable encounter entry and feedback in the intended play context |
| Systems, combat, economy | What changes when this parameter changes? | Input, scenario, seed, units, baseline, effective inherited values | Comparable outcomes with the actual parameter revision |
| Art, animation, VFX, technical art | Does the asset communicate correctly and meet the target budget? | Game camera, lighting, skeleton, LOD, scale, target platform | In-context preview plus only the diagnostics needed for that decision |
| Audio and narrative | Does this voice, line, mix, or branch communicate the intended performance? | Test line, listening context, branch history, character default, authored exception | Repeatable audition or playback linked to the draft being accepted |
| Programming and technical design | Why do authoring and runtime behavior disagree? | Asset revision, runtime state, loader, event conditions, build | A reproducible difference and a trace to the source that owns the behavior |
| QA and compatibility | Can another tester reproduce this failure on the relevant build? | Build/platform, test state, input sequence, seed, save, logs | A replayable setup or evidence package with known limits |
| Localization and accessibility | Does the content fit and remain understandable in context? | Stable string ID, locale, font, placeholders, plural forms, screen/device, input method | In-context review and a round trip that preserves bindings and authored text |
| Production, release, live operations | Is the intended content ready for the intended audience/environment? | Build or content revision, environment, ownership, dependencies, refresh time | An actionable list with traceable evidence; explicit scope for any publishing action |
| Analytics and user research | Does this evidence support the proposed design conclusion? | Event definition, build, cohort, denominator, time window, sampling | Inspectable metrics and limitations tied to the decision, with drill-down where useful |

## Distinguish task changes within one person

An audio author may be selecting a character's default voice, directing one important line, and accepting finished recordings for a build. The inputs and save scopes differ even when every task contains a Play button. The same applies to a designer experimenting with an enemy template, protecting a boss-specific exception, and approving a release configuration.

Make the current task and affected scope clear. Preserve appropriate state when switching tasks. Introduce separate screens or modes only if the distinction is frequent and substantial; a scope selector or an existing project convention may suffice.

## Translate intent into observable behavior

| Request | Find out from evidence | Small useful behavior |
| --- | --- | --- |
| “Skip to the boss.” | Skip travel, test a phase, or repeat a specific attack? What loadout and trigger history make that meaningful? | Enter a valid state through the project's initialization path, with a quick way to repeat it |
| “Expose these values.” | Which values inform the decision? What are their units, valid ranges, dependencies, and save scopes? | A compact control surface with immediate relevant feedback and an explicit persistence scope |
| “Batch-edit enemies.” | Which fields share meaning? Where do values inherit? Which variants are intentional? | Shared selection and change review with discipline-specific feedback and preserved exceptions |
| “Import this spreadsheet.” | Who owns each field? What identifies a row across edits? What happens to missing, duplicate, invalid, or renamed entries? | A small importer using stable IDs, useful errors, and a verified output round trip |
| “Show what is ready.” | Ready according to which criteria, checked by whom, for which version? | Evidence-backed status with unresolved items and refresh time, not a count of files |
| “This preview is wrong.” | Wrong for which decision? Which source and settings actually produced it? | Reproduction of the mismatch before changing presentation or adding controls |

## Resolve competing needs

Start with the shared task: select material, establish context, act, inspect, and hand off. Separate the feedback each decision needs from the operations that can be shared.

If an artist needs instant preview while QA needs runtime fidelity, first check whether both can use the existing runtime path cheaply. If not, consider a fast approximation plus an exact verification path. Explain the supported decisions and the extra maintenance cost. Do not add both automatically.

Respect the working environment. A designer already using an engine inspector may benefit from one action there; a localization coordinator may need a spreadsheet import and readable report; a build engineer may need a command and CI output. Do not force a dashboard, command line, engine plugin, or agent conversation onto every user.

## Choose a justified investment

Estimate benefit from actual task frequency and the repeated setup, waiting, and correction it removes. Compare that benefit with implementation, onboarding, and maintenance. Rough evidence is sufficient; avoid invented precision.

For a one-off conversion, a reviewed script and output can be complete. For a daily authoring tool, saved context, clear defaults, and recovery may earn their cost quickly. For a shared production pipeline, dependency, version, conflict, and partial-failure handling may be necessary. Introduce a reusable abstraction only when a second real case or a known upcoming change justifies it.
