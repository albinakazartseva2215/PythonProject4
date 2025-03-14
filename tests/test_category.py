import pytest

from src.category import Category
from src.exceptions import ZeroProductPrice
from src.product import Product


def test_category_init(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert category_1.category_count == 1
    assert category_1.product_count == 3

    assert category_2.name == "Телевизоры"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_2.category_count == 1
    assert category_2.product_count == 1


def test_category_add_product(category_1, product_3):
    category_1.add_product(product_3)
    assert category_1.product_count == 3


def test_products(category_2):
    assert category_2.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'


def test_category_str(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 27 шт."


def test_category_add_product_smartphone_product(category_1, smartphone_product1):
    category_1.add_product(smartphone_product1)
    assert category_1.products_in_list[-1].name == "Samsung Galaxy S23 Ultra"


def test_category_add_product_error(category_1, product_1):
    with pytest.raises(TypeError):
        category_1.add_product(1) == 0


def test_middle_price(category_1, category_without_products):
    assert category_1.middle_price() == 140333.3
    assert category_without_products.middle_price() == 0


def test_custom_exception(category_1, product_invalid_quantity):
    # Проверяем начальное состояние
    assert len(category_1.products_in_list) == 3

    with pytest.raises(ValueError) as exc_info:
        category_1.add_product(Product(*product_invalid_quantity))
        assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"