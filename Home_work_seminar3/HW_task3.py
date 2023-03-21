# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

list1 = [1, 1, 1, 5, 12, 7, 2, 5, 6, 12, 5, 1, 7, 7, 9, 12, 1, 5, 7]
list2 = []

for item in list1:
    if list1.count(item) > 1:
        list2.append(item)
    #if list2.count(item) > 1:
        #list2.remove(item)
print(*sorted(set(list2)))