"""
Создать модуль с функцией внутри
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток
Функция выводит подсказки "больше" и "меньше"
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь
"""
import random as rnd

def guess(down: int, up: int, chanse: int) -> bool:
    number = rnd.randint(down, up)
    count = 0

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
    down = int(input('Enter number: '))
    up = int(input('Enter number: '))
    chanse = int(input('Enter number: '))
    print(guess(down, up, chanse))