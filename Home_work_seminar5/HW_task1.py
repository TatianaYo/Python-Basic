"""
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла
"""

def tuple_path(s: str) -> tuple[str]:

    a = s.split("\\")
    b = a[-1]
    a.pop()
    a = "\\".join(a)
    c = b.split('.')[0]
    d = b.split('.')[-1]

    tuple1 = (a, c, d)
    print(tuple1)

str1 = 'C:\Татьяна\AppData\Local\Programs\Python\Python311\python.exe'
tuple_path(str1)