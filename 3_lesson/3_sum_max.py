"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func(x, y, z):
    my_list = sorted([x, y, z], reverse= True)
    return my_list[0] + my_list[1]

print(my_func(7, 11, 4))
