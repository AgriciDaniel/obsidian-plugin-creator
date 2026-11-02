import { ItemView, Plugin, WorkspaceLeaf } from "obsidian";

const VIEW_TYPE = "__VIEW_ID__";
const ROOT_CLASS = "__ROOT_CLASS__";

class NoteDashboard extends ItemView {
  constructor(leaf: WorkspaceLeaf, private readonly label: string) {
    super(leaf);
    this.registerEvent(this.app.vault.on("create", () => this.render()));
    this.registerEvent(this.app.vault.on("delete", () => this.render()));
  }

  getViewType(): string { return VIEW_TYPE; }
  getDisplayText(): string { return this.label; }

  async onOpen(): Promise<void> {
    this.contentEl.addClass(ROOT_CLASS);
    this.render();
    await Promise.resolve();
  }

  private render(): void {
    this.contentEl.empty();
    this.contentEl.createEl("h2", { text: this.label });
    const count = this.app.vault.getMarkdownFiles().length;
    this.contentEl.createEl("p", { text: `${count} Markdown notes in this vault.` });
    if (count === 0) this.contentEl.createEl("p", { text: "Create a note to begin." });
  }

  async onClose(): Promise<void> {
    this.contentEl.empty();
    await Promise.resolve();
  }
}

export default class CreatorPlugin extends Plugin {
  onload(): void {
    this.registerView(VIEW_TYPE, (leaf) => new NoteDashboard(leaf, this.manifest.name));
    this.addCommand({
      id: "open-dashboard",
      name: "Open dashboard",
      callback: () => { void this.openDashboard(); },
    });
  }

  private async openDashboard(): Promise<void> {
    const leaf = this.app.workspace.getLeaf("tab");
    await leaf.setViewState({ type: VIEW_TYPE, active: true });
    await this.app.workspace.revealLeaf(leaf);
  }
}
