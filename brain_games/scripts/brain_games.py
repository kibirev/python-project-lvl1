#!/usr/bin/env python
from brain_even import parity_check
from brain_calc import calculation
import prompt


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    print('Choose the game!\nPress \"1\": Brain Even\nPress \"2\": Brain Calc')
    choice = prompt.string('Your choce: ')
    if choice == '1':
        parity_check()
    elif choice == '2':
        calculation()
    else:
        print('Incorrect input! Restart game, please!')


if __name__ == '__main__':
    main()
