# Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

number = int(input('Введите целое число: '))


def fib(num):
    list = [1] * num
    index = 1  # начинаем со второго элемента
    start = 1
    while index < num:
        list[index] = start
        start = list[index] + list[index-1]
        index += 1
    return list


list_fib = fib(number)
print(list_fib)