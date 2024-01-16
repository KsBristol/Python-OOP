from string import ascii_letters


class Person:
    """Данные о персонале некоторого учреждения"""
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-'

    def __init__(self, fio, old, ps, weight):
        # вызов методов по проверке введенных данных, если ок
        # то программа отрабатывает дальше без вызова исключений
        # если будет исключение, то выкинет исключение и
        # программа завершит свою работу
        self.varify_fio(fio)
        self.varify_old(old)
        self.varify_weight(weight)
        self.varify_ps(ps)
        # после проверки на правильность и отсутствии исключений
        # присваиваем переменным введенные данные
        self.__fio = fio.split()  # список ФИО
        self.__old = old  # возраст целое число от 14 до 120
        # серия и номер паспорта строка в формате
        # хххх хххххх , где х число от 0 до 9
        self.__passport = ps
        self.__weight = weight  # вес в кг, вещественное число

        # или можно убрать проверку
        # self.varify_old(old)
        # self.__old = old
        # и вместо этого написать одной трокой обращаясь напрямую в сеттер,
        # где и будет происходить проверка введенных данных
        # self.old = old

    @classmethod
    def varify_fio(cls, fio):
        """Проверка правильности введенных данных ФИО"""
        # проверим строка ли
        if type(fio) != str:
            # если не строка генерируем исключение
            raise TypeError("ФИО должно быть строкой")

        fio_lst = fio.split()

        # Если длина списка не равна 3, то генерируем исключение
        if len(fio_lst) != 3:
            raise TypeError("Неверный формат ФИО")

        # Проверим что в ФИО используются только буквы и символ дефиса
        # вводим доп строку, которая будет содержать все допустимые символы
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

        # переберем
        for s in fio_lst:
            # проверим что в ФИО есть хотя бы один символ
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            # проверим что в ФИО содержатся допустимые символы
            if len(s.strip(letters)) !=0:
                raise TypeError("ФИО содержит недопустимый символ: "
                                "можно использовать только буквы и дефис")

    @classmethod
    def varify_old(cls, old):
        """Проверка правильности введенных данных возраста"""
        # тип данных возраста должен быть int и от 14 до 120
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом в диапазоне [14, 120]")

    @classmethod
    def varify_weight(cls, weight):
        """Проверка правильности введенных данных веса"""
        # тип данных веса должен быть float и от 20 и больше
        if type(weight) != float or weight < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")

    @classmethod
    def varify_ps(cls, ps):
        """Проверка правильности введенных паспортных данных"""
        # тип данных паспорта строка
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")

        ps_lst = ps.split()

        # проверка на длину списка, что данные состоят из двух чисел,
        # первый элемент списка равен 4 и второй элемент равен 6
        if len(ps_lst) != 2 or len(ps_lst[0]) != 4 or len(ps_lst[-1]) != 6:
            raise TypeError("Неверный формат паспорта")

        # данные  паспорта все состоят из чисел
        for p in ps_lst:
            # если элемента не числа
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        """Внесение изменений в ФИО"""
        # проверка на корректность новых данных
        self.varify_fio(fio)
        # занесение данных в случае прохождения проверки
        self.__fio = fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        """Внесение изменений в возраст"""
        # проверка на корректность новых данных
        self.varify_old(old)
        # занесение данных в случае прохождения проверки
        self.__old = old

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        """Внесение изменений в паспортные данные"""
        # проверка на корректность новых данных
        self.varify_ps(ps)
        # занесение данных в случае прохождения проверки
        self.__passport = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        """Внесение изменений в вес"""
        # проверка на корректность новых данных
        self.varify_weight(weight)
        # занесение данных в случае прохождения проверки
        self.__weight = weight


p = Person('Балакирев Сергей Михайлович', 30, '1234 567890', 80.0)
print(p.__dict__)
# {'_Person__fio': ['Балакирев', 'Сергей', 'Михайлович'],
# '_Person__old': 30, '_Person__passport': '1234 567890',
# '_Person__weight': 80.0}
p.old = 100
p.passport = '4567 123456'
print(p.__dict__)
# {'_Person__fio': ['Балакирев', 'Сергей', 'Михайлович'],
# '_Person__old': 100, '_Person__passport': '4567 123456',
# '_Person__weight': 80.0}


# p = Person('Балакирев Сергей Михайлович.', 30, '1234 567890', 80.0)
# Неправильно введенные ФИО дают ошибку:
# File "D:\education\progi\balakirev OOP\rezhimi dostupa,
# deskriptori.py", line 1125, in varify_fio
# raise TypeError("ФИО содержит недопустимый символ: "
# TypeError: ФИО содержит недопустимый символ: можно использовать
# только буквы и дефис