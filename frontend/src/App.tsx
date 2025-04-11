import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { theme } from './theme';
import ProductList from './components/ProductList';
import ProductDetails from './components/ProductDetails';
import PartDetails from './components/PartDetails';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Routes>
          <Route path="/" element={<ProductList />} />
          <Route path="/product/:id" element={<ProductDetails />} />
          <Route path="/part/:id" element={<PartDetails />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App; 