# Напишите программу, которая позволит пользователю
# заполнить анкету, последовательно вводя в программу:
# - имя;
# - возраст;
# - хобби;
# - любимое животное.
# После окончания ввода, выводится заполненная анкета

def get_profile():
    form = dict(name = input('Ваше имя: '),
                age = input('Ваш возраст: '),
                hobby = input('Ваше хобби: '),
                animal = input('Ваше любимое животное: ')
                )
    return form

user = get_profile()

def print_profile(user):
    print('Анкета пользователя:')
    for key, value in user.items():
        print(key, '-', value)

print_profile(user)