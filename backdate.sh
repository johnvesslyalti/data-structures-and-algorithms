#!/bin/bash

start_date="2025-06-01"
end_date="2025-06-06"

current_date=$start_date

while [[ "$current_date" < "$end_date" || "$current_date" == "$end_date" ]]; do
  echo "Log for $current_date" > "log-$current_date.md"
  git add .
  GIT_AUTHOR_DATE="$current_date 12:00:00" GIT_COMMITTER_DATE="$current_date 12:00:00" \
    git commit -m "chore: log for $current_date"
  current_date=$(date -I -d "$current_date + 1 day")
done