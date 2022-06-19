#!/usr/bin/env python
from .brain_even import parity_check
from .brain_calc import calculation
from .brain_gcd import greatest_common_divisor
from .brain_progression import math_progression
from .brain_prime import guessing_simple_number
import prompt


def greet():
    print('Welcome to the Brain Games!')


def main():
    print('May I have your name?')
    greet()
    print(f'Choose the game!\nPress \"1\": Brain Even\nPress \"2\": Brain Calc\nPress \"3\": Brain GSD\n'
          f'Press \"4\": Brain Progression\nPress \"5\": Brain Prime\n')
    choice = prompt.string('Your choice: ')
    if choice == '1':
        parity_check()
    elif choice == '2':
        calculation()
    elif choice == '3':
        greatest_common_divisor()
    elif choice == '4':
        math_progression()
    elif choice == '5':
        guessing_simple_number()
    else:
        print('Incorrect input! Restart game, please!')


if __name__ == '__main__':
    main()
