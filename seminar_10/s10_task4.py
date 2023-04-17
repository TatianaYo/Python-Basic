"""
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
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


class Employer(Human):

    def __init__(self, name: str, age: int, id_: str):
        super().__init__(name, age)
        self.id_ = id_
        self.level = None

    def get_level(self):
        sum_ = 0
        for i in str(self.id_):
            sum_ += int(i)
        self.level = sum_ % 7
        return self.level


e1 = Employer('Sara', 34, 265793)
print(e1.level, e1.get_level(), e1.level)




