'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
(Подсказка: не нумеруйте строки вручную, для этого есть
встроенная функция, которой можно передать параметром первое число,
с которого начинать пересчет.)
'''

my_list = input('Введите несколько слов: ').split()

for ind, el in enumerate(my_list, 1):
    if len(el) > 10:
     el = el[:10]
    print(ind, el)
