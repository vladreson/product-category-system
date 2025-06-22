import pytest

from main import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def sample_smartphone():
    return Smartphone("iPhone", "Cool phone", 1000.0, 10, 95.5, "13 Pro", 256, "Black")


@pytest.fixture
def sample_lawn_grass():
    return LawnGrass("Grass", "Green grass", 50.0, 100, "Russia", "14 days", "Green")


def test_product_inheritance():
    assert issubclass(Smartphone, Product)
    assert issubclass(LawnGrass, Product)


def test_smartphone_attributes(sample_smartphone):
    assert sample_smartphone.model == "13 Pro"
    assert sample_smartphone.memory == 256


def test_lawn_grass_attributes(sample_lawn_grass):
    assert sample_lawn_grass.country == "Russia"
    assert sample_lawn_grass.germination_period == "14 days"


def test_valid_addition(sample_smartphone):
    smartphone2 = Smartphone("Samsung", "Android phone", 800.0, 5, 90.0, "S22", 128, "Blue")
    assert sample_smartphone + smartphone2 == 1000.0 * 10 + 800.0 * 5


def test_invalid_addition(sample_smartphone, sample_lawn_grass):
    with pytest.raises(TypeError):
        sample_smartphone + sample_lawn_grass


def test_category_add_product(sample_smartphone):
    category = Category("Phones", "Mobile phones")
    category.add_product(sample_smartphone)
    assert "iPhone" in category.products


def test_category_add_invalid_product():
    with pytest.raises(TypeError):
        category = Category("Test", "Test category")
        category.add_product("Not a product")


def test_category_counts():
    initial_products = Category.product_count
    initial_categories = Category.category_count

    smartphone = Smartphone("Xiaomi", "Chinese phone", 500.0, 20, 85.0, "Redmi", 64, "White")
    Category("Test", "Test category", [smartphone])

    assert Category.category_count == initial_categories + 1
    assert Category.product_count == initial_products + 1
