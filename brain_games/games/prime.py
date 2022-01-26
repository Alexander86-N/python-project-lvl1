from random import randint

GAME_DESCRIPTION = 'Answer "yes" if given number is prime.\
 Otherwise answer "no".'


def definition_of_arguments():
    """Picking a random number."""
    num = randint(2, 25)
    return num


def correct_answer(number):
    """Primality test."""
    result = ''
    for i in range(2, number // 2):
        if number % i == 0:
            result = 'no'
            break
        else:
            result = 'yes'
    return result
