"""
7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""

import json

firms = {}
bug_line = []

with open('text_7.txt') as f_obg:
    num_line = 1
    for line in f_obg:
        data_firm = line.strip().split()
        try:
            key = data_firm[0]
            profit = int(data_firm[2]) - int(data_firm[3])

        except ValueError:
            bug_line.append(num_line)
        else:
            firms[key] = profit
        num_line+=1

if bug_line:
    print('Не прочитаны данные в строках: ', bug_line)

summ_profit = 0
count_firm = 0

for value in firms.values():
    if value >= 0:
        summ_profit += value
        count_firm += 1

try:
    average_profit = summ_profit / count_firm
except ZeroDivisionError:
    average_profit = 'нет компаний с прибылью'
finally:
    av_profit = dict(average_profit = average_profit)
    data = [firms, av_profit]
    print(data)

with open('file_json.json', 'w') as f_json:
    json.dump(data, f_json)

# не получается в json записать наименование компаний на русском языке