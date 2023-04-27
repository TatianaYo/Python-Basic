"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь.
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
"""


class Rectangle:

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


rectangle = Rectangle(5, 10)
print(f'Периметр = {rectangle.rectangle_perimeter()}\nПлощадь = {rectangle.rectangle_square()}')
