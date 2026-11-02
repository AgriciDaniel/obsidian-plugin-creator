import { ItemView, Plugin, WorkspaceLeaf } from "obsidian";

const VIEW_TYPE = "__VIEW_ID__";
const ROOT_CLASS = "__ROOT_CLASS__";

class NoteChart extends ItemView {
  private observer?: ResizeObserver;
  constructor(leaf: WorkspaceLeaf, private readonly label: string) { super(leaf); }
  getViewType(): string { return VIEW_TYPE; }
  getDisplayText(): string { return this.label; }

  async onOpen(): Promise<void> {
    this.contentEl.addClass(ROOT_CLASS);
    this.contentEl.empty();
    const count = this.app.vault.getMarkdownFiles().length;
    this.contentEl.createEl("h2", { text: this.label });
    this.contentEl.createEl("p", { text: `${count} Markdown notes. Reopen this view to refresh the snapshot.` });
    this.contentEl.createEl("p", { text: "Bar scale: zero to one hundred notes, capped at one hundred." });
    const canvas = this.contentEl.createEl("canvas", {
      attr: { role: "img", "aria-label": `Chart showing ${count} Markdown notes.` },
    });
    const draw = () => {
      const width = Math.max(1, canvas.clientWidth);
      const ratio = Math.min(canvas.ownerDocument.defaultView?.devicePixelRatio ?? 1, 2);
      canvas.width = Math.round(width * ratio);
      canvas.height = Math.round(240 * ratio);
      const context = canvas.getContext("2d");
      if (!context) return;
      context.setTransform(ratio, 0, 0, ratio, 0, 0);
      const theme = canvas.ownerDocument.defaultView?.getComputedStyle(canvas);
      context.fillStyle = theme?.getPropertyValue("--interactive-accent").trim() || "currentColor";
      context.fillRect(20, 20, Math.max(1, (width - 40) * Math.min(count / 100, 1)), 80);
    };
    this.observer = new ResizeObserver(draw);
    this.observer.observe(canvas);
    draw();
    await Promise.resolve();
  }

  async onClose(): Promise<void> {
    this.observer?.disconnect();
    this.observer = undefined;
    this.contentEl.empty();
    await Promise.resolve();
  }
}

export default class CreatorPlugin extends Plugin {
  onload(): void {
    this.registerView(VIEW_TYPE, (leaf) => new NoteChart(leaf, this.manifest.name));
    this.addCommand({ id: "open-chart", name: "Open note chart", callback: () => { void this.openChart(); } });
  }
  private async openChart(): Promise<void> {
    const leaf = this.app.workspace.getLeaf("tab");
    await leaf.setViewState({ type: VIEW_TYPE, active: true });
    await this.app.workspace.revealLeaf(leaf);
  }
}
