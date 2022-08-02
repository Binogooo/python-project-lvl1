from random import randint
import prompt


def hello():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even():
    index = 0
    winscore = 3
    while index < winscore:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if (random_number % 2 == 0 and answer.lower() == 'yes') or random_number % 2 != 0 and answer.lower() == 'no':
            print("Correct!")
            index += 1
        elif random_number % 2 == 0 and answer.lower() == 'no':
            print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, Bill!")
            break
        elif random_number % 2 != 0 and answer.lower() == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, Bill!")
            break
        else:
            print("Your answer is wrong, try again")
            break
        if index == 3:
            grats = (f'Congratulations, {name}!')
    return grats
