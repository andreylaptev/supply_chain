from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy data
parts = [
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
    },
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
]

@app.route('/api/parts', methods=['GET'])
def get_parts():
    return jsonify(parts)

@app.route('/api/parts/<part_id>', methods=['GET'])
def get_part(part_id):
    part = next((p for p in parts if p['id'] == part_id), None)
    if part:
        return jsonify(part)
    return jsonify({'error': 'Part not found'}), 404

if __name__ == '__main__':
    app.run(port=5001) 