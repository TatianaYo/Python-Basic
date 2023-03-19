# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

number = int(input('Enter number: '))

print(hex(number))

#while number > 0:
#    number16 = number % 16
 #   if number16 == 10: number: str = a
  #  if number16 == 10: number: str = a
   # res = str
res = ''
hexadecimal_sys = '0123456789ABCDEF'
 
while number > 0:
    res = hexadecimal_sys[number % 16] + res
    number = number // 16
 
print(res)