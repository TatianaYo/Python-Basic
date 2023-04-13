"""
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
import json


def ident(file_name: str):
    dict_ = {}
    dict_two = {}
    with open(file_name, 'r', encoding='utf-8') as f:  # read file
        data = json.load(f)  # add data in file
        dict_ = data  # save
    while True:
        name_ = input('Enter name: ')
        if name_ == '':  # exit
            break
        id_ = int(input('Enter id: '))
        lev = input('Enter level (1 to 7): ')
        dict_two = {id_: name_}
        # dict_[lev] = dict_two

        if dict_.get(lev) is None:  # check key
            dict_[lev] = dict_two
        else:
            k = dict_.get(lev)
            k.update(dict_two)

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(dict_, f, ensure_ascii=False, indent=2)


ident('ident.json')



