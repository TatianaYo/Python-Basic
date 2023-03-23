# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.


def string_sort(a: str) -> list[int]:
    list1 = set()

    for char in a:
        list1.add(ord(char))
    list1 = sorted(list1, reverse=True)
    return list1


print(string_sort('fdjdfdkjflk ghsdo fgd fdksjh skksk'))