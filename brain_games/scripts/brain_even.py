#!/usr/bin/env python
from .cli import welcome_user, counting, is_mistake
from random import randint
import prompt


def parity_check():
    name = welcome_user("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    correct_answer = 0
    while True:
        number = randint(0, 100)
        print(f'Question: {number}')
        player_answer = prompt.string('Your answer: ')
        if player_answer == 'yes':
            if number % 2 == 0:
                correct_answer = counting(correct_answer)
                if correct_answer == 3:
                    print(f'Congratulations, {name}!')
                    break
            else:
                is_mistake(name, player_answer, 'no')
                break
        else:
            if number % 2 == 1:
                correct_answer = counting(correct_answer)
                if correct_answer == 3:
                    print(f'Congratulations, {name}!')
                    break
            else:
                is_mistake(name, player_answer, 'yes')
                break


def main():
    parity_check()


if __name__ == '__main__':
    main()
