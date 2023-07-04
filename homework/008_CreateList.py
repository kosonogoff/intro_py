# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

number = int(input('Введите число: '))


def create_list(num):
    length = (num * 2) + 1
    start = -num
    numbers = [0] * length

    for i in range(len(numbers)):
        numbers[i] = start
        start += 1

    return numbers


numbers = create_list(number)
print(numbers)


def offset_right(list, step):
    left = list[-step:]
    right = list[:-step]
    return left + right


step = 2  # сдвигаем все элементы списка на 2 позиции вправо
print(offset_right(numbers, step))