#!/usr/bin/env python
from .cli import welcome_user, printing, checking_win
from random import randint


def generation_list():
    temp = [2, 3, 5, 7]
    for index in range(2, 32, 1):
        temp.append(temp[index] + 6)
    subsequence = []
    for position in temp:
        if position == 5 or position % 5 != 0:
            if position == 7 or position % 7 != 0:
                subsequence.append(position)
    return subsequence


def guessing_simple_number():
    string = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    name = welcome_user(string)
    count_correct = 0
    while True:
        number = randint(0, 100)
        subsequence = generation_list()
        player_answer = printing(number, '', '')
        is_simple_number = 'no'
        for index in subsequence:
            if number == index:
                is_simple_number = 'yes'
                break
            else:
                is_simple_number = 'no'
        count_correct = checking_win(name, player_answer, is_simple_number, count_correct)
        if count_correct == 3 or count_correct == 0:
            break


def main():
    guessing_simple_number()


if __name__ == '__main__':
    main()
