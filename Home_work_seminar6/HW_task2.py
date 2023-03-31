"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""
import datetime
from sys import argv


def date_determine(d: str) -> bool:
    try:
        date1 = datetime.datetime.strptime(d, "%d.%m.%Y").date()
        return True
    except:
        return False


def _leap_year(d: str) -> bool:
    y = int(d.split(".")[-1])
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    date_d = input('Enter date in format DD.MM.YYYY: ')
    print(date_determine(date_d))
    print(_leap_year(date_d))
