"""
Подвиг 8. Объявите класс Circle (окружность), объекты которого должны создаваться командой:

circle = Circle(x, y, radius)   # x, y - координаты центра окружности; radius - радиус окружности
В каждом объекте класса Circle должны формироваться локальные приватные атрибуты:

__x, __y - координаты центра окружности (вещественные или целые числа);
__radius - радиус окружности (вещественное или целое положительное число).

Для доступа к этим приватным атрибутам в классе Circle следует объявить объекты-свойства (property):

x, y - для изменения и доступа к значениям __x, __y, соответственно;
radius - для изменения и доступа к значению __radius.

При изменении значений приватных атрибутов через объекты-свойства нужно проверять,
что присваиваемые значения - числа (целые или вещественные). Дополнительно у радиуса
проверять, что число должно быть положительным (строго больше нуля). Сделать все эти
проверки нужно через магические методы. При некорректных переданных числовых значениях,
прежние значения меняться не должны (исключений никаких генерировать при этом не нужно).

Если присваиваемое значение не числовое, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
При обращении к несуществующему атрибуту объектов класса Circle выдавать булево
значение False.

Пример использования класса (эти строчки в программе писать не нужно):

circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный
радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует
"""

# 1 вариант без дескриптора

class Circle:
    """Объекты которого должны создаваться командой:
    circle = Circle(x, y, radius)   # x, y - координаты центра окружности;
    radius - радиус окружности"""

    def __init__(self, x, y, radius):
        """__x, __y - координаты центра окружности (вещественные или целые числа);
        __radius - радиус окружности (вещественное или целое положительное число)."""
        self.__x = x
        self.__y = y
        self.__radius = radius

    def __setattr__(self, key, value):
        """Проверка типа присваиваемых данных локальным атрибутам"""
        if not isinstance(value, (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            if key in ('_Circle__x', '_Circle__y'):
                object.__setattr__(self, key, value)
            elif key == '_Circle__radius' and value > 0:
                object.__setattr__(self, key, value)
            else:
                pass

    def __getattr__(self, item):
        """При обращении к несуществующему атрибуту возвращается значение False"""
        return False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius


# 2 вариант с дескриптором

from typing import Union


class Descriptor:

    def __set_name__(self, owner, name):
        self.name = f"_{owner.__name__}__{name}"

    def __get__(self, instance, owner):
        return property() if instance is None else instance.__dict__[self.name]

    def __set__(self, instance, value: Union[int, float]):
        if type(value) in (int, float):
            if self.name == f"_{instance.__class__.__name__}__radius":
                if value > 0:
                    instance.__dict__[self.name] = value
            else:
                instance.__dict__[self.name] = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


class Circle:
    x = Descriptor()
    y = Descriptor()
    radius = Descriptor()

    def __init__(self, x: Union[int, float], y: Union[int, float], radius: Union[int, float]) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    def __getattr__(self, item):
        return False


# Тесты

assert type(Circle.x) == property and type(Circle.y) == property and type(
    Circle.radius) == property, "в классе Circle должны быть объявлены объекты-свойства x, y и radius"

try:
    cr = Circle(20, '7', 22)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при инициализации объекта с недопустимыми аргументами"

cr = Circle(-20, -7, 1)
cr = Circle(20, 7, 22)
assert cr.x == 20 and cr.y == 7 and cr.radius == 22, "объекты-свойства x, y и radius вернули неверные значения"

cr.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
assert cr.radius == 22, "при присваивании некорректного значения, прежнее значение изменилось"

x, y = cr.x, cr.y
assert x == 20 and y == 7, "объекты-свойства x, y вернули некорректные значения"
assert cr.name == False, "при обращении к несуществующему атрибуту должно возвращаться значение False"

try:
    cr.x = '20'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

cr.y = 7.8
cr.radius = 10.6
