"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)
"""
import time


class MyString(str):
    """Includes all string features"""

    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance

    def __str__(self):
        return f'Класс хранит имя автора, строки и время создания'


if __name__ == '__main__':
    s = MyString('fdnd;lndz', 'Innnf')
    print(s)
    print(s.time)
    print(s.author)
