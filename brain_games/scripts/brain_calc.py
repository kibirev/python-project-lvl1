#!/usr/bin/env python
from cli import welcome_user, printing
from random import randint


def greeting():
    return welcome_user()


def calculation():
    name = greeting()
    print(f"Hello, {name}!\nWhat is the result of the expression?")
    count = 0
    while count < 3:
        operation = randint(0, 2)
        if operation == 0:
            num1, num2 = (randint(0, 100), randint(0, 100), )
            result = num1 + num2
            printing('question', str(num1) + ' + ' + str(num2))
            user_answer = printing('answer')
            if result == int(user_answer):
                printing('correct_answer')
                count += 1
            else:
                printing('game_over', result, user_answer, name)
                break
        elif operation == 1:
            num1, num2 = (randint(0, 100), randint(0, 100), )
            if num1 >= num2:
                result = num1 - num2
                printing('question', str(num1) + ' - ' + str(num2))
            else:
                result = num2 - num1
                printing('question', str(num2) + ' - ' + str(num1))
            user_answer = printing('answer')
            if result == int(user_answer):
                printing('correct_answer')
                count += 1
            else:
                printing('game_over', str(result), user_answer, name)
                break
        elif operation == 2:
            num1, num2 = (randint(0, 10), randint(0, 10), )
            result = num1 * num2
            printing('question', str(num1) + ' * ' + str(num2))
            user_answer = printing('answer')
            if result == int(user_answer):
                printing('correct_answer')
                count += 1
            else:
                printing('game_over', str(result), user_answer, name)
                break
        else:
            pass
    if count == 3:
        printing('congratulation', name)


def main():
    calculation()


if __name__ == '__main__':
    main()
