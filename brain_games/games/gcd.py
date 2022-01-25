from math import gcd
from random import randint

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers..'


def definition_of_arguments():
    num1 = randint(2, 50)
    num2 = randint(2, 50)
    return '{} {}'.format(num1, num2)


def correct_answer(number):
    num = number.split()
    result = str(gcd(int(num[0]), int(num[1])))
    return result