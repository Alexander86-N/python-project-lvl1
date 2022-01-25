#!/usr/bin/env python


from brain_games import general_logic
from brain_games.games import even


def check_for_even():
    """Implements the game process of mini-games Check for Even."""
    general_logic.common_engine(even)


if __name__ == '__main__':
    check_for_even()
