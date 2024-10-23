
def test_lawngrass_init(first_lawn_grass, second_lawn_grass):
    assert first_lawn_grass.name == "Газонная трава"
    assert first_lawn_grass.description == "Элитная трава для газона"
    assert first_lawn_grass.price == 500.0
    assert first_lawn_grass.quantity == 20
    assert first_lawn_grass.country == "Россия"
    assert first_lawn_grass.germination_period == "7 дней"
    assert first_lawn_grass.color == "Зеленый"
    assert second_lawn_grass.name == "Газонная трава 2"
    assert second_lawn_grass.description == "Выносливая трава"
    assert second_lawn_grass.price == 450.0
    assert second_lawn_grass.quantity == 15
    assert second_lawn_grass.country == "США"
    assert second_lawn_grass.germination_period == "5 дней"
    assert second_lawn_grass.color == "Темно-зеленый"
