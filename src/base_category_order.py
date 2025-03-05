from abc import ABC, abstractmethod

from src.product import Product


class BaseCategoryOrder(ABC):
    """Базовый абстрактный класс с именем BaseCategoryOrder, который станет родительским для клаccов Category и Order."""

    @abstractmethod
    def add_product(self, product: Product):
        pass
