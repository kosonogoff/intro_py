# Напишите программу, которая на вход принимает число (N),
# а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

number = int(input('Введите целое число: '))

if number < 0:
    print('Вы ввели отрицательное число')

if number > 0 and number < 2:
    print('Вы ввели слишком маленькое число')

else:
    start = 2
    while start <= number:
        print(start, end = " ")
        start += 2