import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify, request
from flask_cors import CORS
from shared.database import get_db
from repository import ProductRepository
from sqlalchemy.orm import Session
import json

app = Flask(__name__)
CORS(app)

def get_product_repository():
    db = next(get_db())
    return ProductRepository(db)

@app.route('/api/products', methods=['GET'])
def get_products():
    print("Getting products...")
    repo = get_product_repository()
    products = repo.get_all_products()
    print(f"Found {len(products)} products")
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'totalCost': product.total_cost,
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
    repo = get_product_repository()
    product = repo.get_product(int(product_id))
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'totalCost': product.total_cost,
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