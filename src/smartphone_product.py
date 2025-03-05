from src.product import Product


class Smartphone(Product):
    """Kласс-наследник 'Смартфон' от исходного класса Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """Метод для инициализации экземпляра класса-наследника. Задаем значения атрибутам экземпляра."""
        super().__init__(name, description, price, quantity)  # наследуем атрибуты класса из класса-родителя
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

smartphone = Smartphone(
    name="iPhone 15",
    description="Смартфон с мощным процессором",
    price=999.0,
    quantity=10,
    efficiency=95.5,
    model="15 Pro",
    memory=256,
    color="Black",
)