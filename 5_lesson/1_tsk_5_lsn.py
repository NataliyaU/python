'''
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

data = input('Введите данные: ')

if data:
    with open('text_1.txt', 'w', encoding='Utf-8') as file_txt:

        while data:
            file_txt.write(f'{data}\n')
            data = input()

