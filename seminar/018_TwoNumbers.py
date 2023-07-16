# На вход подаются два числа. Напишите метод, который вернёт
# сумму, разность, произведение и частное этих чисел

number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))


def calc(one, two):
    return one + two, one - two, one * two, one / two


result = calc(number_one, number_two)
print(result)
sum, ded, mult, div = result

print(f'Сумма чисел равна {sum}')
print(f'Разность чисел равна {ded}')
print(f'Произведение чисел равно {mult}')
print(f'Деление {number_one} на {number_two} равно {div}')
