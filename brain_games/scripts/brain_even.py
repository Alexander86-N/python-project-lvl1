#!/usr/bin/env python

import prompt
from random import randint


def parity_check():
    print("Welcom to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        num = randint(1, 99)
        print('Question:', num)
        answer = prompt.string('Your answer: ')
        if num % 2 == 0:
            if answer.lower() == 'yes':
                count += 1
                print('Correct!')
            else:
                print("'{}' is wrong answer ;(.\
 Correct answer was 'yes'.".format(answer))
                print("Let's try again, {}!".format(name))
        if num % 2 != 0:
            if answer.lower() == 'no':
                count += 1
                print('Correct!')
            else:
                print("'{}' is wrong answer ;(.\
Correct answer was 'no'.".format(answer))
                print("Let's try again, {}!".format(name))
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    parity_check()
