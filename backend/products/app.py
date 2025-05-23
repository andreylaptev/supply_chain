import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify, request
from flask_cors import CORS
from backend.shared.database import get_db
from backend.products.repository import ProductRepository
from backend.products.service import ProductService

app = Flask(__name__)
CORS(app)

def get_product_service():
    db = next(get_db())
    repository = ProductRepository(db)
    return ProductService(repository)

@app.route('/api/products', methods=['GET'])
def get_products():
    print("Getting products...")
    service = get_product_service()
    products = service.get_all_products()
    print(f"Found {len(products)} products")
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'totalCost': product.total_cost,
        'price': service.calculate_product_price(product),
        'weight': service.calculate_product_weight(product),
        'deliveryTime': product.delivery_time,
        'assemblyLocation': {
            'id': product.assembly_location.id,
            'name': product.assembly_location.name,
            'latitude': product.assembly_location.latitude,
            'longitude': product.assembly_location.longitude
        },
        'parts': [{
            'id': part.part.id,
            'name': part.part.name,
            'deliveryTime': part.part.delivery_time,
            'weight': part.part.weight,
            'price': part.part.price,
            'sourceLocation': {
                'id': part.part.source_location.id,
                'name': part.part.source_location.name,
                'latitude': part.part.source_location.latitude,
                'longitude': part.part.source_location.longitude
            }
        } for part in product.parts]
    } for product in products])

@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    service = get_product_service()
    product = service.get_product(int(product_id))
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'totalCost': product.total_cost,
        'price': service.calculate_product_price(product),
        'weight': service.calculate_product_weight(product),
        'deliveryTime': product.delivery_time,
        'assemblyLocation': {
            'id': product.assembly_location.id,
            'name': product.assembly_location.name,
            'latitude': product.assembly_location.latitude,
            'longitude': product.assembly_location.longitude
        },
        'parts': [{
            'id': part.part.id,
            'name': part.part.name,
            'deliveryTime': part.part.delivery_time,
            'weight': part.part.weight,
            'price': part.part.price,
            'sourceLocation': {
                'id': part.part.source_location.id,
                'name': part.part.source_location.name,
                'latitude': part.part.source_location.latitude,
                'longitude': part.part.source_location.longitude
            }
        } for part in product.parts]
    })

if __name__ == '__main__':
    app.run(port=5000) 