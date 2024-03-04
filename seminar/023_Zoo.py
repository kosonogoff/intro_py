# Задача 2. В зоопарк отправили отчёт о новом поступлении зверей с ошибкой, 
# в результате которой некоторые данные не расшифровались. Расшифруйте данные. 
# Определите, в какой клетке находится лев. Номер клетки совпадает с номером строки.
# абвгдеёжзийклмнопрстуфхцчшщъыьэюя

def ToBinary(basa):
    result = ''
    while basa > 0:
        result = str(basa%2) + result
        basa //= 2
    return '0' * (6 - len(result)) + result

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet = list(alphabet)

animals = ['000001011100001011',
           '010100001100001001010011001011000000']

d = {}
for i in range(len(alphabet)):
    d[ToBinary(i)] = alphabet[i]

print(d)

result = list(map(lambda x: [d[x[i:i+6]] for i in range(0, len(x), 6)], animals))
result = list(map(lambda x: ''.join(x), result))

print(result)