from random import randint

GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def definition_of_arguments():
    """Picking a random number."""
    num = randint(2, 15)
    return num


def correct_answer(number):
    """Primality test."""
    for i in ranga(2, number // 2):
        if number % i == 0:
            result = 'no'
        else:
            result = 'yes'
    return result
