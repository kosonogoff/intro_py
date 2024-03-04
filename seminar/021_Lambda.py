# Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5. 
# Заполните список случайным образом числами от 1 до 100

import random

def FindingDev(list, dev):
    numbers = filter(lambda x: not (x % dev), list)
    return numbers

start = [random.randint(1, 101) for _ in range(15)]
print(start)

dev = 5
finish = FindingDev(start, dev)
finish = list(finish)
print(finish)