#!/usr/bin/env bash
set -e

# Список игр, которые будем запускать
games=(
  "brain_games.scripts.brain_games"
)

# Запуск игр
for game in "${games[@]}"; do
  echo "=== Running $game ==="
  PYTHONPATH=. python -m "$game"
  echo
done
