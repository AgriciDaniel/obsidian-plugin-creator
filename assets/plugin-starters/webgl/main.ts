import { ItemView, Plugin, WorkspaceLeaf } from "obsidian";
import * as THREE from "three";

const VIEW_TYPE = "__VIEW_ID__";
const ROOT_CLASS = "__ROOT_CLASS__";

class SceneView extends ItemView {
  private renderer?: THREE.WebGLRenderer;
  private geometry?: THREE.BoxGeometry;
  private material?: THREE.MeshNormalMaterial;
  private observer?: ResizeObserver;
  constructor(leaf: WorkspaceLeaf, private readonly label: string) { super(leaf); }
  getViewType(): string { return VIEW_TYPE; }
  getDisplayText(): string { return this.label; }

  async onOpen(): Promise<void> {
    this.contentEl.addClass(ROOT_CLASS);
    this.contentEl.empty();
    this.contentEl.createEl("h2", { text: this.label });
    this.contentEl.createEl("p", { text: "Static cube preview. The scene renders on open and resize; it has no animation loop." });
    const host = this.contentEl.createDiv({ cls: "creator-scene" });
    host.setAttribute("role", "img");
    host.setAttribute("aria-label", "Three dimensional cube preview.");
    try {
      const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      this.renderer = renderer;
      renderer.setPixelRatio(Math.min(host.ownerDocument.defaultView?.devicePixelRatio ?? 1, 2));
      host.appendChild(renderer.domElement);
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 20);
      camera.position.z = 4;
      this.geometry = new THREE.BoxGeometry(1, 1, 1);
      this.material = new THREE.MeshNormalMaterial();
      const cube = new THREE.Mesh(this.geometry, this.material);
      cube.rotation.set(0.4, 0.6, 0);
      scene.add(cube);
      const render = () => {
        const width = Math.max(1, host.clientWidth);
        renderer.setSize(width, 320);
        camera.aspect = width / 320;
        camera.updateProjectionMatrix();
        renderer.render(scene, camera);
      };
      this.observer = new ResizeObserver(render);
      this.observer.observe(host);
      render();
    } catch {
      this.dispose();
      host.empty();
      host.createEl("p", { text: "This renderer is unavailable. A readable fallback is required before release." });
    }
    await Promise.resolve();
  }

  private dispose(): void {
    this.observer?.disconnect();
    this.observer = undefined;
    this.geometry?.dispose();
    this.geometry = undefined;
    this.material?.dispose();
    this.material = undefined;
    this.renderer?.dispose();
    this.renderer?.domElement.remove();
    this.renderer = undefined;
  }

  async onClose(): Promise<void> {
    this.dispose();
    this.contentEl.empty();
    await Promise.resolve();
  }
}

export default class CreatorPlugin extends Plugin {
  onload(): void {
    this.registerView(VIEW_TYPE, (leaf) => new SceneView(leaf, this.manifest.name));
    this.addCommand({ id: "open-scene", name: "Open scene preview", callback: () => { void this.openScene(); } });
  }
  private async openScene(): Promise<void> {
    const leaf = this.app.workspace.getLeaf("tab");
    await leaf.setViewState({ type: VIEW_TYPE, active: true });
    await this.app.workspace.revealLeaf(leaf);
  }
}
