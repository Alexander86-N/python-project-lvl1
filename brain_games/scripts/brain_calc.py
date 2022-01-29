#!/usr/bin/env python

from brain_games import engine
from brain_games.games import calculator


def calculate():
    """The user is shown a random mathematical expression that needs \
       to be calculatedand the correct answer written down."""
    engine.start(calculator)


if __name__ == '__main__':
    calculate()
