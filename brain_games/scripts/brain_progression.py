#!/usr/bin/env python
from .cli import welcome_user, printing, counting, is_mistake
from random import randint


def math_progression():
    name = welcome_user('What number is missing in the progression?')
    count_correct_answer = 0
    while True:
        start_number, step, after_before_secret_number = (randint(0, 100), randint(1, 10), randint(0, 9), )
        string_left, string_right = ('', '',)
        correct_answer = None
        for number in range(10):
            if number < after_before_secret_number:
                string_left = string_left + str(start_number) + ' '
                start_number += step
            elif number > after_before_secret_number:
                string_right = string_right + ' ' + str(start_number)
                start_number += step
            else:
                correct_answer = start_number
                start_number += step
        player_answer = printing(string_left, string_right, '..')
        if int(player_answer) == correct_answer:
            count_correct_answer = counting(count_correct_answer)
            if count_correct_answer == 3:
                print(f'Congratulations, {name}!')
                break
        else:
            is_mistake(name, player_answer, correct_answer)
            break


def main():
    math_progression()


if __name__ == '__main__':
    main()
