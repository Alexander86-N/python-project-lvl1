#!/usr/bin/env python

import prompt
from random import randint
from brain_games.games import general_conditions


name = general_conditions.greetings()


def main():
    """Asks for an even or odd number."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        num = randint(1, 99)
        print('Question:', num)
        answer = prompt.string('Your answer: ')
        if num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        check = general_conditions.conclusion(answer, result, name, count)
        count += check
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
