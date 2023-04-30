"""
Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
from string import ascii_letters


def literal(text: str) -> str:
    """
    The function removes all characters except Latin letters and spaces
    >>> literal("hello world")
    'hello world'
    >>> literal("Hello World")
    'hello world'
    >>> literal("Hello! World! привет")
    'hello world '
    >>> literal("Hello! World!")
    'hello world'
    """
    a = ''
    for char in text:
        if char in ascii_letters or char == ' ':
            a += char
    return a.lower()


#print(literal('hello world'))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    # s = 'Привет Ivan, how are you? How old are you?'
    # print(literal(s))