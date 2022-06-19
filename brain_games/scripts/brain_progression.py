#!/usr/bin/env python
from .cli import welcome_user, printing, checking_win
from random import randint


def math_progression():
    name = welcome_user('What number is missing in the progression?')
    count_correct = 0
    while True:
        start_number, step, after_before_secret_number = (randint(0, 100), randint(1, 10), randint(0, 9), )
        string_left, string_right = ('', '',)
        correct = None
        for number in range(10):
            if number < after_before_secret_number:
                string_left = string_left + str(start_number) + ' '
                start_number += step
            elif number > after_before_secret_number:
                string_right = string_right + ' ' + str(start_number)
                start_number += step
            else:
                correct = start_number
                start_number += step
        player = printing(string_left, string_right, '..')
        count_correct = checking_win(name, player, correct, count_correct)
        if count_correct == 3 or count_correct == 0:
            break


def main():
    math_progression()


if __name__ == '__main__':
    main()
