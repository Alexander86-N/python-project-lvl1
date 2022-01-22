#!/usr/bin/env python

import prompt
from random import randint
from brain_games.games import general_conditions


name = general_conditions.greetings()


def work_with_progression():
    """Determining the missing number in an arithmetic progression"""
    print('What number is missing in the progression?')
    count = 0
    while count != 3:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        idx = randint(0, 9)
        my_list = []
        my-list.append(num1)
        for i in range(9):
            num = num1 + num2
            my_list.append(num)
            num1 = num
        result = str(my_list[idx])
        my_list[ind] = '..'
        print('Question:', ' '.join(my_list))
        answer = prompt.string('Your answer: ')
        check = general_conditions.conclusion(answer, result, name, count)
        count += check
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    work_with_progression()