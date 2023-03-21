# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

list1 = [1, 4, 5, 7, 8, 4, 5, 9]

for item in list1:
    if list1.count(item) > 1:
        for i in range(list1.count(item)):
            list1.remove(item)
print(list1)