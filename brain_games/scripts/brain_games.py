import sys
from brain_games.cli import welcome_user
from brain_games.games import (
    brain_even,
    brain_calc,
    brain_gcd,
    brain_progression,
    brain_prime
)

GAMES = {
    "brain-even": brain_even,
    "brain-calc": brain_calc,
    "brain-gcd": brain_gcd,
    "brain-progression": brain_progression,
    "brain-prime": brain_prime
}

def main():
    name = None
    game_choice = None

    for arg in sys.argv[1:]:
        if arg.startswith("--name="):
            name = arg.split("=", 1)[1]
        elif arg.startswith("--game="):
            game_choice = arg.split("=", 1)[1]


    if not name:
        name = welcome_user()

    if game_choice in GAMES:
        GAMES[game_choice].play_game()
        return

    print("\nAvailable games:")
    for idx, game in enumerate(GAMES, start=1):
        print(f"{idx} - {game}")
    print("0 - Exit")

    choice = input("Choose a game (0/1/2/...): ").strip()
    if choice == "0":
        print("Goodbye!")
        sys.exit(0)

    try:
        choice_idx = int(choice) - 1
        game_list = list(GAMES.values())
        if 0 <= choice_idx < len(game_list):
            game_list[choice_idx].play_game()
        else:
            print("Unknown game choice. Exiting.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
