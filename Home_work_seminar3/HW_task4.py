# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.

dict1 = {'cup': 0.5, 'tea': 0.4, 'clother': 2, 'tent': 4, 'sleeping_bag': 3, 'matches': 0.02}

back = 5

for key, item in dict1.items():
    if item <= back:
        back = back - item
        print(key)
    else:
        continue

    