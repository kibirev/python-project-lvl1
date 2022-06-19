#!/usr/bin/env python
from brain_even import parity_check
from brain_calc import calculation
from brain_gcd import greatest_common_divisor
from brain_progression import math_progression
import prompt


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    print('Choose the game!\nPress \"1\": Brain Even\nPress \"2\": Brain Calc\nPress \"3\": Brain GSD')
    choice = prompt.string('Your choce: ')
    if choice == '1':
        parity_check()
    elif choice == '2':
        calculation()
    elif choice == '3':
        greatest_common_divisor()
    elif choice == '4':
        math_progression()
    else:
        print('Incorrect input! Restart game, please!')


if __name__ == '__main__':
    main()
