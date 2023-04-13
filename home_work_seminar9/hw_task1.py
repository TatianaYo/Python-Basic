"""
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""
import csv
import random
from typing import Callable
from functools import wraps
from pathlib import Path
import json


def discrim_from_csv(file_name: str):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(file_name, 'r', encoding='utf-8') as f:
                read_csv = csv.reader(f)
                for i, row in enumerate(read_csv):
                    args = (complex(j) for j in row)
                    result = func(*args, **kwargs)
                    yield result
        return wrapper
    return deco


def save_to_json(func):
    file = Path(f"{func.__name__}.json")
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            json_file = json.load(f)
    else:
        json_file = []

    def wrapper(*args, **kwargs):
        for result in func(*args, **kwargs):
            if result:
                diction = {'args': args, **kwargs, 'result': str(result)}
                json_file.append(diction)
                with open(file, 'w', encoding='utf-8') as json_f:
                    json.dump(json_file, json_f, indent=2)
            else:
                break

    return wrapper


@save_to_json
@discrim_from_csv('file_with_num.csv')
def discriminant(a: float, b: float, c: float):
    if a != 0:
        discrim = b * b - 4 * a * c
        x1 = (-b + discrim ** 0.5) / (2 * a)
        x2 = (-b - discrim ** 0.5) / (2 * a)
        return discrim, x1, x2
    else:
        return 0, 0, 0


def gen_file_csv():
    list1 = []
    with open('file_with_num.csv', 'w', encoding='utf-8') as f:
        file_write = csv.writer(f, delimiter=",", lineterminator="\r")
        for _ in range(random.randint(100, 1001)):
            a, b, c = random.sample(range(-100, 100), 3)
            list1.append([a, b, c])
        file_write.writerows(list1)


if __name__ == '__main__':
    gen_file_csv()
    discriminant()


"""
Долго мучалась, так и не поняла, почему в json файл не сохраняются переданные парамерты.
В итоге полностью запуталась и боюсь что-то переделывать.
"""

