from random import randint, choice

GAME_DESCRIPTION = 'What is the result of the expression?.'


def definition_of_arguments():
    """Selection of random numbers and operations."""
    num1 = str(randint(1, 25))
    num2 = str(randint(1, 25))
    sing = choice(['+', '-', '*'])
    return '{} {} {}'.format(num1, sing, num2)


def correct_answer(number):
    """Calculates the result of a mathematical expression."""
    result = str(eval(number))
    return result
