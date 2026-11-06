# Research behind the working method

Consult this when a design decision would benefit from an example or when revising the skill. The operational guidance is a synthesis, not a claim that any source prescribes this entire workflow. Sources were checked on 2026-11-06. Use current project-version documentation for implementation.

## Primary sources and bounded takeaways

### 1. Form a shared understanding of the work

[David Lightbown, Tools Development at Ubisoft: Building a Shared Vision to Improve the User Experience, GDC 2015](https://www.gdcvault.com/play/1022337/Tools-Development-at-Ubisoft-Building).

The official session abstract describes the risk of starting tools without agreement about what is being built and for whom, and discusses user-centered techniques for forming that agreement. Only the public abstract was reviewed, not the full presentation.

**Application:** Use one concrete task to establish a working interpretation before implementation. The short scenario format and proportional handling of small fixes are choices made for this skill; they are not requirements quoted from the talk.

### 2. Observe actual authoring and review work

[Guerrilla Spotlight: Mathijs Roosen, 2023-07-04](https://www.guerrilla-games.com/read/guerrilla-spotlight-mathijs-roosen).

Roosen describes watching people use their current editors to find bottlenecks and unintuitive behavior, listening across workflows, and collaborating on shared tools. His VideoStore and Review Tool example also concerns feedback on playtests and cinematics.

**Application:** Inspect actual artifacts and work sequences, and include review and handoff in the scope of production tooling. The interview does not imply that every operator needs identical controls or that a prototype needs studio-scale planning.

### 3. Preserve the author's testing context

[inkle, ink and Inky](https://www.inklestudios.com/ink/).

The official overview says Inky refreshes its play pane as writing changes and reloads the choices already made.

**Application:** Preserve the effort needed to reach a useful test position. Retaining a camera, test sentence, filter, or seed is our transfer of this principle. Replay is appropriate only while the preserved state remains valid for the modified content.

### 4. Make inherited changes inspectable

[Unity 6.0, Prefab instance Inspector reference](https://docs.unity3d.com/6000.0/Documentation/Manual/prefab-instance-inspector-reference.html).

Unity's documented Overrides view lists differences between an instance and its prefab and supports applying or reverting changes together or individually.

**Application:** Expose the effective scope of default and instance edits when that distinction matters. This is not a reason to reproduce Unity's UI or add per-item approval to every tool. Follow the project's actual inheritance model.

### 5. Distinguish simulation from game context

[Audiokinetic, Wwise Fundamental Approach, Creating Simulations](https://www.audiokinetic.com/download/documents/Wwise_Fundamental_Approach_en.pdf).

This historical Wwise 2012.1 guide describes Soundcaster simulations made from project objects/events and simulations using sounds triggered by a connected game. It also describes saved sessions.

**Application:** Offer fast exploration and game-context verification when both serve real tasks. This source establishes a design pattern, not current Wwise API behavior, and does not establish a need for free-text synthesis or two preview modes in every tool.

### 6. Verify actual rule and object coverage

[Epic Games, Data Validation in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-validation-in-unreal-engine).

The documentation describes custom asset rules and validation at several object scopes, through editor and command-line entry points. It explicitly notes that command-line validation runs C++ rules by default and that Python validators need registration.

**Application:** Reuse existing validators and confirm which rules and objects actually ran. An empty result may mean missing coverage. These Unreal-specific details illustrate the issue; they are not implementation requirements for other engines.

### 7. Separate the action record from the outcome

[Anthropic, Demystifying evals for AI agents, 2026-01-09](https://www.anthropic.com/research/demystifying-evals-for-ai-agents).

The article distinguishes an agent's transcript from the final state in the environment and describes programmatic, model-based, and human evaluation methods with different strengths and limits.

**Application:** Verify the actual artifact or runtime result and reserve subjective quality judgments for suitable human review. The targeted checks used by this skill are not a prescription to build a full evaluation platform for a small production tool.

## Experience supplied by the repository author

These are user-reported experiences and preferences, not independently reproduced findings or claims from the sources above:

- A voice tool initially exposed the wrong audition task, and changes to controls did not consistently reach old recordings. This motivates identifying the decision first and tracing related processing paths to their outputs.
- Character-wide direction and a deliberately different line performance needed separate save scopes. This motivates preserving authored overrides and making the effects of default changes visible.
- A change-list action needed to describe what would actually be saved, and later dialogue required a clear entry path. This motivates deriving review from pending writes and checking the next content addition.
- Runtime tuning and playtest-data work in game prototypes motivates context-preserving controls and feedback connected to the actual game.
- Rapid prototyping experience motivates completing a small usable loop, avoiding speculative frameworks, and keeping implementation notes out of the operator's main flow. Sample content must not become an assumed creative decision.

The cross-role examples in work-patterns.md are design hypotheses. Test them against the current team's task rather than treating them as empirical facts about everyone in a profession.
