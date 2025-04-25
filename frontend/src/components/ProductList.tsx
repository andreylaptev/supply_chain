import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
  Grid, 
  Card, 
  CardContent, 
  Typography,
  Box,
  Paper,
  Skeleton,
  Chip,
  useTheme,
  alpha,
  Tooltip
} from '@mui/material';
import { Inventory as InventoryIcon } from '@mui/icons-material';
import { Product } from '../types';

const ProductList: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();
  const theme = useTheme();

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        setLoading(true);
        const response = await fetch('http://localhost:5000/api/products');
        const data = await response.json();
        setProducts(data);
      } catch (error) {
        console.error('Error fetching products:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  return (
    <Box>
      <Paper 
        elevation={0} 
        sx={{ 
          p: 3, 
          mb: 4, 
          borderRadius: 2,
          background: `linear-gradient(90deg, ${alpha(theme.palette.primary.main, 0.1)} 0%, ${alpha(theme.palette.background.paper, 0.05)} 100%)`,
          border: `1px solid ${alpha(theme.palette.divider, 0.1)}`
        }}
      >
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
          <InventoryIcon sx={{ mr: 2, color: 'primary.main' }} />
          <Typography variant="h5" component="h1" sx={{ fontWeight: 600 }}>
            Product Catalog
          </Typography>
        </Box>
      </Paper>

      <Grid container spacing={3}>
        {loading ? (
          // Loading skeletons
          Array.from(new Array(6)).map((_, index) => (
            <Grid item xs={12} sm={6} md={4} key={index}>
              <Card sx={{ height: '100%' }}>
                <CardContent>
                  <Skeleton variant="text" width="60%" height={32} />
                  <Skeleton variant="text" width="40%" />
                </CardContent>
              </Card>
            </Grid>
          ))
        ) : (
          // Actual product cards
          products.map((product) => (
            <Grid item xs={12} sm={6} md={4} key={product.id}>
              <Tooltip 
                title="Click to view supply chain details and part information"
                arrow
                placement="top"
              >
                <Card 
                  onClick={() => navigate(`/product/${product.id}`)}
                  sx={{ 
                    cursor: 'pointer',
                    height: '100%',
                    display: 'flex',
                    flexDirection: 'column',
                    transition: 'all 0.3s ease',
                    '&:hover': {
                      transform: 'translateY(-8px)',
                      boxShadow: `0 12px 20px ${alpha(theme.palette.common.black, 0.2)}`,
                      borderColor: theme.palette.primary.main
                    },
                    border: `1px solid ${alpha(theme.palette.divider, 0.1)}`,
                    borderRadius: 2
                  }}
                >
                  <CardContent sx={{ flexGrow: 1 }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                      <InventoryIcon sx={{ mr: 1, color: 'primary.main' }} />
                      <Typography variant="h6" component="h2" sx={{ fontWeight: 600 }}>
                        {product.name}
                      </Typography>
                    </Box>
                    <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                      <Chip 
                        label={`${product.parts.length} parts`} 
                        size="small" 
                        color="primary" 
                        variant="outlined"
                        sx={{ mr: 1 }}
                      />
                      <Chip 
                        label={product.assemblyLocation.name} 
                        size="small" 
                        color="secondary" 
                        variant="outlined"
                      />
                    </Box>
                    <Typography variant="h6" color="primary" sx={{ mt: 2 }}>
                      ${product.price.toFixed(2)}
                    </Typography>
                  </CardContent>
                </Card>
              </Tooltip>
            </Grid>
          ))
        )}
      </Grid>
    </Box>
  );
};

export default ProductList; 