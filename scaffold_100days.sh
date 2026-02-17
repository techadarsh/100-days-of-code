#!/usr/bin/env bash
set -euo pipefail

# 100DaysOfPython folder scaffold
# Usage:
#   ./scaffold_100days.sh            # creates day-001 only
#   ./scaffold_100days.sh 10         # creates day-001..day-010
#   ./scaffold_100days.sh 100        # creates day-001..day-100

DAYS_COUNT="${1:-1}"

pad3 () { printf "%03d" "$1"; }

ROOT_DIR="$(pwd)"

mkdir -p "$ROOT_DIR/notes"
mkdir -p "$ROOT_DIR/days"

for ((i=1; i<=DAYS_COUNT; i++)); do
  DAY="day-$(pad3 "$i")"

  mkdir -p "$ROOT_DIR/days/$DAY/assets"

  # Starter python file for the day
  if [[ ! -f "$ROOT_DIR/days/$DAY/task.py" ]]; then
cat > "$ROOT_DIR/days/$DAY/task.py" << EOF
"""
$DAY - 100 Days of Python

Write your practice code here.
"""

def main() -> None:
    print("Running $DAY")

if __name__ == "__main__":
    main()
EOF
  fi

  # Notes file for the day
  if [[ ! -f "$ROOT_DIR/notes/$DAY.md" ]]; then
cat > "$ROOT_DIR/notes/$DAY.md" << EOF
# $DAY Notes

## Concepts
- 

## Key terms
- 

## Practice
- 

## Summary
- 
EOF
  fi
done

echo "Created scaffold in: $ROOT_DIR"
echo "Days created: $DAYS_COUNT"

