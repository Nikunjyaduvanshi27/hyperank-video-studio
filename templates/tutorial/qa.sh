#!/usr/bin/env sh
# usage: sh qa.sh tools/<slug>   (same gates as qa.py)
exec python "$(dirname "$0")/qa.py" "$@"
