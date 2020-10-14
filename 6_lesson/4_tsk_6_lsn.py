"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
 Для классов TownCar и WorkCar переопределите метод show_speed.
 При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
 выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed = 0, color = None, name = None, is_police= False):
        # как проверить тип присылаемых атрибутов экземпляра
        # (например, проверить, что скорость должна быть int)
        # и вернуть ошибку, не знаю, было мало времени на подумать.
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police:
            return f'Машина {self.name} поехала. Ахтунг! Это ГиБДД'
        else:
            return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        # можно здесь сделать проверку на принимаемый direction
        return f'Машина {self.name} повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость: {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Текущая скорость: {self.speed} - Скорость превышена'
        else:
            return f'Текущая скорость: {self.speed}'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Текущая скорость: {self.speed} - Скорость превышена'
        else:
            return f'Текущая скорость: {self.speed}'

class PoliceCar(Car):
    pass



car_1 = Car(20, 'green', 'Toyota')
print(f'Атрибуты: '
      f'speed = {car_1.speed},'
      f' color = {car_1.color},'
      f' name = {car_1.name}, '
      f'is_police= {car_1.is_police}')

print(car_1.go())
print(car_1.turn('left'))
print(car_1.stop())
print(car_1.show_speed())

car_2 = WorkCar(80, 'white', 'Volvo')

print(f'Для WorkCar: {car_2.show_speed()}')
