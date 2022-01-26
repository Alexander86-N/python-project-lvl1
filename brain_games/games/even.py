from random import randint

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def definition_of_arguments():
    """Picking a random number."""
    num = randint(1, 99)
    return num


def correct_answer(number):
    """Checks if a number is even."""
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result
