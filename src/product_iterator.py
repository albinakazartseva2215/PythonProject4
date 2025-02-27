from src.category import Category
from src.product import Product


class ProductIterator:
    """Вспомогательный класс, с помощью которого можно перебирать товары одной категории"""

    def __init__(self, category_obj):
        if not isinstance(category_obj.products_in_list, list):
            raise ValueError("Список продуктов должен быть list")
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        """Возвращает итератор."""
        self.index = 0
        return self

    def __next__(self):
        """Магический метод возвращает следующий товар из списка товаров категории"""
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration("Нет больше продуктов")


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    iterator = ProductIterator(category1)
    for product in iterator:
        print(product)
