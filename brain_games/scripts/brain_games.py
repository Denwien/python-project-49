import sys
from brain_games.games import (
    brain_even,
    brain_calc,
    brain_gcd,
    brain_prime,
    brain_progression,
)

GAMES = {
    "1": brain_even,
    "2": brain_calc,
    "3": brain_gcd,
    "4": brain_prime,
    "5": brain_progression,
}

GAME_NAMES = {
    "1": "brain-even",
    "2": "brain-calc",
    "3": "brain-gcd",
    "4": "brain-prime",
    "5": "brain-progression",
}


def read_name_nonblocking():
    """
    Если stdin — tty, просим имя через input().
    Если stdin не tty (CI / pipe), пробуем прочитать одну строку из stdin (тесты могут прислать имя),
    иначе возвращаем 'Player' как fallback.
    """
    if sys.stdin.isatty():
        return input("May I have your name? ")
    # stdin не tty — читаем одну строку (может быть пустой)
    try:
        name = sys.stdin.readline().strip()
        return name if name else "Player"
    except Exception:
        return "Player"


def main():
    print("Welcome to the Brain Games!")
    name = read_name_nonblocking()
    print(f"Hello, {name}!\n")

    print("Available games:")
    for key, nm in GAME_NAMES.items():
        print(f"{key} - {nm}")
    print("0 - Exit")

    # Приоритет: 1) аргумент командной строки 2) интерактивный ввод 3) если неинтерактивно и нет аргумента — выход (0)
    if len(sys.argv) > 1:
        choice = sys.argv[1]
    else:
        if sys.stdin.isatty():
            choice = input("Choose a game (0-5): ").strip()
        else:
            # Неинтерактивно и аргументов нет — выбираем выход, чтобы тесты не зависли
            choice = "0"

    if choice in GAMES:
        print(f"\nYou chose {GAME_NAMES[choice]}!\n")
        # вызываем функцию игры (модули должны предоставлять play_game)
        GAMES[choice].play_game()
        return 0
    if choice == "0":
        print("Goodbye!")
        return 0

    print("Invalid choice. Exiting.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
