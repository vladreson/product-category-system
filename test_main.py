import pytest
from main import Product, Category


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Test Description", [sample_product])


def test_private_price_attribute(sample_product):
    # Проверка, что атрибут действительно приватный
    with pytest.raises(AttributeError):
        sample_product.__price


def test_price_getter_setter(sample_product):
    assert sample_product.price == 100.0  # Проверка геттера
    sample_product.price = 150.0
    assert sample_product.price == 150.0  # Проверка сеттера
    sample_product.price = -10  # Должно вывести сообщение об ошибке
    assert sample_product.price == 150.0  # Цена не должна измениться


def test_add_product_type_check(sample_category):
    class FakeProduct: pass

    with pytest.raises(TypeError):
        sample_category.add_product(FakeProduct())  # Неправильный тип
    with pytest.raises(TypeError):
        sample_category.add_product("not a product")  # Неправильный тип

    # Проверка добавления настоящего продукта
    initial_count = len(sample_category.products_list)
    new_product = Product("Valid", "Product", 50.0, 3)
    sample_category.add_product(new_product)
    assert len(sample_category.products_list) == initial_count + 1


def test_new_product_classmethod():
    product_data = {
        "name": "New Product",
        "description": "New Description",
        "price": 200.0,
        "quantity": 5
    }
    product = Product.new_product(product_data)
    assert isinstance(product, Product)
    assert product.name == "New Product"


def test_products_property_formatting(sample_category, sample_product):
    expected_output = f"{sample_product.name}, {sample_product.price} руб. Остаток: {sample_product.quantity} шт."
    assert sample_category.products == expected_output