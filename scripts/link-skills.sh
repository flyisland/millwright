#!/usr/bin/env bash
set -euo pipefail

# Development helper: link this checkout's skills into the local skill directory.
# Existing non-symlink entries require explicit approval before replacement.
REPO="$(cd "$(dirname "$0")/.." && pwd -P)"
DEST="$HOME/.agents/skills"

# Resolve existing ancestors physically, even when the final directory does not
# exist. Reject dangling links and non-directory ancestors rather than guessing.
resolve_directory() {
  local path="$1" parent resolved
  if [ -d "$path" ]; then
    (cd "$path" && pwd -P)
  elif [ -e "$path" ] || [ -L "$path" ]; then
    echo "error: not a usable directory: $path" >&2
    return 1
  else
    parent="$(dirname "$path")"
    resolved="$(resolve_directory "$parent")" || return 1
    printf '%s/%s\n' "${resolved%/}" "$(basename "$path")"
  fi
}

# A parent symlink can route writes into the checkout even when DEST itself is
# not a symlink. Never allow approval to override this source-data protection.
while :; do
  resolved="$(resolve_directory "$DEST")" || exit 1
  case "$resolved" in
    "$REPO"|"$REPO"/*)
      printf 'error: destination %s resolves into this repository: %s\n' "$DEST" "$resolved" >&2
      echo "Linking here could delete the source skills and create self-referencing links." >&2
      echo "Manually fix the destination or its parent symlinks in another terminal." >&2
      printf 'Then type retry to check again; anything else cancels: ' >&2
      answer=''
      if ! IFS= read -r answer || [ "$answer" != retry ]; then
        echo "Cancelled; no skills were changed." >&2
        exit 1
      fi
      ;;
    *) break ;;
  esac
done

names=()
srcs=()
# Capture discovery failures before making any changes (process substitution
# alone would not propagate find's exit status to the calling shell).
manifest="$(mktemp)"
trap 'rm -f "$manifest"' EXIT
find "$REPO/skills" -name SKILL.md -not -path '*/node_modules/*' -not -path '*/deprecated/*' -not -path '*/misc/*' -print0 > "$manifest"
while IFS= read -r -d '' skill_md; do
  src="$(dirname "$skill_md")"
  names+=("$(basename "$src")")
  srcs+=("$src")
done < "$manifest"

# Preflight all entries before modifying any of them.
conflicts=0
for i in "${!names[@]}"; do
  target="$resolved/${names[$i]}"
  if [ -e "$target" ] && [ ! -L "$target" ]; then
    printf 'WARNING: existing file/directory will be permanently deleted: %s\n' "$target" >&2
    conflicts=$((conflicts + 1))
  fi
done
if [ "$conflicts" -gt 0 ]; then
  echo "Local modifications and all files inside these entries will be lost; no backup is made." >&2
  printf 'Delete these entries and replace them with repository symlinks? Type yes to continue: ' >&2
  answer=''
  if ! IFS= read -r answer || [ "$answer" != yes ]; then
    echo "Cancelled; no skills were changed." >&2
    exit 1
  fi
fi

# Use the resolved path so a changed alias cannot redirect the approved writes.
mkdir -p "$resolved"
for i in "${!names[@]}"; do
  name="${names[$i]}"
  src="${srcs[$i]}"
  target="$resolved/$name"
  if [ -e "$target" ] && [ ! -L "$target" ]; then
    rm -rf -- "$target"
  fi
  ln -sfn "$src" "$target"
  printf 'linked %s -> %s (%s)\n' "$name" "$src" "$resolved"
done
