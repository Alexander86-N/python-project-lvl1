#!/usr/bin/env python

from brain_games import engine
from brain_games.games import progression


def work_with_progression():
    """Determining the missing number in an arithmetic progression"""
    engine.start(progression)


if __name__ == '__main__':
    work_with_progression()
