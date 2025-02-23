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
        self.__products = products if products else []
        self.category_count += 1
        self.product_count += len(self.__products)

    def __repr__(self):
        """Метод для создания 'официального' строкового представления объекта"""
        return f"Category(name={self.name}, description={self.description}, products={self.products})"

    def add_product(self, product: Product):
        """Метод для добавления и подсчета товара"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер возвращает возможность просмотра приватного списка товаров"""
        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(products_list)


