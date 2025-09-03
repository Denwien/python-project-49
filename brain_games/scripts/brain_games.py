import sys
from brain_games.games import brain_even

def main():
    name = input("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!\n")

    print("Available games:")
    print("1 - brain-even (check if number is even)")
    print("0 - Exit")

    choice = input("Choose a game (0/1): ").strip()

    if choice == "1":
        print("\nYou chose brain-even!\n")
        brain_even.play_game()
    elif choice == "0":
        print("Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice, exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
