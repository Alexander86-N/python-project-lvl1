from random import randint

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generatec_arguments():
    """Selection of random numbers."""
    num1 = randint(2, 50)
    num2 = randint(2, 50)
    return '{} {}'.format(num1, num2)


def correct_answer(number):
    """Calculates the greatest common divisor of these numbers."""
    num = number.split()
    if int(num[0]) > int(num[1]):
        maxi = int(num[0])
    else:
        maxi = int(num[1])
    for i in range(1, maxi + 1):
        if int(num[0]) % i == 0 and int(num[1]) % i == 0:
            result = i
    return result
