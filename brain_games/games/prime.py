from random import randint

GAME_DESCRIPTION = 'Answer "yes" if given number is prime.\
 Otherwise answer "no".'


def is_prime(number):
    """Primality test."""
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
    if count <= 0:
        return True
    else:
        return False


def generate_question_and_answer():
    """Returns a variant of the question and the correct answer to it."""
    example = randint(2, 10)
    result = 'yes' if is_prime(example) else 'no'
    return example, result
