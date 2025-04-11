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

3. Start the backend services (in separate PowerShell windows):
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

## Troubleshooting

### Common Issues

1. **PowerShell Execution Policy Error**
   - Run PowerShell as Administrator
   - Execute: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

2. **Python Virtual Environment Issues**
   - Delete the existing venv folder: `Remove-Item -Recurse -Force venv`
   - Run setup.bat again

3. **Node.js Dependencies Issues**
   - Delete node_modules folder: `Remove-Item -Recurse -Force node_modules`
   - Run setup.bat again

4. **Port Already in Use**
   - Check if any other application is using ports 3000, 5000, or 5001
   - Kill the process or change the port in the respective configuration files 