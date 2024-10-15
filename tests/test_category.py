
def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство..."
    assert len(first_category.products) == 2
    assert second_category.name == 'Телевизоры'
    assert second_category.description == "Современный телевизор, который позволяет..."
    assert len(second_category.products) == 1
    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert first_category.product_count == 3
    assert second_category.product_count == 3
