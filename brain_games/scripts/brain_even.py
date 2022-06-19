#!/usr/bin/env python
from .cli import welcome_user, counting_correct_answer
from random import randint
import prompt


def parity_check():
    name = welcome_user("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    correct_answer = 0
    while True:
        number = randint(0, 100)
        print(f'Question: {number}')
        player_answer = prompt.string('Your answer: ')
        if player_answer == 'no':
            if number % 2 == 0:
                correct_answer = counting_correct_answer(correct_answer)
                if correct_answer == 3:
                    print(f'Congratulations, {name}!')
                    break
                else:
                    print(f"'{player_answer}' is wrong answer ;(. Correct answer was 'yes'.)\n"
                          f"Let's try again, {name}!")
                    break
        else:
            if number % 2 == 1:
                correct_answer = counting_correct_answer(correct_answer)
                if correct_answer == 3:
                    print(f'Congratulations, {name}!')
                    break
                else:
                    print(f"'{player_answer}' is wrong answer ;(. Correct answer was 'no'.)\n"
                          f"Let's try again, {name}!")
                    break


def main():
    parity_check()


if __name__ == '__main__':
    main()
