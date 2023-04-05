"""
✔ Напишите функцию группового переименования файлов. Она должна:
    ✔ принимать параметр желаемое конечное имя файлов.
    При переименовании в конце имени добавляется порядковый номер.
    ✔ принимать параметр количество цифр в порядковом номере.
    ✔ принимать параметр расширение исходного файла.
    Переименование должно работать только для этих файлов внутри каталога.
    ✔ принимать параметр расширение конечного файла.
    ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
    К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
import os
import pathlib


def rename_group_file(quan_in_num: int, ext: str, new_ext: str, interval: list[int], new_name=''):
    current_dir = os.getcwd()
    print(current_dir)
    count = 0
    for file in os.listdir():
        if file.endswith(ext):
            count += 1
            pathlib.Path(file).rename(f'{file.split(".")[0][interval[0]:interval[1]]}{new_name}{count:0>{quan_in_num}}.{new_ext}')


new_name_file = 'PY'
quan = 4
ext_file = 'txt'
new_ext_file = 'py'
inter = [2, 5]

rename_group_file(quan, ext_file, new_ext_file, inter, new_name_file)