# Дано число N. Найти все его делители. 
# Для каждого делителя укажите чётный он или нечётный
# 10 -> 10 (чётный), 5(нечётный), 2 (чётный), 1(нечётный)

def even(number):
    if number % 2 == 0:
        return 'чётное'
    else:
        return 'нечётное'
    

def divisors():
    number = int(input('Введите целое число: '))

    for i in range(1, number + 1):
        if number % i == 0:
            print(f'{i} - {even(i)}')

divisors()