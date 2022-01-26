from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'


def getting_a_progression(a1, d):
    """Computing members of a progression"""
    numbs = []
    for i in range(10):
        numbs.append(str(a1 + i * d))
    return numbs


def definition_of_arguments():
    """Getting a string representation of a progression"""
    numbers = getting_a_progression(randint(2, 50), randint(2, 50))
    numbers[randint(1, 9)] = '..'
    return ' '.join(numbers)


def correct_answer(number):
    """Calculating the correct answer"""
    nums = number.split()
    idx = nums.index('..')
    if idx >= 2:
        d = int(nums[1]) - int(nums[0])
    else:
        d = int(nums[idx + 2]) - int(nums[idx + 1])
    result = str(int(nums[0]) + idx * d)
    return result