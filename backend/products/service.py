from typing import List, Optional
from shared.models import Product
from repository import ProductRepository

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_product(self, product_id: int) -> Optional[Product]:
        return self.repository.get_product(product_id)

    def get_all_products(self) -> List[Product]:
        return self.repository.get_all_products()

    def create_product(self, product_data: dict) -> Product:
        return self.repository.create_product(product_data)

    def update_product(self, product_id: int, product_data: dict) -> Optional[Product]:
        return self.repository.update_product(product_id, product_data)

    def delete_product(self, product_id: int) -> bool:
        return self.repository.delete_product(product_id)

    def calculate_product_price(self, product: Product) -> float:
        """
        Calculate the retail price of the product based on total cost and markup percentage.
        The markup percentage is set to 20% by default.
        
        Returns:
            float: The calculated retail price
        """
        markup_percentage = 0.2  # 20% markup
        return product.total_cost * (1 + markup_percentage)
    