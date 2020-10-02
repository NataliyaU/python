"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""

def division(x,y):
    if y == 0:
        return
    return x / y

try:
    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))

except ValueError:
    print('Значение введено некорректно')

else:
    result = division(num_1, num_2)
    message = round(result, 2) if result else "Деление на ноль невозможно"

    print(f'{num_1} / {num_2} = {message}')