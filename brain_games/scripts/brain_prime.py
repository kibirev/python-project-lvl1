#!/usr/bin/env python
from .cli import welcome_user, printing, counting
from random import randint


def guessing_simple_number():
    name = welcome_user('Answer "yes" if given number is prime. Otherwise answer "no".')
    count_correct_answer = 0
    while True:
        number = randint(0, 100)
        subsequence_simple_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
                                     83, 89, 97]
        player_answer = printing(number, '', '')
        is_simple_number = 'no'
        for index in subsequence_simple_number:
            if number == index:
                is_simple_number = 'yes'
                break
            else:
                is_simple_number = 'no'
        if player_answer == is_simple_number:
            count_correct_answer = counting(count_correct_answer)
            if count_correct_answer == 3:
                print(f'Congratulations, {name}!')
                break
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{is_simple_number}'.\n"
                  f"Let's try again, {name}!")
            break


def main():
    guessing_simple_number()


if __name__ == '__main__':
    main()
