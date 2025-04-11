@echo off
echo Installing dependencies...
npm install

echo Installing additional type definitions...
npm install --save-dev @types/react @types/react-dom @types/node @types/leaflet

echo Setup complete! You can now start the development server:
echo npm start 