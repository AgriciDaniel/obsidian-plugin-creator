import { build } from "esbuild";
import { builtinModules } from "node:module";

const result = await build({
  entryPoints: ["src/main.ts"],
  bundle: true,
  format: "cjs",
  target: "es2022",
  outfile: "main.js",
  sourcemap: false,
  metafile: true,
  external: ["obsidian", "electron", "@codemirror/*", "@lezer/*", "node:*", ...builtinModules],
  logLevel: "warning",
});

// Print only bundle size and external import names; never source text or note content.
const output = result.metafile.outputs["main.js"];
console.log(JSON.stringify({ bytes: output.bytes, imports: output.imports }, null, 2));
