import pytest
from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство...",
        products=[
            Product(
                name="Samsung Galaxy C23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=180000.0,
                quantity=5,
            ),
            Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет...",
        products=[
            Product(name="'55' QLED 4K", description="Фоновая подсветка", price=123000.0, quantity=7),
        ],
    )


@pytest.fixture
def product():
    return Product(name="'55' QLED 4K", description="Фоновая подсветка", price=123000.0, quantity=7)


@pytest.fixture
def product_dict():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def second_product():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def first_smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def second_smartphone():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def first_lawn_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def second_lawn_grass():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def empty_category():
    return Category(name="Смартфоны", description="Смартфоны, как средство...", products=[])
