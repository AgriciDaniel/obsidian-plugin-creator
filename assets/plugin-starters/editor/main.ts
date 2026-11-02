import { Plugin } from "obsidian";
import { Decoration, DecorationSet, EditorView, MatchDecorator, ViewPlugin, ViewUpdate } from "@codemirror/view";

const matcher = new MatchDecorator({
  regexp: /\bTODO\b/g,
  decoration: Decoration.mark({ class: "__MARK_CLASS__" }),
});

const highlights = ViewPlugin.fromClass(class {
  decorations: DecorationSet;
  constructor(view: EditorView) { this.decorations = matcher.createDeco(view); }
  update(update: ViewUpdate): void {
    this.decorations = matcher.updateDeco(update, this.decorations);
  }
}, { decorations: (instance) => instance.decorations });

export default class CreatorPlugin extends Plugin {
  onload(): void { this.registerEditorExtension(highlights); }
}
