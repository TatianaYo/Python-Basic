"""
✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
    ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
    ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало.
"""
__all__ = ['open_file']


def open_file(a: str, b: str) -> None:
    with (
        open(a, 'r', encoding='utf-8') as f1,
        open(b, 'r', encoding='utf-8') as f2,
        open('open_file.txt', 'w', encoding='utf-8') as f3
    ):
        len_f1 = sum(1 for _ in f1)
        len_f2 = sum(1 for _ in f2)

        for _ in range(max(len_f1, len_f2)):
            text = f1.readline()
            if text == '':
                f1.seek(0)
                text = f1.readline()
            text = text[:-1]

            num = f2.readline()
            if num == '':
                f2.seek(0)
                num = f2.readline()
            num = num[:-1]

            num1, num2 = num.split('|')
            res = int(num1) * float(num2)
            if res < 0:
                f3.write(f'{text.lower()}, {abs(res)}\n')
            else:
                f3.write(f'{text.upper()}, {round(res)}\n')


if __name__ == '__main__':
    open_file('name.txt', 'data.txt')