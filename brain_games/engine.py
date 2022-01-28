import prompt


NUMBER_OF_ROUNDS = 3


def start(game):
    """The main logic of the series of mini games."""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.GAME_DESCRIPTION)
    check = 0
    while check != NUMBER_OF_ROUNDS:
        number = game.definition_of_arguments()
        result = game.correct_answer(number)
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        if answer == result:
            check += 1
            print('Correct!')
            if check == 3:
                print('Congratulations, {}!'.format(name))
        else:
            print("'{}' is wrong answer ;(.\
Correct answer was '{}'.".format(answer, result))
            print("Let's try again, {}!".format(name))
            break
