'''
1. Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу: (
выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
'''

try:
    from sys import argv

    script_name, output, rate, bonus = argv

    output = float(output)
    rate = float(rate)
    bonus = float(bonus)
except ValueError:
    print('Данные для расчета некорректны')
else:
    result = output * rate + bonus
    print(f' ЗП составит: {result} руб.')

