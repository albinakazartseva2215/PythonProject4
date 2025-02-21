class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    # def __str__(self):
    #     return f"Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"


    def __repr__(self):
        return f"Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"
