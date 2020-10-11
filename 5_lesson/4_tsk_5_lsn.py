"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные. При этом английские
числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь'
}
# не понимаю, как в этом случае можно применить генераторное выражение
with open('text_4.txt') as file_read:
    my_list = []
    for line in file_read:
        el = line.strip().split()

        for key, value in numbers.items():
            if key == el[0]:
                el[0] = value
        my_list.append(el)

with open('text_4new.txt', 'w', encoding='Utf-8') as file_create:
    for i in range(len(my_list)):
        line = ' '.join(my_list[i])
        file_create.writelines(f'{line}\n')

