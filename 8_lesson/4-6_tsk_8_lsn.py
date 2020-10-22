"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных
о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
вводимых пользователем данных. Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
"""


class MyOfficeError(Exception):
    def __init__(self, txt):
        self.txt = txt

class OfficeEquipment:
    """ Класс, описывающий оргтехнику компании"""

    counter_for_uid = 0

    def __init__(self, name, color = None):

        self.uid = OfficeEquipment.counter_for_uid + 1
        self.name = name
        self.color = color
        self.location = {}

        OfficeEquipment.counter_for_uid += 1

    def __str__(self):
        return f'{self.uid} - {self.name}'

    def add_to_warehouse(self, amount, wrh, add=False):
        """ Оприходование товара на склад """

        if not isinstance(amount, int):
            print(f'Некорректный тип параметра Количество - {type(amount)}') #raise TypeError?
        elif not isinstance(wrh, Warehouse):
            print(f'Некорректный тип параметра Склад - {type(wrh)}') #raise TypeError?
        else:
            #wrh.add_item(self)
            value = self.location.get(wrh.name)
            if  value is None:
                self.location[wrh.name] = amount
            else:
                self.location[wrh.name] = amount + value
        if not add: # приходуем на склад, если мы еще этого не делали
            wrh.add_item(amount, self, True)

    def issue_to_division(self, amount, wrh, dvsn):
        """ Выдача товара со склада в подразделение"""

        if not isinstance(amount, int):
            print(f'Некорректный тип параметра Количество - {type(amount)}')  # raise TypeError?
        elif not isinstance(wrh, Warehouse):
            print(f'Некорректный тип параметра Склад - {type(wrh)}') #raise
        elif not isinstance(dvsn, Division):
            print(f'Некорректный тип параметра Подразделение - {type(dvsn)}')  # raise
        else:
            value = self.location.get(wrh.name)
            if value is None:
                print('Нет оргтехники на складе')
            elif value < amount:
                print('Нет такого количества оргтехники на складе')
            elif (value - amount) == 0:
                self.location.pop(wrh.name)
                wrh.del_item(amount, self)
            else:
                self.location[wrh.name] = value - amount
                wrh.del_item(amount, self)


                value = self.location.get(dvsn.name)
                if value is None:
                    self.location[dvsn.name] = amount
                else:
                    self.location[dvsn.name] = amount + value




    def get_location_item(self):
        return self.location

    def view_propeties(self):
        stroka = ''
        for key, value in self.__dict__.items():
            st = f'{key}: {value}, '
            stroka += st
        return stroka


class Printer(OfficeEquipment):
    def __init__(self, name, kind, color = None):
        if not isinstance(kind, str):
            print(f'Тип принтера не str')
        else:
            super().__init__(name, color)
            self.kind = kind.lower()
            if self.kind not in ('лазерный', 'струйный'):
                raise ValueError(f'Указан некорректный тип принтера {kind}')

class Scanner(OfficeEquipment):
    def __init__(self, name, speed, color = None):
        super().__init__(name, color)
        self.speed = speed


class Warehouse:

    list_wrhs = []

    def __init__(self, name):
        self.name = name
        if name in Warehouse.list_wrhs:
            raise MyOfficeError('Склад уже есть в списке')
        Warehouse.list_wrhs.append(self.name)
        self.cur_content = {}

    def __str__(self):
        return f'{self.name}'

    def add_item(self, amount, office_eq, add=False):

        if not isinstance(office_eq, OfficeEquipment):
            print('Не тот тип оборудования')
        else:
            key = f'{office_eq.uid}-{office_eq.name}'
            value = self.cur_content.get(key)
            if value is None:
                self.cur_content[key] = amount
            else:
                self.cur_content[key] = amount + value
        if not add: # прописываем location в оргтехнику, если мы еще этого не делали
            office_eq.add_to_warehouse(amount,self, True)

    def del_item(self, amount, office_eq):
        if not isinstance(office_eq, OfficeEquipment):
            print('Не тот тип оборудования')
        else:
            key = f'{office_eq.uid}-{office_eq.name}'
            value = self.cur_content.get(key)
            if value is None:
                print('Нет такой техники на складе')
            elif value < amount:
                print('Нет такого количества на складе')
            elif value == amount:
                self.cur_content.pop(key)
            else:
                self.cur_content[key] = value - amount


    def view_items(self):
        pass

class Division:

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':

    sklad_1 = Warehouse('Склад_1')
    sklad_2 = Warehouse('Склад_2')
    '''
    dbl_sklad = Warehouse('Склад_1')
    '''
    print(Warehouse.list_wrhs)

    a = OfficeEquipment('Телефон', 'белый')
    b = Printer('принтер Hp', 'Лазерный')
    c = Scanner('Cканер G', 35, 'черный')

    ''' Проверка функции оприходования товара на склад'''

    b.add_to_warehouse(2, sklad_1)
    print(b.view_propeties())
    print(sklad_1.cur_content)

    b.add_to_warehouse(3, sklad_1)
    print(b.get_location_item())
    print(sklad_1.cur_content)

    b.add_to_warehouse(4, sklad_2)
    print(b.get_location_item())
    print(sklad_2.cur_content)

    '''
    a.add_to_warehouse(b)
    '''

    ''' Проверка функции выдачи товара со склада'''
    divsn = Division('Подразделение_1')

    b.issue_to_division(8, sklad_1, divsn) # нет столько техники на складе

    b.issue_to_division(2, sklad_1, divsn) # частичное перемещение
    print(b.view_propeties())
    print(sklad_1.cur_content)

    b.issue_to_division(3, sklad_1, divsn)
    print(b.view_propeties())
    print(sklad_1.cur_content)