"""
Создайте функцию-замыкание, которая запрашивает два целых числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
"""
__all__ = ['game']

from typing import Callable


def deco(a: int, count: int) -> Callable[[], None]:
    def ugaday() -> None:
        for i in range(count):
            num = int(input('Enter number from 1 to 100: '))
            if num > a:
                print('The number is less')
            elif num < a:
                print('The number is greater')
            elif num == a:
                print('You win!')
                break
    return ugaday


game = deco(20, 5)
game()


