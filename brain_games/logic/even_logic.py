from random import randint
import prompt


def welcome_user():
    """Ask username."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_result(answer, correct_answer, name):
    """Getting user answer."""
    if answer == str(correct_answer):
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(.Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")


def even_game():
    """Even game code."""
    name = welcome_user()
    counter = 0
    print('Answer "yes" if number is even, otherwise answer "no".')
    for _ in range(3):
        question = randint(1, 101)
        if question % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        get_result(answer, correct_answer, name)
        counter += 1
        if answer != correct_answer:
            break
        if counter == 3:
            print(f"Congratulations, {name}!")
