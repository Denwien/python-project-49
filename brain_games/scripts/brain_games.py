import sys
from brain_games.cli import welcome_user
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
    "1": "brain-even (check if number is even)",
    "2": "brain-calc (simple math calculations)",
    "3": "brain-gcd (greatest common divisor)",
    "4": "brain-prime (check if number is prime)",
    "5": "brain-progression (find missing number in progression)",
}

def main():
    
    name = None
    game_choice = None
    for arg in sys.argv[1:]:
        if arg.startswith("--name="):
            name = arg.split("=")[1]
        elif arg.startswith("--game="):
            game_choice = arg.split("=")[1]

    
    if not name:
        name = welcome_user()

    print("\nAvailable games:")
    for key, description in GAME_NAMES.items():
        print(f"{key} - {description}")
    print("0 - Exit")

    
    if game_choice in GAMES:
        print(f"\nYou chose {GAME_NAMES[game_choice]}!\n")
        GAMES[game_choice].play_game()
        return
    elif game_choice == "0":
        print("Goodbye!")
        sys.exit(0)

    
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
