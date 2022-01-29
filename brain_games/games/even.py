from random import randint

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def correct_answer(number):
    """Checks if a number is even."""
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def generate_question_and_answer():
     """Returns a variant of the question and the correct answer to it."""
    example = randint(1, 99)
    result = str(correct_answer(example))
    return example, result
