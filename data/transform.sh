#!/bin/sh

for i in $(seq 1 5); do
    for file in Driver"$i"/*.xlsx; do
        python3 excel_to_csv.py "$file"
    done
done
