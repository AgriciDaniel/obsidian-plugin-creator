import { Notice, Plugin } from "obsidian";

export default class CreatorPlugin extends Plugin {
  onload(): void {
    this.addCommand({
      id: "show-note-count",
      name: "Show note count",
      callback: () => {
        const count = this.app.vault.getMarkdownFiles().length;
        new Notice(`${this.manifest.name}: ${count} Markdown notes.`);
      },
    });
  }
}
