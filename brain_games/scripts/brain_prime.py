#!/usr/bin/env python

from brain_games import general_logic
from brain_games.games import prime


def prime_number():
    """Asking if a number is prime"""
    general_logic.common_engine(prime)


if __name__ == '__main__':
    prime_number()
