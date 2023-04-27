"""
Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.
"""


class UserException(Exception):
    pass


class LevelError(UserException):
    def __str__(self):
        print('error level')


class AccessError(UserException):
    def __str__(self):
        print('error access')
