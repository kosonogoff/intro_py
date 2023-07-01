# Ручка стоит – 5 рублей, карандаш – 3 рубля, ластик – 4 рубля.
# Кассир последовательно вводит в программу позиции из чека «ручка», «карандаш», «ластик».
# Ввод заканчивается, когда введено слово «стоп». Определите сумму чека.

prices = {"ручка": 5,
          "карандаш": 3,
          "ластик": 4
          }


def check(prices):
    sum = 0
    flag = True

    while flag:
        item = input('Введите товар (ручка, карандаш, ластик) или "стоп" для завершения: ').lower()
        if item == "стоп":
            flag = False
        elif item in prices:
            sum += prices[item]
        else:
            print('Такого товара нет. Введите корректное наименование.')

    return sum

total = check(prices)
print(f'Общая сумма счёта составляет {total} рублей')