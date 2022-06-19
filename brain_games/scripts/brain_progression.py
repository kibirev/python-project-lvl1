#!/usr/bin/env python
from .cli import welcome_user, printing, checking_win
from random import randint


def math_progression():
    name = welcome_user('What number is missing in the progression?')
    count_correct = 0
    while True:
        start, step = (randint(0, 100), randint(1, 10), )
        secret = randint(0, 9)
        string_left, string_right = ('', '',)
        correct = None
        for number in range(10):
            if number < secret:
                string_left = string_left + str(start) + ' '
                start += step
            elif number > secret:
                string_right = string_right + ' ' + str(start)
                start += step
            else:
                correct = start
                start += step
        player = printing(string_left, string_right, '..')
        count_correct = checking_win(name, int(player), correct, count_correct)
        if count_correct == 3 or count_correct == 0:
            break


def main():
    math_progression()


if __name__ == '__main__':
    main()
