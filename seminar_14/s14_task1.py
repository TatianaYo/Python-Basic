"""
Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""
from string import ascii_letters


def literal(text: str) -> str:
    a = ''
    for char in text:
        if char in ascii_letters or char == ' ':
            a += char
    return a.lower()


if __name__ == '__main__':
    s = 'Привет Ivan, how are you? How old are you?'
    print(literal(s))
