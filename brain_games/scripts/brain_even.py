#!/usr/bin/env python


from brain_games import engine
from brain_games.games import even


def check_for_even():
    """Implements the game process of mini-games Check for Even."""
    engine.start(even)


if __name__ == '__main__':
    check_for_even()
