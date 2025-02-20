import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> list[dict]:
    """Функция читает json-файл"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    """Функция создает объекты классов"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            name = product["name"]
            description = product["description"]
            price = product["price"]
            quantity = product["quantity"]
            name_product = Product(name=name, description=description, price=price, quantity=quantity)
            products.append(name_product)
        name = category["name"]
        description = category["description"]

        categories.append(Category(name=name, description=description, products=products))
    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    category_data = create_objects_from_json(raw_data)
    print(raw_data)
    print(category_data)
    print(category_data[1].description)
    print(category_data[1].category_count)
