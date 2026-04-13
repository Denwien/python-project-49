# 🧠 Brain Games

[![Actions Status](https://github.com/Denwien/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Denwien/python-project-49/actions)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Denwien_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Denwien_python-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Denwien_python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Denwien_python-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Denwien_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Denwien_python-project-49)

> A collection of five CLI mini-games that challenge your math and logic skills. Answer three questions in a row correctly — and you win!

---

## 🎮 Games

| Game | Description |
|------|-------------|
| **Brain Even** | Is the number even or odd? |
| **Brain Calc** | Solve a random arithmetic expression |
| **Brain GCD** | Find the greatest common divisor |
| **Brain Progression** | Fill in the missing number in a sequence |
| **Brain Prime** | Determine if a number is prime |

---

## 🚀 Getting Started

### Requirements

- Python >= 3.10
- [uv](https://github.com/astral-sh/uv)

### Installation

    git clone https://github.com/Denwien/python-project-49.git
    cd python-project-49
    uv sync

### Run a game

    python3 brain_games/games/brain_even.py
    python3 brain_games/games/brain_calc.py
    python3 brain_games/games/brain_gcd.py
    python3 brain_games/games/brain_progression.py
    python3 brain_games/games/brain_prime.py

---

## 📁 Project Structure

    brain_games/
    ├── scripts/          # Entry points
    │   ├── brain_calc.py
    │   ├── brain_even.py
    │   ├── brain_gcd.py
    │   ├── brain_prime.py
    │   └── brain_progression.py
    └── games/            # Game logic
        ├── brain_calc.py
        ├── brain_even.py
        ├── brain_gcd.py
        ├── brain_prime.py
        └── brain_progression.py

---

## 🎬 Demo

### Brain Even
[![asciicast](https://asciinema.org/a/oj9UIEVXkhP2RMPvVx3DH2oEw.svg)](https://asciinema.org/a/oj9UIEVXkhP2RMPvVx3DH2oEw)

### Brain Calc
[![asciicast](https://asciinema.org/a/RY0ZcdTt9JMoNKDtVIWkihKOe.svg)](https://asciinema.org/a/RY0ZcdTt9JMoNKDtVIWkihKOe)

### Brain GCD
[![asciicast](https://asciinema.org/a/bfIL8UjlNIAx8gkJKL65MLf6v.svg)](https://asciinema.org/a/bfIL8UjlNIAx8gkJKL65MLf6v)

### Brain Progression
[![asciicast](https://asciinema.org/a/1ROrgSqJXsvL2jmNf8m3Iq1TR.svg)](https://asciinema.org/a/1ROrgSqJXsvL2jmNf8m3Iq1TR)

### Brain Prime
[![asciicast](https://asciinema.org/a/gLGymi2DXeOTbOX5VCbVkolH1.svg)](https://asciinema.org/a/gLGymi2DXeOTbOX5VCbVkolH1)

---

## 🛠️ Built With

- **Python 3.10+**
- **uv** — fast Python package manager
- **SonarCloud** — code quality analysis
- **GitHub Actions** — CI/CD

---

## 👤 Author

**Denwien** · [GitHub](https://github.com/Denwien)
