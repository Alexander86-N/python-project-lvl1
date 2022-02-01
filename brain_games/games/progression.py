from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(first_term, difference, length):
    """Computing members of a progression"""
    numbers = []
    for i in range(length):
        numbers.append(str(first_term + i * difference))
    return numbers


def generate_question_and_answer():
    """Returns a variant of the question and the correct answer to it."""
    a1 = randint(1, 25)
    d = randint(1, 25)
    length = randint(6, 10)
    index = randint(1, length - 1)
    example = generate_progression(a1, d, length)
    result = str(example[index])
    example[index] = '..'
    return ' '.join(example), result
