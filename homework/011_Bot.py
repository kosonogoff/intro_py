# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.

responses = {"Привет": "И тебе привет!",
             "Как тебя зовут": "Меня зовут Алиса",
             "Кто ты": "Я чат-бот, написанный программистом",
             "Какой можешь дать совет": "Покупай биткоин"}


def bot(dict):
    flug = True
    keys = list(dict.keys())

    while flug:
        question = str(input('Введите запрос: '))

        if question in keys:
            print(dict[question])
        else:
            print(
                'Я ещё учусь и не знаю ответа на этот вопрос. Попробуй позже меня снова запустить')
            flug = False


bot(responses)