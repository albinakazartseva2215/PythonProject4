from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс с именем BaseProduct, который станет родительским для класса продуктов."""

    def __init__(self, *args, **kwargs):
        super().__init__()  # Для совместимости с миксинами и другими классам

    @abstractmethod
    def __add__(self, other):
        pass
