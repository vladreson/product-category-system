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


def test_price_setter(sample_product):
    sample_product.price = 150.0
    assert sample_product.price == 150.0
    sample_product.price = -10  # Должно вывести сообщение об ошибке
    assert sample_product.price == 150.0  # Цена не должна измениться


def test_new_product():
    product_data = {
        "name": "New Product",
        "description": "New Description",
        "price": 200.0,
        "quantity": 5
    }
    product = Product.new_product(product_data)
    assert product.name == "New Product"
    assert product.price == 200.0


def test_category_init(sample_category, sample_product):
    assert sample_category.name == "Test Category"
    assert len(sample_category.products_list) == 1
    assert sample_category.products_list[0] == sample_product


def test_add_product(sample_category):
    initial_count = Category.product_count
    new_product = Product("New", "Desc", 50.0, 3)
    sample_category.add_product(new_product)
    assert len(sample_category.products_list) == 2
    assert Category.product_count == initial_count + 1


def test_products_property(sample_category, sample_product):
    expected_output = f"{sample_product.name}, {sample_product.price} руб. Остаток: {sample_product.quantity} шт."
    assert sample_category.products == expected_output