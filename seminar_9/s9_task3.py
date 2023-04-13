"""
Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.
"""
import json
from pathlib import Path


def deco_file(func):
    file = Path(f'{func.__name__}.json')
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    def wrapper(*args, **kwargs):
        new_data = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        data.append(new_data)
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f)
        return result
    return wrapper


@deco_file
def call(*args, **kwargs):
    pass


call(42, 4, 5, 6, a=89, c=23)