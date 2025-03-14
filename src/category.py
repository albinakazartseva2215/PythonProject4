from itertools import product

from src.base_category_order import BaseCategoryOrder
from src.exceptions import ZeroProductPrice
from src.lawngrass_product import LawnGrass
from src.print_mixin import PrintMixin
from src.product import Product
from src.smartphone_product import Smartphone


class Category(BaseCategoryOrder, PrintMixin):
    """Класс для представления категорий товаров с наименованием категорий,
    их описанием, списком продуктов"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0
    quantity = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        self.category_count += 1
        self.product_count += len(self.__products) if products else 0
        for product in self.__products:
            self.quantity += product.quantity
        super().__init__()

    def __str__(self) -> str:
        """Магический метод для строкового представления информации об объекте класса"""
        return f"{self.name}, количество продуктов: {self.quantity} шт."


    @property
    def products(self) -> str:
        """Геттер возвращает возможность просмотра приватного списка товаров"""
        products_list = []
        for product in self.__products:
            products_list.append(str(product))
        return "\n".join(products_list)


    @property
    def products_in_list(self) -> list:
        """Геттер возвращает возможность просмотра приватного списка товаров типа list для итерации"""
        return self.__products


    def get_products(self) -> list:
        """Возвращает приватный атрибут __products."""
        return self.__products


    def add_product(self, product: Product) -> None:
        """Метод для добавления и подсчета товара"""
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroProductPrice("Нельзя добавлять товар с нулевым количеством")
            except ZeroProductPrice as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар добавлен успешно.")
            finally:
                print("Обработка добавления товара завершена.")
        else:
            raise TypeError("Можно добавлять только объекты класса Product")


    def middle_price(self):
        """Метод, который подсчитывает средний ценник всех товаров"""
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 1)
        except ZeroDivisionError:
            return 0
