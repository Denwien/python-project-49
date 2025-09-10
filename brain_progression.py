import random
from brain_games.cli import welcome_user

def generate_progression(length=10):
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    return [start + step * i for i in range(length)]

def play():
    name = welcome_user()
    print('What number is missing in the progression?')

    correct_answers = 0
    while correct_answers < 3:
        progression = generate_progression()
        hidden_index = random.randint(0, len(progression) - 1)
        correct_answer = str(progression[hidden_index])
        progression_display = progression[:]
        progression_display[hidden_index] = '..'
        print("Question: " + " ".join(map(str, progression_display)))
        answer = input("Your answer: ").strip()
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break
