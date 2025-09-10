import random
from math import gcd
from brain_games.cli import welcome_user

def play():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    correct_answers = 0
    while correct_answers < 3:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        print(f"Question: {num1} {num2}")
        answer = input("Your answer: ").strip()
        correct_answer = str(gcd(num1, num2))
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break
