from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy data
products = [
    {
        "id": "1",
        "name": "Laptop",
        "parts": [
            {
                "id": "1",
                "name": "CPU",
                "deliveryTime": "5 days",
                "weight": 0.1,
                "price": 299.99,
                "sourceLocation": {
                    "id": "1",
                    "name": "Intel Factory",
                    "latitude": 45.5155,
                    "longitude": -122.6789
                }
            },
            {
                "id": "2",
                "name": "RAM",
                "deliveryTime": "3 days",
                "weight": 0.05,
                "price": 89.99,
                "sourceLocation": {
                    "id": "2",
                    "name": "Samsung Factory",
                    "latitude": 37.5665,
                    "longitude": 126.9780
                }
            }
        ],
        "assemblyLocation": {
            "id": "3",
            "name": "Main Assembly Plant",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
    },
    {
        "id": "2",
        "name": "Smartphone",
        "parts": [
            {
                "id": "3",
                "name": "Screen",
                "deliveryTime": "4 days",
                "weight": 0.2,
                "price": 199.99,
                "sourceLocation": {
                    "id": "4",
                    "name": "LG Display",
                    "latitude": 37.5665,
                    "longitude": 126.9780
                }
            },
            {
                "id": "4",
                "name": "Battery",
                "deliveryTime": "3 days",
                "weight": 0.15,
                "price": 49.99,
                "sourceLocation": {
                    "id": "5",
                    "name": "Samsung Battery Plant",
                    "latitude": 37.5665,
                    "longitude": 126.9780
                }
            }
        ],
        "assemblyLocation": {
            "id": "6",
            "name": "Phone Assembly Plant",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
    }
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(port=5000) 