#!/usr/bin/env python

import prompt
from random import randint
from math import gcd
from brain_games.games import general_conditions


name = general_conditions.greetings()


def calculate():
    """The user must calculate and enter the greatest common\
        divisor of these numbers."""
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count != 3:
        num1 = randint(1, 200)
        num2 = randint(1, 200)
        result = gcd(num1, num2)
        print('Question:', num1, num2)
        answer = prompt.string('Your answer: ')
        check = general_conditions.conclusion(answer, result, name, count)
        count += check
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    calculate()
