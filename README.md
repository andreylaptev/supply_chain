# Supply Chain Tracking Application

A modern supply chain tracking and visualization application built with React, TypeScript, and Python microservices.

## Project Structure

```
supply_chain/
├── frontend/           # React + TypeScript frontend
├── backend/           # Python microservices
│   ├── products/     # Product service
│   ├── parts/        # Parts service
│   └── shared/       # Shared code and database
└── README.md
```

## Setup Instructions

### Backend Setup (Windows)

1. Open PowerShell as Administrator and run:
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
   ```

2. Navigate to the backend directory and run the setup script:
   ```powershell
   cd backend
   .\setup.bat
   ```

3. Activate the virtual environment:
   ```powershell
   .\venv\Scripts\activate
   ```

4. Initialize the database:
   ```powershell
   python -m shared.init_db
   ```

5. Start the backend services (in separate PowerShell windows):
   ```powershell
   # Terminal 1 - Products Service
   cd backend
   .\venv\Scripts\activate
   python products/app.py

   # Terminal 2 - Parts Service
   cd backend
   .\venv\Scripts\activate
   python parts/app.py
   ```

### Frontend Setup (Windows)

1. Navigate to the frontend directory and run the setup script:
   ```powershell
   cd frontend
   .\setup.bat
   ```

2. Start the development server:
   ```powershell
   npm start
   ```

The application will be available at:
- Frontend: http://localhost:3000
- Products API: http://localhost:5000
- Parts API: http://localhost:5001

## Features
- Product List with detailed views
- Part tracking and visualization
- Supply chain map visualization
- Dark theme with modern UI 