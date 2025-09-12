import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(number: int) -> bool:
    return number % 2 == 0

def generate_round():
    number = random.randint(1, 100)
    question = f'Question: {number}'
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer

def play_game():
    question, correct_answer = generate_round()
    print(question)
    return correct_answer
