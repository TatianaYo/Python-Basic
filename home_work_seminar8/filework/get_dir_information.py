"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
-   Для дочерних объектов указывайте родительскую директорию.
-   Для каждого объекта укажите файл это или директория.
-   Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
__all__ = ['get_dir_information']

from pathlib import Path
import csv
import json
import pickle
import os


def dir_size(path='.') -> int:
    result = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                result += entry.stat().st_size
            elif entry.is_dir():
                result += dir_size(entry.path)
    return result


def file_size(path='.') -> int:
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return dir_size(path)


def get_dir_information(direct: Path):
    json_data = {}
    categories = ['name', 'path', 'size', 'file_or_dir']
    rows = []
    with open('direct_info.json', 'w') as f_json, open('direct_info.csv', 'w', newline='', encoding='utf-8') as f_csv,\
            open('direct_info.pickle', 'wb') as f_pickle:
        for dir_path, dir_name, file_name in os.walk(direct):
            json_data.setdefault(dir_path, {})
            for dir in dir_name:
                size = file_size(dir_path + '/' + dir)
                json_data[dir_path].update({dir: {'size': size, 'file_or_dir': 'directory'}})
                rows.append({'name': dir, 'path': dir_path, 'size': size, 'file_or_dir': 'directory'})
            for fi in file_name:
                size = file_size(dir_path + '/' + fi)
                json_data[dir_path].update({fi: {'size': size, 'file_or_dir': 'file'}})
                rows.append({'name': fi, 'path': dir_path, 'size': size, 'file_or_dir': 'file'})
            #print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
        json.dump(json_data, f_json, indent=2)
        writer = csv.DictWriter(f_csv, fieldnames=categories)
        writer.writeheader()
        writer.writerows(rows)
        pickle.dump(f'{pickle.dumps(json_data)}', f_pickle)


if __name__ == '__main__':
    get_dir_information(Path('/Users/Татьяна/OneDrive/Рабочий стол/Python/Python-Basic'))