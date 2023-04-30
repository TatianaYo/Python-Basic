"""
Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
from string import ascii_letters
import pytest


def literal(text: str) -> str:
    a = ''
    for char in text:
        if char in ascii_letters or char == ' ':
            a += char
    return a.lower()


def test_no_change():
    assert literal('hello world') == 'hello world'


def test_registr():
    assert literal('Hello World') == 'hello world'


def test_punctuation():
    assert literal('Hello world!!!')  == 'hello world'


def test_language():
    assert literal('Привет world!') == ' world'


def test_all():
    assert literal('!Hello Мир!') == 'hello '


if __name__ == '__main__':
    pytest.main(['-vv'])
    # s = 'Привет Ivan, how are you? How old are you?'
    # print(literal(s))