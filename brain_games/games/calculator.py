from random import randint, choice

GAME_DESCRIPTION = 'What is the result of the expression?.'


def definition_of_arguments():
    num1 = str(randint(1, 25))
    num2 = str(randint(1, 25))
    sing = choice(['+', '-', '*'])
    return '{} {} {}'.format(num1, sing, num2)


def correct_answer(number):
    result = str(eval(number))
    return result
