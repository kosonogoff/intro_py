# Организуйте последовательный ввод чисел до тех пор,
# пока не будет введён 0. Подсчитайте среди введённых чисел те,
# которые кратны трём

number = int(input('Введите число: '))
count = 0

while number != 0:
    if number % 3 == 0:
        count += 1
    number = int(input('Введите число: '))

print('Ввод закончен.', end = " ")
print(f'Число чисел кратных трём равно: {count}')