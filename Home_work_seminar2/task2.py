# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

number_1 = fractions.Fraction(input('Введите первую дробь типа a/b: '))
number_2 = fractions.Fraction(input('Введите вторую дробь типа a/b: '))

sum = number_1 + number_2
res = number_1 * number_2

print('Сумма: ', + sum)
print('Произведение: ', + res)