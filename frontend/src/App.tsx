import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { Box, Container } from '@mui/material';
import { theme } from './theme';
import Navigation from './components/Navigation';
import ProductList from './components/ProductList';
import ProductDetails from './components/ProductDetails';
import PartDetails from './components/PartDetails';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Box sx={{ 
          display: 'flex', 
          flexDirection: 'column',
          minHeight: '100vh',
          background: 'linear-gradient(135deg, #121212 0%, #1e1e1e 100%)'
        }}>
          <Navigation />
          <Container maxWidth="lg" sx={{ py: 4, flexGrow: 1 }}>
            <Routes>
              <Route path="/" element={<ProductList />} />
              <Route path="/product/:id" element={<ProductDetails />} />
              <Route path="/part/:id" element={<PartDetails />} />
            </Routes>
          </Container>
          <Box 
            component="footer" 
            sx={{ 
              py: 3, 
              px: 2, 
              mt: 'auto',
              backgroundColor: 'background.paper',
              borderTop: '1px solid',
              borderColor: 'divider'
            }}
          >
            <Container maxWidth="lg">
              <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <Box sx={{ display: 'flex', alignItems: 'center' }}>
                  <Box 
                    component="span" 
                    sx={{ 
                      fontWeight: 700, 
                      color: 'primary.main',
                      fontSize: '1.2rem',
                      mr: 2
                    }}
                  >
                    Supply Chain Tracker
                  </Box>
                  <Box 
                    component="span" 
                    sx={{ 
                      color: 'text.secondary',
                      fontSize: '0.875rem'
                    }}
                  >
                    © {new Date().getFullYear()} All rights reserved
                  </Box>
                </Box>
                <Box sx={{ display: 'flex', gap: 2 }}>
                  <Box 
                    component="span" 
                    sx={{ 
                      color: 'text.secondary',
                      fontSize: '0.875rem',
                      cursor: 'pointer',
                      '&:hover': { color: 'primary.main' }
                    }}
                  >
                    Privacy Policy
                  </Box>
                  <Box 
                    component="span" 
                    sx={{ 
                      color: 'text.secondary',
                      fontSize: '0.875rem',
                      cursor: 'pointer',
                      '&:hover': { color: 'primary.main' }
                    }}
                  >
                    Terms of Service
                  </Box>
                </Box>
              </Box>
            </Container>
          </Box>
        </Box>
      </Router>
    </ThemeProvider>
  );
}

export default App; 