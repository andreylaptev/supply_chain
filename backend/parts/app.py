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
        },
        "suppliers": [
            {
                "id": "1",
                "name": "Intel Corporation",
                "location": {
                    "id": "1",
                    "name": "Intel Factory",
                    "latitude": 45.5155,
                    "longitude": -122.6789
                },
                "address": "2200 Mission College Blvd, Santa Clara, CA 95054",
                "phone": "+1 (408) 765-8080",
                "email": "supplier.relations@intel.com"
            }
        ]
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
        },
        "suppliers": [
            {
                "id": "2",
                "name": "Samsung Electronics",
                "location": {
                    "id": "2",
                    "name": "Samsung Factory",
                    "latitude": 37.5665,
                    "longitude": 126.9780
                },
                "address": "129 Samsung-ro, Yeongtong-gu, Suwon-si, Gyeonggi-do, South Korea",
                "phone": "+82 2 2053 3000",
                "email": "supplier.relations@samsung.com"
            }
        ]
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
        },
        "suppliers": [
            {
                "id": "3",
                "name": "LG Display",
                "location": {
                    "id": "4",
                    "name": "LG Display",
                    "latitude": 37.5665,
                    "longitude": 126.9780
                },
                "address": "128 Yeoui-daero, Yeongdeungpo-gu, Seoul, South Korea",
                "phone": "+82 2 3777 1114",
                "email": "supplier.relations@lgdisplay.com"
            }
        ]
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
        },
        "suppliers": [
            {
                "id": "4",
                "name": "Samsung SDI",
                "location": {
                    "id": "5",
                    "name": "Samsung Battery Plant",
                    "latitude": 37.5665,
                    "longitude": 126.9780
                },
                "address": "150 Samsung-ro, Giheung-gu, Yongin-si, Gyeonggi-do, South Korea",
                "phone": "+82 31 8006 7114",
                "email": "supplier.relations@samsungsdi.com"
            }
        ]
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