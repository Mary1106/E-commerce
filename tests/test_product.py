from src.product import Product


def test_product_init(product):
    assert product.name == "'55' QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_price_setter(product):
    product.price = -100
    assert product.price == 123000.0
    product.price = 0
    assert product.price == 123000.0
    product.price = 100
    assert product.price == 100


def test_price_getter(product):
    assert product.price == 123000.0


def test_new_product():
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
