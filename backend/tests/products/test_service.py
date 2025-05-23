import pytest
from unittest.mock import Mock
from backend.products.service import ProductService
from backend.shared.models import Product, Part, ProductPart

@pytest.fixture
def product_service():
    repository = Mock()
    return ProductService(repository)

def test_calculate_product_weight(product_service):
    # Create mock parts
    part1 = Mock(spec=Part)
    part1.weight = 1.0

    part2 = Mock(spec=Part)
    part2.weight = 2.0

    # Create mock product parts with quantities
    product_part1 = Mock(spec=ProductPart)
    product_part1.part = part1
    product_part1.quantity = 2

    product_part2 = Mock(spec=ProductPart)
    product_part2.part = part2
    product_part2.quantity = 1

    # Create mock product
    product = Mock(spec=Product)
    product.parts = [product_part1, product_part2]

    # Expected weight calculation
    expected_weight = 6.25

    # Actual weight
    actual_weight = product_service.calculate_product_weight(product)

    # Assert
    assert actual_weight == expected_weight
