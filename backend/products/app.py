from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy data
products = [
    {
        "id": "1",
        "name": "Laptop",
        "description": "High-performance laptop for professionals",
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
                }
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
                }
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
                }
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
                }
            }
        ],
        "totalCost": 1239.94,
        "deliveryTime": "10 days",
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
        "description": "Latest smartphone with advanced features",
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
            },
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
        "totalCost": 639.96,
        "deliveryTime": "8 days",
        "assemblyLocation": {
            "id": "6",
            "name": "Phone Assembly Plant",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
    },
    {
        "id": "3",
        "name": "Desktop PC",
        "description": "High-end desktop computer for gaming and content creation",
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
                }
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
                }
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
                }
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
                }
            }
        ],
        "totalCost": 1259.94,
        "deliveryTime": "10 days",
        "assemblyLocation": {
            "id": "10",
            "name": "Desktop Assembly Plant",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
    },
    {
        "id": "4",
        "name": "Tablet",
        "description": "Versatile tablet for work and entertainment",
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
        ],
        "totalCost": 639.96,
        "deliveryTime": "8 days",
        "assemblyLocation": {
            "id": "11",
            "name": "Tablet Assembly Plant",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
    },
    {
        "id": "5",
        "name": "Smartwatch",
        "description": "Advanced smartwatch with health monitoring features",
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
        ],
        "totalCost": 639.96,
        "deliveryTime": "8 days",
        "assemblyLocation": {
            "id": "12",
            "name": "Wearable Assembly Plant",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
    },
    {
        "id": "6",
        "name": "Gaming Console",
        "description": "Next-generation gaming console for immersive gameplay",
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
                }
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
                }
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
                }
            }
        ],
        "totalCost": 1099.95,
        "deliveryTime": "10 days",
        "assemblyLocation": {
            "id": "13",
            "name": "Gaming Console Assembly Plant",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
    },
    {
        "id": "7",
        "name": "Smart TV",
        "description": "4K smart TV with advanced streaming capabilities",
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
                }
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
                }
            }
        ],
        "totalCost": 1219.95,
        "deliveryTime": "10 days",
        "assemblyLocation": {
            "id": "14",
            "name": "TV Assembly Plant",
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