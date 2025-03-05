class PrintMixin:
    """Класс-миксин, который будет при создании объекта, то есть при работе метода __init__, печатать
    в консоль информацию о том, от какого класса и с какими параметрами был создан объект."""

    # def __init__(self):
        #print(repr(self))
    #
    # def __repr__(self):
    #     return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"

    # Получаем все атрибуты объекта

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Вызов __init__ родительского класса
        print(repr(self))

    def __repr__(self):
    # Получаем все атрибуты объекта
        attributes = []
        for key, value in self.__dict__.items():
            if isinstance(value, list):  # Если атрибут — это список
                # Рекурсивно вызываем repr для каждого элемента списка
                value_repr = [repr(item) for item in value]
                attributes.append(f"{value_repr}")
            else:
                attributes.append(f"{value!r}")
        return f"{self.__class__.__name__}({', '.join(attributes)})"
