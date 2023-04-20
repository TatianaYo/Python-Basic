"""
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
"""


class Rectangle:
    """Returns the perimeter and area of a rectangle or quadrangle, and adds and subtracts the perimeters"""

    def __init__(self, length: float, width: float = None):
        self.length = length
        if width is None:
            self.width = length
        else:
            self.width = width

    def rectangle_perimeter(self):
        return (self.length + self.width) * 2

    def rectangle_square(self):
        return self.length * self.width

    def __add__(self, other):
        a = self.length + other.length
        b = self.width + other.width
        return Rectangle(a, b)

    def __sub__(self, other):
        if self.rectangle_perimeter() < other.rectangle_perimeter():
            self, other = other, self
        a = self.length - other.length
        b = self.width - other.width
        return Rectangle(a, b)

    def __str__(self):
        return f'Класс выполняет различные операции с прямоугольниками или квадратами'

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'


rectangle = Rectangle(5, 10)
print(f'Периметр = {rectangle.rectangle_perimeter()}\nПлощадь = {rectangle.rectangle_square()}')
rec1 = Rectangle(2, 8)
rec2 = rectangle + rec1
rec3 = rectangle - rec1
print(rectangle.rectangle_perimeter(), rec1.rectangle_perimeter(), rec2.rectangle_perimeter(), rec3.rectangle_perimeter())
print(rectangle)
