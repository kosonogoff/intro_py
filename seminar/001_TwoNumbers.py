# Напишите программу, которая на вход принимает два ЦЕЛЫХ числа
# и проверяет, является ли второе число квадратом первого

numberFirst = int(input('Введите первое число: '))
numberSecond = int(input('Введите второе число: '))

if numberFirst == numberSecond:
    print('Оба числа равны!')

else:
    if numberSecond > numberFirst:
        if numberSecond % numberFirst == 0:
            print (f'Число {numberSecond} является квадратом числа {numberFirst}')
        else:
            print(f'Число {numberSecond} не является квадратом числа {numberFirst}')
    else:
        temp = numberFirst
        numberFirst = numberSecond
        numberSecond = temp

        if numberSecond % numberFirst == 0:
            print (f'Число {numberSecond} является квадратом числа {numberFirst}')
        else:
            print(f'Число {numberSecond} не является квадратом числа {numberFirst}')