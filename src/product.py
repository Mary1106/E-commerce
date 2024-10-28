from src.baseproduct import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        super().__init__()

    @classmethod
    def new_product(cls, product):
        """Класс-метод принимает на вход cls и продукт для создания в виде словаря. Возвращает экземпляр класса
        Product"""
        return cls(**product)

    @property
    def price(self):
        """Геттер, возвращающий значение приватного атрибута __price"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер, изменяющий значение приватного атрибута __price"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self):
        """Магический метод; возвращает строку с информацией о продукте"""
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """Возвращает сумму произведений цены на количество двух продуктов одной категории, при этом не дает складывать
        два продукта из разных категорий"""
        if type(other) is type(self):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError
