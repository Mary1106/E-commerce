
def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство..."
    assert second_category.name == 'Телевизоры'
    assert second_category.description == "Современный телевизор, который позволяет..."
    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert first_category.product_count == 3
    assert second_category.product_count == 3


def test_products_setter(first_category):
    assert first_category.products == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n')


def test_add_product(first_category, product):
    count_before_add = first_category.product_count
    first_category.add_product(product)
    assert first_category.product_count == count_before_add + 1


def test_magic_str(second_category):
    assert str(second_category) == 'Телевизоры, количество продуктов: 7 шт.'
