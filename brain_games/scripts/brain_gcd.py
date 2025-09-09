import random
from brain_games.cli import welcome_user


def gcd(a, b):
    """Вычисление НОД (алгоритм Евклида)."""
    while b:
        a, b = b, a % b
    return a


def play_game():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    correct_answers = 0
    while correct_answers < 3:
        a, b = random.randint(1, 100), random.randint(1, 100)
        print(f"Question: {a} {b}")
        answer = input("Your answer: ").strip()

        correct_answer = str(gcd(a, b))
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    play_game()


if __name__ == "__main__":
    main()
