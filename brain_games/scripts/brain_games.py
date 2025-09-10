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


def read_name():
    """
    Всегда печатаем 'May I have your name?'.
    Если stdin интерактивный, используем input().
    Если нет — читаем строку из stdin (или ставим Player по умолчанию).
    """
    prompt = "May I have your name?"
    print(prompt, end=" ")
    sys.stdout.flush()

    if sys.stdin.isatty():
        name = input().strip()
    else:
        line = sys.stdin.readline().strip()
        name = line if line else "Player"
    return name


def main():
    print("Welcome to the Brain Games!")
    name = read_name()
    print(f"Hello, {name}!\n")

    print("Available games:")
    for key, nm in GAME_NAMES.items():
        print(f"{key} - {nm}")
    print("0 - Exit")

    if len(sys.argv) > 1:
        choice = sys.argv[1]
    else:
        if sys.stdin.isatty():
            choice = input("Choose a game (0-5): ").strip()
        else:
            choice = "0"

    if choice in GAMES:
        print(f"\nYou chose {GAME_NAMES[choice]}!\n")
        GAMES[choice].play_game()
        return 0
    elif choice == "0":
        print("Goodbye!")
        return 0
    else:
        print("Invalid choice. Exiting.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
