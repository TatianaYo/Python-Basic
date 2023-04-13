"""
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.
"""
__all__ = ['ugaday']

import random


def deco(func):
    def wrapper(a: int, count: int):
        if a < 1 or a > 100:
            a = random.randint(1, 101)
        if count < 1 or count > 10:
            count = random.randint(1, 11)
        result = func(a, count)
        return result
    return wrapper


@deco
def ugaday(a: int, count: int) -> None:
    for i in range(count):
        num = int(input('Enter number from 1 to 100: '))
        if num > a:
            print('The number is less')
        elif num < a:
            print('The number is greater')
        elif num == a:
            print('You win!')
            break


ugaday(120, 15)

