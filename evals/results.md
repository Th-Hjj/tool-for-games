# Initial evaluation record

Date: 2026-11-06.

These are small development trials, not a reliability benchmark. Each task used a fresh delegated agent thread with the session's default model, no model override, and no previous attempts or grading rubric in its prompt. Agents received SKILL.md, one task and its raw context, and the isolated fixture where applicable. No live game project or production service was modified.

## First round

The audio, boss, and initial enemy trials used SKILL.md SHA-256 `602775eee191c2cba91c0ede5cfbae42ae538d9e6719d03289ebe6bb526eabb7`. The localization trial was launched during that round. Its brief explicitly requested a concise design and no code. Prompts and context are retained in cases.json.

| Trial | What actually happened | Assessment |
| --- | --- | --- |
| audio-control | Agent reproduced unchanged PCM through the existing Python CLI, changed the recording/synthesis branches to share one processing step, and exercised the repaired output, related controls, save/reopen and authored overrides. No graphical UI, listening evaluation or game runtime was available. | Pass for fixture repair and evidence reporting. |
| boss-entry | Agent proposed a phase-two sweep repetition action in the existing F8 menu, valid encounter/phase initialization, short-sword/full-health setup, preserved camera edits, repeat after death and a temporary save context. It explicitly stated that no engine execution had happened. | Pass for workflow interpretation and requested design. Runtime behavior remains untested. |
| shared-enemy-editing | Agent separated template and instance changes, preserved Elite's override, treated Drone's skeleton as a meaningful difference, distinguished timing from visual feedback, and included the next enemy's entry path. The answer expanded into a long first-release specification. | Pass for the core decisions; partial for proportional communication. |
| localization-roundtrip | Agent centered the fix on stable IDs, described new/missing/duplicate/stale text and placeholder checks, preserved existing text, and proposed an import/export round trip and game lookup check. It left translation quality to the translator and said the checks had not run. | Pass for the requested concise design. Field ownership and exact merge policies still need the actual importer during implementation. |

### Independent check of the audio artifact

The main agent inspected the repaired diff and reran behavior checks in another copy with the original configuration. All 13 targeted assertions passed: each of three controls changed recording PCM; recording and synthesized routes agreed for the same source and settings; a second character responded; the authored override stayed effective; save/reopen produced identical PCM; line overrides and the other character survived saving; source recordings were unchanged; and the task agent had restored the original authoring configuration.

The original recording path produced identical 5,040-frame PCM at grit 0 and 1. Its PCM SHA-256 was `54de47ca31caa95c81a2c8ba56ceab505d65480440a9bcbaa958ad3512b82409` in both cases. The resulting repair was:

```diff
 if line.get("recording"):
     samples = read_wav(ROOT / line["recording"])
 else:
-    samples = process(synthesize(text, character), settings)
+    samples = synthesize(text, character)
+samples = process(samples, settings)
 write_wav(output, samples)
```

The repaired studio.py had SHA-256 `b8f4e3dd46c90fbb34bb3936b959a419f2782f425fb71558cb19855229a67483`. The repository retains the original faulty fixture as repeatable task input. The repair and generated WAVs are not a delivered audio product.

## Revision from the first round

Added guidance to keep initial proposals focused on the core interaction, editing scope and critical acceptance evidence; detailed specifications require an actual need. Conditional reference checks must not accumulate into mandatory first-release features.

Revised SKILL.md SHA-256: `fea8b46d8fcdd18a27056049b6ca97592ac97e5d7d5c53b9759db3afcad8865c`.

The unchanged enemy-editing task was sent to another fresh agent using this revision. It retained the important inheritance, scope, runtime-preview, compatibility and new-item decisions, and organized the proposal into five behavior sections and eight grouped acceptance checks, compared with the first attempt's eight sections and twelve checks. It also correctly avoided assuming that a different skeleton alone proves a specific animation incompatible. The output remained a substantial design document, so proportional communication is improved but still a point to watch in real use. No engine behavior was executed in either enemy trial; one repeat cannot establish a reliable or causal brevity improvement.

## Second round: remaining six cases (v0.2.0)

Date: 2026-11-06. SKILL.md SHA-256 `ec5f0002485545c4f4ce9aadbad1cd67616398edd41c4604d95e1cecb79719a8` (v0.2.0, after the first-version design shape and the move of content-change checks to production-checks.md). Each case ran once in a fresh delegated agent thread with the session's default model and an empty workspace. Design and review agents received the installed skill directory, the case prompt and its context. Activation agents received only skill names and descriptions (tool-for-games plus six other installed skills) and the prompt, and were asked which skills they would load; this is simulated routing by a model, not a measurement of a host's router.

| Trial | What actually happened | Assessment |
| --- | --- | --- |
| qa-empty-success | Concluded the report cannot decide build-42: it comes from build-41, no validators ran, and zero assets were scanned, so texture budget and localization status are unknown rather than passing. Proposed an "incomplete" status for those three conditions, acceptance checks on a build-42 rerun including a deliberately failing asset, and a status line for the producer. Left the ship decision to the producer, noted that a completeness check does not establish translation quality, and stated that it only reviewed the supplied fields. | Pass. |
| task-switching | Kept one page with an explicit write target (character default, line-specific override, review) that the Save label follows; per-target drafts; late results dropped unless they belong to the latest request for that target; Save disabled when sliders changed after the last audition; review plays the file the game loads and records approval only. Preserved the authored line as a full-parameter override and flagged outputs made stale by a default change. Followed the new shape: scenario, core interaction, write scope, four checks, a one-line later list. It added a short ripple-effect paragraph and two questions about how the override and runtime audio are stored. | Pass. Structure follows the shape; the answer is still a substantial design. |
| reuse-existing | Recommended pinning the six parameters in the existing panel and saving with the existing save, then checking that pins survive a restore before tomorrow. Proposed a code change (a group or default pins) only if pins do not persist, and rejected renaming parameters for a three-day prototype. Made no changes, since no panel code was available. | Pass. |
| single-value | Selected no skill: an isolated value edit. | Pass (simulated routing). |
| ordinary-gameplay | Did not select tool-for-games; selected engineer-any-prototype as an ordinary gameplay change. | Pass for tool-for-games (simulated routing). |
| implicit-workflow | Selected tool-for-games, identifying the daily manual check of 60 prefabs as repeated production work. | Pass (simulated routing). |

## Coverage limits

The bundled skill validator checks naming and frontmatter structure. Local checks also cover metadata, JSON parsing and relative file links; these do not prove runtime behavior or automatic skill selection.

All ten cases have now run at least once: one executable fixture, six design or review scenarios on the first or second revision, and three activation prompts. The first-round trials used the earlier SKILL.md revision and were not rerun on v0.2.0. Activation was checked only by simulated routing from metadata, not in a real host's skill router. No Unity, Unreal, shipped game, human usability session or subjective voice-quality evaluation was run. The small sample does not establish coverage for every game-industry role or show a measured improvement over an agent without the skill.
