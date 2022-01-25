#!/usr/bin/env python

from brain_games import general_logic
from brain_games.games import calculator


def calculate():
    """The user is shown a random mathematical expression that needs \
       to be calculatedand the correct answer written down."""
    general_logic.common_engine(calculator)


if __name__ == '__main__':
    calculate()
