import pytest
from main import Product, Category


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Test Description", [sample_product])


def test_product_init(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


def test_category_init(sample_category, sample_product):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Description"
    assert len(sample_category.products) == 1
    assert sample_category.products[0] == sample_product


def test_category_count():
    initial_count = Category.category_count
    Category("New Category", "Desc", [])
    assert Category.category_count == initial_count + 1


def test_product_count():
    initial_count = Category.product_count
    product = Product("P", "D", 1.0, 1)
    category = Category("C", "D", [product])
    assert Category.product_count == initial_count + 1
    assert len(category.products) == 1
    assert category.products[0].name == "P"
