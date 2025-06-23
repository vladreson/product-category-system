import pytest
from main import Product, Category


def test_product_zero_quantity():
    """Проверка создания продукта с нулевым количеством"""
    with pytest.raises(ValueError) as excinfo:
        Product("Test", "Test", 100.0, 0)
    assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)


def test_product_normal_creation():
    """Проверка создания продукта с нормальным количеством"""
    product = Product("Test", "Test", 100.0, 1)
    assert product.quantity == 1


def test_category_middle_price():
    """Проверка расчета средней цены"""
    product1 = Product("Prod1", "Desc1", 100.0, 2)
    product2 = Product("Prod2", "Desc2", 200.0, 3)
    category = Category("Test", "Test", [product1, product2])
    assert category.middle_price() == 150.0


def test_empty_category_middle_price():
    """Проверка расчета средней цены для пустой категории"""
    category = Category("Empty", "Empty")
    assert category.middle_price() == 0


def test_previous_functionality():
    """Проверка сохранения предыдущей функциональности"""
    product = Product("Test", "Test", 100.0, 1)
    category = Category("Test", "Test", [product])
    assert str(product) == "Test, 100.0 руб. Остаток: 1 шт."
    assert len(category.products.split('\n')) == 1
