# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

string_first = input('Введите первую строку: ').lower()
string_second = input('Введите вторую строку: ').lower()
length_first = len(string_first)
length_second = len(string_second)

def how_many(string, symbol):
    count = 0
    for i in range(len(string)):
        if symbol == string[i]:
            count += 1
    return count


def print_symbol(one, two):
    index = 0

    while index < len(one):
        print(f'Символ "{one[index]}" во второй строке встречается {(how_many(two, one[index]))} раз(а)')
        index += 1

if length_first < length_second:
    print_symbol(string_first, string_second)

else:
    print_symbol(string_second, string_first)