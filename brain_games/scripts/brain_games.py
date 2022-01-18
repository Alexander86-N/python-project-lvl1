#!/usr/bin/env python

from brain_games import cli


def main():
    print("Welcom to the Brain Games!")
    name = cli.welcome_user()
    print('Hello, {}!'.format(name))


if __name__ == '__main__':
    main()
