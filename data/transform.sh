#!/bin/sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

for i in $(seq 1 5); do
    for file in "$SCRIPT_DIR"/Driver"$i"/*.xlsx; do
        python3 "$SCRIPT_DIR"/excel_to_csv.py "$file"
    done
done
