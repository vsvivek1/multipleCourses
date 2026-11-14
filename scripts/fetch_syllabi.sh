#!/usr/bin/env bash
# Download every syllabus PDF listed in a sources.csv and extract its text.
# Usage: scripts/fetch_syllabi.sh syllabi/medical/sources.csv
set -uo pipefail
csv="${1:?path to sources.csv}"
dir="$(dirname "$csv")"
failed=0
tail -n +2 "$csv" | while IFS=, read -r slug post url; do
  [ -z "$slug" ] && continue
  out="$dir/$slug.pdf"
  ok=0
  for u in "$url" "${url/http:/https:}"; do
    if curl -fsSL --retry 3 --retry-delay 5 -A "Mozilla/5.0" -o "$out" "$u" \
       && head -c 5 "$out" | grep -q '%PDF'; then ok=1; break; fi
  done
  if [ "$ok" = 1 ]; then
    pdftotext -layout "$out" "$dir/$slug.txt" || true
    echo "OK   $slug"
  else
    rm -f "$out"; echo "FAIL $slug $url"; failed=1
  fi
done
exit 0
