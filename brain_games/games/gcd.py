from random import randint

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


#def generatec_arguments():
#    """Selection of random numbers."""
#    num1 = randint(2, 50)
#    num2 = randint(2, 50)
#    return '{} {}'.format(num1, num2)


def search_answer(number1, number2):
    """Calculates the greatest common divisor of these numbers."""
   # if number1 > number2:
   #     maxi = number1
   # else:
   #     maxi = number2
    maxi = max(number1, number2)
    for i in range(1, maxi + 1):
        if number1 % i == 0 and number2 % i == 0:
            result = str(i)
    return result

def generate_question_and_answer():
     """Selection of random numbers."""
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    example = '{} {}'.format(num1, num2)
    result = search_answer(num1 ,num2)
    return example, result
