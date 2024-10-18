import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство...",
        products=[
            Product(name="Samsung Galaxy C23 Ultra",
                    description="256GB, Серый цвет, 200MP камера",
                    price=180000.0,
                    quantity=5),
            Product(name="Iphone 15",
                    description="512GB, Gray space",
                    price=210000.0,
                    quantity=8)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет...",
        products=[
            Product(name="'55' QLED 4K",
                    description="Фоновая подсветка",
                    price=123000.0,
                    quantity=7),
        ]
    )


@pytest.fixture
def product():
    return Product(name="'55' QLED 4K", description="Фоновая подсветка", price=123000.0, quantity=7)
