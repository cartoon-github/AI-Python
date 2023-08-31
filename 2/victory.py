born_years = {1938: 'Владимир Высоцкий',
              1834: 'Дмитрий Менделеев',
              1931: 'Михаил Горбачев',
              1870: 'Владимир Ленин (Ульянов)',
              1942: 'Александр Калягин',
              1975: 'Анжелина Джоли',
              1859: 'Артур Конан Дойл',
              1840: 'Петр Ильич Чайковский',
              1967: 'Филипп Киркоров',
              1564: 'Уильям Шекспир'}
again = True

while again:
    right = 0
    wrong = 0

    for year, name in born_years.items():
        answer = input(f'Введите год рождения {name} (YYYY): ')
        if answer == str(year):
            print('Верно!')
            right += 1
        else:
            print('Неверно!')
            wrong += 1

    print(f'Правильных ответов: {right} ({right*100/len(born_years)}%)')
    print(f'Неправильных ответов: {wrong} ({wrong*100/len(born_years)}%)')

    if input('Еще раз? (y/n) ') == 'n':
        again = False