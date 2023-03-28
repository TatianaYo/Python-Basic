"""
Создайте функцию генератор чисел Фибоначчи
"""


def generator_fib(number: int):
    a, b = 0, 1
    for _ in range(number):
        yield a
        a, b = b, a + b


num = int(input('Введите конечное число: '))
print(*generator_fib(num))