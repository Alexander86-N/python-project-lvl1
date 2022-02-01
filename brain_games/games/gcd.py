from random import randint

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def calc_gcd(number1, number2):
    """Calculates the greatest common divisor of these numbers."""
    maxi = max(number1, number2)
    for num in range(1, maxi + 1):
        if number1 % num == 0 and number2 % num == 0:
    return num


def generate_question_and_answer():
    """Returns a variant of the question and the correct answer to it."""
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    example = '{} {}'.format(num1, num2)
    result = str(calc_gcd(num1, num2))
    return example, result
