"""
Создайте класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь.
"""
from math import pi


class Circle:

    def __init__(self, radius: float):
        self.radius = radius

    def circle_len(self):
        return 2 * pi * self.radius

    def circle_square(self):
        return pi * self.radius ** 2


my_circle = Circle(10)
print(f'Длина окружности = {my_circle.circle_len()},\nПлощадь окружности = {my_circle.circle_square()}')