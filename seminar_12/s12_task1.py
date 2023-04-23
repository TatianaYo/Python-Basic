"""
Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
"""


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


f = Factorial(3)
print(f(4))
print(f(3))
print(f(2))
print(f(5))
print(f(6))
print(f.view())
