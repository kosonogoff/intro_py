# Напишите скрипт генератора паролей заданной длины, 
# состоящих из латинских букв и чисел

def gen_pass():
    import random
    import string

    length = int(input('Введите длину пароля: '))

    symbol = string.ascii_letters + string.digits

    password = ''.join(random.sample(symbol, length))
    return password

password = gen_pass()
print(password)