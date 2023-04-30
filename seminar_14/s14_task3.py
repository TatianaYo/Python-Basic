"""
Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
from string import ascii_letters
import unittest


def literal(text: str) -> str:
    a = ''
    for char in text:
        if char in ascii_letters or char == ' ':
            a += char
    return a.lower()


class TestCase(unittest.TestCase):

    def test_no_change(self):
        self.assertEqual(literal('hello world'), 'hello world')

    def test_registr(self):
        self.assertEqual(literal('Hello World'), 'hello world')

    def test_punctuation(self):
        self.assertEqual(literal('Hello world!!!'), 'hello world')

    def test_language(self):
        self.assertEqual(literal('Привет world!'), ' world')

    def test_all(self):
        self.assertEqual(literal('!Hello Мир!'), 'hello ')


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # s = 'Привет Ivan, how are you? How old are you?'
    # print(literal(s))
