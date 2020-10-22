"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class Complex:
    """ Класс для создания комплексных чисел: a + b * i, где i^2 = - 1"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b < 0:
            return f'{self.a}{self.b}i'
        else:
            return f'{self.a}+{self.b}i'

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            a = self.a + other
            b = self.b
            return Complex(a, b)
        elif isinstance(other, Complex):
            a = self.a + other.a
            b = self.b + other.b
            return Complex(a, b)
        else:
            print('Невозможно сложить 2 значения')

    __radd__ = __add__


    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            a = self.a * other
            b = self.b * other
            return Complex(a, b)
        elif isinstance(other, Complex):
            a = self.a * other.a - self.b * other.b
            b = self.a * other.b + other.a * self.b
            return Complex(a, b)
        else:
            print('Невозможно умножить 2 значения')

    __rmul__ = __mul__

if __name__ == '__main__':

    x = Complex(2, 3)
    y = Complex(2, -5)
    z = Complex(1, 1)

    print(x, y, z, sep='\n')

    print(x + 2)
    print(2 + x)
    print(x + y)
    print(x + z)

    print(x * 2)
    print(x * y)




