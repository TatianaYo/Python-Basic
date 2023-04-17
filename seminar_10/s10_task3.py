"""
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.
"""


class Human:

    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    def birthday_human(self):
        self.__age += 1

    def full_name(self):
        return self.name

    def get_age(self):
        return self.__age


h1 = Human('Виктор Александрович Иванов', 34)
print(f'ФИО: {h1.full_name()}')
print(h1.get_age(), h1.birthday_human(), h1.get_age())
