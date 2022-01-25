import prompt


def common_engine():
    """Greeting and introduction to the player."""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(GAME_DESCRIPTION)
    NUMBER_OF_ROUNDS = 3
    while check != NUMBER_OF_ROUNDS:
        print('Question:', definition_of_arguments())
        answer = prompt.string('Your answer: ')
        result = correct_answer()
        check = 0
        if answer == result:
            check += 1
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(.\
Correct answer was '{}'.".format(answer, result))
            print("Let's try again, {}!".format(name))
            break
        return check
     print('Congratulations, {}!'.format(name))
