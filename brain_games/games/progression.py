from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(first_term, difference, length, replacement_index):
    """Computing members of a progression"""
    """Getting a string representation of a progression"""
    numbs = []
    for i in range(length):
        numbs.append(str(first_term + i * difference))
    numbers[replacement_index] = '..'
    return ' '.join(numbers)


def correct_answer(number, item):
    """Calculating the correct answer"""
    nums = number.split()
    if item >= 2:
        d = int(nums[1]) - int(nums[0])
    else:
        d = int(nums[item + 2]) - int(nums[item + 1])
    result = str(int(nums[0]) + item * d)
    return result


def generate_question_and_answer():
     """Returns a variant of the question and the correct answer to it."""
    a1 = randint(1, 25)
    d = randint(1, 25)
    length = randint(6, 10)
    item = randint(1, length)
    example = generate_progression(a1, d, length, item)
    result = str(correct_answer(example, item))
    return example, result
