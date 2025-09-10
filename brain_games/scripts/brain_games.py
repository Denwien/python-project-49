import sys
from brain_games.cli import welcome_user
from brain_games.games import brain_even  # потом добавишь brain_calc и другие

def main():
    # Аргументы командной строки
    name = None
    game_choice = None
    for arg in sys.argv[1:]:
        if arg.startswith("--name="):
            name = arg.split("=")[1]
        elif arg.startswith("--game="):
            game_choice = arg.split("=")[1]

    # Получение имени
    if not name:
        name = welcome_user()

    print("\nAvailable games:")
    print("1 - brain-even (check if number is even)")
    print("0 - Exit")

    # Получение выбора игры
    if not game_choice:
        game_choice = input("Choose a game (0/1): ").strip()

    if game_choice == "1" or game_choice.lower() == "brain-even":
        print("\nYou chose brain-even!\n")
        brain_even.play_game()
    elif game_choice == "0":
        print("Goodbye!")
        sys.exit(0)
    else:
        print("Unknown game")

if __name__ == "__main__":
    main()
