"""
 * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
 Каждый кортеж хранит информацию об отдельном товаре.
 В кортеже должно быть два элемента — номер товара и словарь с параметрами
 (характеристиками товара: название, цена, количество, единица измерения).
 Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя
 (для быстроты попробуйте запрашивать все данные разом — "компьютер 20000 5 шт.").
Для скорости можно не реализовывать проверку на корректность всех-всех данных,
но обязательно используйте правильные типы, не сохраняйте все в строки.
"""

product = input('Введите данные по товару: ')
number = 1
keys = ['название', 'цена', 'количество', 'ед.изм.']
products_list = []

while product != '':

    values = product.split(' ')
    values[1] = float(values[1])
    values[2] = int(values[2])

    my_dict = {}

    for i in range(len(keys)):
        my_dict[keys[i]] = values[i]

    products_list.append((number, my_dict))
    number += 1
    product = input('Введите данные по товару: ')

for i in range(len(products_list)):
    print(products_list[i])

'''
Аналитику попробовала реализовать через транспонирование матрицы из методички.
Вроде получилось, но что-то смущает...
'''

all_values = []
for i in range(len(products_list)):
    all_values.append(products_list[i][1].values())

sort_values = list(zip(*all_values))

# удаляю дубли значений, хотя для цены и кол-ва это, наверное, нелогично.

for i in range(len(sort_values)):
    sort_values[i] = list(set(sort_values[i]))

analytics = {}

for i in range(len(keys)):
    analytics[keys[i]] = sort_values[i]

print(analytics)