# В списке хранятся сведения о количестве осадков, 
# выпавших за каждый день июня.
# Определите в какой период выпало больше осадков:
# в первой или второй половине июня.
# Примечание: список заполняется случайными числами от 0 до 25.

import random

june_precipitation = [random.randint(0, 25) for index in range(30)]
print(june_precipitation)

sum_first = 0
sum_second = 0

for i in range(30):
    if i < 15:
        sum_first += june_precipitation[i]
    else:
        sum_second += june_precipitation[i]

# print(sum_first)
# print(sum_second)

if sum_first > sum_second:
    print(f'В первой половине июня выпало больше осадков, а именно: {sum_first}')
else:
    print(f'Во второй половине июня выпало больше осадков, а именно: {sum_second}')