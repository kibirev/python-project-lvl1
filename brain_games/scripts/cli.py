#!/usr/bin/env python
import prompt


def welcome_user():
    return prompt.string('May I have your name? ')


def printing(type_cli, expression=None, u_answer=None, u_name=None):
    if type_cli == 'question':
        print(f'Question: {expression}')
    elif type_cli == 'correct_answer':
        print('Correct!')
    elif type_cli == 'answer':
        return prompt.string(f'Your answer: ')
    elif type_cli == 'congratulation':
        print(f'Congratulations, {expression}!')
    elif type_cli == 'game_over':
        print(f"'{u_answer}' is wrong answer ;(. Correct answer was '{expression}'.\nLet's try again, {u_name}!")
    else:
        print('Unknown type answer!')
