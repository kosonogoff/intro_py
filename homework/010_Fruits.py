# В списке находятся названия фруктов. Выведите все фрукты,
# названия которых начинаются на заданную букву.
# а –> абрикос, айва, апельсин, арбуз

fruits = ['абрикос',
          'айва',
          'апельсин',
          'арбуз',
          'банан',
          'виноград',
          'гранат',
          'грейпфрут',
          'груша',
          'гуава',
          'дыня',
          'инжир',
          'канталупа',
          'карамбола',
          'киви',
          'красный банан',
          'лимон',
          'манго',
          'марания',
          'мушмула',
          'пепино',
          'персик',
          'питайя',
          'помело',
          'сахарное яблоко',
          'физалис',
          'финик',
          'хурма']

letters = str(input('Введите первую букву названия фрукта: '))

for item in fruits:
    if item.startswith(letters):
        print(item)