import prompt


def greetings():
    """Greeting and introduction to the player."""
    print("Welcom to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def conclusion(answer, result, name, count):
    """Returns the result of the condition."""
    check = 0
    if answer == result:
        check += 1
        print('Correct!')
    else:
        print("'{}' is wrong answer ;(.\
Correct answer was '{}'.".format(answer, result))
        print("Let's try again, {}!".format(name))
    return check
