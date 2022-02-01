from random import randint

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Checks if a number is even."""
    if number % 2 == 0:
        return True
    else:
        return False


def generate_question_and_answer():
    """Returns a variant of the question and the correct answer to it."""
    example = randint(1, 99)
    result = 'yes' if is_even(example) else 'no'
    return example, result
