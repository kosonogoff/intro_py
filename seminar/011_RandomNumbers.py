# Дан список, заполненный случайными числами от 0 до 10.
# Определите, является ли сумма всех элементов чётной

# подключаем библиотеку для генерации рандомных чисел
import random

length = random.randint(5, 15)

# метод для генерации (в строке 20 более компактный вариант)
def generate_list(length):
    numbers = [0] * length

    for index in range(length):
        numbers[index] = random.randint(-100, 100)

    return numbers


# numbers = generate_list(length)
numbers = [random.randint(0, 50) for index in range(length)]

print(numbers)

sum = 0
for index in range(length):
    sum += numbers[index]

print(f'Сумма всех элементов равна: {sum}')

if sum % 2 == 0:
    print('Сумма чётная')
else:
    print('Сумма нечётная')