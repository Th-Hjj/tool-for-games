# Checks for trustworthy production tools

Read the relevant section when a tool has divergent output paths, persistent or inherited content, batch/import work, asynchronous results, or a claimed verification that may be weaker than the task requires. These are conditional checks, not a compulsory checklist for every tool.

## Follow the promise to its consumer

Track one operation through its input, resolved configuration, processing, output, saved/exported artifact, and actual consumer. Identify an observable check at the point where failure could hide.

| Claim | Useful evidence | What it does not establish |
| --- | --- | --- |
| A slider changes a sound | Render the same source with controlled settings and inspect signal/output differences | That the result is perceptually sufficient or creatively preferred |
| The draft was saved | Read the resulting data and reopen it; compare it with the reviewed draft | That the game loaded that revision |
| The game uses the new value | Inspect or exercise the consuming path in the relevant runtime/build | That every untested platform or loading route behaves identically |
| A boss shortcut works | Enter through the real state initialization and run the relevant encounter behavior | That moving the player near a boss established a valid phase or save state |
| An import succeeded | Check identifiers, field mapping, diagnostics, and downstream lookup; re-export if applicable | That an empty error list proves visual fit, translation quality, or completeness |
| A release report is current | Resolve its statuses to the intended build, data revision, and refresh time | That a cached green status proves the current candidate is ready |

For variable or nondeterministic processing, control the seed/source where possible and choose a measurement that isolates the setting. A changed file hash alone may reflect metadata or fresh synthesis. A no-op is only a defect if the input exercises the parameter and the setting is expected to affect it.

## Divergent preview routes and ineffective controls

1. Reproduce the reported failure with a representative item and distinguish its raw source from any processed or cached output.
2. Follow the setting through conversion, resolution, processing, and cache lookup. Check whether the output corresponds to the current source and settings.
3. Inspect sibling controls that use the same processing path. Select old/new content, inherited/overridden settings, or other cases because they exercise distinct routes.
4. Compare outputs on controlled input and meaningful parameter values. Preserve a baseline and verify the saved/exported version through its reader.
5. Show the user how to assess the remaining perceptual or creative question. State whether actual playback was inspected.

Prefer one processing/evaluation path when it meets the workflow. When preview and runtime must differ, identify the approximation and verify the decisions that depend on the difference. Do not silently double-process an already rendered asset while fixing a bypass.

## Inheritance, exceptions, and write scope

Use the project's existing precedence. Make the resolved value and its origin understandable when users need to distinguish defaults, template values, instance overrides, and session drafts. Do not silently introduce a new hierarchy.

For a change to a default, determine which items follow it and which retain an override. For a change to an override, ensure its target is unambiguous. Preserve authored exceptions unless the requested operation includes replacing them. Avoid inferring that an override is redundant just because its current value happens to equal the default; its future behavior can differ.

Have change review show the concrete pending edits and relevant exclusions. Apply that same plan or rebuild it if sources changed. For shared editing or expensive work, detect stale revisions rather than overwriting a colleague's changes. Use the simplest recovery mechanism appropriate to the impact.

## Batch edits and imports

Before writes, resolve targets and field meanings from authoritative data. Check missing/duplicate IDs, invalid values, unit conversion, required dependencies, and scope boundaries when they apply. Preserve stable identifiers and references through renames. Keep authored source distinct from generated output.

Make skipped, failed, and successfully changed items distinguishable. Decide from actual dependencies whether an operation must be atomic or whether partial success is useful. Do not claim that a batch fully succeeded after silently skipping failures.

For costly or long-running work, make progress and cancellation meaningful. Make a retry resume safely or explain its consequences; avoid silently duplicating entries. Use a preview, backup, transaction, or version-controlled output appropriate to the existing pipeline rather than automatically adding all of them.

Check a second asset with a meaningful structural difference and an existing exception. If additions are supported, bring a fresh item through discovery, authoring, preview/validation, persistence, consumption, and reopening. Write down manual registration only when the current design actually requires it; remove avoidable hidden steps.

## Asynchronous previews and long operations

Associate an output with the input, settings, and revision that produced it. A late response must not replace the latest preview while retaining the latest labels. Retain a clear association between the reviewed output and the data to be saved.

If the user edits during processing, mark the result as belonging to the earlier draft or rerun it. If preview is unavailable, say so; do not imply that a new configuration has been previewed. Make failed or cancelled work visible and keep the last successful result identifiable.

## Runtime and environment boundaries

Distinguish temporary runtime tuning from persistent authoring changes. For developer shortcuts, use the existing initialization, save, and build configuration conventions; avoid corrupting player saves or unintentionally including development controls in shipped builds.

For publishing or live configuration tools, identify the target environment and actual write scope. Respect existing authorization and release gates. A request to build a publishing tool does not by itself request a live release.

When the runtime, hardware, services, or assets are unavailable, complete the work that can be checked locally. State the exact remaining verification and provide a short way to perform it. Fixture execution establishes behavior in the fixture, not in the user's game.
