from src.lawngrass_product import LawnGrass
from src.product import Product
from src.smartphone_product import Smartphone


class Category:
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

    def __str__(self) -> str:
        """Магический метод для строкового представления информации об объекте класса"""
        return f"{self.name}, количество продуктов: {self.quantity} шт."

    def __repr__(self) -> str:
        """Метод для создания 'официального' строкового представления объекта"""
        return f"Category(name={self.name}, description={self.description}, products={self.products})"

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
            self.__products.append(product)
            Category.product_count += 1

