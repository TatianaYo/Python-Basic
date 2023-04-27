"""
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и значение по умолчанию.
При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
Реализуйте работу через обработку исключений
"""


def get_dict(dict_, key_dict, val_dict=None):

    try:
        result = dict_[key_dict]
        return result
    except KeyError as k:
        return f'Key not found, default value {val_dict}'


dictionary = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
print(get_dict(dictionary, 5))
