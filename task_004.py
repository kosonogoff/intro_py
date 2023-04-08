# В списке хранятся числа. Нужно выбрать только чётные числа
# и составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

data = [1, 2, 3, 5, 8, 15, 23, 38]

# result = list()

# for i in data:
#    if i % 2 == 0:
#        result.append((i, i**2))

# print(result)


#def select(f, collection):
#    return [f(x) for x in collection]


#def where(f, collection):
#    return [x for x in collection if f(x)]


result = map(int, data) # вместо result = select(int, data)
result = filter(lambda x: x % 2 == 0, result) # вместо result = where(lambda x: x % 2 == 0, result)
result = list(map(lambda x: (x, x**2), result)) # вместо result = list(select(lambda x: (x, x**2), result))
print(result)


# Знакомство с функцией map()

#list_1 = [x for x in range(1, 9)]
#print(list_1)

#list_1 = list(map(lambda x: x + 10, list_1))
#print(list_1)

# C клавиатуры вводится некий набор чисел, 
# в качестве разделителя используется пробел. 
# Этот набор чисел будет считан в качестве строки. 
# Как превратить list строк в list чисел?

#new_data = '15 1234 134 34343 5342 12 12 33 2'
#print(new_data)

#new_data = list(map(int, new_data.split()))
#print(new_data)

# Функция map() равна функции select() выше