from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для представления товара с наименованием, описанием, ценой, количеством"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity=0) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


    @classmethod
    def new_product(cls, dict_product: dict, products=None) -> object:
        """Класс-метод, который принимает на вход параметры товара в словаре
        и возвращает созданный объект класса Product"""
        name_pr = dict_product["name"]
        description_pr = dict_product["description"]
        price_pr = dict_product["price"]
        quantity_pr = dict_product["quantity"]

        if products:
            for product in products:
                if product.name == name_pr:
                    product.quantity += quantity_pr
                    product.price = max(product.__price, price_pr)
                    return product

        return cls(name_pr, description_pr, price_pr, quantity_pr)

    def total_cost(self) -> float:
        return self.price * self.quantity

    @property
    def price(self) -> float:
        """Геттер возвращает возможность просмотра цены товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> str:
        """Сеттер возвращает сообщение, если цена нулевая или отрицательная"""
        self.__price = new_price
        if self.__price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            self.__price = ""

    def __add__(self, other) -> float:
        """Магический метод позволяет суммировать произведение количества товара на стоимость"""
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
