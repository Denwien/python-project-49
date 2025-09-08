import random


def calc_expression():
    """Генерация случайного выражения и вычисление результата"""
    operators = ['+', '-', '*']
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(operators)

    expression = f"{num1} {operator} {num2}"
    result = eval(expression)  # вычисляем выражение

    return expression, result


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    correct_answers = 0
    while correct_answers < 3:
        expression, correct_answer = calc_expression()
        print(f"Question: {expression}")
        answer = input("Your answer: ").strip()

        if answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()