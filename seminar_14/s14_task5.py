"""
На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса
"""
import unittest


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


class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.r1 = Rectangle(5, 15)
        self.r2 = Rectangle(4, 14)
        self.r3 = Rectangle(7, 3)

    def test_square(self):
        self.assertEqual(self.r1.rectangle_square(), 75)

    def test_perimetr(self):
        self.assertEqual(self.r2.rectangle_perimeter(), 36)


if __name__ == '__main__':
    unittest.main(verbosity=2)
# rectangle = Rectangle(5, 10)
# print(f'Периметр = {rectangle.rectangle_perimeter()}\nПлощадь = {rectangle.rectangle_square()}')
