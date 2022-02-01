from random import randint, choice
from operator import add, sub, mul

GAME_DESCRIPTION = 'What is the result of the expression?'


def calc(number1, number2, operation):
    """Calculates the result of a mathematical expression."""
    result = operation(number1, number2)
    return result


def generate_question_and_answer():
    """Selection of random numbers and operations."""
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    operation = choice([['+', add], ['-', sub], ['*', mul]])
    example = '{} {} {}'.format(num1, operation[0], num2)
    result = str(calc(num1, num2, operation[1]))
    return example, result
