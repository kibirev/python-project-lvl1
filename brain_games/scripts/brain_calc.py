#!/usr/bin/env python
from .cli import welcome_user, counting, printing, is_mistake
from random import randint


def calculation():
    name = welcome_user('What is the result of the expression?')
    correct_answer = 0
    while True:
        operation = randint(0, 2)
        num1, num2 = (randint(0, 100), randint(0, 100), )
        if operation == 0:
            player_answer = printing(str(num1), str(num2), ' + ')
            if int(player_answer) == num1 + num2:
                correct_answer = counting(correct_answer)
                if correct_answer == 3:
                    print(f'Congratulations, {name}!')
                    break
            else:
                is_mistake(name, player_answer, num1+num2)
                break
        elif operation == 1:
            if num1 >= num2:
                player_answer = printing(str(num1), str(num2), ' - ')
                if int(player_answer) == num1 - num2:
                    correct_answer = counting(correct_answer)
                    if correct_answer == 3:
                        print(f'Congratulations, {name}!')
                        break
                else:
                    is_mistake(name, player_answer, num1 - num2)
                    break
            else:
                player_answer = printing(str(num2), str(num1), ' - ')
                if int(player_answer) == num2 - num1:
                    correct_answer = counting(correct_answer)
                    if correct_answer == 3:
                        print(f'Congratulations, {name}!')
                        break
                else:
                    is_mistake(name, player_answer, num2 - num1)
                    break
        elif operation == 2:
            player_answer = printing(str(num1), str(num2), ' * ')
            if int(player_answer) == num1 * num2:
                correct_answer = counting(correct_answer)
                if correct_answer == 3:
                    print(f'Congratulations, {name}!')
                    break
            else:
                is_mistake(name, player_answer, num1 * num2)
                break
        else:
            pass


def main():
    calculation()


if __name__ == '__main__':
    main()
