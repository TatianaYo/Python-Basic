"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра
"""
"""
Добавьте к задачам 1 и 2 строки документации для классов.
"""


class Archive():
    """The class stores properties, when creating a new instance, previously created instances are saved to the list"""

    _one = None

    def __init__(self, num: int, val: str) -> None:
        self.num = num
        self.val = val

    def __new__(cls, *args, **kwargs):
        if cls._one is None:
            cls._one = super().__new__(cls)
            cls._one.numbers = []
            cls._one.values = []
        else:
            cls._one.numbers.append(cls._one.num)
            cls._one.values.append(cls._one.val)
        return cls._one

    def __str__(self):
        return f'Класс хранит пару свойств'


s = Archive(123, '1243450')
print(s.numbers, s.values)

s = Archive(12345, '12')
print(s.numbers, s.values)
