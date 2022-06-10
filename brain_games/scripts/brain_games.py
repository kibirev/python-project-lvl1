#!/usr/bin/env python
from cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    print(welcome_user())


if __name__ == '__main__':
    main()
