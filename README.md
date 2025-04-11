# Supply Chain Tracking Application

A modern supply chain tracking and visualization application built with React, TypeScript, and Python microservices.

## Project Structure

```
supply_chain/
├── frontend/           # React + TypeScript frontend
├── backend/           # Python microservices
│   ├── products/     # Product service
│   ├── parts/        # Parts service
│   └── locations/    # Location service
└── README.md
```

## Setup Instructions

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

### Backend Setup
1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the services:
   ```bash
   python backend/products/app.py
   python backend/parts/app.py
   python backend/locations/app.py
   ```

## Features
- Product List with detailed views
- Part tracking and visualization
- Supply chain map visualization
- Dark theme with modern UI 