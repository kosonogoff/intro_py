# Создайте кортеж. Запишите в него 10 случайных чисел

import random

numbers = tuple(random.randint(1, 10) for _ in range(10))
print(numbers)
print(type(numbers))  # проверим тип

numbers = list(numbers) # преобразовал в список
print(numbers)
print(type(numbers))