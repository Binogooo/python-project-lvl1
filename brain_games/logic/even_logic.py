from random import randint
import prompt


def is_even():
    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    print(answer_select)
    index = 0
    winscore = 3
    congrats = print('Congratulations, {name}!')
    while index < winscore:
        if (random_number % 2 == 0 and answer.lower() == 'yes') and (random_number % 2 != 0 and answer.lower() == 'no'):
            print('Correct!')
            index = index + 1
        elif random_number % 2 != 0 and answer.lower() == 'yes':
            print('''"yes" is wrong answer ;(. Correct answer was "no".\nLet's try again, {name}''')
        elif random_number % 2 == 0 and answer.lower() == 'no':
            print('''"yes" is wrong answer ;(. Correct answer was "no".\nLet's try again, {name}''')
        else:
            print('Wrong answer')
        return congrats
