"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('text_3.txt', 'r') as file_txt:
    personal = {}
    for line in file_txt:
        key, value = [num for num in line.strip().split()]
        personal[key] = int(value)
summ = 0
print('Фамилии сотрудников, оклад которых составляет менее 20 тыс.руб: ')
for key, value in personal.items():
    summ = summ + value
    if value < 20000:
        print(f'{key} - {value}')

mean = summ / len(personal)
print(f'Средняя величина дохода на 1 сотр. составляет:\n'
      f'{summ} руб. / {len(personal)} сотр. = {mean:.2f} руб.')

