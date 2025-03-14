from src.base_category_order import BaseCategoryOrder
from src.exceptions import ZeroProductPrice
from src.product import Product


class Order(BaseCategoryOrder):
    """Класс «Заказ», в котором будет ссылка на то, какой товар был куплен, количество купленного товара,
    а также итоговая стоимость. В заказе может быть указан только один товар."""

    def __init__(self, product):
        self.product = product if product else []

    def add_product(self, product: Product) -> None:
        """Метод для добавления и подсчета товара"""
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroProductPrice("Нельзя добавлять товар с нулевым количеством")
            except ZeroProductPrice as e:
                print(str(e))
            else:
                self.product.quantity += product.quantity
                print("Товар добавлен успешно.")
            finally:
                print("Обработка добавления товара завершена.")

        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    def __str__(self):
        """Магический метод для строкового представления информации об объекте класса"""
        return f"товар: {self.product.name}, количество товара: {self.product.quantity} шт., стоимость товара: {self.product.price * self.product.quantity}"


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 3)
    order_product = Order(product1)
    print(str(order_product))
    order_product.add_product(product2)
    print(str(order_product))
