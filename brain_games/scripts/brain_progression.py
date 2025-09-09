import random
from brain_games.cli import welcome_user


def generate_progression(start, step, length):
    return [start + i * step for i in range(length)]


def main():
    name = welcome_user()
    print("What number is missing in the progression?")

    for _ in range(3):
        start = random.randint(1, 20)   
        step = random.randint(2, 5)     
        length = 10                     
        progression = generate_progression(start, step, length)
        hidden_index = random.randint(0, length - 1)
        correct_answer = progression[hidden_index]
        progression[hidden_index] = ".."

        question = " ".join(map(str, progression))
        print(f"Question: {question}")
        answer = input("Your answer: ")

        if answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
