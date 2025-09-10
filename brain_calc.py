import random
from brain_games.cli import welcome_user

def play():
    name = welcome_user()
    print('Welcome to the Brain Calc game!')
    print('What is the result of the expression?')

    correct_answers = 0
    while correct_answers < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        question = f"{num1} {operator} {num2}"
        print(f"Question: {question}")
        answer = input("Your answer: ").strip()
        correct_answer = str(eval(question))
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break
