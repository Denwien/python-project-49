
### Hexlet tests and linter status:
[![Actions Status](https://github.com/Denwien/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Denwien/python-project-49/actions)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Denwien_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Denwien_python-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Denwien_python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Denwien_python-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Denwien_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Denwien_python-project-49)

# Brain Games

Набор консольных игр для тренировки логики и математических навыков.  
Игрок отвечает на вопросы, после трёх правильных ответов подряд игра считается пройденной.

## Структура проекта

```
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
```

## Минимальные требования

- Python >= 3.10
- uv

## Установка

```
git clone https://github.com/Denwien/python-project-49.git
cd python-project-49
uv lock
uv sync
```

## Запуск игр

Игры можно запускать напрямую из \`brain_games/games/\`:

```bash
python3 brain_games/games/brain-even.py
python3 brain_games/games/brain-calc.py
python3 brain_games/games/brain-gcd.py
python3 brain_games/games/brain-progression.py
python3 brain_games/games/brain-prime.py

```

## Демонстрация

### Brain Even
https://asciinema.org/a/oj9UIEVXkhP2RMPvVx3DH2oEw

### Brain Calc
https://asciinema.org/a/RY0ZcdTt9JMoNKDtVIWkihKOe

### Brain GCD
https://asciinema.org/a/bfIL8UjlNIAx8gkJKL65MLf6v

### Brain Progression
https://asciinema.org/a/1ROrgSqJXsvL2jmNf8m3Iq1TR

### Brain Prime
https://asciinema.org/a/gLGymi2DXeOTbOX5VCbVkolH1
