ren = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

profit = ren - costs

if profit < 0:
    print('Компания работает в убыток:', profit)
elif profit == 0:
    print('Компания работает в ноль')
else:
    print('Компания работает в прибыль:', profit)
    print(f'Рентабельность составляет: {round(profit / ren * 100, 1)}%')

    num = int(input('Введите численность: '))
    print('Прибыль на 1 сотрудника составляет: ', round(profit / num, 1))