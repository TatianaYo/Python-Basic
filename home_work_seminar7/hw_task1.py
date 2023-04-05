"""
✔ Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
    ✔ расширение
    ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
    ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
    ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
    ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
    ✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""
import random as rnd
import os


glas_str = 'аеуиыяюоэ'
sogl_str = 'йцкнгшщзхфвпрлджчсмтб'


def create_file(expan: str, min_len=6, max_len=30, min_num=256, max_num=4096, quan_file=42):
    for _ in range(quan_file):
        file_name = ''
        for i in range(rnd.randint(min_len, max_len)): #создаем имя
            file_name += glas_str[rnd.randint(0, len(glas_str)-1)] \
                    + sogl_str[rnd.randint(0, len(sogl_str)-1)]
        with open('text.txt', 'wb') as f: #создаем файл
            for j in range(rnd.randint(min_num, max_num)): #записываем количество байт
                f.write(b'j')
        f_name = os.path.splitext('text.txt')[0]
        exp = os.path.splitext('text.txt')[-1]
        f_name, exp = file_name, expan
        os.rename('text.txt', file_name + expan)


create_file('.bin')
