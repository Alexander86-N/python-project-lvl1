#!/usr/bin/env python

import prompt
from random import randint, choice


def main():
    print("Welcom to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    count = 0
    while count != 3:
        num1 = str(randint(1, 25))
        num2 = str(randint(1, 25))
        sing = choice(['+', '-', '*'])
        result = eval(num1 + sing + num2)
        print('Question:', num1, sing, num2)
        answer = prompt.string('Your answer: ')
        if answwer == result:
            count += 1
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(.Correct answer was '{}'.".format(answer, result))
            print("Let's try again, {}!".format(name))
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
