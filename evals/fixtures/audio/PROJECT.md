# Offline audio tool

Python standard library only. Run `python3 make_fixture_audio.py` once to create the source WAV files, then use `python3 studio.py --help` for the authoring entry point. The source WAVs are synthetic signals suitable for inspecting processing changes; they do not represent character performances.

`voices.json` holds character defaults and optional line overrides. Draft controls edit character defaults. A line override takes precedence, including an override whose number equals the current default. `question` is a deliberately authored exception. Source recordings are raw, without the three effects baked in. `preview.wav` is disposable output. The same preview entry point is used after reopening the tool. There is no connected game runtime or graphical interface in this small project.
