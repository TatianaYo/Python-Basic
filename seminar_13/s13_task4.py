"""
Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
"""
import json


class User:

    def __init__(self, name: str, id_: int, level: int):
        self.name = name
        self.id_ = id_
        self.level = level


def read_json(file_name: str):
    users = set()
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for level, value in data.items():
        for id_, name in value.items():
            users.add(User(name=name, id_=int(id_), level=int(level)))
    return users


print(read_json('ident.json'))
