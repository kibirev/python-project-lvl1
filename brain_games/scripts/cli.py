#!/usr/bin/env python
import prompt


def welcome_user(description_of_game):
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!\n{description_of_game}")
    return name


def printing_question_and_answer(arg1, arg2, char=''):
    print(f'Question: {str(arg1)}{char}{str(arg2)}')
    return prompt.string(f'Your answer: ')


def counting_correct_answer(count):
    print('Correct!')
    count += 1
    return count
