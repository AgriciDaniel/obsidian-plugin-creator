import { MarkdownRenderChild, Plugin } from "obsidian";

const ROOT_CLASS = "__ROOT_CLASS__";
const BLOCK_TYPE = "__BLOCK_ID__";

class CountWidget extends MarkdownRenderChild {
  constructor(container: HTMLElement, private readonly noteCount: () => number) {
    super(container);
  }

  onload(): void {
    this.containerEl.addClass(ROOT_CLASS);
    const status = this.containerEl.createEl("p", { attr: { "aria-live": "polite" } });
    const refresh = () => { status.setText(`${this.noteCount()} Markdown notes in this vault.`); };
    const button = this.containerEl.createEl("button", { text: "Refresh count" });
    this.registerDomEvent(button, "click", refresh);
    refresh();
  }

  onunload(): void { this.containerEl.empty(); }
}

export default class CreatorPlugin extends Plugin {
  onload(): void {
    this.registerMarkdownCodeBlockProcessor(BLOCK_TYPE, (_source, element, context) => {
      context.addChild(new CountWidget(element, () => this.app.vault.getMarkdownFiles().length));
    });
  }
}
