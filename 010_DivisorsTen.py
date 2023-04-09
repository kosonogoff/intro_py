# Найдите все числа до 10000, у которых 
# количество делителей равно 10

number = 10000

def divisors_ten(number):
    count_ten = 0

    for num in range(1, number + 1):
        count = 0
        
        for div in range(1, num + 1):
            if num % div == 0:
                count += 1
        
        if count == 10:
            count_ten += 1
            print(num)

    return count_ten

print(f'В числе {number} количество чисел, у которых 10 делителей, равно: {divisors_ten(number)}')