from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base  # Import Base from the same package

# Association table for part-supplier relationship
part_supplier = Table(
    'part_supplier',
    Base.metadata,
    Column('part_id', Integer, ForeignKey('parts.id'), primary_key=True),
    Column('supplier_id', Integer, ForeignKey('suppliers.id'), primary_key=True)
)

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # Relationships
    parts = relationship("Part", back_populates="source_location")
    assembly_products = relationship("Product", back_populates="assembly_location")
    suppliers = relationship("Supplier", back_populates="location")

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'))

    # Relationships
    location = relationship("Location", back_populates="suppliers")
    parts = relationship("Part", secondary=part_supplier, back_populates="suppliers")

class Part(Base):
    __tablename__ = 'parts'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    delivery_time = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    source_location_id = Column(Integer, ForeignKey('locations.id'))

    # Relationships
    source_location = relationship("Location", back_populates="parts")
    suppliers = relationship("Supplier", secondary=part_supplier, back_populates="parts")
    products = relationship("ProductPart", back_populates="part")

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    total_cost = Column(Float, nullable=False)
    delivery_time = Column(String, nullable=False)
    assembly_location_id = Column(Integer, ForeignKey('locations.id'))

    # Relationships
    assembly_location = relationship("Location", back_populates="assembly_products")
    parts = relationship("ProductPart", back_populates="product")

    def calculate_price(self) -> float:
        """
        Calculate the retail price of the product based on the sum of all parts' prices
        plus a markup percentage.
        
        Returns:
            float: The calculated retail price
        """
        markup_percentage = 0.25  # 25% markup
        parts_total = sum(part.part.price * part.quantity for part in self.parts)
        return parts_total * (1 + markup_percentage)

class ProductPart(Base):
    __tablename__ = 'product_parts'

    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    part_id = Column(Integer, ForeignKey('parts.id'), primary_key=True)
    quantity = Column(Integer, nullable=False, default=1)

    # Relationships
    product = relationship("Product", back_populates="parts")
    part = relationship("Part", back_populates="products") 