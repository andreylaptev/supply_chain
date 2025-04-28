from .database import SessionLocal
from .models import Location, Part, Product, Supplier, ProductPart
from sqlalchemy.orm import Session

def seed_database():
    db = SessionLocal()
    
    try:
        # Create locations
        locations = [
            Location(name="Intel Factory", latitude=45.5155, longitude=-122.6789),
            Location(name="Samsung Factory", latitude=37.5665, longitude=126.9780),
            Location(name="Main Assembly Plant", latitude=37.7749, longitude=-122.4194),
            Location(name="LG Display", latitude=37.5665, longitude=126.9780),
            Location(name="Samsung Battery Plant", latitude=37.5665, longitude=126.9780),
            Location(name="ASUS Factory", latitude=25.0330, longitude=121.5654),
            Location(name="NVIDIA Factory", latitude=37.4419, longitude=-122.1430),
            Location(name="Western Digital Factory", latitude=37.7749, longitude=-122.4194),
            Location(name="Corsair Factory", latitude=37.7749, longitude=-122.4194),
            Location(name="Desktop Assembly Plant", latitude=37.7749, longitude=-122.4194),
            Location(name="Tablet Assembly Plant", latitude=37.7749, longitude=-122.4194),
            Location(name="Wearable Assembly Plant", latitude=37.7749, longitude=-122.4194),
            Location(name="Gaming Console Assembly Plant", latitude=37.7749, longitude=-122.4194),
            Location(name="TV Assembly Plant", latitude=37.7749, longitude=-122.4194)
        ]
        
        for location in locations:
            db.add(location)
        db.commit()
        
        # Create suppliers
        suppliers = [
            Supplier(
                name="Intel Corporation",
                address="2200 Mission College Blvd, Santa Clara, CA 95054",
                phone="+1 (408) 765-8080",
                email="supplier.relations@intel.com",
                location_id=1
            ),
            Supplier(
                name="Samsung Electronics",
                address="129 Samsung-ro, Yeongtong-gu, Suwon-si, Gyeonggi-do, South Korea",
                phone="+82 2 2053 3000",
                email="supplier.relations@samsung.com",
                location_id=2
            ),
            Supplier(
                name="LG Display",
                address="LG Twin Towers, 20 Yeouido-dong, Yeongdeungpo-gu, Seoul, South Korea",
                phone="+82 2 3777 1114",
                email="supplier.relations@lgdisplay.com",
                location_id=4
            ),
            Supplier(
                name="ASUS",
                address="No. 15, Li-Te Rd., Beitou Dist., Taipei City 112, Taiwan",
                phone="+886 2 2894 3447",
                email="supplier.relations@asus.com",
                location_id=6
            ),
            Supplier(
                name="NVIDIA Corporation",
                address="2788 San Tomas Expressway, Santa Clara, CA 95051",
                phone="+1 (408) 486-2000",
                email="supplier.relations@nvidia.com",
                location_id=7
            ),
            Supplier(
                name="Western Digital",
                address="5601 Great Oaks Parkway, San Jose, CA 95119",
                phone="+1 (408) 801-1000",
                email="supplier.relations@wdc.com",
                location_id=8
            ),
            Supplier(
                name="Corsair",
                address="47100 Bayside Parkway, Fremont, CA 94538",
                phone="+1 (510) 657-8747",
                email="supplier.relations@corsair.com",
                location_id=9
            )
        ]
        
        for supplier in suppliers:
            db.add(supplier)
        db.commit()
        
        # Create parts
        parts = [
            Part(
                name="CPU",
                delivery_time="5 days",
                weight=0.1,
                price=299.99,
                source_location_id=1
            ),
            Part(
                name="RAM",
                delivery_time="3 days",
                weight=0.05,
                price=89.99,
                source_location_id=2
            ),
            Part(
                name="Screen",
                delivery_time="4 days",
                weight=0.2,
                price=199.99,
                source_location_id=4
            ),
            Part(
                name="Battery",
                delivery_time="3 days",
                weight=0.15,
                price=49.99,
                source_location_id=5
            ),
            Part(
                name="Motherboard",
                delivery_time="6 days",
                weight=0.5,
                price=159.99,
                source_location_id=6
            ),
            Part(
                name="GPU",
                delivery_time="7 days",
                weight=0.3,
                price=499.99,
                source_location_id=7
            ),
            Part(
                name="Storage SSD",
                delivery_time="4 days",
                weight=0.08,
                price=129.99,
                source_location_id=8
            ),
            Part(
                name="Power Supply",
                delivery_time="5 days",
                weight=0.4,
                price=79.99,
                source_location_id=9
            )
        ]
        
        for part in parts:
            db.add(part)
        db.commit()
        
        # Create products
        products = [
            Product(
                name="Laptop",
                description="High-performance laptop for professionals",
                total_cost=1239.94,
                delivery_time="10 days",
                assembly_location_id=3,
                weight=2.5
            ),
            Product(
                name="Smartphone",
                description="Latest smartphone with advanced features",
                total_cost=639.96,
                delivery_time="8 days",
                assembly_location_id=3,
                weight=0.2
            ),
            Product(
                name="Desktop PC",
                description="High-end desktop computer for gaming and content creation",
                total_cost=1259.94,
                delivery_time="10 days",
                assembly_location_id=10,
                weight=8.0
            ),
            Product(
                name="Tablet",
                description="Versatile tablet for work and entertainment",
                total_cost=639.96,
                delivery_time="8 days",
                assembly_location_id=11,
                weight=0.5
            ),
            Product(
                name="Smartwatch",
                description="Advanced smartwatch with health monitoring features",
                total_cost=639.96,
                delivery_time="8 days",
                assembly_location_id=12,
                weight=0.05
            ),
            Product(
                name="Gaming Console",
                description="Next-generation gaming console for immersive gameplay",
                total_cost=1099.95,
                delivery_time="10 days",
                assembly_location_id=13,
                weight=4.5
            ),
            Product(
                name="Smart TV",
                description="4K smart TV with advanced streaming capabilities",
                total_cost=1219.95,
                delivery_time="10 days",
                assembly_location_id=14,
                weight=15.0
            )
        ]
        
        for product in products:
            db.add(product)
        db.commit()
        
        # Create product-part relationships
        product_parts = [
            # Laptop parts
            ProductPart(product_id=1, part_id=1, quantity=1),  # CPU
            ProductPart(product_id=1, part_id=2, quantity=2),  # RAM
            ProductPart(product_id=1, part_id=5, quantity=1),  # Motherboard
            ProductPart(product_id=1, part_id=6, quantity=1),  # GPU
            ProductPart(product_id=1, part_id=7, quantity=1),  # Storage SSD
            ProductPart(product_id=1, part_id=8, quantity=1),  # Power Supply
            
            # Smartphone parts
            ProductPart(product_id=2, part_id=1, quantity=1),  # CPU
            ProductPart(product_id=2, part_id=2, quantity=1),  # RAM
            ProductPart(product_id=2, part_id=3, quantity=1),  # Screen
            ProductPart(product_id=2, part_id=4, quantity=1),  # Battery
            
            # Desktop PC parts
            ProductPart(product_id=3, part_id=1, quantity=1),  # CPU
            ProductPart(product_id=3, part_id=2, quantity=4),  # RAM
            ProductPart(product_id=3, part_id=5, quantity=1),  # Motherboard
            ProductPart(product_id=3, part_id=6, quantity=1),  # GPU
            ProductPart(product_id=3, part_id=7, quantity=2),  # Storage SSD
            ProductPart(product_id=3, part_id=8, quantity=1),  # Power Supply
            
            # Tablet parts
            ProductPart(product_id=4, part_id=1, quantity=1),  # CPU
            ProductPart(product_id=4, part_id=2, quantity=1),  # RAM
            ProductPart(product_id=4, part_id=3, quantity=1),  # Screen
            ProductPart(product_id=4, part_id=4, quantity=1),  # Battery
            
            # Smartwatch parts
            ProductPart(product_id=5, part_id=1, quantity=1),  # CPU
            ProductPart(product_id=5, part_id=2, quantity=1),  # RAM
            ProductPart(product_id=5, part_id=3, quantity=1),  # Screen
            ProductPart(product_id=5, part_id=4, quantity=1),  # Battery
            
            # Gaming Console parts
            ProductPart(product_id=6, part_id=1, quantity=1),  # CPU
            ProductPart(product_id=6, part_id=2, quantity=2),  # RAM
            ProductPart(product_id=6, part_id=6, quantity=1),  # GPU
            ProductPart(product_id=6, part_id=7, quantity=1),  # Storage SSD
            ProductPart(product_id=6, part_id=8, quantity=1),  # Power Supply
            
            # Smart TV parts
            ProductPart(product_id=7, part_id=1, quantity=1),  # CPU
            ProductPart(product_id=7, part_id=2, quantity=1),  # RAM
            ProductPart(product_id=7, part_id=3, quantity=1),  # Screen
            ProductPart(product_id=7, part_id=6, quantity=1),  # GPU
            ProductPart(product_id=7, part_id=7, quantity=1),  # Storage SSD
        ]
        
        for product_part in product_parts:
            db.add(product_part)
        db.commit()
        
        print("Database seeded successfully!")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database() 