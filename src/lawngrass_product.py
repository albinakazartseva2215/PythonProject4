from src.print_mixin import PrintMixin
from src.product import Product


class LawnGrass(Product, PrintMixin):
    """Kласс-наследник 'Трава газонная' от исходного класса Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Метод для инициализации экземпляра класса-наследника. Задаем значения атрибутам экземпляра."""
        super().__init__(name, description, price, quantity)  # наследуем атрибуты класса из класса-родителя
        self.country = country
        self.germination_period = germination_period
        self.color = color


    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
