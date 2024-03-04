# Задача 1. На вход подаётся четырёхзначное число.
# Получите список, состоящий из цифр данного числа, увеличенных на 10.
# 9650 –> [19, 16, 15, 10]
# 1043 –> [11, 10, 14, 13]

number = input('Введите число: ')

def NumberToList(num):
    spisok = [int(letter) for letter in num]
    result = list(map(lambda x: x + 10, spisok))
    return result

print(NumberToList(number))