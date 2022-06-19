#!/usr/bin/env python
from .cli import welcome_user, printing, counting, is_mistake
from random import randint


def guessing_simple_number():
    string = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    name = welcome_user(string)
    count_correct_answer = 0
    while True:
        number = randint(0, 100)
        temp = [2, 3, 5, 7]
        for index in range(2, 32, 1):
            temp.append(temp[index] + 6)
        subsequence = []
        for not_multiple_of_five in temp:
            if not_multiple_of_five == 5 or not_multiple_of_five % 5 != 0:
                subsequence.append(not_multiple_of_five)
        player_answer = printing(number, '', '')
        is_simple_number = 'no'
        for index in subsequence:
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
            is_mistake(name, player_answer, is_simple_number)
            break


def main():
    guessing_simple_number()


if __name__ == '__main__':
    main()
