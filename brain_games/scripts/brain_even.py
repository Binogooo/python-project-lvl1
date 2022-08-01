#!/usr/bin/env python3

import prompt
from random import randint
from  brain_games.logic.even_logic import is_even


def hello():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    print('Welcome to the Brain Games!')
    hello()
    is_even()


if __name__ == '__main__':
    main()
