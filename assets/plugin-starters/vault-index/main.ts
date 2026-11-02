import { Notice, Plugin, TFile } from "obsidian";

export default class CreatorPlugin extends Plugin {
  private readonly index = new Map<string, number | null>();
  private initialized = false;

  onload(): void {
    this.registerEvent(this.app.metadataCache.on("changed", (file) => {
      if (this.initialized && file.extension === "md") this.refresh(file);
    }));
    this.registerEvent(this.app.vault.on("delete", (file) => { this.index.delete(file.path); }));
    this.registerEvent(this.app.vault.on("rename", (file, oldPath) => {
      this.index.delete(oldPath);
      if (this.initialized && file instanceof TFile && file.extension === "md") this.refresh(file);
    }));
    this.addCommand({ id: "summarize-index", name: "Summarize heading index", callback: () => {
      this.index.clear();
      for (const file of this.app.vault.getMarkdownFiles()) this.refresh(file);
      this.initialized = true;
      const values = [...this.index.values()];
      const known = values.filter((value): value is number => value !== null);
      const headings = known.reduce((sum, value) => sum + value, 0);
      new Notice(`${known.length} cached notes, ${headings} headings, ${values.length - known.length} notes with no cached data.`);
    } });
  }

  private refresh(file: TFile): void {
    const cache = this.app.metadataCache.getFileCache(file);
    this.index.set(file.path, cache ? (cache.headings?.length ?? 0) : null);
  }

  onunload(): void { this.index.clear(); }
}
