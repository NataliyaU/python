"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__()
для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять
поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:

    def __init__(self, array):
        self.array = array
        self._rows = len(array)
        self._columns = max(len(i) for i in array)
        # + должна быть проверка на list и каждого элемента lists = int

    def __str__(self):
        stroka = ''
        for i in self.array:
            st = ' '.join([str(item) for item in i])
            stroka += f'{st}\n'
        return stroka

    def __add__(self, other):

        def sum_lists(list_1, list_2):
            # функция суммирует 2 списка (ряды матриц)
            len_1 = len(list_1)
            len_2 = len(list_2)
            sum_list = list(map(lambda x, y: x + y, list_1, list_2))
            if len_1 > len_2:
                sum_list.extend(list_1[len_2:len_1])
            elif len_2 > len_1:
                sum_list.extend(list_2[len_1:len_2])

            return sum_list

        new_lists = []

        if isinstance(other, Matrix):

            # проверяю количество рядов 2х матриц
            if self._rows == other._rows:
                for i in range(self._rows):
                    row = sum_lists(self.array[i], other.array[i])
                    new_lists.append(row)
            elif self._rows < other._rows:
                for i in range(self._rows):
                    row = sum_lists(self.array[i], other.array[i])
                    new_lists.append(row)
                new_lists.extend(other.array[self._rows:other._rows])
            else:
                for i in range(other._rows):
                    row = sum_lists(self.array[i], other.array[i])
                    new_lists.append(row)
                new_lists.extend(self.array[other._rows:self._rows])

            return Matrix(new_lists)

        else:
            raise TypeError(f'Unsupported data type {type(other)}')

    def __len__(self):
        return len(self.array)

a = Matrix([[1, 2, 3], [4, 5, 6]])

b = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(f'Матрица a:\n{a}')
print(f'Cумма матриц a + b:\n{a + b}')