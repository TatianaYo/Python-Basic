"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь.
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
"""


class UserException(Exception):
    pass


class RectangleValueError(UserException):
    def __str__(self):
        return 'Значение должно быть положительным'


class RectangleValueTypeError(UserException):
    def __str__(self):
        return 'Значение должно быть числом'


class Rectangle:

    def __init__(self, length, width=None):
        if isinstance(length, str) or isinstance(width, str):
            raise RectangleValueTypeError
        self.length = float(length)
        if width is None:
            self.width = float(length)
        else:
            self.width = float(width)
        if self.length <= 0 or self.width <= 0:
            raise RectangleValueError

    def rectangle_perimeter(self):
        return (self.length + self.width) * 2

    def rectangle_square(self):
        return self.length * self.width


rectangle = Rectangle(5, 6)
print(f'Периметр = {rectangle.rectangle_perimeter()}\nПлощадь = {rectangle.rectangle_square()}')
