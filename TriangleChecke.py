"""
Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было
бы создавать командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.

В классе TriangleChecker необходимо объявить метод is_triangle(),
который бы возвращал следующие коды:

1 - если хотя бы одна сторона не число (не float или int) или хотя
бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.

Прочитайте из входного потока строку, содержащую три числа, разделенных
пробелами, командой:

a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные
значения a, b, c. Вызовите метод is_triangle() из объекта tr и выведите результат
на экран (код, который она вернет).

Sample Input:

3 4 5
Sample Output:

3
"""


class TriangleChecker:
    def __init__(self, a, b, c):
        """
        :param a: длина стороны a
        :param b: длина стороны b
        :param c: длина стороны c
        """
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        """
        :return:
        1 - если хотя бы одна сторона не число (не float или int) или хотя
        бы одно число меньше или равно нулю;
        2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
        3 - стороны a, b, c образуют треугольник.
        """
        # if isinstance(self.a, float | int) is False or\
        #         isinstance(self.b, float | int) is False or\
        #         isinstance(self.c, float | int) is False or\
        #         self.a <= 0 or self.b <= 0 or self.c <= 0:
        #     return 1
        if type(self.a) not in (int, float) or\
                type(self.b) not in (int, float) or\
                type(self.c) not in (int, float) or \
                self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 1
        elif self.a >= (self.c + self.b) or\
                self.b >= (self.a + self.c) or\
                self.c >= (self.a + self.b):
            return 2
        else:
            return 3


a, b, c = map(int, input().split())


tr = TriangleChecker(a, b, c)
print(tr.is_triangle())