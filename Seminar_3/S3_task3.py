# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

my_tuple = (5, 'fbhste', False, 5.36, 'vgy', 6, 2.458)
my_dict = {}

for item in my_tuple:
  #  if type(item) in my_dict.keys():
  #      my_dict[type(item)] = item
  #  else   
    key = my_dict.setdefault(type(item), list())
    key.append(item)
print(my_dict)