import pytest
from main import BaseProduct, Product, Smartphone, LawnGrass, Category


def test_base_product_is_abstract():
    """Проверка, что BaseProduct действительно абстрактный"""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Test", 100.0, 10)


def test_product_creation_logging(capsys):
    """Проверка логирования создания продукта"""
    _ = Product("Test", "Description", 100.0, 5)  # Используем _ для неиспользуемой переменной
    captured = capsys.readouterr()
    assert "Создание объекта Product с параметрами:" in captured.out
    assert "'name': 'Test'" in captured.out
    assert "'price': 100.0" in captured.out


def test_smartphone_inheritance():
    """Проверка наследования Smartphone"""
    smartphone = Smartphone("iPhone", "Smartphone", 1000.0, 10, 95.0, "13", 256, "Black")
    assert isinstance(smartphone, Product)
    assert smartphone.model == "13"
    assert str(smartphone) == "iPhone, 1000.0 руб. Остаток: 10 шт."


def test_lawn_grass_inheritance():
    """Проверка наследования LawnGrass"""
    grass = LawnGrass("Grass", "Green", 50.0, 100, "Russia", "14 days", "Green")
    assert isinstance(grass, Product)
    assert grass.country == "Russia"
    assert str(grass) == "Grass, 50.0 руб. Остаток: 100 шт."


def test_category_add_product():
    """Проверка добавления продукта в категорию"""
    category = Category("Test", "Test category")
    product = Product("Test", "Test", 100.0, 5)
    category.add_product(product)
    assert "Test, 100.0 руб. Остаток: 5 шт." in category.products


def test_category_add_invalid_product():
    """Проверка обработки неверного типа продукта"""
    category = Category("Test", "Test category")
    with pytest.raises(TypeError):
        category.add_product("Not a product")


def test_product_str_representation():
    """Проверка строкового представления продукта"""
    product = Product("Test", "Test", 100.0, 5)
    assert str(product) == "Test, 100.0 руб. Остаток: 5 шт."
