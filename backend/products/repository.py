from sqlalchemy.orm import Session
from backend.shared.models import Product, Part, Location
from typing import List, Optional

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_product(self, product_id: int) -> Optional[Product]:
        return self.db.query(Product).filter(Product.id == product_id).first()

    def get_all_products(self) -> List[Product]:
        print("Querying database for products...")
        products = self.db.query(Product).all()
        print(f"Found {len(products)} products in database")
        for product in products:
            print(f"Product: {product.name} (ID: {product.id})")
        return products

    def create_product(self, product_data: dict) -> Product:
        product = Product(**product_data)
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update_product(self, product_id: int, product_data: dict) -> Optional[Product]:
        product = self.get_product(product_id)
        if product:
            for key, value in product_data.items():
                setattr(product, key, value)
            self.db.commit()
            self.db.refresh(product)
        return product

    def delete_product(self, product_id: int) -> bool:
        product = self.get_product(product_id)
        if product:
            self.db.delete(product)
            self.db.commit()
            return True
        return False 