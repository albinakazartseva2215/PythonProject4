class Product:
    """Класс для представления товара с наименованием, описанием, ценой, количеством"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        return (
            f"Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"
        )

    @classmethod
    def new_product(cls, dict_product: dict, products=None):
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

    @property
    def price(self):
        """Геттер возвращает возможность просмотра цены товара"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер возвращает сообщение, если цена нулевая или отрицательная"""
        self.__price = new_price
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
