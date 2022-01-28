from random import randint, choice
from operator import add, sub, mul

GAME_DESCRIPTION = 'What is the result of the expression?.'


#def definition_of_arguments():
#    """Selection of random numbers and operations."""
#    num1 = str(randint(1, 25))
#    num2 = str(randint(1, 25))
#    sing = choice(['+', '-', '*'])
#    return '{} {} {}'.format(num1, sing, num2)


#def correct_answer(number):
#    """Calculates the result of a mathematical expression."""
#    result = str(eval(number))
#    return result


def calc(number1,number2,sing):
    """Calculates the result of a mathematical expression."""
    result = sing(number1, number2)
    return result


def generate_question_and_answer():
     """Selection of random numbers and operations."""
    num1 = str(randint(1, 25))
    num2 = str(randint(1, 25))
    sing = choice([['+', add], ['-', sub], ['*', mul]])
    example = '{} {} {}'.format(num1, sing[0], num2)
    result = calc(num1 ,num2, sing[1])
    return example, result
