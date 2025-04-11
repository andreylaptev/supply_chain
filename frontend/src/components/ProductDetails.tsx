import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { 
  Grid, 
  Card, 
  CardContent, 
  Typography,
  Box,
  Paper,
  Skeleton,
  Chip,
  Divider,
  useTheme,
  alpha,
  Tooltip
} from '@mui/material';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { Inventory as InventoryIcon, Build as BuildIcon, LocationOn as LocationIcon } from '@mui/icons-material';
import { Product, Part } from '../types';

const ProductDetails: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [product, setProduct] = useState<Product | null>(null);
  const [loading, setLoading] = useState(true);
  const theme = useTheme();

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        setLoading(true);
        const response = await fetch(`http://localhost:5000/api/products/${id}`);
        const data = await response.json();
        setProduct(data);
      } catch (error) {
        console.error('Error fetching product:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchProduct();
  }, [id]);

  if (loading) {
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
          <Skeleton variant="text" width="40%" height={40} />
          <Skeleton variant="text" width="60%" />
        </Paper>
        <Grid container spacing={3}>
          <Grid item xs={12} md={6}>
            <Skeleton variant="rectangular" height={400} />
          </Grid>
          <Grid item xs={12} md={6}>
            <Skeleton variant="rectangular" height={400} />
          </Grid>
        </Grid>
      </Box>
    );
  }

  if (!product) {
    return (
      <Paper 
        elevation={0} 
        sx={{ 
          p: 4, 
          textAlign: 'center',
          borderRadius: 2,
          background: `linear-gradient(90deg, ${alpha(theme.palette.error.main, 0.1)} 0%, ${alpha(theme.palette.background.paper, 0.05)} 100%)`,
          border: `1px solid ${alpha(theme.palette.error.main, 0.2)}`
        }}
      >
        <Typography variant="h5" color="error" gutterBottom>
          Product Not Found
        </Typography>
        <Typography variant="body1" color="text.secondary">
          The requested product could not be found. Please try again or return to the product list.
        </Typography>
      </Paper>
    );
  }

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
            icon={<LocationIcon />}
          />
        </Box>
        <Typography variant="body1" color="text.secondary">
          Product details and supply chain information.
        </Typography>
      </Paper>
      
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Paper 
            elevation={0} 
            sx={{ 
              p: 3, 
              mb: 3, 
              borderRadius: 2,
              background: theme.palette.background.paper,
              border: `1px solid ${alpha(theme.palette.divider, 0.1)}`
            }}
          >
            <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
              <BuildIcon sx={{ mr: 2, color: 'primary.main' }} />
              <Typography variant="h6" sx={{ fontWeight: 600 }}>
                Component Parts
              </Typography>
            </Box>
            <Divider sx={{ mb: 3 }} />
            <Grid container spacing={2}>
              {product.parts.map((part) => (
                <Grid item xs={12} sm={6} key={part.id}>
                  <Tooltip 
                    title="Click to view detailed part information"
                    arrow
                    placement="top"
                  >
                    <Card 
                      onClick={() => navigate(`/part/${part.id}`)}
                      sx={{ 
                        cursor: 'pointer',
                        transition: 'all 0.3s ease',
                        '&:hover': {
                          transform: 'translateY(-4px)',
                          boxShadow: `0 8px 16px ${alpha(theme.palette.common.black, 0.2)}`,
                          borderColor: theme.palette.primary.main
                        },
                        border: `1px solid ${alpha(theme.palette.divider, 0.1)}`,
                        borderRadius: 2
                      }}
                    >
                      <CardContent>
                        <Typography variant="subtitle1" sx={{ fontWeight: 600 }}>
                          {part.name}
                        </Typography>
                        <Box sx={{ display: 'flex', alignItems: 'center', mt: 1 }}>
                          <Chip 
                            label={part.sourceLocation.name} 
                            size="small" 
                            color="secondary" 
                            variant="outlined"
                            icon={<LocationIcon />}
                          />
                        </Box>
                      </CardContent>
                    </Card>
                  </Tooltip>
                </Grid>
              ))}
            </Grid>
          </Paper>
        </Grid>

        <Grid item xs={12} md={6}>
          <Paper 
            elevation={0} 
            sx={{ 
              p: 3, 
              mb: 3, 
              borderRadius: 2,
              background: theme.palette.background.paper,
              border: `1px solid ${alpha(theme.palette.divider, 0.1)}`
            }}
          >
            <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
              <LocationIcon sx={{ mr: 2, color: 'primary.main' }} />
              <Typography variant="h6" sx={{ fontWeight: 600 }}>
                Supply Chain Map
              </Typography>
            </Box>
            <Divider sx={{ mb: 3 }} />
            <Box sx={{ height: 400, width: '100%', borderRadius: 2, overflow: 'hidden' }}>
              <MapContainer
                center={[20, 0]}
                zoom={2}
                style={{ height: '100%', width: '100%' }}
              >
                <TileLayer
                  url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                  attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                />
                
                {/* Assembly Location Marker */}
                <Marker
                  position={[product.assemblyLocation.latitude, product.assemblyLocation.longitude]}
                >
                  <Popup>
                    <Typography variant="subtitle2" sx={{ fontWeight: 600 }}>
                      Assembly Location
                    </Typography>
                    <Typography variant="body2">
                      {product.assemblyLocation.name}
                    </Typography>
                  </Popup>
                </Marker>

                {/* Part Source Locations */}
                {product.parts.map((part) => (
                  <Marker
                    key={part.id}
                    position={[part.sourceLocation.latitude, part.sourceLocation.longitude]}
                  >
                    <Popup>
                      <Typography variant="subtitle2" sx={{ fontWeight: 600 }}>
                        {part.name} Source
                      </Typography>
                      <Typography variant="body2">
                        {part.sourceLocation.name}
                      </Typography>
                    </Popup>
                  </Marker>
                ))}
              </MapContainer>
            </Box>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default ProductDetails; 