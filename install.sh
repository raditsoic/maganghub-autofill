#!/usr/bin/env bash
# Symlink the skill into user-level skill dirs (Claude Code + omp) so it is global.
set -euo pipefail
src="$(cd "$(dirname "$0")" && pwd)/skills/maganghub-autofill"
for dir in "$HOME/.claude/skills" "$HOME/.omp/agent/skills"; do
  mkdir -p "$dir"
  ln -sfn "$src" "$dir/maganghub-autofill"
  echo "linked $dir/maganghub-autofill -> $src"
done
