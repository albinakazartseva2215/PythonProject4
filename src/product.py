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
        self.price = price
        self.quantity = quantity


    def __repr__(self):
        return f"Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"
