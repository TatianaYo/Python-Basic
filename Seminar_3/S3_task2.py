# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

a = input('Enter: ')

if a.isdecimal():
    res = int(a)
elif a.replace('.', '').replace('-','').isdecimal():
    res = float(a)
elif not a.islower():
    res = a.lower()
else:
    res = a.upper()

print(f'{res = } {type(res)}')