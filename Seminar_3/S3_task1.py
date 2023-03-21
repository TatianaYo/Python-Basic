# Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные (без повтора)
# элементы исходного списка.

my_list = [1, 3, 7, 4, 7, 3]
print(my_list)

my_list2 = []

for item in my_list:
    if item not in my_list2:
        my_list2.append(item)
print(my_list2)

my_list3 = list(set(my_list))
print(my_list3)