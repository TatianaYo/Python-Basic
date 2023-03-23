"""✔ Функция принимает на вход три списка одинаковой длины:
   ✔ имена str,
   ✔ ставка int,
   ✔ премия str с указанием процентов вида «10.25%».
   ✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
   ✔ Сумма рассчитывается как ставка умноженная на процент премии. """


def dict_create(a: list[str], b: list[int], c: list[str]) -> dict[str, float]:
    result = {}
    
    for name, level, bonus in zip(a, b, c):
        result[name] = (level * float(bonus[:-1])) / 100
    return result


list1 = ['Ваня', 'Петя', 'Коля']
list2 = [300, 250, 400]
list3 = ['11.5%', '10.3%', '12%']
print(dict_create(list1, list2, list3))