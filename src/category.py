from src.product import Product


class Category:
    """Класс для представления категорий товаров с наименованием категорий,
       их описанием, списком продуктов"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


    def __repr__(self):
        """Метод для создания 'официального' строкового представления объекта"""
        return f"Category(name={self.name}, description={self.description}, products={self.products})"


    def add_product(self, product):
        """Метод для добавления и подсчета товара"""
        self.products.append(product)
        Category.product_count += 1
