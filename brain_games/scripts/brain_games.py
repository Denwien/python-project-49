import sys
from brain_games.cli import welcome_user
from brain_games.games import brain_even, brain_calc, brain_gcd, brain_prime, brain_progression

def main():
    # Получаем аргументы командной строки
    name = None
    game_choice = None
    for arg in sys.argv[1:]:
        if arg.startswith("--name="):
            name = arg.split("=")[1]
        elif arg.startswith("--game="):
            game_choice = arg.split("=")[1]

    # Если имя не передано через аргументы
    if not name:
        name = welcome_user()

    print("\nAvailable games:")
    print("1 - brain-even (check if number is even)")
    print("2 - brain-calc (simple math)")
    print("3 - brain-gcd (greatest common divisor)")
    print("4 - brain-prime (prime number check)")
    print("5 - brain-progression (progression game)")
    print("0 - Exit")

    # Если игра не передана через аргументы
    if not game_choice:
        game_choice = input("Choose a game (0-5): ").strip()

    if game_choice == "1":
        print("\nYou chose brain-even!\n")
        brain_even.play_game()
    elif game_choice == "2":
        print("\nYou chose brain-calc!\n")
        brain_calc.play_game()
    elif game_choice == "3":
        print("\nYou chose brain-gcd!\n")
        brain_gcd.play_game()
    elif game_choice == "4":
        print("\nYou chose brain-prime!\n")
        brain_prime.play_game()
    elif game_choice == "5":
        print("\nYou chose brain-progression!\n")
        brain_progression.play_game()
    elif game_choice == "0":
        print("Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()

