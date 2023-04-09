# Дано число N. Заполните список длиной N элементами 1, -3, 9, -27, 81, -243...
# N = 5 -> [1, -3, 9, -27, 81]

numbers = []
length = int(input('Введите необходимую длину списка: '))

for el in range(length):
    #print(f'{el} -> {(-3)**el}')
    numbers.append((-3)**el)

print(numbers)