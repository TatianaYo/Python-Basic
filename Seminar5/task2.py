"""
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.
"""

#def dict_create(s: str) -> dict:

string_user = 'Text string'
res_dict = {key: ord(key) for key in string_user}

res = {}
for key in string_user:
    res[key] = ord(key)

print(res_dict)
print(res)