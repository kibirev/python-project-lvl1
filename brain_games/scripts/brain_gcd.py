#!/usr/bin/env python
from cli import welcome_user, printing, counting, is_mistake
from random import randint
from math import gcd


def greatest_common_divisor():
    name = welcome_user('Find the greatest common divisor of given numbers.')
    correct_answer = 0
    while True:
        num1, num2 = (randint(0, 100), randint(0, 100), )
        player_answer = printing(str(num1), str(num2), ' ')
        if int(player_answer) == gcd(num1, num2):
            correct_answer = counting(correct_answer)
            if correct_answer == 3:
                print(f'Congratulations, {name}!')
                break
        else:
            is_mistake(name, player_answer, gcd(num1, num2))
            break


def main():
    greatest_common_divisor()


if __name__ == '__main__':
    main()
