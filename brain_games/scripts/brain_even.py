#!/usr/bin/env python3

import prompt
import math

def hello():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even():
    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    index = 0
    winscore = 3
    while index < winscore:
        if random_number % 2 == 0 and answer.lower() == 'yes':
            print('Correct!')
            index += 1
        elif random_number % 2 == 0 and answer.lower() == 'no':
            print("no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, Bill!")
        elif random_number % 2 != 0 and answer.lower() == 'yes':
            print("yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, Bill!")
        elif random_number % 2 != 0 and answer.lower() == 'no':
            print('Correct!')
        congrats = print('Congratulations, {name}!')
    return congrats

    




def main():
    print('Welcome to the Brain Games!')
    hello()
    is_even()

if __name__ == '__main__':
    main()




