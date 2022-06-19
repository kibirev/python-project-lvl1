#!/usr/bin/env python
from .cli import welcome_user, counting, printing, checking_win
from random import randint


def addition(name, num1, num2, count_correct):
    player_answer = printing(str(num1), str(num2), ' + ')
    return checking_win(name, player_answer, num1 + num2, count_correct)


def subtraction(name, num1, num2, count_correct):
    if num1 >= num2:
        player_answer = printing(str(num1), str(num2), ' - ')
        return checking_win(name, player_answer, num1 - num2, count_correct)
    else:
        player_answer = printing(str(num2), str(num1), ' - ')
        return checking_win(name, player_answer, num2 - num1, count_correct)


def multiplication(name, num1, num2, count_correct):
    player_answer = printing(str(num1), str(num2), ' * ')
    return checking_win(name, player_answer, num1 * num2, count_correct)


def calculation():
    name = welcome_user('What is the result of the expression?')
    count_correct = 0
    while True:
        operation = randint(0, 2)
        num1, num2 = (randint(0, 100), randint(0, 100), )
        if operation == 0:
            count_correct = addition(name, num1, num2, count_correct)
        elif operation == 1:
            count_correct = subtraction(name, num1, num2, count_correct)
        else:
            count_correct = multiplication(name, num1, num2, count_correct)
        if count_correct == 3 or count_correct == 0:
            break


def main():
    calculation()


if __name__ == '__main__':
    main()
