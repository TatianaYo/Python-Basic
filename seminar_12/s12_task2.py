"""
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
"""
import json


class Factorial:

    def __init__(self, k: int):
        self.k = k
        self.key_list = [None] * self.k
        self.val_list = [None] * self.k

    def __call__(self, num: int, *args, **kwargs):
        if num == 1 or num == 0:
            return 1
        result = 1
        for i in range(1, num + 1):
            result *= i
        self.val_list.append(result)
        self.val_list.pop(0)
        self.key_list.append(num)
        self.key_list.pop(0)
        return result

    def view(self):
        return f'{self.val_list}\n{self.key_list}'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('file_fac.json', 'w', encoding='utf-8') as f:
            dict_json = dict(zip(self.key_list, self.val_list))
            json.dump(dict_json, f, ensure_ascii=False, indent=2)


#f = Factorial(3)
with Factorial(3) as f:
    print(f(4))
    print(f(3))
    print(f(2))
    print(f(5))
    print(f(6))
    print(f.view())
