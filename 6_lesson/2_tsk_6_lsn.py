"""
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны
передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см
толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculation_weight(self, weight1x1x1 = 25, thickness = 5):
        weight = self.__length * self.__width * weight1x1x1 * thickness / 1000

        return f'{self.__length}м * {self.__width}м * {weight1x1x1}кг * {thickness}см = {weight} т'

r = Road(5000, 20)
print(r.calculation_weight())

