
def test_smartphone_init(first_smartphone, second_smartphone):
    assert first_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert first_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert first_smartphone.quantity == 5
    assert first_smartphone.price == 180000.0
    assert first_smartphone.color == "Серый"
    assert first_smartphone.memory == 256
    assert first_smartphone.model == "S23 Ultra"
    assert first_smartphone.efficiency == 95.5
    assert second_smartphone.name == "Iphone 15"
    assert second_smartphone.description == "512GB, Gray space"
    assert second_smartphone.quantity == 8
    assert second_smartphone.price == 210000.0
    assert second_smartphone.color == "Gray space"
    assert second_smartphone.memory == 512
    assert second_smartphone.model == "15"
    assert second_smartphone.efficiency == 98.2
