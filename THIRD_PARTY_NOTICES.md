# Third-Party Notices

Obsidian Plugin Brain (`obsidian-plugin-brain`) v0.2.0 has **zero runtime third-party Python dependencies**. The package and static plugin analyzer import only from the Python 3.11+ standard library, enforced by `pyproject.toml` (`dependencies = []`) and verified by `tests/test_pipeline.py`.

## Build-Time Dependencies

The Python CLI package uses standard PEP 517 build backends when installed in editable or wheel mode. Neither backend is bundled in repository distributions:

### setuptools

- Project: <https://github.com/pypa/setuptools>
- License: MIT
- License text: <https://github.com/pypa/setuptools/blob/main/LICENSE>
- Usage: Referenced in `[build-system]` of `pyproject.toml`. Not bundled.

### wheel

- Project: <https://github.com/pypa/wheel>
- License: MIT
- License text: <https://github.com/pypa/wheel/blob/main/LICENSE.txt>
- Usage: Referenced in `[build-system]` of `pyproject.toml`. Not bundled.

## Adapted First-Party / Open-Source Material

### claude-obsidian Markdown Link Scanner

- Project: <https://github.com/AgriciDaniel/claude-obsidian>
- Upstream module: `claude_obsidian/markdown_links.py`
- License: MIT (authored by AgriciDaniel)
- Usage: Shipped via Brainstein 2.0.0 in `scripts/_markdown_links.py` so `scripts/lint_vault.py` parses Obsidian wikilinks identically to Obsidian itself while ignoring fenced code, inline code, math blocks, HTML comments, and `%%comments%%`.

```text
MIT License

Copyright (c) 2026 AgriciDaniel (AI Marketing Hub)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Referenced External Trademarks and Documentation

Obsidian, JSON Canvas, CodeMirror, Three.js, Electron, React, Svelte, Vue, esbuild, and Vite are trademarks or open-source projects of their respective maintainers. All primary documentation citations in `references/public-sources.json` and `references/canon/` remain the property of their upstream authors and are summarized or quoted in short attributed excerpts under fair reference and `PUBLISHING_NOTICE.md`.

## Three.js reference starter

The 3D source starter imports Three.js as an external development dependency.
The reviewed MIT license is retained in `references/creator/toolchain/three-LICENSE.txt`
and included in generated WebGL project notices. No node_modules dependency tree
or vendor implementation bundle is distributed in this source repository.
