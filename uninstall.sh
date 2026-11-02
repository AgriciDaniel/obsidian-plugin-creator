#!/usr/bin/env bash
set -euo pipefail

target="claude"
custom_path=""
while [ "$#" -gt 0 ]; do
  case "$1" in
    --target) target="${2:?}"; shift 2 ;;
    --path) custom_path="${2:?}"; shift 2 ;;
    -h|--help) echo "Usage: ./uninstall.sh [--target claude|codex|agents|gemini|openclaw|portable|custom|all] [--path DIR] (default: claude)"; exit 0 ;;
    *) echo "ERROR: unknown argument: $1" >&2; exit 2 ;;
  esac
done

case "${target}" in codex|claude|agents|gemini|openclaw|portable|custom|all) ;; *) echo "ERROR: invalid target" >&2; exit 2 ;; esac
if [ "${target}" = "custom" ] && [ -z "${custom_path}" ]; then
  echo "ERROR: --target custom requires --path" >&2
  exit 2
fi
base_home="${OBSIDIAN_PLUGIN_BRAIN_INSTALL_HOME:-${HOME}}"

python_bin="${PYTHON_BIN:-}"
if [ -z "${python_bin}" ]; then
  for candidate in python3 python; do
    if command -v "${candidate}" >/dev/null 2>&1; then python_bin="${candidate}"; break; fi
  done
fi
if [ -z "${python_bin}" ]; then
  echo "ERROR: no python3 interpreter on PATH; set PYTHON_BIN" >&2
  exit 1
fi

target_dir() {
  case "$1" in
    codex) echo "${base_home}/.codex/skills/obsidian-plugin-brain" ;;
    claude) echo "${base_home}/.claude/skills/obsidian-plugin-brain" ;;
    agents) echo "${base_home}/.agents/skills/obsidian-plugin-brain" ;;
    openclaw) echo "${base_home}/.openclaw/skills/obsidian-plugin-brain" ;;
    portable) echo "${base_home}/.agent-skills/obsidian-plugin-brain" ;;
    custom) echo "${custom_path%/}/obsidian-plugin-brain" ;;
  esac
}

remove_one() {
  local dir="$1"
  if [ -d "${dir}" ]; then
    rm -rf "${dir}"
    echo "Removed ${dir}"
  else
    echo "Obsidian Plugin Brain is not installed at ${dir}"
  fi
}

remove_gemini() {
  local dir="${base_home}/.gemini/obsidian-plugin-brain"
  local loader="${base_home}/.gemini/GEMINI.md"
  remove_one "${dir}"
  if [ -f "${loader}" ]; then
    "${python_bin}" - "${loader}" <<'PY'
from __future__ import annotations

import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
start = "<!-- obsidian-plugin-brain-install:start -->"
end = "<!-- obsidian-plugin-brain-install:end -->"
text = path.read_text(encoding="utf-8")
pattern = f"\n*{re.escape(start)}.*?{re.escape(end)}\n*"
new_text = re.sub(pattern, "\n", text, flags=re.S).strip()
if new_text:
    path.write_text(new_text + "\n", encoding="utf-8")
else:
    path.unlink()
PY
    echo "Obsidian Plugin Brain Gemini loader cleaned at ${loader}"
  fi
}

if [ "${target}" = "all" ]; then
  for name in codex claude agents openclaw portable; do
    remove_one "$(target_dir "${name}")"
  done
  remove_gemini
elif [ "${target}" = "gemini" ]; then
  remove_gemini
else
  remove_one "$(target_dir "${target}")"
fi
