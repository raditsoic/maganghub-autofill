#!/usr/bin/env bash
# Fail unless every manifest carries the same version. Prints the version on success.
# Optional arg: expected version (e.g. 0.2.0, no leading "v").
set -euo pipefail
cd "$(dirname "$0")/.."

plugin=$(jq -r '.version' .claude-plugin/plugin.json)
claude=$(jq -r '.plugins[0].version' .claude-plugin/marketplace.json)
omp=$(jq -r '.plugins[0].version' .omp-plugin/marketplace.json)

if [[ "$plugin" != "$claude" || "$plugin" != "$omp" ]]; then
  echo "version mismatch: plugin.json=$plugin claude marketplace=$claude omp marketplace=$omp" >&2
  exit 1
fi
if [[ -n "${1:-}" && "$1" != "$plugin" ]]; then
  echo "expected $1 but manifests say $plugin" >&2
  exit 1
fi
echo "$plugin"
