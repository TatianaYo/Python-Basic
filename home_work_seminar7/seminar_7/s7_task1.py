"""
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции
"""
import random as rnd

__all__ = ['gen_file']

MIN_LIMIT = -1000
MAX_LIMIT = 1000


def gen_file(cnt_line: int, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(cnt_line):
            tmp_str = str(rnd.randint(MIN_LIMIT, MAX_LIMIT)) \
                      + '|' + str(rnd.uniform(MIN_LIMIT, MAX_LIMIT))
            #print(tmp_str)
            f.write(f'{tmp_str}\n')


#gen_file(5, 'data.txt')

