"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""


class Clothes:

    total_consumption = 0
    def __init__(self, name):
        self.name = name

class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        # не понимаю, как наследовать атрибут name,
        # чтобы его пользователь тоже вводил при создании объекта класса Coat
        super().__init__(name= 'пальто')

    # не разобралась, как реализовать с propety
    def consumption(self):
        cons = self.size / 6.5 + 0.5
        Clothes.total_consumption += cons
        return cons

class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        super().__init__(name='костюм')

    def consumtion(self):
        cons = 2 * self.height + 0.3
        Clothes.total_consumption += cons
        return cons

a = Clothes('куртка')
b = Coat(10)
c = Suit(100)

print(b.consumption())
print(c.consumtion())
print(a.total_consumption)

