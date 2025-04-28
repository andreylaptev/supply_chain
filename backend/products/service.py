from typing import List, Optional
from backend.shared.models import Product
from backend.products.repository import ProductRepository
import random

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_product(self, product_id: int) -> Optional[Product]:
        return self.repository.get_product(product_id)

    def get_all_products(self) -> List[Product]:
        return self.repository.get_all_products()

    def create_product(self, product_data: dict) -> Product:
        # Add random weight between 1 and 10 kg
        product_data['weight'] = round(random.uniform(1.0, 10.0), 2)
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

    def calculate_product_weight(self, product: Product) -> float:
        """
        Calculate the total weight of the product using the formula:
        weight = (sum_of_part_weights * 1.15) + (total_quantity * 0.3) + 0.75
        
        Where:
        - sum_of_part_weights: Sum of weights of all parts
        - total_quantity: Total quantity of all parts
        - 0.75: Weight of padding material
        
        Returns:
            float: The calculated product weight in kilograms
        """
        sum_of_part_weights = sum(part.part.weight * part.quantity for part in product.parts)
        total_quantity = sum(part.quantity for part in product.parts)
        padding_weight = 0.75  # kg
        
        total_weight = (sum_of_part_weights * 1.15) + (total_quantity * 0.3) + padding_weight
        return round(total_weight, 2)
    