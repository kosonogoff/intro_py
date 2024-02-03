# Напишите программу, в которой пользователь будет 
# задавать две строки, а программа - определять 
# количество вхождений одной строки в другую.
# «qwe» «qwertyqwe» -> 2

stringFirst = input('Введите первую строку: ')
lengthFirst = len(stringFirst)

stringSecond = input('Введите вторую строку: ')
lengthSecond = len(stringSecond)

count = 0

if lengthSecond > lengthFirst:
    for i in range(lengthSecond):
        #print(stringSecond[i:i+lengthFirst])
        temp = stringSecond[i:i+lengthFirst]
        if temp == stringFirst:
            count += 1
    print(f'В строке "{stringSecond}" подстрока "{stringFirst}" встречается {count} раз(а).')

else:
    for i in range(lengthFirst):
        temp = stringFirst[i:i+lengthSecond]
        if temp == stringSecond:
            count += 1
    print(f'В строке "{stringFirst}" подстрока "{stringSecond}" встречается {count} раз(а).')