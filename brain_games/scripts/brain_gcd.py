#!/usr/bin/env python

from brain_games import general_logic
from brain_games.games import gcd


def greatest_common_divisor():
    """The user must calculate and enter the greatest common\
        divisor of these numbers."""
    general_logic.common_engine(gcd)


if __name__ == '__main__':
    greatest_common_divisor()
