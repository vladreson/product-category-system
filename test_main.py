import pytest
from main import Product, Category


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def another_product():
    return Product("Another Product", "Another Description", 200.0, 5)


@pytest.fixture
def sample_category(sample_product, another_product):
    return Category("Test Category", "Test Description", [sample_product, another_product])


def test_product_str(sample_product):
    assert str(sample_product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_category_str(sample_category):
    assert str(sample_category) == "Test Category, количество продуктов: 15 шт."


def test_product_addition(sample_product, another_product):
    assert sample_product + another_product == 100.0 * 10 + 200.0 * 5


def test_invalid_addition(sample_product):
    with pytest.raises(TypeError):
        sample_product + "Not a product"


def test_category_products_property(sample_category):
    expected_output = "Test Product, 100.0 руб. Остаток: 10 шт.\nAnother Product, 200.0 руб. Остаток: 5 шт."
    assert sample_category.products == expected_output


def test_empty_category():
    empty_category = Category("Empty", "No products", [])
    assert str(empty_category) == "Empty, количество продуктов: 0 шт."
    assert empty_category.products == ""
