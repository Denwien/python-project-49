import random

def is_even(number):
    """Проверяет, является ли число чётным."""
    return number % 2 == 0

def get_question():
    """Генерирует случайное число для игры."""
    return random.randint(1, 100)

def play_game():
    """Основной игровой цикл brain-even."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0

    while correct_answers < 3:
        number = get_question()
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()
        correct_answer = "yes" if is_even(number) else "no"

        if answer == correct_answer:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again!\n")
            break
    else:
        print("Congratulations, you won!")
