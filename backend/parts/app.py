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
    },
    {
        "id": "5",
        "name": "Motherboard",
        "deliveryTime": "6 days",
        "weight": 0.5,
        "price": 159.99,
        "sourceLocation": {
            "id": "6",
            "name": "ASUS Factory",
            "latitude": 25.0330,
            "longitude": 121.5654
        },
        "suppliers": [
            {
                "id": "5",
                "name": "ASUS",
                "location": {
                    "id": "6",
                    "name": "ASUS Factory",
                    "latitude": 25.0330,
                    "longitude": 121.5654
                },
                "address": "15 Li-Te Road, Peitou, Taipei 112, Taiwan",
                "phone": "+886 2 2894 3447",
                "email": "supplier.relations@asus.com"
            }
        ]
    },
    {
        "id": "6",
        "name": "GPU",
        "deliveryTime": "7 days",
        "weight": 0.3,
        "price": 499.99,
        "sourceLocation": {
            "id": "7",
            "name": "NVIDIA Factory",
            "latitude": 37.4419,
            "longitude": -122.1430
        },
        "suppliers": [
            {
                "id": "6",
                "name": "NVIDIA Corporation",
                "location": {
                    "id": "7",
                    "name": "NVIDIA Factory",
                    "latitude": 37.4419,
                    "longitude": -122.1430
                },
                "address": "2788 San Tomas Expressway, Santa Clara, CA 95051",
                "phone": "+1 (408) 486-2000",
                "email": "supplier.relations@nvidia.com"
            }
        ]
    },
    {
        "id": "7",
        "name": "Storage SSD",
        "deliveryTime": "4 days",
        "weight": 0.08,
        "price": 129.99,
        "sourceLocation": {
            "id": "8",
            "name": "Western Digital Factory",
            "latitude": 37.7749,
            "longitude": -122.4194
        },
        "suppliers": [
            {
                "id": "7",
                "name": "Western Digital",
                "location": {
                    "id": "8",
                    "name": "Western Digital Factory",
                    "latitude": 37.7749,
                    "longitude": -122.4194
                },
                "address": "5601 Great Oaks Parkway, San Jose, CA 95119",
                "phone": "+1 (408) 801-1000",
                "email": "supplier.relations@wdc.com"
            }
        ]
    },
    {
        "id": "8",
        "name": "Power Supply",
        "deliveryTime": "5 days",
        "weight": 0.4,
        "price": 79.99,
        "sourceLocation": {
            "id": "9",
            "name": "Corsair Factory",
            "latitude": 37.7749,
            "longitude": -122.4194
        },
        "suppliers": [
            {
                "id": "8",
                "name": "Corsair",
                "location": {
                    "id": "9",
                    "name": "Corsair Factory",
                    "latitude": 37.7749,
                    "longitude": -122.4194
                },
                "address": "47100 Bayside Parkway, Fremont, CA 94538",
                "phone": "+1 (510) 657-8747",
                "email": "supplier.relations@corsair.com"
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