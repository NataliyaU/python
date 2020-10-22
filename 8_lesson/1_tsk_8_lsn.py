"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class MyDate:

    @classmethod
    def transform_date(cls, date_str):
        date_list = date_str.strip().split('-')
        try:
            day, month, year = [int(i) for i in date_list]
        except:
            raise ValueError('Некорректно введен формат dd-mm-yyyy')
        else:
            valid = MyDate.validalion(day, month, year)
            if valid:
                return day, month, year

    @staticmethod
    def validalion(day, month, year):
        if day not in range(1, 32):
            raise ValueError('Дата некорректна')
        elif month not in range(1, 13):
            raise ValueError('Meсяц введен некорректно')
        elif len(str(year)) != 4:
            raise ValueError('Год введен некорректно: yyyy')
        else:
            return True

    def __init__(self, date_str):
        # прверка на передаваемый формат
        self.date_str = date_str
        self.day, self.month, self.year = MyDate.transform_date(self.date_str)

    def __str__(self):
        return f'{self.day} {self.month} {self.year}'


print(MyDate('13-10-2020'))

date = MyDate('11-12-2020')
print(date)
print(date.day, date.month, date.year)

