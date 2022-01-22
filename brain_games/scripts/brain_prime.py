#!/usr/bin/env python

import prompt
from random import randint
from brain_games.games import general_conditions


name = general_conditions.greetings()


def prime_number():
    """Asking if a number is prime"""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count != 3:
        num = randint(2, 50)
        result = ''
        for i in range(2, num // 2):
            if num % i == 0:
                result = 'no'
                break
            else:
                result = 'yes'
        print('Question:', num)
        answer = prompt.string('Your answer: ')
        check = general_conditions.conclusion(answer, result, name, count)
        count += check
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    prime_number()
