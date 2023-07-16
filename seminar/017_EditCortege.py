# Создайте кортеж, заполненный случайными числами.
# Напишите метод, который заменяет элемент в
# кортеже по заданному индексу другим случайным числом.

import random

number = int(input('Введите целое число: '))
cortege = tuple(random.randint(1, 100) for _ in range(number))
print(cortege)


def edit(cortege, index):
    temp = list(cortege)
    temp[index] = random.randint(1, 100)
    new = tuple(temp)
    return new


def change(numbers, i):
    return numbers[:i] + (random.randint(1, 100), ) + numbers[i+1:]


index = int(input('Введите индекс элемента: '))
new = edit(cortege, index)
print(new)

top = change(cortege, index)
print(top)
