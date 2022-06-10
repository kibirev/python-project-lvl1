from cli import welcome_user
from random import randint
import prompt


def greeting():
    return welcome_user()


def parity_check():
    name = greeting()
    print(f"Hello, {name}!\nAnswer \"yes\" if the number is even, otherwise answer \"no\".")
    count = 0
    while count < 3:
        number = randint(0, 100)
        print(f'Question:{number}')
        while True:
            answer = prompt.string('Your answer: ')
            if answer == 'yes':
                if number % 2 == 0:
                    print('Correct!')
                    count += 1
                    break
                else:
                    count = 0
                    print(f"yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}")
                    break
            elif answer == 'no':
                if number % 2 == 1:
                    print('Correct!')
                    count += 1
                    break
                else:
                    count = 0
                    print(f"yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}")
                    break
            else:
                count = 0
                print(f"You can write only 'yes' or 'mo'.\nLet's try again, {name}")
                break
    print(f'Congratulations, {name}!')


def main():
    parity_check()


if __name__ == '__main__':
    main()
