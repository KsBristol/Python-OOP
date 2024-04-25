"""
Создайте дата-класс Product, который хранит информацию о названии продукта и о его
цене. При выводе товара должна отображаться только информация о его имени.
Затем создайте класс продуктовой корзины Cart, в котором должна быть реализована возможность:
добавлять товары в корзины при помощи метода add_product. Добавляется один продукт за один вызов метода
посчитать общую сумму содержащихся товаров в корзине при помощи метода get_total
возможность применить скидку через apply_discount. Данный метод должен принимать размер скидки -
целое число от 1 до 100, обозначающее % от цены, и сохраняет его в экземпляре класса. Если
передать любое другое значение, то нужно вызывать исключение. Данный метод возвращать ничего не должен
raise ValueError('Неправильное значение скидки')

Пришли сотрудники отдела продаж и решили добавить возможность работы продуктовой корзины с промокодами
Для этого нужно создать дата-класс Promo, который содержит код промокода и значение его скидки.
Примечание: в реальных приложениях используется база данных для хранения всех активных промокодов,
у нас ее нет, поэтому давайте договоримся, что все активные промокоды будут находиться в глобальной
переменной ACTIVE_PROMO.
Проверьте, чтобы значение скидки было целым числом и находилось в пределах от 1 до 100,
обозначает % от цены. При всех остальных значениях будем считать, что промокод не дает скидку
(как вариант,  можете указать, что значение скидки составляет 0)

Далее вам понадобиться добавить метод apply_promo в классе Cart, который получает на вход код
промокода и заведен  ли в переменной ACTIVE_PROMO промокод с таким названием. Если существует,
то необходимо применить его номинал к корзине товаров. Сам метод apply_promo ничего не возвращает,
только печатает текст "Промокод <promo> успешно применился" или "Промокода <promo> не существует"

А вот при вызове метода get_total должен учитываться промокод или скидка, если они были применены.

ACTIVE_PROMO = [
    Promo('new', 20),
    Promo('all_goods', 30),
]

product1 = Product('Книга', 100.0)
product2 = Product('Флешка', 50.0)
product3 = Product('Ручка', 10.0)
print(product1, product2, product3)

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
print(cart.get_total())

# Применение промокода в 30%
cart.apply_promo('all_goods')
# Применение скидки в 10%. Промокод должен отмениться
cart.apply_discount(10)
print(cart.get_total())
Sample Output 2:

Product(name='Книга') Product(name='Флешка') Product(name='Ручка')
160.0
Промокод all_goods успешно применился
144.0
"""

from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float = field(repr=False)


@dataclass
class Cart:
    summ: float = field(repr=False, init=False)
    discount: int = field(repr=False, init=False, default=1)
    basket: list = field(repr=False, init=False, default_factory=list)

    def add_product(self, product):
        self.basket.append(product)

    def get_total(self):
        self.summ = 0

        for i in self.basket:
            self.summ += i.price

        if self.discount == 1:
            return self.summ
        else:
            return self.summ - self.discount * self.summ

    def apply_discount(self, discount_p):
        if type(discount_p) != int or discount_p < 1 or discount_p > 100:
            raise ValueError('Неправильное значение скидки')
        else:
            self.discount = discount_p / 100

    def apply_promo(self, kod_promo):
        # ACTIVE_PROMO= [Promo(kod_promo='new', discount_kod_promo=20),
        # Promo(kod_promo='all_goods', discount_kod_promo=30)]

        for i in ACTIVE_PROMO:
            itog = []
            if kod_promo == i.kod_promo:
                itog.append(i.discount_kod_promo)

        if len(itog) == 1:
            self.discount = itog[0] / 100
            print(f'Промокод {kod_promo} успешно применился')
        else:
            print(f'Промокода {kod_promo} не существует')


@dataclass
class Promo:
    kod_promo: str
    discount_kod_promo: int = field(default=1)

    @staticmethod
    def check_disc(disc_new):
        if type(disc_new) != int or disc_new < 1 or disc_new > 100:
            raise ValueError('Неправильное значение скидки')
        else:
            return disc_new

    def __post_init__(self):
        self.discount_kod_promo = self.check_disc(self.discount_kod_promo)


ACTIVE_PROMO = [
    Promo('new', 20),
    Promo('all_goods', 30),
]

product1 = Product('Книга', 100.0)
product2 = Product('Флешка', 50.0)
product3 = Product('Ручка', 10.0)
print(product1, product2, product3)

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
print(cart.get_total())

# Применение несуществующего промокода
cart.apply_promo('goods')
print(cart.get_total())

# Product(name='Книга') Product(name='Флешка') Product(name='Ручка')
# 160.0
# Промокода goods не существует
# 160.0

