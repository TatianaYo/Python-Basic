"""
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""

string_user = 'Text string'
res_dict = {key: ord(key) for key in string_user}

my_iter = iter(res_dict.items())
for i in range(5):
    print(next(my_iter))