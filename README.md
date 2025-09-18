
### Hexlet tests and linter status:
[![Actions Status](https://github.com/Denwien/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Denwien/python-project-49/actions)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Denwien_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Denwien_python-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Denwien_python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Denwien_python-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Denwien_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Denwien_python-project-49)

# Brain Games

Набор консольных игр для тренировки логики и математических навыков.  
Игрок отвечает на вопросы, после трёх правильных ответов подряд игра считается пройденной.

## Структура проекта

\`\`\`
brain_games/
├── __init__.py
├── scripts/
│   ├── __init__.py
│   ├── brain_calc.py
│   ├── brain_even.py
│   ├── brain_gcd.py
│   ├── brain_prime.py
│   └── brain_progression.py
└── games/
    ├── brain_calc.py
    ├── brain_even.py
    ├── brain_gcd.py
    ├── brain_prime.py
    └── brain_progression.py
\`\`\`

## Минимальные требования

- Python >= 3.10
- uv

## Установка

\`\`\`bash
git clone https://github.com/Denwien/python-project-49.git
cd python-project-49
uv lock
uv sync
\`\`\`

## Запуск игр

Игры можно запускать напрямую из \`scripts/\`:

\`\`\`bash
python brain_games/scripts/brain-even.py
python brain_games/scripts/brain-calc.py
python brain_games/scripts/brain-gcd.py
python brain_games/scripts/brain-progression.py
python brain_games/scripts/brain-prime.py
\`\`\`

## Демонстрация

### Brain Even
[![asciicast](https://asciinema.org/a/XXXXXXXX.svg)](https://asciinema.org/a/XXXXXXXX)

### Brain Calc
[![asciicast](https://asciinema.org/a/YYYYYYYY.svg)](https://asciinema.org/a/YYYYYYYY)

### Brain GCD
[![asciicast](https://asciinema.org/a/ZZZZZZZZ.svg)](https://asciinema.org/a/ZZZZZZZZ)

### Brain Progression
[![asciicast](https://asciinema.org/a/AAAAAAAA.svg)](https://asciinema.org/a/AAAAAAAA)

### Brain Prime
[![asciicast](https://asciinema.org/a/BBBBBBBB.svg)](https://asciinema.org/a/BBBBBBBB)
