#!/usr/bin/env python
from .cli import welcome_user, counting_correct_answer, printing_question_and_answer
from random import randint


def calculation():
    name = welcome_user('What is the result of the expression?')
    correct_answer = 0
    while True:
        operation, num1, num2 = (randint(0, 2), randint(0, 100), randint(0, 100), )
        if operation == 0:
            player_answer = printing_question_and_answer(str(num1), str(num2), ' + ')
            if int(player_answer) == num1 + num2:
                correct_answer = counting_correct_answer(correct_answer)
                if correct_answer == 3:
                    print(f'Congratulations, {name}!')
                    break
            else:
                print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{num1+num2}'.)\n"
                      f"Let's try again, {name}!")
                break
        elif operation == 1:
            if num1 >= num2:
                player_answer = printing_question_and_answer(str(num1), str(num2), ' - ')
                if int(player_answer) == num1 - num2:
                    correct_answer = counting_correct_answer(correct_answer)
                    if correct_answer == 3:
                        print(f'Congratulations, {name}!')
                        break
                else:
                    print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{num1 - num2}'.\n"
                          f"Let's try again, {name}!")
                    break
            else:
                player_answer = printing_question_and_answer(str(num2), str(num1), ' - ')
                if int(player_answer) == num2 - num1:
                    correct_answer = counting_correct_answer(correct_answer)
                    if correct_answer == 3:
                        print(f'Congratulations, {name}!')
                        break
                else:
                    print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{num2 - num1}'.\n"
                          f"Let's try again, {name}!")
                    break
        elif operation == 2:
            player_answer = printing_question_and_answer(str(num1), str(num2), ' * ')
            if int(player_answer) == num1 * num2:
                correct_answer = counting_correct_answer(correct_answer)
                if correct_answer == 3:
                    print(f'Congratulations, {name}!')
                    break
            else:
                print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{num1*num2}'.\n"
                      f"Let's try again, {name}!")
                break
        else:
            pass


def main():
    calculation()


if __name__ == '__main__':
    main()
