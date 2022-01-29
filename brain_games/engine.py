import prompt


NUMBER_OF_ROUNDS = 3


def start(game):
    """The main logic of the series of mini games."""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.GAME_DESCRIPTION)
    for _ in range(NUMBER_OF_ROUNDS):
        example, result = game.generate_question_and_answer()
        print('Question:', example)
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(.\
Correct answer was '{}'.".format(answer, result))
            print("Let's try again, {}!".format(name))
            return
    print('Congratulations, {}!'.format(name))
