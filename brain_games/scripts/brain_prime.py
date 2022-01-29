#!/usr/bin/env python

from brain_games import engine
from brain_games.games import prime


def prime_number():
    """Asking if a number is prime"""
    engine.start(prime)


if __name__ == '__main__':
    prime_number()
