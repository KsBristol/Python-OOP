from string import ascii_letters


class Registration:
    """Будет проверять только введенный логин И пароль. Под логином мы будем
    подразумевать почту пользователя"""

    def __init__(self, login, password):

        self.__login = None
        self.login = login

        self.__password = None
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        """Проверка логина"""
        if not isinstance(login, str):
            raise TypeError('Логин должен быть строкой')
        else:
            if login.count('@') != 1:
                raise ValueError(f"Логин {login} должен содержать один символ '@'")
            else:
                if login.split('@')[-1].count('.') != 1:
                    raise ValueError(f"В логине {login} должна быть '.' после символа '@'")
                else:
                    self.__login = login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        """Проверка пароля"""
        if not isinstance(password, str):
            raise TypeError('Пароль должен быть строкой')
        else:
            if not 4 < len(password) < 12:
                raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
            else:
                if not self.is_include_digit(password):
                    raise ValueError('Пароль должен содержать хотя бы одну цифру')
                else:
                    if not self.is_include_all_register(password):
                        raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
                    else:
                        if not self.is_include_only_latin(password):
                            raise ValueError('Пароль должен содержать только латинский алфавит')
                        else:
                            if self.check_password_dictionary(password):
                                raise ValueError('Ваш пароль содержится в списке самых легких')
                            else:
                                self.__password = password

    @staticmethod
    def is_include_digit(password):
        """Новый пароль должен содержать хотя бы одну цифру. Проверяем наличие цифр.
        В случае отсутствия цифрового символа в сеттере будем вызывать исключение:
        ValueError('Пароль должен содержать хотя бы одну цифру')"""
        for i in '0123456789':
            if i in password:
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        """Новый пароль должен содержать элементы верхнего и нижнего регистра.
        Проверяем элементы строчки на регистр. В случае ошибки в сеттере будем вызывать:
        ValueError ('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')"""
        for i in ascii_letters:
            if i in password:
                return True
        return False

    @staticmethod
    def is_include_only_latin(password):
        """Новый пароль должен содержать только латинские символы.
        Проверяем каждый элемент пароля на принадлежность к латинскому алфавиту
        (проверка должна быть как в верхнем, так и нижнем регистре). В случае,
        если встретится нелатинский символ, вызвать ошибку ValueError('Пароль
        должен содержать только латинский алфавит')."""
        prov = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        for i in prov:
            if i not in password:
                return True
        return False

    @staticmethod
    def check_password_dictionary(password):
        """Пароль не должен совпадать ни с одним из легких паролей,
        хранящихся в файле easy_passwords.txt. Проверяем наличие нашего пароля в
        данном файле. Если значение совпадет со значением из файла, то в сеттере вызываем
        исключение: ValueError('Ваш пароль содержится в списке самых легких')"""
        with open('easy_passwords.txt') as f:
            prov = f.read().split('\n')

        return password in prov


# Ниже код для проверки класса Registration

try:
    s2 = Registration("fga", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")

try:
    s2 = Registration("fg@a", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")

s2 = Registration("translate@gmail.com", "as1SNdf")
try:
    s2.login = "asdsa12asd."
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12asd как можно записать такой логин?")

try:
    s2.login = "asdsa12@asd"
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12@asd как можно записать такой логин?")

assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "KissasSAd1f"
except ValueError as e:
    pass
else:
    raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "124244242"
except ValueError as e:
    pass
else:
    raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "RYIWUhjkdbfjfgdsffds"
except ValueError as e:
    pass
else:
    raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "CaT"
except ValueError as e:
    pass
else:
    raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "monkey"
except ValueError as e:
    pass
else:
    raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

try:
    s2.password = "HelloQEWq"
except ValueError as e:
    pass
else:
    raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = [4, 32]
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

try:
    s2.password = 123456
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

print('U r hacked Pentagon')