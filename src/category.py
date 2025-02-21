from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """

        :rtype: object
        """
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


    # def __str__(self):
    #     return Category(name=self.name, description=self.description, products=self.products)


    def __repr__(self):
        return f"Category(name={self.name}, description={self.description}, products={self.products})"


    def add_product(self, product):
        self.products.append(product)
        Category.product_count += 1
