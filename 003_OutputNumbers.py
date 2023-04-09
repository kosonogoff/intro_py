# Напишите программу, которая будет на вход
# принимать ЦЕЛОЕ число N и выводить числа от -N до N

number = int(input('Введите число: '))
# или использовать модуль n = abs(int(input(’Введите число: ‘)))

if number == 0:
    print('Вы ввели ноль.')

else:
    if number > 0:
        start = -number
        while start <= number:
            print(f'{start}', end = " ")
            start += 1
    
    else:
        start = number
        number = -number
        while start <= number:
            print(f'{start}', end = " ")
            start += 1  