#!/usr/bin/env python
import prompt


def welcome_user(description_of_game):
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!\n{description_of_game}")
    return name


def printing(arg1, arg2, char=''):
    print(f'Question: {str(arg1)}{char}{str(arg2)}')
    return prompt.string(f'Your answer: ')


def counting(count):
    print('Correct!')
    count += 1
    return count


def is_mistake(user_name,user_answer, right_answer):
    string = "' is wrong answer ;(. Correct answer was '"
    print(f"'{user_answer}{string}{right_answer}'.")
    print(f"Let's try again, {user_name}!")


def checking_win(name, player_ans, correct_ans, count_ans):
    if int(player_ans) == correct_ans:
        count_correct_answer = counting(int(count_ans))
        if count_correct_answer == 3:
            print(f'Congratulations, {name}!')
        return count_correct_answer
    else:
        is_mistake(name, player_ans, correct_ans)
        return 0
