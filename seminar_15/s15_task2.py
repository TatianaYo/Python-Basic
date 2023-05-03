"""
На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её работы в файл.
Напишите аналогичный декоратор, но внутри используйте модуль logging.
"""
import json
from pathlib import Path
import logging


FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.INFO, filename='deco.log', encoding='utf-8', format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def deco_file(func):

    def wrapper(*args, **kwargs):
        data = []
        new_data = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        data.append(new_data)
        print(new_data)
        logger.info(new_data)
        return result
    return wrapper


@deco_file
def call(*args, **kwargs):
    pass


call(42, 4, 5, 4, a=89, c=23)
