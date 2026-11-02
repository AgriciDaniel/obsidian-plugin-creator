import { ItemView, Plugin, PluginSettingTab, Setting, WorkspaceLeaf, requestUrl } from "obsidian";
import { ViewPlugin } from "@codemirror/view";
import { createRoot, Root } from "react-dom/client";
import * as THREE from "three";

export const VIEW_TYPE_SPATIAL = "spatial-graph-codex-view";

export class SpatialGraphView extends ItemView {
  private root: Root | null = null;
  private renderer: THREE.WebGLRenderer | null = null;
  private observer: ResizeObserver | null = null;

  getViewType(): string {
    return VIEW_TYPE_SPATIAL;
  }

  getDisplayText(): string {
    return "Spatial graph";
  }

  async onOpen(): Promise<void> {
    this.root = createRoot(this.contentEl);
    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.observer = new ResizeObserver(() => {
      if (this.contentEl.doc.visibilityState === "hidden") return;
      const rect = this.contentEl.getBoundingClientRect();
      this.renderer?.setSize(rect.width, rect.height);
    });
    this.observer.observe(this.contentEl);
    this.registerDomEvent(this.contentEl.doc, "visibilitychange", () => {
      if (this.contentEl.doc.visibilityState === "hidden") {
        this.renderer?.setAnimationLoop(null);
      }
    });
  }

  async onClose(): Promise<void> {
    this.observer?.disconnect();
    this.renderer?.dispose();
    this.root?.unmount();
  }
}

class SpatialSettingTab extends PluginSettingTab {
  display(): void {
    const { containerEl } = this;
    containerEl.empty();
    new Setting(containerEl).setName("Graph rendering").setHeading();
  }
}

export default class SpatialGraphPlugin extends Plugin {
  async onload(): Promise<void> {
    this.registerView(VIEW_TYPE_SPATIAL, (leaf: WorkspaceLeaf) => new SpatialGraphView(leaf));
    this.registerEditorExtension(ViewPlugin.fromClass(class {}));
    this.registerMarkdownCodeBlockProcessor("spatial-query", (source, el) => {
      el.createDiv({ text: source });
    });
    this.app.workspace.onLayoutReady(() => {
      this.registerEvent(this.app.vault.on("create", () => {}));
    });
    this.addCommand({
      id: "open-spatial-view",
      name: "Open spatial graph",
      callback: async () => {
        await requestUrl({ url: "https://obsidian.md" });
      }
    });
    this.addSettingTab(new SpatialSettingTab(this.app, this));
  }

  onunload(): void {
    // Do not call detachLeavesOfType here; Obsidian restores leaf layout on reload.
  }
}
