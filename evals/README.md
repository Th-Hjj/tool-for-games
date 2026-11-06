# Skill evaluation

These are maintainer materials, separate from the skill's working instructions. The cases check transferable decisions, scope, and evidence rather than whether an answer repeats vocabulary from SKILL.md.

## Run a case

Use a fresh agent thread. Give it the skill, one case's `prompt` and `context` from [cases.json](cases.json), and its fixture when present. Do not provide expected outcomes, this rubric, previous attempts, or an explanation that it is an evaluation. Keep any implementation in an isolated copy of the fixture. Inspect the final artifacts and actual execution as well as the agent's answer.

For the audio case, copy `fixtures/audio` to a temporary project and run `python3 make_fixture_audio.py` there. The source fixture contains the malfunction to be repaired; it is evaluation input, not a delivered voice tool. These WAVs are deterministic test signals, not production dialogue. The fixture intentionally provides no graphical UI or connected game runtime. Retain the original fixture unchanged for another attempt.

For activation cases, present only the skill's frontmatter description alongside normal available skill metadata and the user request. Explicitly attaching the complete skill tests instruction-following, not automatic selection. Classifying prompts by hand is only a metadata review; it does not establish a real host's routing accuracy.

## What to inspect

| Case | Evidence of useful behavior | Material failure |
| --- | --- | --- |
| audio-control | Executes the reported path; inspects related controls/routes; compares controlled audio samples; checks save/reopen and an authored exception; distinguishes output differences from listening judgment | Reports only that settings/logs changed, fixes one bypass while equivalent routes remain broken, or claims unperformed listening/game verification |
| boss-entry | Uses the operation record to target phase-two repetition; preserves camera work; handles valid encounter initialization, loadout, replay and save scope; uses existing F8 surface | Only teleports a transform, invents unavailable APIs as verified facts, or builds a new dashboard |
| shared-enemy-editing | Shares selection/review/recovery; retains useful per-discipline feedback; respects Elite override and Drone skeleton; covers a new enemy entering the workflow | Treats all numeric or animation fields as interchangeable or requires a general asset platform |
| localization-roundtrip | Follows stable IDs; handles duplicate/missing/new/stale content and placeholders; checks the consuming lookup and round trip | Continues matching by English text or treats schema validity as translation approval |
| qa-empty-success | Separates absent coverage, stale build and actual failure; identifies a useful report with evidence | Says zero errors means ready or claims to have run unavailable validation |
| single-value / ordinary-gameplay | Completes ordinary work without creating a tooling project | Expands a single content/gameplay change into tool development |
| implicit-workflow | Recognizes repeated production work as a tooling task without requiring the keyword “tool” | Misses the workflow or demands a complete specification before inspecting context |
| task-switching | Makes input, state and save scope appropriate to each task; handles authored exceptions and late output | Treats every Play/Save action as equivalent or turns sample text into character direction |
| reuse-existing | Uses existing pin/search/grouping to solve tomorrow's task | Proposes an independent tool or speculative infrastructure without benefit |

Grade each as **pass**, **partial**, or **fail**, with the concrete supporting behavior. Note the model/harness when known, available environment, skill revision, and what actually ran. Do not turn a few trials into a reliability percentage.

Structural validation, scenario reasoning, fixture execution, real engine integration, automatic activation, and creative quality are different forms of evidence. Report them separately. Keep results in [results.md](results.md).
