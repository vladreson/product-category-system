import pytest
from main import Product, Smartphone, LawnGrass, Category


def test_class_comparison_with_is():
    """Проверка сравнения классов с помощью is"""
    smartphone1 = Smartphone("Phone1", "Desc", 1000.0, 2, 90.0, "M1", 64, "Black")
    smartphone2 = Smartphone("Phone2", "Desc", 2000.0, 3, 95.0, "M2", 128, "White")
    grass = LawnGrass("Grass", "Green", 50.0, 10, "RU", "14d", "Green")

    # Проверка сложения объектов одного класса
    assert smartphone1.__class__ is smartphone2.__class__
    assert smartphone1 + smartphone2 == 1000 * 2 + 2000 * 3

    # Проверка ошибки при сложении разных классов
    with pytest.raises(TypeError) as e:
        smartphone1 + grass
    assert "Нельзя складывать товары разных классов" in str(e.value)


def test_category_add_product_with_is():
    """Проверка добавления в категорию с проверкой класса"""
    category = Category("Test", "Test")
    product = Product("Prod", "Desc", 100.0, 5)
    smartphone = Smartphone("Phone", "Desc", 1000.0, 2, 90.0, "M1", 64, "Black")

    # Проверка добавления разрешенных классов
    category.add_product(product)
    category.add_product(smartphone)
    assert len(category.products_list) == 2

    # Проверка ошибки при добавлении неразрешенного класса
    with pytest.raises(TypeError) as e:
        category.add_product("Not a product")
    assert "Можно добавлять только объекты Product" in str(e.value)
