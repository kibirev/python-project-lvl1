#!/usr/bin/env python
from .cli import welcome_user, printing_question_and_answer, counting_correct_answer
from random import randint
from math import gcd


def greatest_common_divisor():
    name = welcome_user('Find the greatest common divisor of given numbers.')
    correct_answer = 0
    while True:
        num1, num2 = (randint(0, 100), randint(0, 100), )
        player_answer = printing_question_and_answer(str(num1), str(num2), '')
        if int(player_answer) == gcd(num1, num2):
            correct_answer = counting_correct_answer(correct_answer)
            if correct_answer == 3:
                print(f'Congratulations, {name}!')
                break
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{gcd(num1, num2)}'.\n"
                  f"Let's try again, {name}!")
            break


def main():
    greatest_common_divisor()


if __name__ == '__main__':
    main()
