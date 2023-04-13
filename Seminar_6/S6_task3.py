"""
Улучшаем задачу 2.
Добавьте возможность запуска функции "угадайки" из модуля в командной строке терминала
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение
"""
__all__ = ['guess']


from sys import argv
import random as rnd


def guess(down: int = 0, up: int = 100, chanse: int = 5) -> bool:
    number = rnd.randint(down, up)

    for i in range(chanse):
        print(f'Enter number from {down} to {up}: ')
        num = int(input())
        if num > number:
            print('Number is smaller')
        elif num < number:
            print('Number is bigger')
        else:
            return True
    return False


if __name__ == '__main__':
    #tmp, *param = argv
    down = int(input('Enter number: '))
    up = int(input('Enter number: '))
    chanse = int(input('Enter number: '))
    print(guess(down, up, chanse))
    #print(guess(*(int(n) for n in param)))

#python S6_task3.py 2 10 3