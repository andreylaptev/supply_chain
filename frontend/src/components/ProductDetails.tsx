import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { 
  Container, 
  Grid, 
  Card, 
  CardContent, 
  Typography,
  Box
} from '@mui/material';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { Product, Part } from '../types';

const ProductDetails: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [product, setProduct] = useState<Product | null>(null);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await fetch(`http://localhost:5000/api/products/${id}`);
        const data = await response.json();
        setProduct(data);
      } catch (error) {
        console.error('Error fetching product:', error);
      }
    };

    fetchProduct();
  }, [id]);

  if (!product) {
    return <Typography>Loading...</Typography>;
  }

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom sx={{ mb: 4 }}>
        {product.name}
      </Typography>
      
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Typography variant="h6" gutterBottom>
            Parts
          </Typography>
          <Grid container spacing={2}>
            {product.parts.map((part) => (
              <Grid item xs={12} sm={6} key={part.id}>
                <Card 
                  onClick={() => navigate(`/part/${part.id}`)}
                  sx={{ cursor: 'pointer' }}
                >
                  <CardContent>
                    <Typography variant="h6">{part.name}</Typography>
                  </CardContent>
                </Card>
              </Grid>
            ))}
          </Grid>
        </Grid>

        <Grid item xs={12} md={6}>
          <Typography variant="h6" gutterBottom>
            Supply Chain Map
          </Typography>
          <Box sx={{ height: 400, width: '100%' }}>
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
                  Assembly Location: {product.assemblyLocation.name}
                </Popup>
              </Marker>

              {/* Part Source Locations */}
              {product.parts.map((part) => (
                <Marker
                  key={part.id}
                  position={[part.sourceLocation.latitude, part.sourceLocation.longitude]}
                >
                  <Popup>
                    {part.name} Source: {part.sourceLocation.name}
                  </Popup>
                </Marker>
              ))}
            </MapContainer>
          </Box>
        </Grid>
      </Grid>
    </Container>
  );
};

export default ProductDetails; 