# Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

number = float(input('Введите число: '))

result = int(number * 10 // 1) % 10

if result == 0:
    print('Нет. Первая цифра после запятой - ноль.')
else:
    print(f'Первая цифра после запятой: {result}')