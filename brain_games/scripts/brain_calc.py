#!/usr/bin/env python

import prompt
from random import randint, choice
from brain_games.games import general_conditions


name = general_conditions.greetings()


def calculate():
    """The user is shown a random mathematical expression that needs \
       to be calculatedand the correct answer written down."""
    print('What is the result of the expression?')
    count = 0
    while count != 3:
        num1 = str(randint(1, 25))
        num2 = str(randint(1, 25))
        sing = choice(['+', '-', '*'])
        result = str(eval(num1 + sing + num2))
        print('Question:', num1, sing, num2)
        answer = prompt.string('Your answer: ')
        check = general_conditions.conclusion(answer, result, name, count)
        count += check
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    calculate()
