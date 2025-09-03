import random

def is_even(number):
    return number % 2 == 0

def get_question():
    return random.randint(1, 100)

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = get_question()
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()
        correct_answer = "yes" if is_even(number) else "no"

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
            correct_answers += 1

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
