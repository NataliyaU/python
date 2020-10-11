"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать
сумму чисел в файле и выводить ее на экран.
"""

import random

def create_file(f_obg):
    count_num = random.randint(10, 30)
    for _ in range(count_num):
        number = random.randint(1, 100)
        f_obg.write(f'{number} ')


def read_file(f_obg):
    content = f_obg.read()
    my_list = [int(num) for num in content.strip().split()]
    summ = sum(my_list)
    print(summ)

with open('text_5.txt', 'w', encoding= 'Utf-8') as f_obg:
    create_file(f_obg)

with open('text_5.txt') as f_obg:
    read_file(f_obg)
