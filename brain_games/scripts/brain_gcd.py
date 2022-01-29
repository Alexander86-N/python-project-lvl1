#!/usr/bin/env python

from brain_games import engine
from brain_games.games import gcd


def greatest_common_divisor():
    """The user must calculate and enter the greatest common\
        divisor of these numbers."""
    engine.start(gcd)


if __name__ == '__main__':
    greatest_common_divisor()
