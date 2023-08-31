born_year = ''
while born_year != '1799':
    born_year = input('Введите год рождения А.С.Пушкина ')
    if born_year != '1799':
        print('Неверно')

born_day = ''
while born_day != '06.06':    
    born_day = input('Введите день и месяц рождения (dd.mm): ')
    if born_day != '06.06':
        print('Неерно')

print('Верно')