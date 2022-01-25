from random import randint

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def definition_of_arguments():
    num = randint(1, 99)
    return num

number = definition_of_arguments()

def correct_answer(number):
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result
