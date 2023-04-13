"""
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой функции.
"""
import time
from typing import Callable


def count(num: int = 1):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Result {time_for_count}')
            return result
        return wrapper
    return deco


@count(5)
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(5) = }')
print(f'{factorial(5) = }')
