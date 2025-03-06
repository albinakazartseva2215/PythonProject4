from src.product import Product


def test_product_init(product_1, product_2):
    assert product_1.name == "Samsung Galaxy C23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5

    assert product_2.name == '55" QLED 4K'
    assert product_2.description == "Фоновая подсветка"
    assert product_2.price == 123000.0
    assert product_2.quantity == 7


def test_new_product(dict_new_product):
    result = Product.new_product(dict_new_product)
    assert result.price == 180000.0


def test_price_zero(capsys, product_5):
    product_5.price = 0
    massage = capsys.readouterr()
    assert massage.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_price(product_1):
    assert product_1.price == 180000.0


def test_total_cost(product_1):
    assert product_1.total_cost() == 900000.0


def test_str(product_1):
    assert str(product_1) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add(product_1, product_2):
    assert product_1 + product_2 == 1761000.0
