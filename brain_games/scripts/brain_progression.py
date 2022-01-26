#!/usr/bin/env python

from brain_games import general_logic
from brain_games.games import ar_progression


def work_with_progression():
    """Determining the missing number in an arithmetic progression"""
    general_logic.common_engine(ar_progression)


if __name__ == '__main__':
    work_with_progression()
