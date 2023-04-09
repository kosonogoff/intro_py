# Напишите программу, которая находит наибольшее и
# наименьшее число из списка значений

data = [1,466,2,34,6,6,62,7,8,-99,322124,57,8,9433678,874,45,757,4]

#print(f'min = {min(data)}')
#print(f'max = {max(data)}')

min_value = data[0]
max_value = data[0]

for i in data:
    #print(i)
    if i < min_value:
        min_value = i
    if i > max_value:
        max_value = i

print(f'min = {min_value}')
print(f'max = {max_value}')