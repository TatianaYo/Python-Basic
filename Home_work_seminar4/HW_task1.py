"""✔ Функция получает на вход список чисел и два индекса.
   ✔ Вернуть сумму чисел между переданными индексами.
   ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
"""
def sum_between_ind(list_num: list[int], index1: int, index2: int) -> None:

    sum_num = 0
    START_I = 0

    if index1 < START_I:
        index1 = START_I - 1
    if index2 > len(list_num) - 1:
        index2 = len(list_num)

    for i in range(index1 + 1, index2):
        sum_num += list_num[i]
    print(sum_num)


list1 = [3, 6, 4, 10, 24, 7, 12, 32, 6, 15]
ind_1 = -8
ind_2 = 2
sum_between_ind(list1, ind_1, ind_2)