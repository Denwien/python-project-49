import sys
from brain_games.games import (
    brain_even,
    brain_calc,
    brain_gcd,
    brain_prime,
    brain_progression
)

GAMES = {
    "1": brain_even,
    "2": brain_calc,
    "3": brain_gcd,
    "4": brain_prime,
    "5": brain_progression,
}

GAME_NAMES = {
    "1": "brain-even (check if number is even)",
    "2": "brain-calc (simple math calculations)",
    "3": "brain-gcd (greatest common divisor)",
    "4": "brain-prime (check if number is prime)",
    "5": "brain-progression (find missing number in progression)",
}

def main():
    # Проверка аргумента командной строки
    if len(sys.argv) > 1:
        choice = sys.argv[1].strip()
    else:
        print("Available games:")
        for key, name in GAME_NAMES.items():
            print(f"{key} - {name}")
        print("0 - Exit")
        choice = input("Choose a game (0-5): ").strip()

    if choice in GAMES:
        print(f"\nYou chose {GAME_NAMES[choice]}!\n")
        GAMES[choice].play_game()
    elif choice == "0":
        print("Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
