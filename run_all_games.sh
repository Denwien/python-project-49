#!/usr/bin/env bash

# Скрипт для запуска всех игр в bin/ и проверки выполнения
for game in bin/brain-*; do
    echo "=== Running $game ==="
    
    # Запуск игры с передачей имени 'denis' и сохранение вывода
    output=$(PYTHONPATH=. python "$game" <<< $'denis\n' 2>&1)
    exit_code=$?

    # Вывод результата игры
    echo "$output"

    # Проверка статуса выполнения
    if [ $exit_code -eq 0 ]; then
        echo "Status: Passed"
    else
        echo "Status: Failed (exit code $exit_code)"
    fi

    echo
done
