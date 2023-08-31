born_year = input('Введите год рождения А.С.Пушкина ')
if born_year == '1799':
    born_day = input('Введите день и месяц рождения (dd.mm): ')
    if born_day == '06.06':
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')