#3. Напишите код, который запрашивает число и сообщает является ли оно простым 
#или составным. Используйте правило для проверки: “Число является простым,
# если делится нацело только на единицу и на себя”. 
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
MIN_NUM = 0
MAX_NUM = 100001

number = int(input("Введите число от 1 до 100000: "))

if MIN_NUM < number < MAX_NUM:
    if number % 2 != 0:
        print('Число простое')
    else:
        print('Число составное')
else:
    print('Выходит за диапазон')