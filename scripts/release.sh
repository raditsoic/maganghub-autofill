#!/usr/bin/env bash
# Cut a release: bump manifests, roll CHANGELOG, commit, tag.
# Usage: scripts/release.sh <major.minor.patch>
# Pushing stays manual: git push origin main --follow-tags
set -euo pipefail
cd "$(dirname "$0")/.."

new="${1:-}"
if [[ ! "$new" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "usage: $0 <major.minor.patch>" >&2
  exit 1
fi

[[ -z "$(git status --porcelain)" ]] || { echo "working tree not clean" >&2; exit 1; }
[[ "$(git rev-parse --abbrev-ref HEAD)" == "main" ]] || { echo "release from main only" >&2; exit 1; }
git rev-parse -q --verify "refs/tags/v$new" >/dev/null && { echo "tag v$new exists" >&2; exit 1; }

old=$(scripts/check-versions.sh)
if [[ "$(printf '%s\n%s\n' "$old" "$new" | sort -V | tail -n1)" != "$new" || "$old" == "$new" ]]; then
  echo "new version $new must be greater than current $old" >&2
  exit 1
fi

grep -q '^## \[Unreleased\]' CHANGELOG.md || { echo "CHANGELOG.md has no [Unreleased] section" >&2; exit 1; }
# Require at least one entry under Unreleased.
awk '/^## \[Unreleased\]/{f=1;next} /^## \[/{f=0} f && /^- /{found=1} END{exit !found}' CHANGELOG.md \
  || { echo "[Unreleased] is empty; nothing to release" >&2; exit 1; }

bump() { # file jq-filter
  jq --arg v "$new" "$2" "$1" > "$1.tmp" && mv "$1.tmp" "$1"
}
bump .claude-plugin/plugin.json '.version = $v'
bump .claude-plugin/marketplace.json '.plugins[0].version = $v'
bump .omp-plugin/marketplace.json '.plugins[0].version = $v'

today=$(date +%F)
tmp=$(mktemp)
awk -v v="$new" -v d="$today" -v old="$old" -v repo="raditsoic/maganghub-autofill" '
  /^## \[Unreleased\]/ { print; print ""; print "## [" v "] - " d; next }
  /^\[Unreleased\]:/ {
    print "[Unreleased]: https://github.com/" repo "/compare/v" v "...HEAD"
    print "[" v "]: https://github.com/" repo "/compare/v" old "...v" v
    next
  }
  { print }
' CHANGELOG.md > "$tmp" && mv "$tmp" CHANGELOG.md

scripts/check-versions.sh "$new" >/dev/null
git add CHANGELOG.md .claude-plugin .omp-plugin
git commit -q -m "chore(release): v$new"
git tag -a "v$new" -m "v$new"
echo "released v$new locally. Publish: git push origin main --follow-tags"
