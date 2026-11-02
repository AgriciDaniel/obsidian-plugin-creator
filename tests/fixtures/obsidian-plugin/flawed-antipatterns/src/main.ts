import { Plugin, PluginSettingTab } from "obsidian";
import { EditorView } from "@codemirror/view";
import fs from "node:fs";
import * as THREE from "three";

class BadSettings extends PluginSettingTab {
  display(): void {
    this.containerEl.createEl("h2", { text: "General Settings" });
  }
}

export default class BadPlugin extends Plugin {
  async onload(): Promise<void> {
    const globalRef = (window as unknown as { app: unknown }).app;
    void globalRef;
    void EditorView;
    void fs.existsSync;
    void THREE.Scene;
    this.app.vault.on("create", (file) => {
      void this.app.vault.rename(file, "other.md");
    });
    this.addCommand({
      id: "obsidian-bad-plugin-run",
      name: "Run bad command",
      hotkeys: [{ modifiers: ["Mod"], key: "b" }],
      callback: async () => {
        const res = await fetch("https://api.github.com");
        document.body.innerHTML = await res.text();
      }
    });
    this.addSettingTab(new BadSettings(this.app, this));
  }

  onunload(): void {
    this.app.workspace.detachLeavesOfType("bad-view");
  }
}
