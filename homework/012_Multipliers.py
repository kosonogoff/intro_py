# Дано натуральное число N. Напишите метод, который вернёт список простых множителей
# числа N и количество этих множителей.
# 60 -> 2, 2, 3, 5

number = int(input('Введите число: '))
number = abs(number)

def multipliers(num):
    multi = []
    start = 2
    while num > 2:
        while num % start == 0:
            res = num / start
            multi.append(start)
            num = res

        start += 1
    return multi


result = multipliers(number)
print(f'Число {number} имеет следующие множители: {result}')