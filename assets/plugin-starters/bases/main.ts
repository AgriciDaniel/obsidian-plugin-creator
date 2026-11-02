import { BasesView, Plugin, QueryController } from "obsidian";

const VIEW_TYPE = "__VIEW_ID__";
const ROOT_CLASS = "__ROOT_CLASS__";

class NoteList extends BasesView {
  readonly type = VIEW_TYPE;
  private readonly root: HTMLElement;

  constructor(controller: QueryController, parent: HTMLElement) {
    super(controller);
    this.root = parent.createDiv({ cls: ROOT_CLASS });
  }

  onDataUpdated(): void {
    this.root.empty();
    const entries = this.data.groupedData.flatMap((group) => group.entries);
    const shown = entries.slice(0, 200);
    this.root.createEl("p", { text: `Showing ${shown.length} of ${entries.length} matching files.` });
    if (entries.length === 0) {
      this.root.createEl("p", { text: "No files match this query." });
      return;
    }
    const list = this.root.createEl("ul");
    for (const entry of shown) list.createEl("li", { text: entry.file.path });
  }
}

export default class CreatorPlugin extends Plugin {
  onload(): void {
    this.registerBasesView(VIEW_TYPE, {
      name: this.manifest.name,
      icon: "list",
      factory: (controller, container) => new NoteList(controller, container),
    });
  }
}
