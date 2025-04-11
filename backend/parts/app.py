import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify, request
from flask_cors import CORS
from shared.database import get_db
from repository import PartRepository
from sqlalchemy.orm import Session
import json

app = Flask(__name__)
CORS(app)

def get_part_repository():
    db = next(get_db())
    return PartRepository(db)

@app.route('/api/parts', methods=['GET'])
def get_parts():
    repo = get_part_repository()
    parts = repo.get_all_parts()
    return jsonify([{
        'id': part.id,
        'name': part.name,
        'deliveryTime': part.delivery_time,
        'weight': part.weight,
        'price': part.price,
        'sourceLocation': {
            'id': part.source_location.id,
            'name': part.source_location.name,
            'latitude': part.source_location.latitude,
            'longitude': part.source_location.longitude
        },
        'suppliers': [{
            'id': supplier.id,
            'name': supplier.name,
            'address': supplier.address,
            'phone': supplier.phone,
            'email': supplier.email,
            'location': {
                'id': supplier.location.id,
                'name': supplier.location.name,
                'latitude': supplier.location.latitude,
                'longitude': supplier.location.longitude
            }
        } for supplier in part.suppliers]
    } for part in parts])

@app.route('/api/parts/<part_id>', methods=['GET'])
def get_part(part_id):
    repo = get_part_repository()
    part = repo.get_part(int(part_id))
    
    if not part:
        return jsonify({'error': 'Part not found'}), 404
    
    return jsonify({
        'id': part.id,
        'name': part.name,
        'deliveryTime': part.delivery_time,
        'weight': part.weight,
        'price': part.price,
        'sourceLocation': {
            'id': part.source_location.id,
            'name': part.source_location.name,
            'latitude': part.source_location.latitude,
            'longitude': part.source_location.longitude
        },
        'suppliers': [{
            'id': supplier.id,
            'name': supplier.name,
            'address': supplier.address,
            'phone': supplier.phone,
            'email': supplier.email,
            'location': {
                'id': supplier.location.id,
                'name': supplier.location.name,
                'latitude': supplier.location.latitude,
                'longitude': supplier.location.longitude
            }
        } for supplier in part.suppliers]
    })

if __name__ == '__main__':
    app.run(port=5001) 