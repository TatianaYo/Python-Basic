"""
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы,состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл
"""
import random as rnd

__all__ = ['gen_name']

glas_str = 'аеуиыяюоэ'
sogl_str = 'йцкнгшщзхфвпрлджчсмтб'


def gen_name(cnt_line: int, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(cnt_line):
            result_str = ''
            for j in range(rnd.randint(2, 4)):
                result_str += glas_str[rnd.randint(0, len(glas_str)-1)] \
                        + sogl_str[rnd.randint(0, len(sogl_str)-1)]
            result_str = result_str.capitalize()
            #print(result_str)
            f.write(f'{result_str}\n')


#gen_name(5, 'name.txt')

