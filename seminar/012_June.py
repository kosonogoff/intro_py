# В списке хранятся сведения о количестве осадков, выпавших за каждый день июня.
# Определите в какой период выпало больше осадков: в первой или второй половине июня.
# Примечание: список заполняется случайными числами от 0 до 25.

import random

days = 30
june = [random.randint(0, 25) for _ in range(days)]
print(june)

first_part = june [:15] # сделал срез первой половины месяца
second_part = june [15:] # сделал срез второй половины месяца
# print(first_part)
# print(second_part)

def rain(list): # написал метод для нахождения суммы чисел в списке
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

sum_first = rain(first_part)
sum_second = rain(second_part)
# print(sum_first)
# print(sum_second)

if sum_first > sum_second:
    print(f'В первой половине июня выпало больше осадков, а именно: {sum_first}')
elif sum_second > sum_first:
    print(f'Во второй половине июня выпало больше осадков, а именно: {sum_second}')
else:
    print(f'Количество осадков в обеих половинах месяца одинаковая, а именно {sum_first}')