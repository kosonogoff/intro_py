# Сгенерируйте список случайных чисел от 1 до 20,
# состоящий из 10 элементов. Удалите из списка
# дубликаты уже имеющихся элементов. Определите,
# сколько элементов было удалено.
# [1, 2, 9, 5, 2, 18, 3, 5, 13, 2] -> [1, 2, 9, 5, 18, 3, 13]
# Удалено элементов: 3

import random

numbers = [random.randint(1, 20) for _ in range(10)]
first = len(numbers)
print(numbers)

new = list(set(numbers))
second = len(new)
print(new)
print(f'Было удалено элементов: {first-second}')