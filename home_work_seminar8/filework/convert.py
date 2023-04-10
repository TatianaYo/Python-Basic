"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json


def convert(file_name: str) -> None:
    diction = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            li = line.split(',')
            #print(line)
            diction[li[0].capitalize()] = float(li[1])
        #print(diction)
        with open('file_json.json', 'w', encoding='utf-8') as f:
            json.dump(diction, f, ensure_ascii=False, indent=2)


convert('open_file.txt')

