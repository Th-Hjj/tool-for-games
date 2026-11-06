# Integration points

Where common engines let a tool attach, record undo, hook imports and run validation. Entry points only, not tutorials. Written on 2026-11-06; confirm names against the engine version the project uses, and prefer whatever the project already has.

## Unity

- **Where the UI goes:** `EditorWindow` (UI Toolkit or IMGUI), custom inspectors (`CustomEditor`) and `PropertyDrawer`s, `MenuItem` and context-menu actions, Scene view overlays. Data often lives in ScriptableObjects and prefabs.
- **Undo:** call `Undo.RecordObject` before changing an object; `Undo.RegisterCreatedObjectUndo` for new objects. `SerializedObject.ApplyModifiedProperties` records undo for serialized edits. Mark directly modified assets with `EditorUtility.SetDirty`. After changing a prefab instance through code, call `PrefabUtility.RecordPrefabInstancePropertyModifications`.
- **Overrides:** `PrefabUtility.GetObjectOverrides` and `GetPropertyModifications` read instance overrides; `ApplyPropertyOverride` and `RevertPropertyOverride` change them deliberately.
- **Batch writes:** wrap bulk asset changes in `AssetDatabase.StartAssetEditing` / `StopAssetEditing` with `try/finally`, then `AssetDatabase.SaveAssets`.
- **Import hooks:** `AssetPostprocessor` for existing formats; `ScriptedImporter` for custom formats.
- **Validation hooks:** no single built-in framework. Common entry points are build callbacks (`IPreprocessBuildWithReport`), Edit Mode tests, and a static method run in CI with `-batchmode -executeMethod`.

## Unreal Engine 5

- **Where the UI goes:** Editor Utility Widgets and Editor Utility Blueprints (including scripted asset actions); C++ editor modules with Slate; Python editor scripting through the `unreal` module.
- **Undo:** in C++, open an `FScopedTransaction` and call `Modify()` on each object before changing it; in Python, use `unreal.ScopedEditorTransaction`.
- **Import hooks:** DataTable and CurveTable import from CSV or JSON, with reimport; `UFactory` subclasses or Interchange pipelines for custom formats; `unreal.AssetImportTask` for scripted imports.
- **Validation hooks:** the Data Validation plugin (`UEditorValidatorBase` subclasses and `IsDataValid`) runs on save, from the editor, and through the `DataValidation` commandlet. Confirm which validators are registered for the entry point you use.

## Godot 4

- **Where the UI goes:** an `EditorPlugin` (`plugin.cfg` plus a `@tool` script) adds docks, bottom panels or a main-screen view; `EditorInspectorPlugin` customizes inspector properties; `EditorScript` runs one-off editor scripts.
- **Undo:** `EditorUndoRedoManager` from `EditorPlugin.get_undo_redo()`: `create_action`, `add_do_property` / `add_undo_property` (or methods), `commit_action`.
- **Import hooks:** `EditorImportPlugin` for custom formats; post-import scripts (`EditorScenePostImport`) for imported scenes.
- **Validation hooks:** no built-in framework. `@tool` nodes can report problems through `_get_configuration_warnings()`; batch checks can run headless with `--script`.

## Spreadsheets and command-line tools

- Keep a stable ID column, and import through the project's existing pipeline rather than a parallel loader.
- Give commands a dry-run mode that prints the planned changes, and a nonzero exit code on failure so CI can rely on them.
