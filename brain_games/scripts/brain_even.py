#!/usr/bin/env python
from .cli import welcome_user, checking_win
from random import randint
import prompt


def checking(name, correct_answer, count_correct):
    player_answer = prompt.string('Your answer: ')
    if player_answer == 'yes':
        return checking_win(name, 'yes', correct_answer, count_correct)
    else:
        return checking_win(name, 'no', correct_answer, count_correct)


def parity_check():
    string = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
    name = welcome_user(string)
    count_correct = 0
    while True:
        number = randint(0, 100)
        print(f'Question: {number}')
        if number % 2 == 0:
            count_correct = checking(name, 'yes', count_correct)
        else:
            count_correct = checking(name, 'no', count_correct)
        if count_correct == 3 or count_correct == 0:
            break


def main():
    parity_check()


if __name__ == '__main__':
    main()
