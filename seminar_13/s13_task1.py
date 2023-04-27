"""
Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def get_num(text: str = None) -> int:

    while True:
        num_str = input(text)
        try:
            num = int(num_str)
            break
        except ValueError as e:
            print(f'Ваш ввод привел к ошибке: {e}\n')
            try:
                num = float(num_str)
                break
            except ValueError as e:
                print(f'Ваш ввод привел к ошибке: {e}\n')
    return num


number = get_num('Enter number: ')
print(f'Entering number {number}')