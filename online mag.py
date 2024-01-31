"""Имитация оформления заказа в онлайн магазине"""


class Product:
    """Класс, описывающий товар"""

    def __init__(self, name, price):
        """Название товара и стоимость"""
        self.name = name
        self.price = price


class User:
    """Класс, описывающий покупателя"""

    def __init__(self, login, balance=0):
        """Логин пользователя и баланс его счета (по умолчанию 0)"""
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.__balance}'

    @property
    def balance(self):
        """Возвращает значение баланса покупателя"""
        return self.__balance

    @balance.setter
    def balance(self, balance):
        """Устанавливает новое значение баланса покупателя"""
        self.__balance = balance

    def deposit(self, value):
        """Принимает числовое значение и прибавляет его к балансу покупателя"""
        self.__balance = self.__balance + value

    def payment(self, value):
        """Принимает числовое значение, которое должно списаться с баланса покупателя"""
        prov = self.__balance - value
        if prov < 0:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.__balance = self.__balance - value
            return True


class Cart:
    """Класс корзины, куда пользователь будет складывать товары"""

    def __init__(self, user):
        # экземпляр класса User
        self.user = user

        # пустой словарь для хранения товаров и их количества
        # (ключ словаря — товар, значение — количество)
        self.goods = {}

        # итоговая сумма заказа
        self.__total = 0

    def add(self, product, amount=1):
        """Метод принимает на вход экземпляр класса Product и количество товаров
        (amount = по умолчанию 1). Метод должен увеличивает в корзине количество
        указанного товара на переданное значение количества и пересчитывает итоговую сумму"""
        self.goods[product] = self.goods.get(product, 0) + amount
        self.__total = self.__total + product.price * amount

    def remove(self, product, amount=1):
        """Метод принимает на вход экземпляр класса Product и количество товаров
        (amount = по умолчанию 1). Метод должен уменьшает в корзине количество
        указанного товара на переданное значение количества и пересчитывает
        итоговую сумму заказа.
        """
        # Если количество товара в корзине меньше, чем просит удалить пользователь
        if amount > self.goods[product]:
            # удаляем товар полностью из корзины, а количество меняем на то,
            # что было в корзине.
            amount = self.goods[product]
            del self.goods[product]
            self.__total = self.__total - product.price * amount
        else:
            self.goods[product] = self.goods.get(product, 0) - amount
            self.__total = self.__total - product.price * amount

    @property
    def total(self):
        """Возвращает итоговую сумму заказа"""
        return self.__total

    def order(self):
        """Метод использует метод payment из класса User
        и передает в него итоговую сумму корзины. В случае, если средств
        пользователю хватило, выводит сообщение «Заказ оплачен», в противном случае -
        «Проблема с оплатой»"""

        if self.user.payment(self.__total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        sorted_lst = sorted(self.goods, key=lambda x: x.name)
        print('---Your check---')
        for elem in sorted_lst:
            if self.goods[elem] > 0:
                print(f"{elem.name} {elem.price} {self.goods[elem]} {self.goods[elem] * elem.price}")
        print(f'---Total: {self.__total}---')


# тесты
billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user)  # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total)  # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order()  # Заказ оплачен
print(cart_billy.user.balance)  # 20
